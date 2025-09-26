from abc import ABC

from clappia_api_tools.enums import FieldType
from clappia_api_tools.models.request import (
    AddPageBreakRequest,
    CreateAppRequest,
    ReorderSectionRequest,
    UpdateAppMetadataRequest,
    UpdatePageBreakRequest,
    UpsertFieldAddressRequest,
    UpsertFieldAIRequest,
    UpsertFieldButtonRequest,
    UpsertFieldCheckboxRequest,
    UpsertFieldCodeReaderRequest,
    UpsertFieldCodeRequest,
    UpsertFieldCounterRequest,
    UpsertFieldDatabaseRequest,
    UpsertFieldDateRequest,
    UpsertFieldDependencyAppRequest,
    UpsertFieldDropdownRequest,
    UpsertFieldEazypayPaymentGatewayRequest,
    UpsertFieldEmailInputRequest,
    UpsertFieldEmojiRequest,
    UpsertFieldFileRequest,
    UpsertFieldFormulaRequest,
    UpsertFieldGpsLocationRequest,
    UpsertFieldImageViewerRequest,
    UpsertFieldLiveTrackingRequest,
    UpsertFieldManualAddressRequest,
    UpsertFieldNfcReaderRequest,
    UpsertFieldNumberInputRequest,
    UpsertFieldPaypalPaymentGatewayRequest,
    UpsertFieldPdfViewerRequest,
    UpsertFieldPhoneNumberRequest,
    UpsertFieldProgressBarRequest,
    UpsertFieldRadioRequest,
    UpsertFieldRazorpayPaymentGatewayRequest,
    UpsertFieldReadOnlyFileRequest,
    UpsertFieldReadOnlyTextRequest,
    UpsertFieldRestApiRequest,
    UpsertFieldRichTextEditorRequest,
    UpsertFieldSignatureRequest,
    UpsertFieldSliderRequest,
    UpsertFieldStripePaymentGatewayRequest,
    UpsertFieldTagsRequest,
    UpsertFieldTextAreaRequest,
    UpsertFieldTextRequest,
    UpsertFieldTimeRequest,
    UpsertFieldToggleRequest,
    UpsertFieldUniqueSequentialRequest,
    UpsertFieldUrlInputRequest,
    UpsertFieldValidationRequest,
    UpsertFieldVideoViewerRequest,
    UpsertFieldVoiceRequest,
    UpsertSectionRequest,
)
from clappia_api_tools.models.response import (
    AppDefinitionResponse,
    BaseResponse,
    FieldOperationResponse,
    PageBreakOperationResponse,
    ReorderSectionOperationResponse,
    UpsertSectionOperationResponse,
)
from clappia_api_tools.utils.logging_utils import get_logger

from .base_client import BaseAPIKeyClient, BaseAuthTokenClient, BaseClappiaClient

# Union type for all field request types
FieldRequestUnion = (
    UpsertFieldTextRequest
    | UpsertFieldTextAreaRequest
    | UpsertFieldDependencyAppRequest
    | UpsertFieldRestApiRequest
    | UpsertFieldAddressRequest
    | UpsertFieldDatabaseRequest
    | UpsertFieldDateRequest
    | UpsertFieldAIRequest
    | UpsertFieldCodeRequest
    | UpsertFieldCodeReaderRequest
    | UpsertFieldEmailInputRequest
    | UpsertFieldEmojiRequest
    | UpsertFieldFileRequest
    | UpsertFieldGpsLocationRequest
    | UpsertFieldLiveTrackingRequest
    | UpsertFieldManualAddressRequest
    | UpsertFieldPhoneNumberRequest
    | UpsertFieldProgressBarRequest
    | UpsertFieldSignatureRequest
    | UpsertFieldCounterRequest
    | UpsertFieldSliderRequest
    | UpsertFieldTimeRequest
    | UpsertFieldToggleRequest
    | UpsertFieldValidationRequest
    | UpsertFieldVideoViewerRequest
    | UpsertFieldVoiceRequest
    | UpsertFieldFormulaRequest
    | UpsertFieldImageViewerRequest
    | UpsertFieldRichTextEditorRequest
    | UpsertFieldNfcReaderRequest
    | UpsertFieldNumberInputRequest
    | UpsertFieldPdfViewerRequest
    | UpsertFieldReadOnlyFileRequest
    | UpsertFieldReadOnlyTextRequest
    | UpsertFieldTagsRequest
    | UpsertFieldUniqueSequentialRequest
    | UpsertFieldDropdownRequest
    | UpsertFieldRadioRequest
    | UpsertFieldUrlInputRequest
    | UpsertFieldCheckboxRequest
    | UpsertFieldRazorpayPaymentGatewayRequest
    | UpsertFieldEazypayPaymentGatewayRequest
    | UpsertFieldPaypalPaymentGatewayRequest
    | UpsertFieldStripePaymentGatewayRequest
    | UpsertFieldButtonRequest
)

logger = get_logger(__name__)


class AppDefinitionClient(BaseClappiaClient, ABC):
    """Abstract client for managing Clappia app definitions.

    This client handles retrieving and managing app definitions, including
    getting app definitions, creating apps, adding fields, and updating fields.

    Note: This is an abstract base class that contains business logic but no authentication.
    Use AppDefinitionAPIKeyClient or AppDefinitionAuthTokenClient for actual usage.
    """

    def create_app(self, request: CreateAppRequest) -> BaseResponse:
        """Create a new app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False, message=env_error, operation="create_app"
            )

        payload = request.to_json()

        logger.info(f"Creating app with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/createApp",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False, message=error_message, operation="create_app"
            )

        return BaseResponse(
            success=True,
            message="Successfully created app",
            data=response_data,
            operation="create_app",
        )

    def get_definition(
        self, app_id: str, version_variable_name: str | None = None
    ) -> AppDefinitionResponse:
        """Retrieve the complete definition for a specific app."""
        params = {"appId": app_id}
        if version_variable_name:
            params["versionVariableName"] = version_variable_name

        logger.info(f"Getting app definition for app_id: {app_id}")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET", endpoint="/getAppDefinition", params=params
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppDefinitionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="get_definition",
            )

        return AppDefinitionResponse(
            success=True,
            message="Successfully retrieved app definition",
            app_id=app_id,
            version_variable_name=version_variable_name,
            data=response_data,
            operation="get_definition",
        )

    def add_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: FieldRequestUnion,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a field to a Clappia app.

        Args:
            app_id: The ID of the app to add the field to
            section_index: The index of the section
            field_index: The index of the field
            page_index: The index of the page
            field_name: The name of the field
            request: The request object containing the field configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used
        Returns:
            FieldOperationResponse: Response containing the result of the operation
        """
        if isinstance(request, UpsertFieldTextRequest):
            return self._add_text_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldTextAreaRequest):
            return self._add_textarea_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldDependencyAppRequest):
            return self._add_dependency_app_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldRestApiRequest):
            return self._add_rest_api_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldAddressRequest):
            return self._add_address_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldDatabaseRequest):
            return self._add_database_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldDateRequest):
            return self._add_date_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldAIRequest):
            return self._add_ai_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldCodeRequest):
            return self._add_code_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldCodeReaderRequest):
            return self._add_code_reader_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldEmailInputRequest):
            return self._add_email_input_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldEmojiRequest):
            return self._add_emoji_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldFileRequest):
            return self._add_file_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldGpsLocationRequest):
            return self._add_gps_location_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldLiveTrackingRequest):
            return self._add_live_tracking_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldManualAddressRequest):
            return self._add_manual_address_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldPhoneNumberRequest):
            return self._add_phone_number_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldProgressBarRequest):
            return self._add_progress_bar_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldSignatureRequest):
            return self._add_signature_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldCounterRequest):
            return self._add_counter_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldSliderRequest):
            return self._add_slider_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldTimeRequest):
            return self._add_time_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldToggleRequest):
            return self._add_toggle_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldValidationRequest):
            return self._add_validation_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldVideoViewerRequest):
            return self._add_video_viewer_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldVoiceRequest):
            return self._add_voice_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldFormulaRequest):
            return self._add_formula_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldImageViewerRequest):
            return self._add_image_viewer_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldRichTextEditorRequest):
            return self._add_rich_text_editor_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldNfcReaderRequest):
            return self._add_nfc_reader_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldNumberInputRequest):
            return self._add_number_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldPdfViewerRequest):
            return self._add_pdf_viewer_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldReadOnlyFileRequest):
            return self._add_read_only_file_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldReadOnlyTextRequest):
            return self._add_read_only_text_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldTagsRequest):
            return self._add_tag_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldUniqueSequentialRequest):
            return self._add_unique_sequential_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldDropdownRequest):
            return self._add_drop_down_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldRadioRequest):
            return self._add_radio_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldUrlInputRequest):
            return self._add_url_input_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldCheckboxRequest):
            return self._add_checkbox_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldRazorpayPaymentGatewayRequest):
            return self._add_razorpay_payment_gateway_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldEazypayPaymentGatewayRequest):
            return self._add_eazypay_payment_gateway_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldPaypalPaymentGatewayRequest):
            return self._add_paypal_payment_gateway_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldStripePaymentGatewayRequest):
            return self._add_stripe_payment_gateway_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        elif isinstance(request, UpsertFieldButtonRequest):
            return self._add_button_field(
                app_id,
                section_index,
                field_index,
                page_index,
                field_name,
                request,
                version_variable_name,
            )
        else:
            raise ValueError(f"Unsupported field request type: {type(request)}")

    def update_field(
        self,
        app_id: str,
        field_name: str,
        request: FieldRequestUnion,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a field in a Clappia app.

        Args:
            app_id: The ID of the app containing the field
            field_name: The name of the field
            request: The request object containing the updated field configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            FieldOperationResponse: Response containing the result of the operation
        """
        if isinstance(request, UpsertFieldTextRequest):
            return self._update_text_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldTextAreaRequest):
            return self._update_textarea_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldDependencyAppRequest):
            return self._update_dependency_app_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldRestApiRequest):
            return self._update_rest_api_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldAddressRequest):
            return self._update_address_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldDatabaseRequest):
            return self._update_database_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldDateRequest):
            return self._update_date_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldAIRequest):
            return self._update_ai_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldCodeRequest):
            return self._update_code_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldCodeReaderRequest):
            return self._update_code_reader_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldEmailInputRequest):
            return self._update_email_input_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldEmojiRequest):
            return self._update_emoji_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldFileRequest):
            return self._update_file_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldGpsLocationRequest):
            return self._update_gps_location_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldLiveTrackingRequest):
            return self._update_live_tracking_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldManualAddressRequest):
            return self._update_manual_address_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldPhoneNumberRequest):
            return self._update_phone_number_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldProgressBarRequest):
            return self._update_progress_bar_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldSignatureRequest):
            return self._update_signature_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldCounterRequest):
            return self._update_counter_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldSliderRequest):
            return self._update_slider_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldTimeRequest):
            return self._update_time_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldToggleRequest):
            return self._update_toggle_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldValidationRequest):
            return self._update_validation_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldVideoViewerRequest):
            return self._update_video_viewer_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldVoiceRequest):
            return self._update_voice_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldFormulaRequest):
            return self._update_formula_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldImageViewerRequest):
            return self._update_image_viewer_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldRichTextEditorRequest):
            return self._update_rich_text_editor_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldNfcReaderRequest):
            return self._update_nfc_reader_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldNumberInputRequest):
            return self._update_number_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldPdfViewerRequest):
            return self._update_pdf_viewer_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldReadOnlyFileRequest):
            return self._update_read_only_file_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldReadOnlyTextRequest):
            return self._update_read_only_text_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldTagsRequest):
            return self._update_tag_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldUniqueSequentialRequest):
            return self._update_unique_sequential_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldDropdownRequest):
            return self._update_drop_down_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldRadioRequest):
            return self._update_radio_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldUrlInputRequest):
            return self._update_url_input_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldCheckboxRequest):
            return self._update_checkbox_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldRazorpayPaymentGatewayRequest):
            return self._update_razorpay_payment_gateway_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldEazypayPaymentGatewayRequest):
            return self._update_eazypay_payment_gateway_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldPaypalPaymentGatewayRequest):
            return self._update_paypal_payment_gateway_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldStripePaymentGatewayRequest):
            return self._update_stripe_payment_gateway_field(
                app_id, field_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFieldButtonRequest):
            return self._update_button_field(
                app_id, field_name, request, version_variable_name
            )
        else:
            raise ValueError(f"Unsupported field request type: {type(request)}")

    def reorder_field(
        self,
        app_id: str,
        source_page_index: int,
        target_page_index: int,
        source_section_index: int,
        target_section_index: int,
        index_in_target_section: int,
        field_name: str,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Reorder a field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="reorder_field",
            )

        payload = {
            "appId": app_id,
            "sourcePageIndex": source_page_index,
            "targetPageIndex": target_page_index,
            "sourceSectionIndex": source_section_index,
            "targetSectionIndex": target_section_index,
            "indexInTargetSection": index_in_target_section,
            "fieldName": field_name,
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(f"Reordering field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/reorderField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="reorder_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully reordered field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            field_name=field_name,
            operation="reorder_field",
            data=response_data,
        )

    def _add_text_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldTextRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a text field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_text_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.SINGLE_LINE_TEXT.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding text field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_text_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added text field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_text_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_text_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldTextRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a text field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_text_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating text field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_text_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated text field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_text_field",
            field_name=field_name,
            data=response_data,
        )

    # TextArea Field Methods
    def _add_textarea_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldTextAreaRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a textarea field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_textarea_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.MULTI_LINE_TEXT.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding textarea field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_textarea_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added textarea field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_textarea_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_textarea_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldTextAreaRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a textarea field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_textarea_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating textarea field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_textarea_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated textarea field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_textarea_field",
            field_name=field_name,
            data=response_data,
        )

    # Dependency App Field Methods
    def _add_dependency_app_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldDependencyAppRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a dependency app field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_dependency_app_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.GET_DATA_FROM_OTHER_APPS.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding dependency app field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_dependency_app_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added dependency app field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_dependency_app_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_dependency_app_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldDependencyAppRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a dependency app field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_dependency_app_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating dependency app field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_dependency_app_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated dependency app field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_dependency_app_field",
            field_name=field_name,
            data=response_data,
        )

    # Rest API Field Methods
    def _add_rest_api_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldRestApiRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a REST API field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_rest_api_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.GET_DATA_FROM_REST_APIS.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding REST API field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_rest_api_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added REST API field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_rest_api_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_rest_api_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldRestApiRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a REST API field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_rest_api_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating REST API field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_rest_api_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated REST API field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_rest_api_field",
            field_name=field_name,
            data=response_data,
        )

    # Address Field Methods
    def _add_address_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldAddressRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add an address field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_address_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.GEO_ADDRESS.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding address field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_address_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added address field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_address_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_address_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldAddressRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update an address field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_address_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating address field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_address_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated address field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_address_field",
            field_name=field_name,
            data=response_data,
        )

    # Database Field Methods
    def _add_database_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldDatabaseRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a database field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_database_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.DATABASE.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding database field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_database_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added database field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_database_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_database_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldDatabaseRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a database field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_database_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating database field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_database_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated database field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_database_field",
            field_name=field_name,
            data=response_data,
        )

    # Date Field Methods
    def _add_date_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldDateRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a date field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_date_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.DATE_SELECTOR.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding date field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_date_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added date field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_date_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_date_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldDateRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a date field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_date_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating date field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_date_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated date field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_date_field",
            field_name=field_name,
            data=response_data,
        )

    # AI Field Methods
    def _add_ai_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldAIRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add an AI field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_ai_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.AI.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding AI field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_ai_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added AI field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_ai_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_ai_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldAIRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update an AI field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_ai_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating AI field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_ai_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated AI field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_ai_field",
            field_name=field_name,
            data=response_data,
        )

    # Code Field Methods
    def _add_code_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldCodeRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a code field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_code_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.CODE.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding code field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_code_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added code field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_code_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_code_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldCodeRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a code field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_code_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating code field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_code_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated code field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_code_field",
            field_name=field_name,
            data=response_data,
        )

    # Code Reader Field Methods
    def _add_code_reader_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldCodeReaderRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a code reader field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_code_reader_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.CODE_SCANNER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding code reader field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_code_reader_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added code reader field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_code_reader_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_code_reader_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldCodeReaderRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a code reader field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_code_reader_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating code reader field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_code_reader_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated code reader field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_code_reader_field",
            field_name=field_name,
            data=response_data,
        )

    # Email Input Field Methods
    def _add_email_input_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldEmailInputRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add an email input field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_email_input_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.EMAIL_INPUT.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding email input field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_email_input_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added email input field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_email_input_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_email_input_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldEmailInputRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update an email input field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_email_input_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating email input field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_email_input_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated email input field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_email_input_field",
            field_name=field_name,
            data=response_data,
        )

    # Emoji Field Methods
    def _add_emoji_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldEmojiRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add an emoji field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_emoji_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.RATINGS.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding emoji field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_emoji_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added emoji field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_emoji_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_emoji_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldEmojiRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update an emoji field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_emoji_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating emoji field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_emoji_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated emoji field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_emoji_field",
            field_name=field_name,
            data=response_data,
        )

    # File Field Methods
    def _add_file_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldFileRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a file field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_file_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.FILE.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding file field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_file_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added file field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_file_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_file_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldFileRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a file field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_file_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating file field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_file_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated file field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_file_field",
            field_name=field_name,
            data=response_data,
        )

    # GPS Location Field Methods
    def _add_gps_location_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldGpsLocationRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a GPS location field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_gps_location_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.GPS_LOCATION.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding GPS location field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_gps_location_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added GPS location field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_gps_location_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_gps_location_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldGpsLocationRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a GPS location field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_gps_location_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating GPS location field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_gps_location_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated GPS location field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_gps_location_field",
            field_name=field_name,
            data=response_data,
        )

    # Live Tracking Field Methods
    def _add_live_tracking_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldLiveTrackingRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a live tracking field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_live_tracking_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.LIVE_TRACKING.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding live tracking field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_live_tracking_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added live tracking field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_live_tracking_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_live_tracking_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldLiveTrackingRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a live tracking field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_live_tracking_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating live tracking field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_live_tracking_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated live tracking field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_live_tracking_field",
            field_name=field_name,
            data=response_data,
        )

    # Manual Address Field Methods
    def _add_manual_address_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldManualAddressRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a manual address field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_manual_address_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.ADDRESS.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding manual address field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_manual_address_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added manual address field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_manual_address_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_manual_address_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldManualAddressRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a manual address field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_manual_address_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating manual address field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_manual_address_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated manual address field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_manual_address_field",
            field_name=field_name,
            data=response_data,
        )

    # Phone Number Field Methods
    def _add_phone_number_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldPhoneNumberRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a phone number field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_phone_number_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.PHONE_NUMBER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding phone number field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_phone_number_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added phone number field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_phone_number_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_phone_number_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldPhoneNumberRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a phone number field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_phone_number_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating phone number field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_phone_number_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated phone number field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_phone_number_field",
            field_name=field_name,
            data=response_data,
        )

    # Progress Bar Field Methods
    def _add_progress_bar_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldProgressBarRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a progress bar field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_progress_bar_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.PROGRESS_BAR.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding progress bar field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_progress_bar_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added progress bar field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_progress_bar_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_progress_bar_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldProgressBarRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a progress bar field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_progress_bar_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating progress bar field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_progress_bar_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated progress bar field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_progress_bar_field",
            field_name=field_name,
            data=response_data,
        )

    # Signature Field Methods
    def _add_signature_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldSignatureRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a signature field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_signature_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.SIGNATURE.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding signature field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_signature_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added signature field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_signature_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_signature_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldSignatureRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a signature field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_signature_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating signature field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_signature_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated signature field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_signature_field",
            field_name=field_name,
            data=response_data,
        )

    # Counter Field Methods
    def _add_counter_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldCounterRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a counter field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_counter_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.COUNTER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding counter field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_counter_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added counter field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_counter_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_counter_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldCounterRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a counter field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_counter_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating counter field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_counter_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated counter field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_counter_field",
            field_name=field_name,
            data=response_data,
        )

    # Slider Field Methods
    def _add_slider_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldSliderRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a slider field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_slider_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.SLIDER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding slider field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_slider_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added slider field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_slider_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_slider_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldSliderRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a slider field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_slider_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating slider field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_slider_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated slider field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_slider_field",
            field_name=field_name,
            data=response_data,
        )

    # Time Field Methods
    def _add_time_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldTimeRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a time field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_time_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.TIME_SELECTOR.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding time field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_time_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added time field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_time_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_time_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldTimeRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a time field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_time_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating time field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_time_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated time field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_time_field",
            field_name=field_name,
            data=response_data,
        )

    # Toggle Field Methods
    def _add_toggle_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldToggleRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a toggle field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_toggle_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.TOGGLE.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding toggle field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_toggle_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added toggle field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_toggle_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_toggle_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldToggleRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a toggle field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_toggle_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating toggle field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_toggle_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated toggle field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_toggle_field",
            field_name=field_name,
            data=response_data,
        )

    # Validation Field Methods
    def _add_validation_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldValidationRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a validation field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_validation_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.VALIDATION.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding validation field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_validation_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added validation field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_validation_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_validation_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldValidationRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a validation field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_validation_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating validation field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_validation_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated validation field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_validation_field",
            field_name=field_name,
            data=response_data,
        )

    # Video Viewer Field Methods
    def _add_video_viewer_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldVideoViewerRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a video viewer field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_video_viewer_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.VIDEO_VIEWER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding video viewer field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_video_viewer_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added video viewer field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_video_viewer_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_video_viewer_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldVideoViewerRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a video viewer field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_video_viewer_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating video viewer field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_video_viewer_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated video viewer field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_video_viewer_field",
            field_name=field_name,
            data=response_data,
        )

    # Voice Field Methods
    def _add_voice_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldVoiceRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a voice field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_voice_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.AUDIO.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding voice field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_voice_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added voice field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_voice_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_voice_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldVoiceRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a voice field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_voice_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating voice field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_voice_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated voice field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_voice_field",
            field_name=field_name,
            data=response_data,
        )

    # Formula Field Methods
    def _add_formula_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldFormulaRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a formula field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_formula_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.CALCULATIONS_AND_LOGIC.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding formula field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_formula_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added formula field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_formula_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_formula_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldFormulaRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a formula field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_formula_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating formula field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_formula_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated formula field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_formula_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_image_viewer_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldImageViewerRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add an image field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_image_field",
                field_name=field_name,
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.IMAGE_VIEWER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding image field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_image_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added image field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_image_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_image_viewer_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldImageViewerRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update an image field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_image_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating image field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_image_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated image field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_image_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_rich_text_editor_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldRichTextEditorRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a rich text editor field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_rich_text_editor_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.RICH_TEXT_EDITOR.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding rich text editor field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_rich_text_editor_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added rich text editor field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_rich_text_editor_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_rich_text_editor_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldRichTextEditorRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a rich text editor field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_rich_text_editor_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating rich text editor field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_rich_text_editor_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated rich text editor field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_rich_text_editor_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_nfc_reader_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldNfcReaderRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add an NFC reader field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_nfc_reader_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.NFC_READER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding NFC reader field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_nfc_reader_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added NFC reader field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_nfc_reader_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_nfc_reader_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldNfcReaderRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update an NFC reader field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_nfc_reader_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating NFC reader field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_nfc_reader_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated NFC reader field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_nfc_reader_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_number_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldNumberInputRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a number field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_number_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.NUMBER_INPUT.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding number field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_number_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added number field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_number_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_number_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldNumberInputRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a number field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_number_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating number field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_number_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated number field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_number_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_pdf_viewer_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldPdfViewerRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a PDF viewer field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_pdf_viewer_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.PDF_VIEWER.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding PDF viewer field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_pdf_viewer_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added PDF viewer field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_pdf_viewer_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_pdf_viewer_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldPdfViewerRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a PDF viewer field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_pdf_viewer_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating PDF viewer field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_pdf_viewer_field",
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated PDF viewer field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_pdf_viewer_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_read_only_file_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldReadOnlyFileRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a read only field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_read_only_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.ATTACHED_FILES.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding read only field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_read_only_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added read only field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_read_only_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_read_only_file_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldReadOnlyFileRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a read only field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_read_only_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating read only field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_read_only_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated read only field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_read_only_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_read_only_text_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldReadOnlyTextRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a read only text field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_read_only_text_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.HTML.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding read only text field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_read_only_text_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added read only text field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_read_only_text_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_read_only_text_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldReadOnlyTextRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a read only text field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_read_only_text_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating read only text field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_read_only_text_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated read only text field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_read_only_text_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_tag_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldTagsRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a tag field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_tag_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.TAGS.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding tag field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_tag_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added tag field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_tag_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_tag_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldTagsRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a tag field in an app."""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_tag_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating tag field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_tag_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated tag field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_tag_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_unique_sequential_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldUniqueSequentialRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a unique sequential field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_unique_sequential_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.UNIQUE_NUMBERING.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding unique sequential field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_unique_sequential_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added unique sequential field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_unique_sequential_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_unique_sequential_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldUniqueSequentialRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a unique sequential field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_unique_sequential_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating unique sequential field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_unique_sequential_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated unique sequential field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_unique_sequential_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_drop_down_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldDropdownRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a drop down field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_drop_down_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.DROP_DOWN.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding drop down field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_drop_down_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added drop down field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_drop_down_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_drop_down_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldDropdownRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a drop down field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_drop_down_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating drop down field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_drop_down_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated drop down field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_drop_down_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_radio_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldRadioRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a radio field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_radio_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.SINGLE_SELECTOR.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding radio field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_radio_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added radio field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_radio_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_radio_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldRadioRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a radio field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_radio_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating radio field in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_radio_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated radio field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_radio_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_url_input_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldUrlInputRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a URL input field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_url_input_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.URL_INPUT.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding URL input field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_url_input_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added URL input field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_url_input_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_url_input_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldUrlInputRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a URL input field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_url_input_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating URL input field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_url_input_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated URL input field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_url_input_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_checkbox_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldCheckboxRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a checkbox field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_checkbox_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.MULTI_SELECTOR.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding checkbox field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_checkbox_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added checkbox field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_checkbox_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_checkbox_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldCheckboxRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a checkbox field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_checkbox_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating checkbox field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_checkbox_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated checkbox field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_checkbox_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_razorpay_payment_gateway_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldRazorpayPaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a razorpay payment gateway field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_razorpay_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.PAYMENT_GATEWAY.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding razorpay payment gateway field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_razorpay_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added razorpay payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_razorpay_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_razorpay_payment_gateway_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldRazorpayPaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a razorpay payment gateway field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_razorpay_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating razorpay payment gateway field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_razorpay_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated razorpay payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_razorpay_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_eazypay_payment_gateway_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldEazypayPaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add an eazypay payment gateway field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_eazypay_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.PAYMENT_GATEWAY.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding eazypay payment gateway field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_eazypay_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added eazypay payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_eazypay_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_eazypay_payment_gateway_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldEazypayPaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update an eazypay payment gateway field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_eazypay_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating eazypay payment gateway field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_eazypay_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated eazypay payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_eazypay_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_paypal_payment_gateway_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldPaypalPaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a paypal payment gateway field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_paypal_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.PAYMENT_GATEWAY.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding paypal payment gateway field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_paypal_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added paypal payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_paypal_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_paypal_payment_gateway_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldPaypalPaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a paypal payment gateway field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_paypal_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating paypal payment gateway field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_paypal_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated paypal payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_paypal_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_stripe_payment_gateway_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldStripePaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a stripe payment gateway field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_stripe_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "pageIndex": page_index,
            "fieldType": FieldType.PAYMENT_GATEWAY.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding stripe payment gateway field to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_stripe_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added stripe payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_stripe_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_stripe_payment_gateway_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldStripePaymentGatewayRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a stripe payment gateway field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_stripe_payment_gateway_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating stripe payment gateway field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_stripe_payment_gateway_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated stripe payment gateway field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_stripe_payment_gateway_field",
            field_name=field_name,
            data=response_data,
        )

    def _add_button_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        page_index: int,
        field_name: str,
        request: UpsertFieldButtonRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Add a button field to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="add_button_field",
            )

        payload = {
            "appId": app_id,
            "sectionIndex": section_index,
            "fieldIndex": field_index,
            "fieldType": FieldType.BUTTON.value,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Adding button field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_button_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully added button field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_button_field",
            field_name=field_name,
            data=response_data,
        )

    def _update_button_field(
        self,
        app_id: str,
        field_name: str,
        request: UpsertFieldButtonRequest,
        version_variable_name: str | None = None,
    ) -> FieldOperationResponse:
        """Update a button field in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                field_name=field_name,
                operation="update_button_field",
            )

        payload = {
            "appId": app_id,
            "fieldName": field_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating button field in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_button_field",
                field_name=field_name,
            )

        return FieldOperationResponse(
            success=True,
            message="Successfully updated button field",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_button_field",
            field_name=field_name,
            data=response_data,
        )

    def add_page_break(
        self, request: AddPageBreakRequest
    ) -> PageBreakOperationResponse:
        """Add a page break to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return PageBreakOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                page_index=request.page_index,
                operation="add_page_break",
                version_variable_name=request.version_variable_name,
            )

        payload = {
            "appId": request.app_id,
            "pageIndex": request.page_index,
            "sectionIndex": request.section_index,
            "pageMetadata": request.page_metadata.to_json(),
        }
        if request.version_variable_name is not None:
            payload["versionVariableName"] = request.version_variable_name
        logger.info(
            f"Adding page break to app_id: {request.app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addPageBreak",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return PageBreakOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                page_index=request.page_index,
                version_variable_name=request.version_variable_name,
                operation="add_page_break",
                data=response_data,
            )

        return PageBreakOperationResponse(
            success=True,
            message=f"Page break after Page with index {request.page_index} and after section with index {request.section_index} added successfully",
            app_id=request.app_id,
            page_index=request.page_index,
            version_variable_name=request.version_variable_name,
            operation="add_page_break",
            data=response_data,
        )

    def update_page(
        self, request: UpdatePageBreakRequest
    ) -> PageBreakOperationResponse:
        """Update page break settings in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return PageBreakOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                page_index=request.page_index,
                operation="update_page",
                version_variable_name=request.version_variable_name,
            )

        payload = {
            "appId": request.app_id.strip(),
            "pageIndex": request.page_index,
            "pageMetadata": request.page_metadata.to_json(),
        }
        if request.version_variable_name is not None:
            payload["versionVariableName"] = request.version_variable_name
        logger.info(
            f"Updating page '{request.page_index}' in app_id: {request.app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updatePageBreak",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return PageBreakOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                page_index=request.page_index,
                version_variable_name=request.version_variable_name,
                operation="update_page",
                data=response_data,
            )

        return PageBreakOperationResponse(
            success=True,
            message=f"Page at index {request.page_index} updated successfully",
            app_id=request.app_id,
            page_index=request.page_index,
            version_variable_name=request.version_variable_name,
            operation="update_page",
            data=response_data,
        )

    def reorder_section(
        self, request: ReorderSectionRequest
    ) -> ReorderSectionOperationResponse:
        """Reorder a section within an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ReorderSectionOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                version_variable_name=request.version_variable_name,
                source_section_index=request.source_section_index,
                target_section_index=request.target_section_index,
                source_page_index=request.source_page_index,
                target_page_index=request.target_page_index,
                operation="reorder_section",
            )

        payload = {
            "appId": request.app_id.strip(),
            "sourceSectionIndex": request.source_section_index,
            "targetSectionIndex": request.target_section_index,
        }
        if request.version_variable_name is not None:
            payload["versionVariableName"] = request.version_variable_name

        if request.source_page_index is not None:
            payload["sourcePageIndex"] = request.source_page_index
        if request.target_page_index is not None:
            payload["targetPageIndex"] = request.target_page_index

        logger.info(
            f"Reordering section in app_id: {request.app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/reorderSection",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ReorderSectionOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                version_variable_name=request.version_variable_name,
                source_section_index=request.source_section_index,
                target_section_index=request.target_section_index,
                source_page_index=request.source_page_index,
                target_page_index=request.target_page_index,
                operation="reorder_section",
                data=response_data,
            )

        return ReorderSectionOperationResponse(
            success=True,
            message="Section reordered successfully",
            app_id=request.app_id,
            version_variable_name=request.version_variable_name,
            source_section_index=request.source_section_index,
            target_section_index=request.target_section_index,
            source_page_index=request.source_page_index,
            target_page_index=request.target_page_index,
            operation="reorder_section",
            data=response_data,
        )

    def add_section(
        self, request: UpsertSectionRequest
    ) -> UpsertSectionOperationResponse:
        """Add a section to an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return UpsertSectionOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                section_index=request.section_index,
                page_index=request.page_index,
                operation="add_section",
                version_variable_name=request.version_variable_name,
            )

        payload = request.to_json()
        if request.version_variable_name is not None:
            payload["versionVariableName"] = request.version_variable_name
        logger.info(
            f"Adding section to app_id: {request.app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/addSection",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return UpsertSectionOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                version_variable_name=request.version_variable_name,
                section_index=request.section_index,
                page_index=request.page_index,
                operation="add_section",
                data=response_data,
            )

        return UpsertSectionOperationResponse(
            success=True,
            message="Section added successfully",
            app_id=request.app_id,
            section_index=request.section_index,
            version_variable_name=request.version_variable_name,
            operation="add_section",
            data=response_data,
        )

    def update_section(
        self, request: UpsertSectionRequest
    ) -> UpsertSectionOperationResponse:
        """Update a section in an app."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return UpsertSectionOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                section_index=request.section_index,
                page_index=request.page_index,
                operation="update_section",
                version_variable_name=request.version_variable_name,
            )

        payload = request.to_json()
        if request.version_variable_name is not None:
            payload["versionVariableName"] = request.version_variable_name
        logger.info(
            f"Updating section in app_id: {request.app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateSection",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return UpsertSectionOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                version_variable_name=request.version_variable_name,
                section_index=request.section_index,
                page_index=request.page_index,
                operation="update_section",
                data=response_data,
            )

        return UpsertSectionOperationResponse(
            success=True,
            message="Section updated successfully",
            app_id=request.app_id,
            version_variable_name=request.version_variable_name,
            section_index=request.section_index,
            page_index=request.page_index,
            operation="update_section",
            data=response_data,
        )

    def get_app_versions(self, app_id: str) -> AppDefinitionResponse:
        """Get an app version."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return AppDefinitionResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="get_app_versions",
            )

        params = {
            "appId": app_id,
        }

        logger.info(f"Getting app versions in app_id: {app_id} with params: {params}")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET",
            endpoint="/getAppVersions",
            params=params,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppDefinitionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="get_app_versions",
            )

        return AppDefinitionResponse(
            success=True,
            message="Successfully retrieved app versions",
            app_id=app_id,
            operation="get_app_versions",
            data=response_data,
        )

    def create_new_app_version(
        self, app_id: str, version_name: str
    ) -> AppDefinitionResponse:
        """Create a new app version."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return AppDefinitionResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="create_new_app_version",
            )

        payload = {
            "appId": app_id,
            "versionName": version_name,
        }

        logger.info(
            f"Creating new app version in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/createNewAppVersion",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppDefinitionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="create_new_app_version",
            )

        return AppDefinitionResponse(
            success=True,
            message="Successfully created new app version",
            app_id=app_id,
            operation="create_new_app_version",
            data=response_data,
        )

    def update_app_version(
        self, app_id: str, initial_version_name: str, new_version_name: str
    ) -> AppDefinitionResponse:
        """Update an app version."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return AppDefinitionResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="update_app_version",
            )

        payload = {
            "appId": app_id,
            "initialVersionName": initial_version_name,
            "newVersionName": new_version_name,
        }

        logger.info(f"Updating app version in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateAppVersion",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppDefinitionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="update_app_version",
            )

        return AppDefinitionResponse(
            success=True,
            message="Successfully updated app version",
            app_id=app_id,
            operation="update_app_version",
            data=response_data,
        )

    def update_live_version(
        self, app_id: str, version_variable_name: str
    ) -> AppDefinitionResponse:
        """Update the live app version."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return AppDefinitionResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_live_version",
            )

        payload = {
            "appId": app_id,
            "versionVariableName": version_variable_name,
        }

        logger.info(
            f"Updating live version in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateLiveVersion",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppDefinitionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_live_version",
            )

        return AppDefinitionResponse(
            success=True,
            message="Successfully updated live version",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_live_version",
            data=response_data,
        )

    def update_app_metadata(
        self,
        app_id: str,
        request: UpdateAppMetadataRequest,
        version_variable_name: str | None = None,
    ) -> AppDefinitionResponse:
        """Update app metadata."""
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return AppDefinitionResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_app_metadata",
            )

        payload = {
            "appId": app_id,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Updating app metadata in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="/updateAppMetadata",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppDefinitionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_app_metadata",
            )

        return AppDefinitionResponse(
            success=True,
            message="Successfully updated app metadata",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_app_metadata",
            data=response_data,
        )


class AppDefinitionAPIKeyClient(BaseAPIKeyClient, AppDefinitionClient):
    """Client for managing Clappia app definitions with API key authentication.
    This client combines API key authentication with all app definition business logic.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize app definition client with API key.

        Args:
            api_key: Clappia API key.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAPIKeyClient.__init__(self, api_key, base_url, timeout)


class AppDefinitionAuthTokenClient(BaseAuthTokenClient, AppDefinitionClient):
    """Client for managing Clappia app definitions with auth token authentication.

    This client combines auth token authentication with all app definition business logic.
    """

    def __init__(
        self,
        auth_token: str,
        workplace_id: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize app definition client with auth token.

        Args:
            auth_token: Clappia Auth token.
            workplace_id: Clappia Workplace ID.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAuthTokenClient.__init__(self, auth_token, workplace_id, base_url, timeout)
