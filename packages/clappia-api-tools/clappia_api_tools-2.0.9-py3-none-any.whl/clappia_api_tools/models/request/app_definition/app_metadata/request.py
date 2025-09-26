import re
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator

from ....json_serialized import JsonSerializableMixin

HEX_COLOR_REGEX = re.compile(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")


class ExternalStatusDefinition(BaseModel, JsonSerializableMixin):
    name: str = Field(..., min_length=1, description="Name of the status")
    color: str = Field(
        ..., min_length=1, description="Color of the status in hex format"
    )

    @field_validator("color")
    @classmethod
    def validate_color(cls, v: str) -> str:
        if not HEX_COLOR_REGEX.match(v):
            raise ValueError(
                "Status color must be a valid hex code (e.g. #000000 or #FFF)"
            )
        return v


class UpdateAppMetadataRequest(BaseModel, JsonSerializableMixin):
    app_name: str | None = Field(
        default=None, description="Name of the app, < 30 chars"
    )
    app_description: str | None = Field(
        default=None, description="Description of the app, < 100 chars"
    )
    is_analytics_enabled: bool | None = Field(
        default=None, description="Whether analytics is enabled"
    )
    requires_authentication: bool | None = Field(
        default=None, description="Whether authentication is required"
    )
    allow_embedding: bool | None = Field(
        default=None, description="Whether embedding is allowed"
    )
    require_auth_for_submissions: bool | None = Field(
        default=None, description="Whether authentication is required for submissions"
    )
    can_user_submit: bool | None = Field(
        default=None, description="Whether user can submit"
    )
    can_user_save_draft: bool | None = Field(
        default=None, description="Whether user can save draft"
    )
    statuses: list[ExternalStatusDefinition] | None = Field(
        default=None,
        min_length=1,
        description="Statuses of the app, they can be used to review submissions. Example: [{'name': 'Pending', 'color': '#000000'}, {'name': 'Approved', 'color': '#000000'}]",
    )
    post_submission_message_text: str | None = Field(
        default=None,
        description="Post submission message text, can contain field references. Example: 'Thank you for submitting your form. The submission id is {submissionId}.'",
    )
    submit_button_label: str | None = Field(
        default=None, description="Submit button label"
    )
    submission_display_name: str | None = Field(
        default=None, description="Custom submission display name, < 30 chars"
    )
    allow_viewing_submissions: bool | None = Field(
        default=None, description="Whether viewing submissions is allowed"
    )
    allow_submit_another: bool | None = Field(
        default=None, description="Whether submitting another is allowed"
    )
    allow_printing_submissions: bool | None = Field(
        default=None, description="Whether printing submissions is allowed"
    )
    save_draft_button_label: str | None = Field(
        default=None, description="Label for save draft button"
    )
    discard_draft_button_label: str | None = Field(
        default=None, description="Label for discard draft button"
    )
    print_submission_button_label: str | None = Field(
        default=None, description="Label for print submission button"
    )
    view_submissions_button_label: str | None = Field(
        default=None, description="Label for view submissions button"
    )
    submit_another_button_label: str | None = Field(
        default=None, description="Label for submit another button"
    )
    submission_view_mode: Literal["modal", "rightPanel"] | None = Field(
        default=None, description="Submission view mode (modal or rightPanel)"
    )
    default_app_view: Literal["appHome", "analytics", "submissions"] | None = Field(
        default=None, description="Default app view (appHome, analytics, submissions)"
    )

    @field_validator("app_name")
    @classmethod
    def validate_app_name(cls, v: str | None) -> str | None:
        if v is not None and len(v) > 30:
            raise ValueError("app_name must be less than 30 characters")
        return v

    @field_validator("app_description")
    @classmethod
    def validate_app_description(cls, v: str | None) -> str | None:
        if v is not None and len(v) > 100:
            raise ValueError("app_description must be less than 100 characters")
        return v

    @field_validator("submission_display_name")
    @classmethod
    def validate_submission_display_name(cls, v: str | None) -> str | None:
        if v is not None:
            if len(v) == 0:
                raise ValueError("submission_display_name cannot be empty")
            if len(v) > 30:
                raise ValueError(
                    "submission_display_name must be less than 30 characters"
                )
        return v

    @model_validator(mode="after")
    def validate_statuses_unique(self) -> "UpdateAppMetadataRequest":
        if self.statuses:
            names = [s.name for s in self.statuses]
            if len(names) != len(set(names)):
                raise ValueError("statuses must not contain duplicate names")
        return self
