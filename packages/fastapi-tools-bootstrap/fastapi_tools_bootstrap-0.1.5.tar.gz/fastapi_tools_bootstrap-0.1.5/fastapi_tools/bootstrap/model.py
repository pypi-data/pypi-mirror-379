from contextlib import AbstractAsyncContextManager, AsyncExitStack, asynccontextmanager
from functools import wraps
from typing import Any, AsyncGenerator, Awaitable, Callable, Literal, Protocol, overload

_bootstraps = []


def register[F: Callable[[Any], AbstractAsyncContextManager]](
    kind: list[str] | Literal["*"] = "*",
) -> Callable[[F], F]:
    def wrapper(func: F) -> F:
        _bootstraps.append((tuple(kind), func))
        return func

    return wrapper


type _Callback = Callable[[Any], Awaitable[None]]


@overload
def on_start[F: _Callback](__func: F, /) -> F: ...


@overload
def on_start[F: _Callback](
    *, kind: list[str] | Literal["*"] = "*"
) -> Callable[[F], F]: ...


def on_start[F: _Callback](
    __func: F | None = None, /, *, kind: list[str] | Literal["*"] = "*"
) -> Callable[[F], F] | F:
    def wrapper(func: F) -> F:
        @register(kind)
        @asynccontextmanager
        @wraps(func)
        async def on_start(app: Any) -> AsyncGenerator[None, None]:
            await func(app)
            yield

        return func

    if __func is not None:
        return wrapper(__func)
    else:
        return wrapper


@overload
def on_exit[F: _Callback](__func: F, /) -> F: ...


@overload
def on_exit[F: _Callback](
    *, kind: list[str] | Literal["*"] = "*"
) -> Callable[[F], F]: ...


def on_exit[F: _Callback](
    __func: F | None = None, /, *, kind: list[str] | Literal["*"] = "*"
) -> Callable[[F], F] | F:
    def wrapper(func: F) -> F:
        @register(kind)
        @asynccontextmanager
        @wraps(func)
        async def on_exit(app: Any) -> AsyncGenerator[None, None]:
            yield
            await func(app)

        return func

    if __func is not None:
        return wrapper(__func)
    else:
        return wrapper


class SupportsAClose(Protocol):
    async def aclose(self) -> None: ...


def close_on_exit[T: SupportsAClose](
    __obj: T, /, *, kind: list[str] | Literal["*"] = "*"
) -> T:
    @register(kind)
    @asynccontextmanager
    @wraps(__obj.aclose)
    async def on_exit(app: Any) -> AsyncGenerator[None, None]:
        yield
        await __obj.aclose()

    return __obj


def lifespan(
    kind: str | Literal["*"] = "*",
) -> Callable[[Any], AbstractAsyncContextManager]:
    if kind == "*":
        chain = tuple(c[1] for c in _bootstraps)
    else:
        chain = tuple(c[1] for c in _bootstraps if (c[0] == "*" or kind in c[0]))

    @asynccontextmanager
    async def lifespan(app: Any) -> AsyncGenerator[None, None]:
        async with AsyncExitStack() as stack:
            for c in chain:
                await stack.enter_async_context(c(app))
            yield

    return lifespan
