from bonsai import LDAPSearchScope
from pydantic import BaseModel, ConfigDict


class LDAPConfig(BaseModel):
    server_url: str
    search_base: str | None = None
    search_scope: LDAPSearchScope | None = None
    username: str = ""
    password: str = ""
    max_conn: int = 10
    max_age: int = 600
    connect_timeout: float = 1.0

    model_config = ConfigDict(frozen=True, extra="forbid")
