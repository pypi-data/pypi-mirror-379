from __future__ import annotations

import asyncio
from random import randint
from typing import TYPE_CHECKING, cast

from pydantic import TypeAdapter
from redis import backoff as redis_backoff
from redis import exceptions as redis_exceptions
from redis.asyncio import Redis, Sentinel
from redis.asyncio.retry import Retry

from .cache import ALRUCache, AOCache
from .config import RedisConfig, RetryConfig, SentinelConfig
from .task import TaskManager

__all__ = ("RedisClientFactory",)

if TYPE_CHECKING:
    from typing import Any

    from redis.asyncio import Connection

    from .protocol import RedisClientProtocol


class ARedis(Redis):
    def create_online_cache(self, ttl: int) -> AOCache:
        return AOCache(self, ttl)

    def create_task_manager(
        self,
        group_name: str,
        running_time_limit: int = 600,
        result_expires_in: int = 3600,
        error_expires_in: int = 60,
    ) -> TaskManager:
        return TaskManager(
            cast("RedisClientProtocol", self),
            group_name,
            running_time_limit,
            result_expires_in,
            error_expires_in,
        )


class RedisClientFactory:
    __slots__ = ("_is_sentinel", "_init_config")

    def __init__(
        self, config: RedisConfig | SentinelConfig | None = None, /, **kwargs: Any
    ):
        config_model: RedisConfig | SentinelConfig = TypeAdapter(
            RedisConfig | SentinelConfig
        ).validate_python(
            {**(config.model_dump(exclude_none=True) if config else {}), **kwargs}
        )
        self._is_sentinel = isinstance(config_model, SentinelConfig)
        self._init_config = config_model.model_dump(exclude_none=True)

    def _get_client[T: Redis](self, redis_class: type[T], **kwargs: Any) -> T:
        init_config: dict[str, Any] = {**self._init_config, **kwargs}
        if retry := init_config.pop("retry", None):
            assert isinstance(retry, RetryConfig)
            init_config["retry"] = Retry(**retry.__dict__)
        if self._is_sentinel:
            service_name = init_config.pop("service_name")
            sentinel_kwargs = {**init_config.pop("sentinel_kwargs", {})}
            for k, v in init_config.items():
                if k.startswith("socket_"):
                    sentinel_kwargs.setdefault(k, v)
            sentinel = Sentinel(**init_config, sentinel_kwargs=sentinel_kwargs)
            return sentinel.master_for(service_name, redis_class=redis_class)
        return redis_class(**init_config)

    def get_client(self, **kwargs: Any) -> ARedis:
        return self._get_client(ARedis, **kwargs)

    def create_client_lru_cache(self, maxsize: int, ttl: int) -> ALRUCache:
        async def on_connect(conn: Connection) -> None:
            await conn.on_connect()
            await conn.send_command("CLIENT TRACKING ON NOLOOP")
            response = await conn.read_response()
            if response != b"OK":
                raise redis_exceptions.ConnectionError("Could not enable tracking")

            task: asyncio.Task = asyncio.create_task(_aredis_cache_ping(client))

            async def invalidation_callback(data: Any) -> None:
                cache.flush(data[1])

            conn._parser.set_invalidation_push_handler(invalidation_callback)  # type:ignore[attr-defined]
            conn_parser_on_disconnect = conn._parser.on_disconnect

            def on_disconnect() -> None:
                task.cancel()
                cache.flush()
                conn_parser_on_disconnect()

            conn._parser.on_disconnect = on_disconnect  # type:ignore[method-assign]

        client = self._get_client(
            redis_class=_RedisCacheClient,
            protocol=3,
            decode_responses=False,
            retry=RetryConfig(redis_backoff.ConstantBackoff(0.25), 7),
            retry_on_error=[redis_exceptions.ConnectionError],
            redis_connect_func=on_connect,
        )
        client.single_connection_client = True

        cache = ALRUCache(client, maxsize, ttl)
        return cache


async def _aredis_cache_ping(redis: Redis) -> None:
    while True:
        await asyncio.sleep(randint(5, 10))
        try:
            await redis.ping()
        except redis_exceptions.ConnectionError:
            continue


class _RedisCacheClient(Redis):
    async def _send_command_parse_response(
        self,
        conn: Connection,
        command_name: str,
        *args: Any,
        enable_key_tracking: Any = None,
        **options: Any,
    ) -> Any:
        if conn.is_connected:
            # only process push requests if connected
            await conn.process_invalidation_messages()
        if command_name:
            await conn.send_command(*args)
            result = await self.parse_response(conn, command_name, **options)
            if enable_key_tracking:
                await conn.process_invalidation_messages()
                await conn.send_command("TOUCH", enable_key_tracking)
                await self.parse_response(conn, "TOUCH")
            return result
