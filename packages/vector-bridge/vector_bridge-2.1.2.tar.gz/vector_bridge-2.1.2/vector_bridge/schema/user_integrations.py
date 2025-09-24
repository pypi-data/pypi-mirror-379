from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field
from vector_bridge.schema.security_group import SecurityGroup


class Role(StrEnum):
    user = "user"
    admin = "admin"


class UserIntegration(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: str
    integration_id: str
    integration_name: str
    security_group_id: str


class UserIntegrationWithPermissions(BaseModel):
    integration_id: str
    integration_name: str
    security_group: SecurityGroup


class UserIntegrationList(BaseModel):
    user_integrations: list[UserIntegration]
    limit: int
    last_evaluated_key: str | None = Field(default=None)
