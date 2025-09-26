from abc import ABC

from clappia_api_tools.enums import NodeType, TriggerType
from clappia_api_tools.models.request import (
    UpsertAiWorkflowStepRequest,
    UpsertApprovalWorkflowStepRequest,
    UpsertCodeWorkflowStepRequest,
    UpsertConditionWorkflowStepRequest,
    UpsertCreateSubmissionWorkflowStepRequest,
    UpsertDatabaseWorkflowStepRequest,
    UpsertDeleteSubmissionWorkflowStepRequest,
    UpsertEditSubmissionWorkflowStepRequest,
    UpsertEmailWorkflowStepRequest,
    UpsertFindSubmissionWorkflowStepRequest,
    UpsertLoopWorkflowStepRequest,
    UpsertMobileNotificationWorkflowStepRequest,
    UpsertRestApiWorkflowStepRequest,
    UpsertSlackWorkflowStepRequest,
    UpsertSmsWorkflowStepRequest,
    UpsertWaitWorkflowStepRequest,
    UpsertWhatsAppWorkflowStepRequest,
)
from clappia_api_tools.models.response import (
    WorkflowResponse,
    WorkflowStepResponse,
)
from clappia_api_tools.utils.logging_utils import get_logger

from .base_client import BaseAPIKeyClient, BaseAuthTokenClient, BaseClappiaClient

WorkflowStepRequestUnion = (
    UpsertAiWorkflowStepRequest
    | UpsertApprovalWorkflowStepRequest
    | UpsertCodeWorkflowStepRequest
    | UpsertConditionWorkflowStepRequest
    | UpsertDatabaseWorkflowStepRequest
    | UpsertEmailWorkflowStepRequest
    | UpsertLoopWorkflowStepRequest
    | UpsertMobileNotificationWorkflowStepRequest
    | UpsertRestApiWorkflowStepRequest
    | UpsertSlackWorkflowStepRequest
    | UpsertSmsWorkflowStepRequest
    | UpsertWaitWorkflowStepRequest
    | UpsertWhatsAppWorkflowStepRequest
    | UpsertCreateSubmissionWorkflowStepRequest
    | UpsertDeleteSubmissionWorkflowStepRequest
    | UpsertFindSubmissionWorkflowStepRequest
    | UpsertEditSubmissionWorkflowStepRequest
)


logger = get_logger(__name__)


class WorkflowDefinitionClient(BaseClappiaClient, ABC):
    """Abstract client for managing Clappia workflow definitions.

    This client handles retrieving and managing workflow definitions, including
    getting workflows, adding workflow steps, removing workflow steps,
    updating workflow steps, and reordering workflow steps.

    Note: This is an abstract base class that contains business logic but no authentication.
    Use WorkflowDefinitionAPIKeyClient or WorkflowDefinitionAuthTokenClient for actual usage.
    """

    def get_workflow(
        self,
        app_id: str,
        trigger_type: str,
        version_variable_name: str | None = None,
    ) -> WorkflowResponse:
        """Get a workflow definition for a specific app and trigger type"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="get_workflow",
                version_variable_name=version_variable_name,
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                operation="get_workflow",
                version_variable_name=version_variable_name,
            )

        params = {
            "appId": app_id,
            "triggerType": trigger_type,
        }
        if version_variable_name:
            params["versionVariableName"] = version_variable_name

        logger.info(
            f"Getting workflow for app_id: {app_id} with trigger_type: {trigger_type} and version_variable_name: {version_variable_name}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="GET", endpoint="workflowdefinitionv2/getWorkflow", params=params
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="get_workflow",
                version_variable_name=version_variable_name,
            )

        return WorkflowResponse(
            success=True,
            message="Successfully retrieved workflow definition",
            app_id=app_id,
            data=response_data,
            operation="get_workflow",
            version_variable_name=version_variable_name,
        )

    def add(
        self,
        app_id: str,
        trigger_type: str,
        request: WorkflowStepRequestUnion,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a workflow step to a Clappia app.

        Args:
            app_id: The ID of the app to add the step to
            trigger_type: The trigger type of the workflow
            request: The request object containing the step configuration
            step_variable_name: The variable name of the step, if not provided, a random variable name will be generated
            parent_step_variable_name: The variable name of the parent step, below which the new step will be added
            version_variable_name: The variable name of the version, if not provided, the live version is used
        Returns:
            WorkflowStepResponse: Response containing the result of the operation
        """
        if isinstance(request, UpsertAiWorkflowStepRequest):
            return self._add_ai_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertApprovalWorkflowStepRequest):
            return self._add_approval_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertCodeWorkflowStepRequest):
            return self._add_code_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertConditionWorkflowStepRequest):
            return self._add_condition_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertDatabaseWorkflowStepRequest):
            return self._add_database_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertEmailWorkflowStepRequest):
            return self._add_email_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertLoopWorkflowStepRequest):
            return self._add_loop_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertMobileNotificationWorkflowStepRequest):
            return self._add_mobile_notification_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertRestApiWorkflowStepRequest):
            return self._add_rest_api_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertSlackWorkflowStepRequest):
            return self._add_slack_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertSmsWorkflowStepRequest):
            return self._add_sms_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertWaitWorkflowStepRequest):
            return self._add_wait_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertWhatsAppWorkflowStepRequest):
            return self._add_whatsapp_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertCreateSubmissionWorkflowStepRequest):
            return self._add_create_submission_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertDeleteSubmissionWorkflowStepRequest):
            return self._add_delete_submission_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertFindSubmissionWorkflowStepRequest):
            return self._add_find_submission_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        elif isinstance(request, UpsertEditSubmissionWorkflowStepRequest):
            return self._add_edit_submission_step(
                app_id,
                trigger_type,
                request,
                step_variable_name,
                parent_step_variable_name,
                version_variable_name,
            )
        else:
            raise ValueError(f"Unsupported workflow step request type: {type(request)}")

    def update(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: WorkflowStepRequestUnion,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a workflow step in a Clappia app.

        Args:
            app_id: The ID of the app containing the step
            trigger_type: The trigger type of the workflow
            step_variable_name: The variable name of the step to update
            request: The request object containing the updated step configuration
            version_variable_name: The variable name of the version, if not provided, the live version is used
        Returns:
            WorkflowStepResponse: Response containing the result of the operation
        """
        if isinstance(request, UpsertAiWorkflowStepRequest):
            return self._update_ai_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertApprovalWorkflowStepRequest):
            return self._update_approval_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertCodeWorkflowStepRequest):
            return self._update_code_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertConditionWorkflowStepRequest):
            return self._update_condition_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertDatabaseWorkflowStepRequest):
            return self._update_database_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertEmailWorkflowStepRequest):
            return self._update_email_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertLoopWorkflowStepRequest):
            return self._update_loop_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertMobileNotificationWorkflowStepRequest):
            return self._update_mobile_notification_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertRestApiWorkflowStepRequest):
            return self._update_rest_api_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertSlackWorkflowStepRequest):
            return self._update_slack_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertSmsWorkflowStepRequest):
            return self._update_sms_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertWaitWorkflowStepRequest):
            return self._update_wait_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertWhatsAppWorkflowStepRequest):
            return self._update_whatsapp_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertCreateSubmissionWorkflowStepRequest):
            return self._update_create_submission_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertDeleteSubmissionWorkflowStepRequest):
            return self._update_delete_submission_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertFindSubmissionWorkflowStepRequest):
            return self._update_find_submission_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        elif isinstance(request, UpsertEditSubmissionWorkflowStepRequest):
            return self._update_edit_submission_step(
                app_id, trigger_type, step_variable_name, request, version_variable_name
            )
        else:
            raise ValueError(f"Unsupported workflow step request type: {type(request)}")

    def reorder_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        parent_step_variable_name: str,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Reorder a workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="reorder",
                version_variable_name=version_variable_name,
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="reorder",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            "parentVariableName": parent_step_variable_name,
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Reordering workflow step for app_id: {app_id} with step: {step_variable_name}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/reorderWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="reorder",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully reordered workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="reorder",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _add_ai_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertAiWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add an AI workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_ai_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_ai_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.AI_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding AI workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_ai_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added AI workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_ai_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_ai_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertAiWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update an AI workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_ai_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_ai_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating AI workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_ai_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated AI workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_ai_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    def _add_approval_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertApprovalWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add an approval workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_approval_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_approval_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.APPROVAL_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding approval workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_approval_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added approval workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_approval_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_approval_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertApprovalWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update an approval workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_approval_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_approval_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Updating approval workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_approval_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated approval workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_approval_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Code Workflow Step Methods
    def _add_code_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertCodeWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a code workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_code_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_code_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.CODE_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding code workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_code_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added code workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_code_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_code_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertCodeWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a code workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_code_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_code_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Updating code workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_code_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated code workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_code_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Condition Workflow Step Methods
    def _add_condition_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertConditionWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a condition workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_condition_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_condition_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.CONDITION_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding condition workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_condition_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added condition workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_condition_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_condition_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertConditionWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a condition workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_condition_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_condition_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Updating condition workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_condition_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated condition workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_condition_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Database Workflow Step Methods
    def _add_database_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertDatabaseWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a database workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_database_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_database_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.DATABASE_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding database workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_database_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added database workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_database_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_database_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertDatabaseWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a database workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_database_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_database_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating database workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_database_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated database workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_database_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Email Workflow Step Methods
    def _add_email_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertEmailWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add an email workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_email_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_email_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.EMAIL_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding email workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_email_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added email workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_email_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_email_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertEmailWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update an email workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_email_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_email_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating email workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_email_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated email workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_email_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Loop Workflow Step Methods
    def _add_loop_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertLoopWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a loop workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_loop_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_loop_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.LOOP_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding loop workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_loop_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added loop workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_loop_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_loop_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertLoopWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a loop workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_loop_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_loop_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating loop workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_loop_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated loop workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_loop_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Mobile Notification Workflow Step Methods
    def _add_mobile_notification_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertMobileNotificationWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a mobile notification workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_mobile_notification_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_mobile_notification_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.MOBILE_NOTIFICATION_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding mobile notification workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_mobile_notification_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added mobile notification workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_mobile_notification_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_mobile_notification_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertMobileNotificationWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a mobile notification workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_mobile_notification_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_mobile_notification_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating mobile notification workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_mobile_notification_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated mobile notification workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_mobile_notification_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # REST API Workflow Step Methods
    def _add_rest_api_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertRestApiWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a REST API workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_rest_api_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_rest_api_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.REST_API_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding REST API workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_rest_api_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added REST API workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_rest_api_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_rest_api_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertRestApiWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a REST API workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_rest_api_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_rest_api_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating REST API workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_rest_api_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated REST API workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_rest_api_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Slack Workflow Step Methods
    def _add_slack_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertSlackWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a Slack workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_slack_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_slack_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.SLACK_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding Slack workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_slack_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added Slack workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_slack_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_slack_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertSlackWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a Slack workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_slack_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_slack_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating Slack workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_slack_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated Slack workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_slack_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # SMS Workflow Step Methods
    def _add_sms_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertSmsWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add an SMS workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_sms_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_sms_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.SMS_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding SMS workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_sms_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added SMS workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_sms_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_sms_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertSmsWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update an SMS workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_sms_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_sms_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating SMS workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_sms_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated SMS workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_sms_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Wait Workflow Step Methods
    def _add_wait_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertWaitWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a wait workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_wait_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_wait_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.WAIT_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding wait workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_wait_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added wait workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_wait_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_wait_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertWaitWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a wait workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_wait_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_wait_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating wait workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_wait_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated wait workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_wait_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # WhatsApp Workflow Step Methods
    def _add_whatsapp_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertWhatsAppWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a WhatsApp workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_whatsapp_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_whatsapp_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.WHATSAPP_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding WhatsApp workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_whatsapp_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added WhatsApp workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_whatsapp_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_whatsapp_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertWhatsAppWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a WhatsApp workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_whatsapp_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_whatsapp_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating WhatsApp workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_whatsapp_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated WhatsApp workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_whatsapp_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Create Submission Workflow Step Methods
    def _add_create_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertCreateSubmissionWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a create submission workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_create_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_create_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.CREATE_SUBMISSION_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding create submission workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_create_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added create submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_create_submission_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_create_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertCreateSubmissionWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a create submission workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_create_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_create_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating create submission workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_create_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated create submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_create_submission_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Delete Submission Workflow Step Methods
    def _add_delete_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertDeleteSubmissionWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a delete submission workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_delete_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_delete_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.DELETE_SUBMISSION_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding delete submission workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_delete_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added delete submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_delete_submission_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_delete_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertDeleteSubmissionWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a delete submission workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_delete_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_delete_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating delete submission workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_delete_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated delete submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_delete_submission_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Find Submission Workflow Step Methods
    def _add_find_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertFindSubmissionWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add a find submission workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_find_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_find_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.FIND_SUBMISSION_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding find submission workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_find_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added find submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_find_submission_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_find_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertFindSubmissionWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update a find submission workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_find_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_find_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating find submission workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_find_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated find submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_find_submission_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    # Edit Submission Workflow Step Methods
    def _add_edit_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        request: UpsertEditSubmissionWorkflowStepRequest,
        step_variable_name: str | None = None,
        parent_step_variable_name: str | None = None,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Add an edit submission workflow step to a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_edit_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_edit_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "nodeType": NodeType.EDIT_SUBMISSION_NODE.value,
            **request.to_json(),
        }
        if step_variable_name is not None:
            payload["stepVariableName"] = step_variable_name
        if parent_step_variable_name is not None:
            payload["parentVariableName"] = parent_step_variable_name
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding edit submission workflow step to app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_edit_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added edit submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_edit_submission_step",
            step_variable_name=step_variable_name,
            parent_step_variable_name=parent_step_variable_name,
            data=response_data,
        )

    def _update_edit_submission_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        request: UpsertEditSubmissionWorkflowStepRequest,
        version_variable_name: str | None = None,
    ) -> WorkflowStepResponse:
        """Update an edit submission workflow step in a Clappia app"""

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_edit_submission_step",
            )

        if trigger_type not in [t.value for t in TriggerType]:
            return WorkflowStepResponse(
                success=False,
                message=f"Invalid trigger type: {trigger_type}, allowed types are: {', '.join([t.value for t in TriggerType])}",
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_edit_submission_step",
            )

        payload = {
            "appId": app_id,
            "triggerType": trigger_type,
            "stepVariableName": step_variable_name,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating edit submission workflow step in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_edit_submission_step",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated edit submission workflow step",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_edit_submission_step",
            step_variable_name=step_variable_name,
            data=response_data,
        )


class WorkflowDefinitionAPIKeyClient(BaseAPIKeyClient, WorkflowDefinitionClient):
    """Client for managing Clappia workflow definitions with API key authentication.

    This client combines API key authentication with all workflow definition business logic.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize workflow definition client with API key.

        Args:
            api_key: Clappia API key.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAPIKeyClient.__init__(self, api_key, base_url, timeout)


class WorkflowDefinitionAuthTokenClient(BaseAuthTokenClient, WorkflowDefinitionClient):
    """Client for managing Clappia workflow definitions with auth token authentication.

    This client combines auth token authentication with all workflow definition business logic.
    """

    def __init__(
        self,
        auth_token: str,
        workplace_id: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize workflow definition client with auth token.

        Args:
            auth_token: Clappia Auth token.
            workplace_id: Clappia Workplace ID.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAuthTokenClient.__init__(self, auth_token, workplace_id, base_url, timeout)
