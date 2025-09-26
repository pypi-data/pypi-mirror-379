from pydantic import Field

from .base_response import BaseResponse


class WorkflowResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )


class WorkflowStepResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    step_variable_name: str | None = Field(
        default=None, description="Variable name of the affected step"
    )
    parent_step_variable_name: str | None = Field(
        default=None, description="Parent step variable name"
    )
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )
