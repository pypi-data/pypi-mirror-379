from __future__ import annotations

import warnings
from asyncio import Condition, get_running_loop
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Self

from bonsai import LDAPDN, LDAPClient, LDAPEntry, LDAPSearchScope, errors
from bonsai.asyncio import AIOLDAPConnection
from pydantic import TypeAdapter

from .config import LDAPConfig


class LDAPPoolError(Exception):
    """Connection pool related errors."""


class LDAPClosedPoolError(LDAPPoolError):
    pass


class LDAPEmptyPoolError(LDAPPoolError):
    pass


LDAPConnectionErrors = (errors.ConnectionError, errors.TimeoutError)


if TYPE_CHECKING:

    class Connection(AIOLDAPConnection):
        age: float = 0.0
else:
    Connection = AIOLDAPConnection


class ConnectionPool:
    __slots__ = (
        "_connect",
        "_max_conn",
        "_max_age",
        "_idles",
        "_used",
        "_lock",
        "_closed",
    )

    def __init__(
        self,
        connect: Callable[[], Awaitable[Connection]],
        max_conn: int = 10,
        max_age: int = 300,
    ) -> None:
        self._connect = connect
        self._max_conn = max_conn
        self._max_age = max_age
        self._idles: set[Connection] = set()
        self._used: set[Connection] = set()
        self._lock = Condition()
        self._closed = False

    async def get_connection(self) -> Connection:
        async with self._lock:
            await self._lock.wait_for(
                lambda: self._idles or len(self._used) < self._max_conn or self._closed
            )
            if self._closed:
                raise LDAPClosedPoolError("Pool is closed.")
            try:
                conn = self._idles.pop()
            except KeyError:
                if len(self._used) < self._max_conn:
                    conn = await self._connect()
                    conn.age = (
                        (get_running_loop().time() + self._max_age)
                        if self._max_age > 0
                        else -1
                    )
                else:
                    raise LDAPEmptyPoolError("Pool is empty.") from None
            self._used.add(conn)
            self._lock.notify()
            return conn

    async def release_connection(self, conn: Connection) -> None:
        async with self._lock:
            if self._closed:
                raise LDAPClosedPoolError("Pool is closed.")
            try:
                self._used.remove(conn)
            except KeyError:
                raise LDAPPoolError(
                    "The %r is not managed by this pool." % conn
                ) from None
            if not conn.closed and 0 < conn.age <= get_running_loop().time():
                conn.close()
            if not conn.closed:
                self._idles.add(conn)
            self._lock.notify()

    def _close(self) -> None:
        for conn in self._idles:
            try:
                conn.close()
            except Exception as exc:
                warnings.warn(
                    f"Exception is raised during closing idle connection: {exc}",
                    ResourceWarning,
                    source=self,
                )
        for conn in self._used:
            try:
                conn.close()
            except Exception as exc:
                warnings.warn(
                    f"Exception is raised during closing used connection: {exc}",
                    ResourceWarning,
                    source=self,
                )
        self._idles = set()
        self._used = set()
        self._closed = True

    async def close(self) -> None:
        async with self._lock:
            self._close()
            self._lock.notify_all()

    def __del__(self) -> None:
        if self._idles or self._used:
            warnings.warn(f"Unclosed LDAP client {self!r}", ResourceWarning, source=self)
            try:
                context = {"client": self, "message": "Unclosed LDAP client"}
                get_running_loop().call_exception_handler(context)
            except RuntimeError:
                pass
            self._close()


class LDAPFactory:
    __slots__ = ("_init_config",)

    def __init__(self, config: LDAPConfig | None = None, /, **kwargs: Any):
        config_model: LDAPConfig = TypeAdapter(LDAPConfig).validate_python(
            {**(config.model_dump(exclude_none=True) if config else {}), **kwargs}
        )
        self._init_config = config_model.model_dump(exclude_none=True)

    def get_async_client(self, **kwargs: Any) -> LDAPAClient:
        return LDAPAClient(**{**self._init_config, **kwargs})


class LDAPAClient:
    __slots__ = ("_search_base", "_search_scope", "_pool")

    def __init__(
        self,
        server_url: str,
        search_base: str | None = None,
        search_scope: LDAPSearchScope | int | None = None,
        username: str = "",
        password: str = "",
        max_conn: int = 10,
        max_age: int = 600,
        connect_timeout: float = 1.0,
    ):
        client = LDAPClient(server_url)
        client.set_credentials("SIMPLE", user=username, password=password)
        self._search_base = search_base
        self._search_scope = search_scope
        self._pool = ConnectionPool(
            connect=lambda: client.connect(is_async=True, timeout=connect_timeout),
            max_conn=max_conn,
            max_age=max_age,
        )

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        await self.aclose()

    async def call_with_retry[T](self, do: Callable[[Connection], Awaitable[T]]) -> T:
        failures = 0
        while True:
            conn = await self._pool.get_connection()
            try:
                return await do(conn)
            except LDAPConnectionErrors:
                conn.close()
                failures += 1
                if failures > 1:
                    raise
            finally:
                await self._pool.release_connection(conn)

    async def aclose(self) -> None:
        await self._pool.close()

    async def whoami(self) -> str:
        return await self.call_with_retry(lambda c: c.whoami())

    async def search(
        self,
        filter_exp: str | None,
        /,
        base: str | LDAPDN | None = None,
        scope: LDAPSearchScope | int | None = None,
        attrlist: list[str] | None = None,
        timeout: float | None = None,
        sizelimit: int = 0,
        attrsonly: bool = False,
        sort_order: list[str] | None = None,
    ) -> LDAPEntry:
        base = self._search_base if base is None else base
        scope = self._search_scope if scope is None else scope
        return await self.call_with_retry(
            lambda c: c.search(
                base=base,
                scope=scope,
                filter_exp=filter_exp,
                attrlist=attrlist,
                timeout=timeout,
                sizelimit=sizelimit,
                attrsonly=attrsonly,
                sort_order=sort_order,
            )
        )
