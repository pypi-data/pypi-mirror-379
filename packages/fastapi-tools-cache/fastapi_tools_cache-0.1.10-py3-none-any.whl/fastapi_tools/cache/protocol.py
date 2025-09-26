from __future__ import annotations

from typing import Any, Awaitable, Protocol

from redis.typing import EncodableT, ExpiryT, KeyT


class RedisCommandsProtocol[T](Protocol):
    def set(
        self,
        name: KeyT,
        value: EncodableT,
        ex: ExpiryT = ...,
        px: ExpiryT = ...,
        nx: bool = ...,
        xx: bool = ...,
        keepttl: bool = ...,
        get: bool = ...,
    ) -> T: ...

    def delete(self, *names: KeyT) -> T: ...

    def hset(
        self,
        name: KeyT = ...,
        key: KeyT = ...,
        value: EncodableT = ...,
        mapping: dict[KeyT, EncodableT] = ...,
    ) -> T: ...

    def hget(
        self,
        name: KeyT = ...,
        key: KeyT = ...,
    ) -> T: ...

    def hgetall(
        self,
        name: KeyT = ...,
    ) -> T: ...

    def hexpire(
        self,
        name: KeyT,
        seconds: ExpiryT,
        *fields: KeyT,
        nx: bool = ...,
        xx: bool = ...,
        gt: bool = ...,
        lt: bool = ...,
    ) -> T: ...

    def httl(self, key: KeyT, *fields: KeyT) -> T: ...


class RedisClientProtocol(RedisCommandsProtocol[Awaitable[Any]], Protocol):
    def pipeline(self) -> RedisPipelineProtocol: ...


class RedisPipelineProtocol(RedisCommandsProtocol["RedisPipelineProtocol"], Protocol):
    def execute(self) -> Awaitable[Any]: ...
