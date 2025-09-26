from typing import Optional
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, HttpUrl, ConfigDict


class Owner(BaseModel):
    name: str
    identifier: str

    model_config = ConfigDict(extra="ignore")


class Customer(BaseModel):
    name: str

    model_config = ConfigDict(extra="ignore")


class Tenant(BaseModel):
    identifier: str
    production_url: HttpUrl
    uuid: UUID
    owner: Owner
    customer: Customer

    model_config = ConfigDict(extra="ignore")


class Service(BaseModel):
    id: UUID
    name: str
    slug: str
    tenant: UUID
    identifier: Optional[str] = None

    model_config = {"extra": "ignore"}


class UserRoleEnum(str, Enum):
    user = "user"
    admin = "admin"
    operator = "operator"


class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: Optional[str] = None
    role: UserRoleEnum
    tenant_url: HttpUrl
