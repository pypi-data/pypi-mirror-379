from typing import Any

from pydantic import BaseModel, Field

from ..workplace_user import WorkplaceUser
from .base_response import BaseResponse


class AppMetaData(BaseModel):
    """Response model for app metadata"""

    app_id: str = Field(description="App ID")
    name: str = Field(description="App name")
    created_at: int = Field(description="App created at")
    created_by: dict[str, Any] = Field(description="App created by")
    updated_at: int = Field(description="App updated at")
    updated_by: dict[str, Any] = Field(description="App updated by")

    @classmethod
    def from_json(cls, json_data: dict[str, Any]) -> "AppMetaData":
        """Create AppMetaData instance from JSON data with proper field mapping"""
        mapped_data = {
            "app_id": json_data.get("appId", ""),
            "name": json_data.get("name", ""),
            "created_at": json_data.get("createdAt", 0),
            "created_by": json_data.get("createdBy", {}),
            "updated_at": json_data.get("lastUpdatedAt", 0),
            "updated_by": json_data.get("lastUpdatedBy", {}),
        }
        return cls(**mapped_data)


# For get workplace user apps
class AppUserMetaData(BaseModel):
    """Response model for app metadata"""

    app_id: str = Field(description="App ID")
    name: str = Field(description="App name")

    @classmethod
    def from_json(cls, json_data: dict[str, Any]) -> "AppUserMetaData":
        """Create AppUserMetaData instance from JSON data with proper field mapping"""
        mapped_data = {
            "app_id": json_data.get("appId", ""),
            "name": json_data.get("name", ""),
        }
        return cls(**mapped_data)


class AppUserResponse(BaseResponse):
    """Response model for app user operations"""

    app_id: str = Field(description="App ID")
    permissions: dict[str, bool] | None = Field(
        default=None, description="User permissions"
    )


class WorkplaceUsersResponse(BaseResponse):
    """Response model for workplace users operations"""

    users: list[WorkplaceUser] = Field(description="List of users")
    token: str | None = Field(default=None, description="Token, needed for pagination")
