from typing import Any

from pydantic import Field

from .base_response import BaseResponse


class SubmissionResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    submission_id: str | None = Field(default=None, description="Submission ID")


class SubmissionsResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    metadata: dict[str, Any] | None = Field(default=None, description="Metadata")


class SubmissionsAggregationResponse(BaseResponse):
    app_id: str = Field(description="App ID")


class SubmissionsExcelResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    url: str | None = Field(
        default=None, description="Download URL for the exported file"
    )


class SubmissionsCountResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    total_count: int | None = Field(
        default=None, description="Total number of submissions"
    )
    filtered_count: int | None = Field(
        default=None, description="Number of submissions after applying filters"
    )
