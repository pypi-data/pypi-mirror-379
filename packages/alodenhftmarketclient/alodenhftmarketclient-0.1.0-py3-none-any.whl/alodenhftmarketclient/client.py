import asyncio
import contextlib
from dataclasses import dataclass
from typing import Any, AsyncIterator, Awaitable, Callable, Dict, Optional

import httpx
import websockets

from .protocol import ensure_envelope, dumps_compact, try_loads


Json = Dict[str, Any]
OnEvent = Callable[[Json], Awaitable[None]] | Callable[[Json], None]


@dataclass
class Handshake:
    status: str
    user_id: str
    token: str
    is_admin: bool

    
class MarketClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.token: Optional[str] = None
        self._http: Optional[httpx.AsyncClient] = None

    async def _http_client(self) -> httpx.AsyncClient:
        if self._http is None:
            self._http = httpx.AsyncClient(base_url=self.base_url, timeout=5.0)
        return self._http

    async def aclose(self) -> None:
        if self._http is not None:
            await self._http.aclose()
        self._http = None

    async def handshake(self, token: Optional[str] = None) -> Handshake:
        cli = await self._http_client()
        payload: Json = {"token": token or self.token}
        r = await cli.post("/auth/handshake", json=payload)
        r.raise_for_status()
        data = r.json()
        self.token = data.get("token") or token or self.token
        return Handshake(
            status=data.get("status", ""),
            user_id=data.get("user_id", ""),
            token=data.get("token", ""),
            is_admin=bool(data.get("is_admin", False)),
        )

    async def api_request(self, op: str, payload: Optional[Json] = None, *, as_role: Optional[str] = None, timeout: float = 5.0) -> Json:
        cli = await self._http_client()
        req: Json = {"op": op, "payload": payload or {}}
        if as_role:
            req["as"] = as_role
        headers: Dict[str, str] = {"content-type": "application/json"}
        if self.token:
            headers["X-Auth-Token"] = self.token
        r = await cli.post("/api/request", json=req, headers=headers, timeout=timeout)
        r.raise_for_status()
        return r.json()

    async def open_cmd(self, on_event: Optional[OnEvent] = None) -> "CmdChannel":
        if not self.token:
            raise RuntimeError("Call handshake() first to obtain a token")
        url = self._ws_url("/ws/cmd")
        ws = await websockets.connect(url)
        return CmdChannel(ws, on_event=on_event)

    async def open_md(self) -> "MdStream":
        if not self.token:
            raise RuntimeError("Call handshake() first to obtain a token")
        url = self._ws_url("/ws/md")
        ws = await websockets.connect(url)
        return MdStream(ws)

    def _ws_url(self, path: str) -> str:
        assert self.token, "token required"
        # Derive ws/wss from base_url scheme
        # Accept base_url like http://host:port or https://host
        base = self.base_url
        if base.startswith("https://"):
            scheme = "wss://"
            rest = base[len("https://"):]
        elif base.startswith("http://"):
            scheme = "ws://"
            rest = base[len("http://"):]
        else:
            # Default to ws
            scheme = "ws://"
            rest = base
        from urllib.parse import urlencode
        q = f"{path}?{urlencode({'token': self.token})}"
        return f"{scheme}{rest}{q}"


class CmdChannel:
    def __init__(self, ws: websockets.WebSocketClientProtocol, *, on_event: Optional[OnEvent] = None):
        self._ws = ws
        self._on_event = on_event
        self._reader_task: Optional[asyncio.Task] = None
        self._pending: Dict[str, asyncio.Future] = {}
        self._closed = False
        self._start_reader()

    def _start_reader(self) -> None:
        async def _reader() -> None:
            try:
                async for msg in self._ws:
                    o = try_loads(msg)
                    if not isinstance(o, dict):
                        continue
                    if o.get("type") == "response" and isinstance(o.get("corr_id"), str):
                        fid = o.get("corr_id")
                        fut = self._pending.pop(fid, None)
                        if fut and not fut.done():
                            fut.set_result(o)
                        continue
                    if o.get("type") == "event":
                        cb = self._on_event
                        if cb:
                            try:
                                res = cb(o)
                                if asyncio.iscoroutine(res):
                                    await res
                            except Exception:
                                # swallow callback errors to keep stream alive
                                pass
                        continue
            except Exception:
                # Close all pending
                for fut in list(self._pending.values()):
                    if not fut.done():
                        fut.set_exception(ConnectionError("CMD closed"))
                self._pending.clear()
                self._closed = True

        self._reader_task = asyncio.create_task(_reader())

    async def send(self, op: str, payload: Optional[Json] = None, *, as_role: Optional[str] = None, timeout: float = 5.0) -> Json:
        if self._closed:
            raise ConnectionError("CMD channel is closed")
        req: Json = {"op": op, "payload": payload or {}}
        if as_role:
            req["as"] = as_role
        env = ensure_envelope(req)
        line = dumps_compact(env)
        fut: asyncio.Future = asyncio.get_event_loop().create_future()
        self._pending[env["msg_id"]] = fut
        await self._ws.send(line)
        try:
            return await asyncio.wait_for(fut, timeout=timeout)
        except Exception:
            if env["msg_id"] in self._pending:
                self._pending.pop(env["msg_id"], None)
            raise

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        try:
            await self._ws.close()
        except Exception:
            pass
        if self._reader_task:
            self._reader_task.cancel()
            with contextlib.suppress(Exception):
                await self._reader_task

    async def __aenter__(self) -> "CmdChannel":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()


class MdStream:
    def __init__(self, ws: websockets.WebSocketClientProtocol):
        self._ws = ws
        self._closed = False

    def __aiter__(self) -> AsyncIterator[Json]:
        return self._iter()

    async def _iter(self) -> AsyncIterator[Json]:
        try:
            async for msg in self._ws:
                o = try_loads(msg)
                if isinstance(o, dict):
                    yield o
        finally:
            await self.close()

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        try:
            await self._ws.close()
        except Exception:
            pass

    async def __aenter__(self) -> "MdStream":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

