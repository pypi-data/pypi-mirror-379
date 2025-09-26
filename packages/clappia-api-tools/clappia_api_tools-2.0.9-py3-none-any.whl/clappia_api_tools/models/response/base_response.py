from typing import Any

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    success: bool = Field(description="Whether operation was successful")
    message: str | None = Field(default=None, description="Response message")
    data: Any | None = Field(default=None, description="Response data")
    operation: str | None = Field(
        default=None, description="Type of operation performed"
    )
