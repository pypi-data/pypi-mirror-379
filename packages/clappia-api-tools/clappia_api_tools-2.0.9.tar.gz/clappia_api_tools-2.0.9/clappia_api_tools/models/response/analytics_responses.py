from pydantic import Field

from .base_response import BaseResponse


class ChartResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )
