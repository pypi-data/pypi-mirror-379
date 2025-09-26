from __future__ import annotations

import asyncio, signal, time
from collections import deque
from typing import Optional, Any, Union, Literal, Deque, overload

from pyroute import Route
from configio.schemas import PathType
from nemoria.logger import logger
from nemoria.config import DEFAULT_TIMEOUT, PING_TIMEOUT, HANDSHAKE_TIMEOUT
from nemoria.protocol import Connection, Frame, Action, JSON
from nemoria.utils import send, recv


"""
Async TCP client for the Nemoria in-memory store.

- Opens a TCP connection, performs a handshake, and exchanges framed requests.
- Serializes request/response usage of a single socket with `self.lock`.
- Buffers out-of-order frames in `self.inbox` while waiting for a specific reply.
- Provides helpers for GET/ALL/SET/DELETE/DROP/PURGE/SAVE/PING.

SAVE behavior:
    When `save_on_disk=True` (or `save()` is called), the client sends a SAVE
    frame as a one-way signal and does not wait for any server reply. If you need
    durability confirmation, add an explicit confirmation step at the protocol level.
"""


class Client:
    """
    Minimal async client for the Nemoria store protocol.

    Responsibilities:
        - Connect/close TCP sockets and perform the initial handshake.
        - Send framed requests and await matching replies when the protocol responds.
        - Offer convenience methods for common store operations.

    Concurrency:
        A single `StreamReader`/`StreamWriter` pair is shared. To avoid concurrent
        reads on the same reader, calls are serialized with `self.lock`. Out-of-order
        frames are buffered in `self.inbox`.
    """

    def __init__(
        self,
        host: Union[Literal["localhost", "127.0.0.1"], str] = "localhost",
        port: int = 8888,
        password: Optional[str] = None,
    ) -> None:
        """
        Create a client (does not connect).

        Args:
            host: Server host or IP.
            port: Server TCP port.
            password: Optional shared secret for frame auth/enc.
        """
        self.host = host
        self.port = port
        self.password = password

        self.connection: Optional[Connection] = None
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None

        # Buffer unrelated frames while waiting for a specific reply.
        self.inbox: Deque[Frame] = deque(maxlen=1024)

        # Serialize request/response I/O over one socket.
        self.lock = asyncio.Lock()

    async def connect(self) -> bool:
        """
        Open the TCP connection and complete the handshake.

        - Connect to (host, port).
        - Send HANDSHAKE and parse `Connection` metadata.
        - Register SIGINT/SIGTERM handlers for best-effort graceful close.

        Returns:
            True on success; False otherwise.
        """
        try:
            self.reader, self.writer = await asyncio.open_connection(
                self.host, self.port
            )
            if (connection_json := await self.handshake()) is None:
                raise ConnectionError
            self.connection = Connection.deserialize(
                connection_json, self.reader, self.writer
            )
            logger.info(f"{self.connection} SECURED.")

            # Best-effort OS signal handlers (may not exist on some platforms).
            loop = asyncio.get_running_loop()
            try:
                loop.add_signal_handler(
                    signal.SIGINT, lambda: asyncio.create_task(self.close())
                )
                loop.add_signal_handler(
                    signal.SIGTERM, lambda: asyncio.create_task(self.close())
                )
            except NotImplementedError:
                pass
            return True

        except ConnectionError:
            logger.error("Connection not established.")
        except Exception:
            logger.error(f"Connection to {(self.host, self.port)} FAILED.")
            await self.close()
        return False

    async def close(self) -> None:
        """
        Close the socket and release resources.

        Idempotent: safe to call multiple times.
        """
        if self.writer is not None:
            try:
                self.writer.close()
                try:
                    await self.writer.wait_closed()
                    logger.info(f"{self.connection or 'CLIENT'} CLOSED.")
                except Exception:
                    pass
            finally:
                self.writer = None
                self.reader = None

    async def shutdown(self) -> None:
        """
        Request server shutdown (best effort).

        Raises:
            ConnectionError: If not connected.
        """
        if self.reader is None or self.writer is None:
            raise ConnectionError("Connection not established.")
        await self._request(Frame(action=Action.SHUTDOWN))

    async def _send(self, frame: Frame) -> None:
        """
        Send a frame to the server (no reply expected).

        Raises:
            ConnectionError: If not connected.
        """
        if self.reader is None or self.writer is None:
            raise ConnectionError("Connection not established.")
        await send(self.writer, frame, self.password)

    async def _receive(self, reply_to: Optional[Frame] = None) -> Optional[Frame]:
        """
        Receive the next frame; optionally wait for a specific reply.

        If `reply_to` is given, unrelated frames are buffered in `self.inbox`
        until a matching reply arrives.

        Returns:
            The frame, or None if the connection closed.

        Raises:
            ConnectionError: If not connected.
        """
        if self.reader is None or self.writer is None:
            raise ConnectionError("Connection not established.")

        while True:
            # Prefer buffered frames first.
            for f in list(self.inbox):
                if reply_to is not None and reply_to == f.reply_to:
                    self.inbox.remove(f)
                    return f

            # Await a new frame from the wire.
            try:
                response = await recv(self.reader, self.password)
            except (
                EOFError,
                ConnectionError,
                ConnectionResetError,
                OSError,
                asyncio.IncompleteReadError,
            ):
                await self.close()
                return None

            if response is None:
                await self.close()
                return None

            if reply_to is not None:
                if reply_to == response.reply_to:
                    return response
                self.inbox.append(response)
                continue

            return response

    async def _request(
        self, frame: Frame, timeout: Optional[float] = DEFAULT_TIMEOUT
    ) -> Optional[Frame]:
        """
        Send a request and await its matching response when the protocol replies.

        Calls are serialized by `self.lock` to avoid concurrent reads.

        Returns:
            Matching response frame, or None on timeout/close.

        Raises:
            ConnectionError: If not connected.
        """
        if self.reader is None or self.writer is None:
            raise ConnectionError("Connection not established.")

        async with self.lock:
            try:
                await self._send(frame)
            except (ConnectionError, ConnectionResetError, OSError) as e:
                logger.error(f"Connection error while sending: {e}")
                await self.close()
                return None

            try:
                coro = self._receive(reply_to=frame)
                return await asyncio.wait_for(coro, timeout) if timeout else await coro
            except asyncio.TimeoutError:
                logger.error(f"Request timed out after {timeout:.2f}s")
                return None

    async def is_alive(self) -> bool:
        """
        Quick liveness probe.

        Returns:
            True if socket endpoints are healthy and PING succeeds.
        """
        if self.reader is None or self.writer is None:
            return False
        if self.reader.at_eof() or self.writer.is_closing():
            return False
        return (await self.ping()) is not None

    async def get(self, route: Optional[Route] = None) -> Optional[Any]:
        """
        GET a single value.

        Args:
            route: Route/key to read.

        Returns:
            Value from the response, or None on failure.
        """
        frame = await self._request(Frame(action=Action.GET, route=route))
        return None if frame is None else frame.value

    async def all(self) -> Optional[JSON]:
        """
        Fetch the entire store (server-defined semantics).

        Returns:
            The store JSON, or None on failure.
        """
        frame = await self._request(Frame(action=Action.ALL))
        return None if frame is None else frame.value

    @overload
    async def set(
        self,
        *,
        route: Optional[Route] = ...,
        value: Optional[Any] = ...,
        overwrite_conflicts: bool = ...,
        save_on_disk: Literal[False] = False,
        codec: None = None,
        path: None = None,
        threadsafe: bool = True,
    ) -> None: ...
    @overload
    async def set(
        self,
        *,
        route: Optional[Route] = ...,
        value: Optional[Any] = ...,
        overwrite_conflicts: bool = ...,
        save_on_disk: Literal[True] = True,
        codec: Literal["json", "yaml"] = ...,
        path: PathType = ...,
        threadsafe: bool = True,
    ) -> None: ...

    async def set(
        self,
        *,
        route: Optional[Route] = None,
        value: Optional[Any] = None,
        overwrite_conflicts: bool = False,
        save_on_disk: bool = False,
        codec: Optional[Literal["json", "yaml"]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Set a value.

        Args:
            route: Path to write.
            value: Protocol-serializable value.
            overwrite_conflicts: Overwrite non-mapping nodes when building intermediates.
            save_on_disk: Also send a one-way SAVE after the update (no reply expected).
            codec, path, threadsafe: SAVE parameters (required if `save_on_disk=True`).
        """
        await self._request(
            Frame(
                action=Action.SET,
                route=route,
                value={
                    "value": value,
                    "overwrite_conflicts": overwrite_conflicts,
                    "save_on_disk": save_on_disk,
                    "codec": None if codec is None else codec,
                    "path": None if path is None else str(path),
                    "threadsafe": threadsafe,
                },
            )
        )

    @overload
    async def delete(
        self,
        *,
        route: Optional[Route] = ...,
        save_on_disk: Literal[False] = False,
        codec: None = None,
        path: None = None,
        threadsafe: bool = True,
    ) -> None: ...
    @overload
    async def delete(
        self,
        *,
        route: Optional[Route] = ...,
        save_on_disk: Literal[True] = True,
        codec: Literal["json", "yaml"] = ...,
        path: PathType = ...,
        threadsafe: bool = True,
    ) -> None: ...

    async def delete(
        self,
        *,
        route: Optional[Route] = None,
        save_on_disk: bool = False,
        codec: Optional[Literal["json", "yaml"]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Delete a subtree.

        Semantics:
            Removes the target subtree. Collapsing parents is server-defined.

        Args:
            route: Path to remove.
            save_on_disk: Also send a one-way SAVE after the update (no reply expected).
            codec, path, threadsafe: SAVE parameters (required if `save_on_disk=True`).
        """
        await self._request(
            Frame(
                action=Action.DELETE,
                route=route,
                value={
                    "save_on_disk": save_on_disk,
                    "codec": None if codec is None else codec,
                    "path": None if path is None else str(path),
                    "threadsafe": threadsafe,
                },
            )
        )

    @overload
    async def drop(
        self,
        *,
        route: Optional[Route] = ...,
        save_on_disk: Literal[False] = False,
        codec: None = None,
        path: None = None,
        threadsafe: bool = True,
    ) -> None: ...
    @overload
    async def drop(
        self,
        *,
        route: Optional[Route] = ...,
        save_on_disk: Literal[True] = True,
        codec: Literal["json", "yaml"] = ...,
        path: PathType = ...,
        threadsafe: bool = True,
    ) -> None: ...

    async def drop(
        self,
        *,
        route: Optional[Route] = None,
        save_on_disk: bool = False,
        codec: Optional[Literal["json", "yaml"]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Drop a key and prune empty ancestors.

        Semantics:
            Removes the target key (and subtree). Ancestor pruning is server-defined.

        Args:
            route: Path to drop.
            save_on_disk: Also send a one-way SAVE after the update (no reply expected).
            codec, path, threadsafe: SAVE parameters (required if `save_on_disk=True`).
        """
        await self._request(
            Frame(
                action=Action.DROP,
                route=route,
                value={
                    "save_on_disk": save_on_disk,
                    "codec": None if codec is None else codec,
                    "path": None if path is None else str(path),
                    "threadsafe": threadsafe,
                },
            )
        )

    @overload
    async def purge(
        self,
        *,
        save_on_disk: Literal[False] = False,
        codec: None = None,
        path: None = None,
        threadsafe: bool = True,
    ) -> None: ...
    @overload
    async def purge(
        self,
        *,
        save_on_disk: Literal[True],
        codec: Literal["json", "yaml"],
        path: PathType,
        threadsafe: bool = True,
    ) -> None: ...

    async def purge(
        self,
        *,
        save_on_disk: bool = False,
        codec: Optional[Literal["json", "yaml"]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Clear the entire store (destructive).

        Args:
            save_on_disk: Also send a one-way SAVE after clearing (no reply expected).
            codec, path, threadsafe: SAVE parameters (required if `save_on_disk=True`).
        """
        await self._request(
            Frame(
                action=Action.PURGE,
                value={
                    "save_on_disk": save_on_disk,
                    "codec": None if codec is None else codec,
                    "path": None if path is None else str(path),
                    "threadsafe": threadsafe,
                },
            )
        )

    async def save(
        self,
        codec: Literal["json", "yaml"],
        path: PathType,
        *,
        threadsafe: bool = True,
    ) -> None:
        """
        Send a SAVE frame as a one-way persistence request.

        Notes:
            This method does not wait for any server reply. Use a separate
            confirmation/verification step if your workflow requires it.
        """
        await self._send(
            Frame(
                action=Action.SAVE,
                value={"codec": codec, "path": str(path), "threadsafe": threadsafe},
            )
        )

    async def ping(self) -> Optional[float]:
        """
        Send PING and return round-trip latency in milliseconds.

        Returns:
            RTT in ms, or None on timeout/connection error.
        """
        start = time.perf_counter()
        if (await self._request(Frame(action=Action.PING), PING_TIMEOUT)) is None:
            return None
        rtt_ms = (time.perf_counter() - start) * 1000.0
        logger.info(f"{self.connection} PONG (RTT: {rtt_ms:.1f} ms).")
        return rtt_ms

    async def handshake(self) -> Optional[JSON]:
        """
        Perform the protocol handshake and return server connection info.

        Returns:
            Serialized `Connection` JSON from the server, or None on failure.
        """
        resp = await self._request(Frame(action=Action.HANDSHAKE), HANDSHAKE_TIMEOUT)
        return None if resp is None or resp.value is None else resp.value
