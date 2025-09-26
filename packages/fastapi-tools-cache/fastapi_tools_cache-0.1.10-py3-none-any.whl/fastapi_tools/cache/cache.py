from __future__ import annotations

from collections import OrderedDict
from pickle import dumps as pickle_dumps
from pickle import loads as pickle_loads
from typing import TYPE_CHECKING, Any

__all__ = ("ALRUCache",)


if TYPE_CHECKING:
    from typing import Sequence

    from redis.asyncio import Redis as ARedis


class ACache[K, V]:
    """Async cache interface"""

    __slots__ = ()

    async def aget(
        self,
        key: K,
    ) -> V:
        raise NotImplementedError()

    async def aset(
        self,
        key: K,
        value: V,
        expires_in: int | None = None,
    ) -> None:
        raise NotImplementedError()

    async def aclear(self, key: K) -> None:
        raise NotImplementedError()


class ALRUCache(ACache[bytes, Any]):
    __slots__ = ("_client", "_data", "_maxsize", "_ttl")

    def __init__(self, client: ARedis, maxsize: int, ttl: int):
        self._client = client
        self._data: OrderedDict[bytes, Any] = OrderedDict()
        self._maxsize = maxsize
        self._ttl = ttl

    def __repr__(self) -> str:
        return "%s(%s, maxsize=%r, currsize=%r)" % (
            self.__class__.__name__,
            repr(self._data),
            self._maxsize,
            len(self._data),
        )

    def _get(self, key: bytes) -> Any:
        ret = self._data[key]
        self._data.move_to_end(key)
        return ret

    def _set(self, key: bytes, value: Any) -> None:
        maxsize = self._maxsize
        if len(self._data) >= maxsize and key not in self._data:
            self._data.popitem(last=False)
        self._data[key] = value

    async def aget(self, key: bytes) -> Any:
        # fetch push events
        await self._client.execute_command("")
        try:
            return self._get(key)
        except KeyError:
            pass
        ret = await self._client.get(key)
        if ret is None:
            raise KeyError(key)
        result = pickle_loads(ret)
        self._set(key, result)
        return result

    async def aset(
        self,
        key: bytes,
        value: Any,
        expires_in: int | None = None,
    ) -> None:
        await self._client.execute_command(
            "SET",
            key,
            pickle_dumps(value),
            "EX",
            expires_in or self._ttl,
            enable_key_tracking=key,
        )
        self._set(key, value)

    async def aclear(self, key: bytes) -> None:
        self._data.pop(key, None)
        await self._client.delete(key)

    async def aclose(self) -> None:
        await self._client.aclose()

    def flush(self, keys: Sequence[bytes] | None = None) -> None:
        if keys is None:
            self._data.clear()
        else:
            data = self._data
            for key in keys:
                data.pop(key, None)


class AOCache(ACache[bytes, Any]):
    __slots__ = ("_ttl", "_client")

    def __init__(self, client: ARedis, ttl: int) -> None:
        self._ttl = ttl
        self._client = client

    async def aget(
        self,
        key: bytes,
    ) -> Any:
        ret = await self._client.get(key)
        if ret is None:
            raise KeyError(key)
        return pickle_loads(ret)

    async def aset(
        self,
        key: bytes,
        value: Any,
        expires_in: int | None = None,
    ) -> None:
        await self._client.set(
            key,
            pickle_dumps(value),
            ex=expires_in or self._ttl,
        )

    async def alock(
        self,
        key: bytes,
        value: Any,
        expires_in: int | None = None,
    ) -> bool:
        return bool(
            await self._client.set(
                key,
                pickle_dumps(value),
                ex=expires_in or self._ttl,
                nx=True,
            )
        )

    async def aclear(self, key: bytes) -> None:
        await self._client.delete(key)
