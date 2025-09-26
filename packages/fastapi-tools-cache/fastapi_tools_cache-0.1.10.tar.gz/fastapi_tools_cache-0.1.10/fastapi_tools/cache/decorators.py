from __future__ import annotations

import asyncio
import functools
from collections import defaultdict
from collections.abc import MutableMapping
from contextlib import asynccontextmanager
from hashlib import blake2b
from typing import TYPE_CHECKING, overload

from .cache import ACache

__all__ = ("cached",)


if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Callable
    from typing import Any, Protocol

    class ACallable[**P, T](Protocol):
        __name__: str
        __module__: str

        async def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T: ...

    class CallableCache[**P, T](Protocol):
        async def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T: ...
        async def clear_cache_entry(self, *args: P.args, **kwargs: P.kwargs) -> None: ...


class GroupLock:
    __slots__ = ("_locks",)

    def __init__(self) -> None:
        self._locks: dict[Any, asyncio.Lock] = defaultdict(asyncio.Lock)

    @asynccontextmanager
    async def lock(self, key: Any) -> AsyncIterator[bool]:
        lock = self._locks[key]
        was_locked = not lock.locked()
        async with lock:
            yield was_locked
            if not was_locked:
                del self._locks[key]


def hashkey(prefix: Any, args: tuple[Any, ...], kwargs: dict[str, Any]) -> bytes:
    return blake2b(
        repr((prefix, args, sorted(kwargs.items()))).encode(),
        digest_size=24,
        person=b"cache-key",
    ).digest()


@overload
def cached[**P, T](
    cache: MutableMapping,
) -> Callable[[ACallable[P, T]], ACallable[P, T]]: ...


@overload
def cached[**P, T](
    cache: ACache,
    *,
    expires_in: int | None = None,
    prefix: str | None = None,
) -> Callable[[ACallable[P, T]], CallableCache[P, T]]: ...


def cached[**P, T](
    cache: MutableMapping | ACache,
    *,
    expires_in: int | None = None,
    prefix: str | None = None,
) -> Callable[[ACallable[P, T]], CallableCache[P, T] | ACallable[P, T]]:
    def decorator(func: ACallable[P, T]) -> CallableCache[P, T] | ACallable[P, T]:
        group_lock = GroupLock()

        if isinstance(cache, ACache):
            cache_prefix = (prefix.encode() + b":") if prefix else b"cached:"
            func_name = f"{func.__module__}.{func.__name__}"

            async def wrapper(*args: Any, **kwargs: Any) -> Any:
                k = cache_prefix + hashkey(func_name, args, kwargs)
                try:
                    return await cache.aget(k)
                except KeyError:
                    pass
                async with group_lock.lock(k) as was_locked:
                    if was_locked:
                        try:
                            return await cache.aget(k)
                        except KeyError:
                            pass
                    v = await func(*args, **kwargs)
                    try:
                        await cache.aset(k, v, expires_in)
                    except ValueError:
                        pass
                    return v

            async def clear_cache_entry(*args: Any, **kwargs: Any) -> None:
                await cache.aclear(cache_prefix + hashkey(func_name, args, kwargs))

            setattr(wrapper, "clear_cache_entry", clear_cache_entry)

        elif isinstance(cache, MutableMapping):

            async def wrapper(*args: Any, **kwargs: Any) -> Any:
                k = hashkey("", args, kwargs)
                try:
                    return cache[k]
                except KeyError:
                    pass
                async with group_lock.lock(k) as was_locked:
                    if was_locked:
                        try:
                            return cache[k]
                        except KeyError:
                            pass
                    v = await func(*args, **kwargs)
                    try:
                        cache[k] = v
                    except ValueError:
                        pass
                    return v
        else:
            raise TypeError("Invalid cache object")

        return functools.update_wrapper(wrapper, func)

    return decorator
