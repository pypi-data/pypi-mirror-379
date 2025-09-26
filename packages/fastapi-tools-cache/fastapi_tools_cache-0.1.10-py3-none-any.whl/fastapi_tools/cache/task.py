from __future__ import annotations

import asyncio
import base64
import functools
import pickle
from hashlib import blake2b
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Self,
    get_type_hints,
)

if TYPE_CHECKING:
    from .protocol import RedisClientProtocol


__all__ = (
    "TaskState",
    "TaskRunningError",
    "TaskManager",
    "TaskLogger",
    "Task",
)


class Task:
    __slots__ = (
        "name",
        "trace_id",
        "_executor",
        "_call_after",
    )

    def __init__(
        self,
        executor: Callable[[], Awaitable[None]],
        name: str,
        trace_id: str,
        call_after: list[tuple[Callable[..., Awaitable[None]], Any]],
    ) -> None:
        self.name = name
        self.trace_id = trace_id
        self._executor = executor
        self._call_after = call_after

    def call_after[*P](
        self,
        func: Callable[[*P], Awaitable[None]],
        *args: *P,
    ) -> Self:
        self._call_after.append((func, args))
        return self

    async def __call__(self) -> None:
        await self._executor()

    def __repr__(self) -> str:
        return f"Task<{self.name}, {self.trace_id}>"


type TaskLogger = Callable[[str], Awaitable[None]]


def hashkey(prefix: tuple[Any, ...], args: tuple[Any, ...]) -> bytes:
    return blake2b(repr((prefix, args)).encode(), digest_size=24).digest()


class TaskManager:
    __slots__ = (
        "_client",
        "_group_prefix",
        "_running_time_limit",
        "_result_expires_in",
        "_error_expires_in",
        "_logger_arg_cache",
    )

    _logger_arg_cache: dict[Callable[..., Awaitable[Any]], bool]

    def __init__(
        self,
        client: RedisClientProtocol,
        group_name: str,
        running_time_limit: int = 600,
        result_expires_in: int = 3600,
        error_expires_in: int = 60,
    ):
        self._client = client
        self._group_prefix = b"task_group:" + group_name.encode() + b":"
        self._running_time_limit = running_time_limit
        self._result_expires_in = result_expires_in
        self._error_expires_in = error_expires_in
        self._logger_arg_cache = {}

    async def get_task_state(self, trace_id: str) -> TaskState | None:
        try:
            key = base64.b64decode(trace_id.encode())
        except ValueError:
            return None
        if len(key) != 48:
            return None
        return await self._get_task_state(key[:24], key[24:])

    async def list_running_tasks[T](
        self, func: Callable[..., Awaitable[T]]
    ) -> list[TaskState[T]]:
        data = await self._client.hgetall(
            self._group_prefix + self._get_task_group_id(func)
        )
        if data:
            return [pickle.loads(s) for s in data.values()]
        return []

    def add_task[*P, T](
        self,
        func: Callable[[TaskLogger, *P], Awaitable[T]] | Callable[[*P], Awaitable[T]],
        *args: *P,
        task_key: tuple[Any, ...] | None = None,
        running_time_limit: int | None = None,
        result_expires_in: int | None = None,
        error_expires_in: int | None = None,
    ) -> Task:
        name, group_id, trace_id = self._get_task_name_group_id_and_trace_id(
            func, args if task_key is None else task_key
        )
        return self._create_task(
            name,
            group_id,
            trace_id,
            func,
            args,
            running_time_limit or self._running_time_limit,
            result_expires_in or self._result_expires_in,
            error_expires_in or self._error_expires_in,
        )

    async def get_task_result[*P, T](
        self,
        func: Callable[[TaskLogger, *P], Awaitable[T]] | Callable[[*P], Awaitable[T]],
        *args: *P,
        task_key: Any = None,
        running_time_limit: int | None = None,
        result_expires_in: int | None = None,
        error_expires_in: int | None = None,
    ) -> TaskState[T] | Task:
        name, group_id, trace_id = self._get_task_name_group_id_and_trace_id(
            func, args if task_key is None else task_key
        )
        if state := await self._get_task_state(group_id, trace_id):
            return state
        return self._create_task(
            name,
            group_id,
            trace_id,
            func,
            args,
            running_time_limit or self._running_time_limit,
            result_expires_in or self._result_expires_in,
            error_expires_in or self._error_expires_in,
        )

    @staticmethod
    def _get_func_name(func: Any) -> str:
        return f"{func.__module__}.{func.__name__}"

    def _get_task_group_id(self, func: Any) -> bytes:
        return blake2b(
            self._group_prefix + self._get_func_name(func).encode(),
            digest_size=24,
            person=b"task-manager",
        ).digest()

    def _get_task_name_group_id_and_trace_id(
        self, func: Any, args: tuple[Any, ...]
    ) -> tuple[str, bytes, bytes]:
        name = self._get_func_name(func)
        h = blake2b(
            self._group_prefix + name.encode(), digest_size=24, person=b"task-manager"
        )
        group_id = h.digest()
        h.update(repr(args).encode())
        trace_id = h.digest()
        return name, group_id, trace_id

    async def _get_task_state(
        self, group_id: bytes, trace_id: bytes
    ) -> TaskState | None:
        if resp := await self._client.hget(self._group_prefix + group_id, trace_id):
            return pickle.loads(resp)
        return None

    def _get_logger_arg(self, func: Callable[..., Awaitable[Any]]) -> bool:
        try:
            return self._logger_arg_cache[func]
        except KeyError:
            result = False
            for ann in get_type_hints(func).values():
                result = ann in (TaskLogger, TaskLogger.__value__)
                break
            self._logger_arg_cache[func] = result
            return result

    def _create_task(
        self,
        name: str,
        group_id: bytes,
        trace_id: bytes,
        func: Callable[..., Awaitable[Any]],
        args: tuple[Any, ...],
        running_time_limit: int,
        result_expires_in: int,
        error_expires_in: int,
    ) -> Task:
        call_after: list[tuple[Callable[..., Awaitable[None]], Any]] = []
        client = self._client
        group_key = self._group_prefix + group_id
        lock_key = self._group_prefix + b"lock:" + trace_id
        logger_arg = self._get_logger_arg(func)

        async def executor() -> None:
            if not await client.set(lock_key, b"1", ex=running_time_limit + 1, nx=True):
                # Кто-то запустил таску раньше нас, выходим
                return None

            state: TaskStateRunning = TaskStateRunning([], name, args)
            await (
                client.pipeline()
                .hset(group_key, trace_id, pickle.dumps(state))
                .hexpire(group_key, running_time_limit, trace_id)
                .execute()
            )

            if logger_arg:

                async def logger(text: str) -> None:
                    state._log.append(text)
                    ttl = (await client.httl(group_key, trace_id))[0]
                    if ttl > 0:
                        await (
                            client.pipeline()
                            .hset(group_key, trace_id, pickle.dumps(state))
                            .hexpire(group_key, ttl, trace_id)
                            .execute()
                        )

                runnable: Any = functools.partial(func, logger)
            else:
                runnable = func

            try:
                expires_in = result_expires_in
                try:
                    async with asyncio.timeout(running_time_limit):
                        try:
                            result: TaskState = TaskStateDone(
                                await runnable(*args), name, args
                            )
                        except Exception as err:
                            expires_in = error_expires_in
                            result = TaskStateError(err, name, args)
                except TimeoutError:
                    expires_in = error_expires_in
                    result = TaskStateTimeout(name, args)
                await (
                    client.pipeline()
                    .hset(group_key, trace_id, pickle.dumps(result))
                    .hexpire(group_key, expires_in, trace_id)
                    .execute()
                )
            finally:
                await client.delete(lock_key)

            if call_after and result and result.is_done():
                for after_func, after_args in call_after:
                    await after_func(*after_args)

        return Task(
            executor, name, base64.b64encode(group_id + trace_id).decode(), call_after
        )


class TaskRunningError(RuntimeError):
    pass


class TaskState[T]:
    __slots__ = ("name", "args", "trace_id")

    def __init__(self, name: str, args: tuple[Any, ...]) -> None:
        self.name = name
        self.args = args

    async def __call__(self) -> None:
        raise TaskRunningError("Invalid flow")

    @staticmethod
    def get_status() -> str:
        raise TaskRunningError("Invalid flow")

    @staticmethod
    def is_running() -> bool:
        return False

    @staticmethod
    def is_done() -> bool:
        return False

    @staticmethod
    def is_error() -> bool:
        return False

    @staticmethod
    def is_timeout() -> bool:
        return False

    def get_log(self) -> list[str]:
        raise TaskRunningError("Invalid flow")

    def get_result(self) -> T:
        raise TaskRunningError("Invalid flow")

    def get_error(self) -> Exception:
        raise TaskRunningError("Invalid flow")


class TaskStateRunning[T](TaskState[T]):
    __slots__ = ("_log",)

    def __init__(self, log: list[str], name: str, args: tuple[Any, ...]) -> None:
        super().__init__(name, args)
        self._log = log

    @staticmethod
    def get_status() -> str:
        return "running"

    @staticmethod
    def is_running() -> bool:
        return True

    def get_log(self) -> list[str]:
        return self._log


class TaskStateDone[T](TaskState[T]):
    __slots__ = ("_result",)

    def __init__(self, result: Any, name: str, args: tuple[Any, ...]) -> None:
        super().__init__(name, args)
        self._result = result

    @staticmethod
    def get_status() -> str:
        return "done"

    def get_result(self) -> T:
        return self._result

    @staticmethod
    def is_done() -> bool:
        return True


class TaskStateError[T](TaskState[T]):
    __slots__ = ("_error",)

    def __init__(self, error: Exception, name: str, args: tuple[Any, ...]) -> None:
        super().__init__(name, args)
        self._error = error

    @staticmethod
    def get_status() -> str:
        return "error"

    @staticmethod
    def is_error() -> bool:
        return True

    def get_error(self) -> Exception:
        return self._error


class TaskStateTimeout[T](TaskState[T]):
    __slots__ = ()

    @staticmethod
    def get_status() -> str:
        return "timeout"

    @staticmethod
    def is_timeout() -> bool:
        return True
