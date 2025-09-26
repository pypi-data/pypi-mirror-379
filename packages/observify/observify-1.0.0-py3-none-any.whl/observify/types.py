from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Callable

Env = str  # 'PROD' | 'HMG' | 'DEV' | custom


@dataclass
class SdkMetric:
    ts: int
    method: str
    route: str
    status: int
    dur_ms: int
    req_bytes: Optional[int] = None
    res_bytes: Optional[int] = None
    request_id: Optional[str] = None
    trace_id: Optional[str] = None
    service: Optional[str] = None
    env: Optional[Env] = None
    release: Optional[str] = None


@dataclass
class Config:
    remoteUrl: str
    apiKey: str
    protectedRoutes: List[str] = field(default_factory=list)
    debug: bool = False
    service: Optional[str] = None
    env: Optional[Env] = None
    release: Optional[str] = None
    batchSize: int = 100
    flushIntervalMs: int = 60_000
    requestTimeoutMs: int = 10_000
    measureBodyBytes: bool = False
