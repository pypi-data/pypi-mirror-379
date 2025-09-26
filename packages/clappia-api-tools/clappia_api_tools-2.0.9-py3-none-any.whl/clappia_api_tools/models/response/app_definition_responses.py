from pydantic import Field

from .base_response import BaseResponse


class AppDefinitionResponse(BaseResponse):
    app_id: str = Field(description="App ID")
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )


class FieldOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where field was modified")
    field_name: str | None = Field(default=None, description="Name of the field")
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )


class PageBreakOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where page break was modified")
    page_index: int | None = Field(default=None, description="Page index")
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )


class ReorderSectionOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where section was modified")
    source_section_index: int | None = Field(
        default=None, description="Source section index"
    )
    target_section_index: int | None = Field(
        default=None, description="Target section index"
    )
    source_page_index: int | None = Field(default=None, description="Source page index")
    target_page_index: int | None = Field(default=None, description="Target page index")
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )


class UpsertSectionOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where section was added")
    section_index: int | None = Field(
        default=None, description="Index where section was added"
    )
    page_index: int | None = Field(
        default=None, description="Page index where section was added"
    )
    version_variable_name: str | None = Field(
        default=None, description="Version variable name"
    )
