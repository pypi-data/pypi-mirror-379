from __future__ import annotations
import time
from typing import Any, Dict, Callable, Optional
from .types import Config, SdkMetric
from .batching import get_manager, parse_int_safe as _parse_int_safe


def _pick_request_id(headers: Dict[str, Any]) -> Optional[str]:
    return (
        headers.get("x-request-id")
        or headers.get("request-id")
        or headers.get("x-correlation-id")
        or None
    )


def _pick_trace_id(headers: Dict[str, Any]) -> Optional[str]:
    hdr = str(headers.get("traceparent", "")).strip()
    parts = hdr.split("-")
    if len(parts) == 4 and len(parts[1]) == 32:
        return parts[1]
    return headers.get("x-trace-id") or None

# -------- ASGI (FastAPI/Starlette)


class ObservifyASGIMiddleware:
    def __init__(self, app, config: Config):
        self.app = app
        self.cfg = config
        self.batch = get_manager(config)
        self.protected = set(config.protectedRoutes or [])

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        path = scope.get("path", "/")
        if path in self.protected:
            return await self.app(scope, receive, send)

        method = scope.get("method", "GET")
        headers = {k.decode().lower(): v.decode()
                   for k, v in scope.get("headers", [])}
        req_id = _pick_request_id(headers)
        trace_id = _pick_trace_id(headers)

        req_bytes = _parse_int_safe(headers.get("content-length"))
        start = int(time.time() * 1000)
        res_bytes = 0
        status_code_holder = {"status": 200}

        async def send_wrapper(message):
            nonlocal res_bytes
            if message["type"] == "http.response.start":
                status_code_holder["status"] = message.get("status", 200)
                headers_list = message.get("headers", [])
                for k, v in headers_list:
                    if k.decode().lower() == "content-length":
                        cl = _parse_int_safe(v.decode())
                        if cl:
                            res_bytes = cl
            elif message["type"] == "http.response.body":
                body = message.get("body") or b""
                res_bytes += len(body)
            await send(message)

        await self.app(scope, receive, send_wrapper)

        dur = int(time.time() * 1000) - start
        route = scope.get("route", None)
        route_pattern = getattr(route, "path", None) or getattr(
            route, "path_format", None)
        if not route_pattern:
            route_pattern = scope.get("root_path", "") + path

        metric = SdkMetric(
            ts=start,
            method=method,
            route=route_pattern,
            status=status_code_holder["status"],
            dur_ms=dur,
            req_bytes=req_bytes or None,
            res_bytes=res_bytes or None,
            request_id=req_id or None,
            trace_id=trace_id or None,
            service=self.cfg.service,
            env=self.cfg.env,
            release=self.cfg.release,
        )
        if self.cfg.debug:
            print("[observify] metric", metric)
        self.batch.add(metric)

# -------- Django (WSGI/ASGI)


class ObservifyDjangoMiddleware:
    def __init__(self, get_response: Callable):
        try:
            from django.conf import settings  # type: ignore
            cfg_dict = getattr(settings, "OBSERVIFY_CONFIG", None)
            if not cfg_dict:
                raise RuntimeError("OBSERVIFY_CONFIG ausente em settings")
            self.cfg = Config(**cfg_dict)  # type: ignore
        except Exception as e:
            raise RuntimeError(f"Configure OBSERVIFY_CONFIG em settings: {e}")

        self.get_response = get_response
        self.batch = get_manager(self.cfg)
        self.protected = set(self.cfg.protectedRoutes or [])

    def __call__(self, request):
        path = getattr(request, "path", "/") or "/"
        if path in self.protected:
            return self.get_response(request)

        method = request.method
        headers = {k.lower(): v for k, v in request.headers.items()}
        req_id = _pick_request_id(headers)
        trace_id = _pick_trace_id(headers)

        req_bytes = _parse_int_safe(headers.get("content-length"))
        if not req_bytes and self.cfg.measureBodyBytes:
            try:
                body = request.body
                req_bytes = len(body)
            except Exception:
                pass

        start = int(time.time() * 1000)
        response = self.get_response(request)
        dur = int(time.time() * 1000) - start

        res_bytes = _parse_int_safe(response.get("Content-Length"))
        if res_bytes is None:
            try:
                if hasattr(response, "content"):
                    res_bytes = len(response.content)
                else:
                    total = 0
                    chunks = []
                    for chunk in response:
                        if isinstance(chunk, bytes):
                            total += len(chunk)
                        elif isinstance(chunk, str):
                            total += len(chunk.encode("utf-8"))
                            chunk = chunk.encode("utf-8")
                        chunks.append(chunk)

                    def _gen():
                        for c in chunks:
                            yield c
                    response.streaming_content = _gen()
                    res_bytes = total
            except Exception:
                res_bytes = None

        try:
            rm = getattr(request, "resolver_match", None)
            route_pattern = rm.route if rm and getattr(
                rm, "route", None) else path
        except Exception:
            route_pattern = path

        metric = SdkMetric(
            ts=start,
            method=method,
            route=route_pattern,
            status=getattr(response, "status_code", 0),
            dur_ms=dur,
            req_bytes=req_bytes or None,
            res_bytes=res_bytes or None,
            request_id=req_id or None,
            trace_id=trace_id or None,
            service=self.cfg.service,
            env=self.cfg.env,
            release=self.cfg.release,
        )
        if self.cfg.debug:
            print("[observify] metric", metric)
        self.batch.add(metric)
        return response

# Factories


def django_middleware_factory(cfg: Config):
    class _Injected(ObservifyDjangoMiddleware):
        def __init__(self, get_response: Callable):
            self.cfg = cfg
            self.get_response = get_response
            self.batch = get_manager(self.cfg)
            self.protected = set(self.cfg.protectedRoutes or [])
    return _Injected


def fastapi_integration(app, cfg: Config):
    app.add_middleware(ObservifyASGIMiddleware, config=cfg)
    return app
