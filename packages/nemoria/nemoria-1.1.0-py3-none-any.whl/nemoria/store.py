from __future__ import annotations

import asyncio
from typing import Optional, Any, Dict, Literal, overload, cast

from configio import ConfigIO, Loader, Codec
from configio.schemas import PathType
from pyroute import Route
from nemoria.logger import logger
from nemoria.protocol import JSON

"""
Async-friendly nested key-value store with per-route locks.

`Store` keeps data as nested dictionaries (`JSON`) and uses a *flat* map of
`asyncio.Lock`s keyed by `Route` (including `None`). A meta-lock
(`locks_guard`) serializes on-demand lock creation to avoid duplicate locks.

Quick start:
    store = Store()
    await store.set(route=Route("users", "42", "name"), value="Alice")
    name = await store.get(route=Route("users", "42", "name"))
    await store.delete(route=Route("users", "42"))      # collapse only immediate parent
    await store.drop(route=Route("users"))              # prune empty ancestors
    await store.save(Codec.JSON, "/path/state.json")    # async + atomic persistence

Persistence:
    Call `save(codec, path)` to persist `self.data` atomically (temp→replace)
    via ConfigIO. Codecs: `Codec.JSON`, `Codec.YAML`.

Typing:
    Overloads on `set`/`delete`/`drop`/`purge` require `codec` and `path`
    when `save_on_disk=True`.
"""


class Store:
    """
    Async-safe nested store with a flat per-route lock map.

    Attributes:
        data: Nested dictionary of arbitrary values (`JSON`).
        locks: Map of `Route | None` → `asyncio.Lock`.
        locks_guard: Meta-lock that serializes lock creation.

    Notes:
        - `get()` returns `None` for missing paths.
        - `set()` creates intermediate dicts as needed.
        - `delete()` can collapse only the *immediate* parent to `None`.
        - `drop()` recursively prunes empty ancestors.
    """

    def __init__(self, initial_data: Optional[JSON] = None) -> None:
        """
        Initialize store state.

        Args:
            initial_data: Optional initial JSON (shallow-copied to avoid aliasing).
        """
        self.data: JSON = dict(initial_data) if initial_data else {}
        self.locks: Dict[Optional[Route], asyncio.Lock] = {}  # Route (or None) -> Lock
        self.locks_guard = asyncio.Lock()

    async def lock(self, route: Optional[Route] = None) -> asyncio.Lock:
        """
        Return the per-route lock, creating it lazily under `locks_guard`.
        """
        lock = self.locks.get(route)
        if lock is not None:
            return lock
        async with self.locks_guard:
            return self.locks.setdefault(route, asyncio.Lock())

    async def get(self, route: Optional[Route] = None) -> Any:
        """
        Read the value at `route` (or root if `None`). Returns `None` if missing.
        """
        async with await self.lock(route):
            try:
                return await ConfigIO.get(Loader.DATA, data=self.data, route=route)
            except TypeError as e:
                logger.error(f"[GET] -> {e}")
                return None

    async def all(self) -> JSON:
        """
        Return the live internal dictionary (mutable; expose with care).
        """
        async with self.locks_guard:
            return self.data

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
        codec: Literal[Codec.JSON, Codec.YAML] = ...,
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
        codec: Optional[Literal[Codec.JSON, Codec.YAML]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Write `value` at `route`, creating intermediates as needed.

        If `save_on_disk=True`, requires `codec` and `path` and persists after update.
        """
        async with await self.lock(route):
            try:
                self.data = cast(
                    JSON,
                    await ConfigIO.set(
                        Loader.DATA,
                        data=self.data,
                        route=route,
                        value=value,
                        overwrite_conflicts=overwrite_conflicts,
                        save=False,
                    ),
                )

                if not save_on_disk:
                    return
                if codec is None or path is None:
                    logger.error(
                        "[SET] -> CODEC and PATH are required for saving on disk."
                    )
                    return
                await self.save(codec, path, threadsafe=threadsafe)

            except (TypeError, ValueError, OSError) as e:
                logger.error(f"[SET] -> {e}")

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
        codec: Literal[Codec.JSON, Codec.YAML] = ...,
        path: PathType = ...,
        threadsafe: bool = True,
    ) -> None: ...

    async def delete(
        self,
        *,
        route: Optional[Route] = None,
        save_on_disk: bool = False,
        codec: Optional[Literal[Codec.JSON, Codec.YAML]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Delete the subtree at `route`. May collapse only the *immediate* parent to `None`.
        """
        async with await self.lock(route):
            try:
                self.data = cast(
                    JSON,
                    await ConfigIO.delete(
                        Loader.DATA,
                        data=self.data,
                        route=route,
                        save=False,
                    ),
                )

                if not save_on_disk:
                    return
                if codec is None or path is None:
                    logger.error(
                        "[DELETE] -> CODEC and PATH are required for saving on disk."
                    )
                    return
                await self.save(codec, path, threadsafe=threadsafe)

            except (TypeError, ValueError, OSError) as e:
                logger.error(f"[DELETE] -> {e}")

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
        codec: Literal[Codec.JSON, Codec.YAML] = ...,
        path: PathType = ...,
        threadsafe: bool = True,
    ) -> None: ...

    async def drop(
        self,
        *,
        route: Optional[Route] = None,
        save_on_disk: bool = False,
        codec: Optional[Literal[Codec.JSON, Codec.YAML]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Drop the key at `route` and recursively prune empty ancestors.
        """
        async with await self.lock(route):
            try:
                self.data = cast(
                    JSON,
                    await ConfigIO.delete(
                        Loader.DATA,
                        data=self.data,
                        route=route,
                        drop=True,
                        save=False,
                    ),
                )

                if not save_on_disk:
                    return
                if codec is None or path is None:
                    logger.error(
                        "[DROP] -> CODEC and PATH are required for saving on disk."
                    )
                    return
                await self.save(codec, path, threadsafe=threadsafe)

            except (TypeError, ValueError, OSError) as e:
                logger.error(f"[DROP] -> {e}")

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
        codec: Literal[Codec.JSON, Codec.YAML],
        path: PathType,
        threadsafe: bool = True,
    ) -> None: ...

    async def purge(
        self,
        *,
        save_on_disk: bool = False,
        codec: Optional[Literal[Codec.JSON, Codec.YAML]] = None,
        path: Optional[PathType] = None,
        threadsafe: bool = True,
    ) -> None:
        """
        Clear all data and locks. Optionally persist the empty store.
        """
        async with self.locks_guard:
            self.data.clear()
            self.locks.clear()

            if not save_on_disk:
                return
            if codec is None or path is None:
                logger.error(
                    "[PURGE] -> CODEC and PATH are required for saving on disk."
                )
                return
            await self.save(codec, path, threadsafe=threadsafe)

    async def save(
        self,
        codec: Literal[Codec.JSON, Codec.YAML],
        path: PathType,
        *,
        threadsafe: bool = True,
    ) -> None:
        """
        Persist `self.data` atomically via ConfigIO (temp→replace).
        """
        async with self.locks_guard:
            try:
                # Note: argument order follows your current ConfigIO API.
                await ConfigIO.save(self.data, codec, path, threadsafe=threadsafe)
            except (TypeError, ValueError, OSError) as e:
                logger.error(f"[SAVE] -> {e}")
