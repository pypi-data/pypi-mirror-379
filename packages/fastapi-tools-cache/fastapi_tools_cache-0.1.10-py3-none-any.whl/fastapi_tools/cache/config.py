import importlib
from collections.abc import Generator, Mapping
from contextlib import contextmanager
from typing import Annotated, Any

from annotated_types import MinLen
from pydantic import BaseModel, field_validator
from redis import backoff as redis_backoff
from redis import exceptions as redis_exceptions
from redis.asyncio.retry import Retry as ARetry
from redis.retry import Retry

__all__ = (
    "RedisConfig",
    "SentinelConfig",
    "RetryConfig",
)


@contextmanager
def _catch_exceptions() -> Generator[None, None, None]:
    try:
        yield
    except Exception as e:
        raise ValueError(str(e))


def _import_object(path_or_obj: Any) -> Any:
    if isinstance(path_or_obj, str):
        if "." not in path_or_obj:
            raise ValueError(f"'{path_or_obj}' is not a valid object path")
        module, ref = path_or_obj.rsplit(".", 1)
        return getattr(importlib.import_module(module), ref)
    return path_or_obj


class RedisBackoffModel(BaseModel):
    cls: type[redis_backoff.AbstractBackoff] = redis_backoff.NoBackoff
    params: dict[str, Any] = {}

    model_config = {
        "extra": "forbid",
        "frozen": True,
        "arbitrary_types_allowed": True,
    }

    # noinspection PyNestedDecorators
    @field_validator("cls", mode="before")
    @classmethod
    def _validate_cls(cls, v: Any) -> Any:
        with _catch_exceptions():
            return _import_object(v)


class RedisRetryModel(BaseModel):
    backoff: redis_backoff.AbstractBackoff = redis_backoff.NoBackoff()
    retries: int = 1

    model_config = {
        "extra": "forbid",
        "frozen": True,
        "arbitrary_types_allowed": True,
    }

    # noinspection PyNestedDecorators
    @field_validator("backoff", mode="before")
    @classmethod
    def _validate_backoff(cls, v: Any) -> Any:
        if isinstance(v, redis_backoff.AbstractBackoff):
            return v
        instance = RedisBackoffModel.model_validate(v)
        with _catch_exceptions():
            return instance.cls(**instance.params)


class RetryConfig:
    def __init__(self, backoff: redis_backoff.AbstractBackoff, retries: int):
        self.backoff = backoff
        self.retries = retries

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(backoff={self.backoff}, retries={self.retries})"
        )


class BaseRedisConfig(BaseModel):
    db: int = 0
    username: str | None = None
    password: str | None = None
    socket_timeout: float | None = None
    socket_connect_timeout: float | None = None
    socket_keepalive: bool | None = None
    socket_keepalive_options: Mapping[str, int | str] | None = None
    retry_on_timeout: bool = False
    retry_on_error: list[type[redis_exceptions.RedisError]] | None = None
    retry: RetryConfig | None = None
    ssl: bool = False
    ssl_keyfile: str | None = None
    ssl_certfile: str | None = None
    ssl_cert_reqs: str | int | None = None
    ssl_ca_certs: str | None = None
    ssl_ca_data: str | None = None
    ssl_check_hostname: bool | None = None
    ssl_password: str | None = None
    max_connections: int | None = None
    health_check_interval: float = 0
    client_name: str | None = None

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "frozen": True,
    }

    # noinspection PyNestedDecorators
    @field_validator("retry_on_error", mode="before")
    @classmethod
    def _validate_retry_on_error(cls, v: Any) -> Any:
        if v and isinstance(v, (list, tuple)):
            with _catch_exceptions():
                return [_import_object(v) for v in v]
        return []

    # noinspection PyNestedDecorators
    @field_validator("retry", mode="before")
    @classmethod
    def _validate_retry(cls, v: Any) -> Any:
        if isinstance(v, (Retry, ARetry)):
            v = {"backoff": v._backoff, "retries": v._retries}
        elif isinstance(v, RetryConfig):
            v = v.__dict__
        instance = RedisRetryModel.model_validate(v)
        return RetryConfig(**instance.model_dump())


class RedisConfig(BaseRedisConfig):
    host: str = "localhost"
    port: int = 6379


class SentinelConfig(BaseRedisConfig):
    service_name: str
    sentinels: Annotated[list[tuple[str, int]], MinLen(min_length=1)]
    sentinel_kwargs: BaseRedisConfig | None = None
    min_other_sentinels: int = 0
