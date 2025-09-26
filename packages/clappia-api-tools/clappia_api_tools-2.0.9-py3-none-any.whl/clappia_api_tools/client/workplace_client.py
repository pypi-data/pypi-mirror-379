from abc import ABC
from typing import Any, Literal

from pydantic import EmailStr

from clappia_api_tools.models.permissions import Permission
from clappia_api_tools.models.request import (
    AddUserToWorkplaceRequest,
    UpdateWorkplaceUserAttributesRequest,
    UpdateWorkplaceUserDetailsRequest,
)
from clappia_api_tools.models.response import (
    AppUserResponse,
    BaseResponse,
    WorkplaceUsersResponse,
)
from clappia_api_tools.models.response.workplace_responses import (
    AppMetaData,
    AppUserMetaData,
)
from clappia_api_tools.models.workplace_user import WorkplaceUser
from clappia_api_tools.utils.logging_utils import get_logger

from .base_client import BaseAPIKeyClient, BaseAuthTokenClient, BaseClappiaClient

logger = get_logger(__name__)


class WorkplaceClient(BaseClappiaClient, ABC):
    """Client for managing Clappia workplace users.

    This client handles workplace user management operations including
    adding users to workplace, updating user details, attributes, roles,
    groups, and adding users to apps.
    """

    def _validate_email_phone_requirements(
        self,
        email_address: EmailStr | None,
        phone_number: str | None,
        operation: str,
    ) -> BaseResponse | None:
        """Validate email/phone number requirements.

        Args:
            email_address: Email address of the user
            phone_number: Phone number of the user
            operation: Operation name for error response

        Returns:
            BaseResponse with error if validation fails, None if validation passes
        """
        if email_address is None and phone_number is None:
            return BaseResponse(
                success=False,
                message="One of email address or phone number is required",
                operation=operation,
            )

        if email_address is not None and phone_number is not None:
            return BaseResponse(
                success=False,
                message="Only one of email address or phone number is required",
                operation=operation,
            )

        return None

    def _validate_environment(self, operation: str) -> BaseResponse | None:
        """Validate environment configuration.

        Args:
            operation: Operation name for error response

        Returns:
            BaseResponse with error if validation fails, None if validation passes
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False,
                message=env_error,
                operation=operation,
            )
        return None

    def _build_user_identifier_payload(
        self,
        email_address: EmailStr | None,
        phone_number: str | None,
        base_payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build payload with user identifier (email or phone).

        Args:
            email_address: Email address of the user
            phone_number: Phone number of the user
            base_payload: Base payload dictionary to add identifiers to

        Returns:
            Dictionary with user identifier added
        """
        if base_payload is None:
            payload: dict[str, Any] = {}
        else:
            payload = base_payload.copy()

        if email_address is not None:
            payload["emailAddress"] = email_address
        if phone_number is not None:
            payload["phoneNumber"] = phone_number

        return payload

    def add_user_to_workplace(
        self,
        request: AddUserToWorkplaceRequest,
    ) -> BaseResponse:
        """Add a user to the workplace.

        Args:
            email_address: Email address of the user (only one of email or phone is required)
            phone_number: Phone number of the user (only one of email or phone is required)
            first_name: First name of the user
            last_name: Last name of the user
            group_names: List of group names to assign to the user
            attributes: User attributes as key-value pairs

        Returns:
            base: Response containing operation result
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False,
                message=env_error,
                operation="add_user_to_workplace",
            )

        payload: dict[str, Any] = {
            "firstName": request.first_name,
            "lastName": request.last_name,
            "groupNames": request.group_names,
            "attributes": request.attributes,
        }

        if request.email_address is not None:
            payload["emailAddress"] = request.email_address
        if request.phone_number is not None:
            payload["phoneNumber"] = request.phone_number

        logger.info(f"Adding user to workplace with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workplace/addUserToWorkplace",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False,
                message=error_message,
                operation="add_user_to_workplace",
            )

        return BaseResponse(
            success=True,
            message="Successfully added user to workplace",
            operation="add_user_to_workplace",
            data=response_data,
        )

    def update_workplace_user_details(
        self,
        request: UpdateWorkplaceUserDetailsRequest,
    ) -> BaseResponse:
        """Update workplace user details.

        Args:
            email_address: Email address of the user (only one of email or phone is required)
            phone_number: Phone number of the user (only one of email or phone is required)
            updated_details: Dictionary containing the details to update

        Returns:
            WorkplaceUserDetailsResponse: Response containing operation result
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False,
                message=env_error,
                operation="update_workplace_user_details",
            )

        payload: dict[str, Any] = {
            "updatedDetails": {
                "firstName": request.updated_details.get("first_name"),
                "lastName": request.updated_details.get("last_name"),
                "emailAddress": request.updated_details.get("email_address"),
                "phoneNumber": request.updated_details.get("phone_number"),
            }
        }

        if request.email_address is not None:
            payload["emailAddress"] = str(request.email_address)
        if request.phone_number is not None:
            payload["phoneNumber"] = request.phone_number

        logger.info(f"Updating workplace user details with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workplace/updateWorkplaceUserDetails",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False,
                message=error_message,
                operation="update_workplace_user_details",
            )

        return BaseResponse(
            success=True,
            message="Successfully updated workplace user details",
            operation="update_workplace_user_details",
            data=response_data,
        )

    def update_workplace_user_attributes(
        self,
        request: UpdateWorkplaceUserAttributesRequest,
    ) -> BaseResponse:
        """Update workplace user attributes.

        Args:
            email_address: Email address of the user (only one of email or phone is required)
            phone_number: Phone number of the user (only one of email or phone is required)
            attributes: Dictionary containing the attributes to update

        Returns:
            WorkplaceUserAttributesResponse: Response containing operation result
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False,
                message=env_error,
                operation="update_workplace_user_attributes",
            )

        payload: dict[str, Any] = {
            "attributes": request.attributes,
        }

        if request.email_address is not None:
            payload["emailAddress"] = str(request.email_address)
        if request.phone_number is not None:
            payload["phoneNumber"] = request.phone_number

        logger.info(f"Updating workplace user attributes with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workplace/updateWorkplaceUserAttributes",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False,
                message=error_message,
                operation="update_workplace_user_attributes",
            )

        return BaseResponse(
            success=True,
            message="Successfully updated workplace user attributes",
            operation="update_workplace_user_attributes",
            data=response_data,
        )

    def update_workplace_user_role(
        self,
        email_address: EmailStr | None = None,
        phone_number: str | None = None,
        role: Literal["Workplace Manager", "App Builder", "User"] = "User",
    ) -> BaseResponse:
        """Update workplace user role.

        Args:
            email_address: Email address of the user (only one of email or phone is required)
            phone_number: Phone number of the user (only one of email or phone is required)
            role: The new role for the user

        Returns:
            WorkplaceUserRoleResponse: Response containing operation result
        """
        validation_error = self._validate_email_phone_requirements(
            email_address, phone_number, "update_workplace_user_role"
        )
        if validation_error:
            return validation_error

        if not role or role not in ["Workplace Manager", "App Builder", "User"]:
            return BaseResponse(
                success=False,
                message="Role is required and must be one of: Workplace Manager, App Builder, User",
                operation="update_workplace_user_role",
            )

        env_error = self._validate_environment("update_workplace_user_role")
        if env_error:
            return env_error

        payload = self._build_user_identifier_payload(
            email_address, phone_number, {"role": role}
        )

        logger.info(f"Updating workplace user role with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workplace/updateWorkplaceUserRole",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False,
                message=error_message,
                operation="update_workplace_user_role",
            )

        return BaseResponse(
            success=True,
            message=f"Successfully updated workplace user role to {role}",
            operation="update_workplace_user_role",
            data=response_data,
        )

    def update_workplace_user_groups(
        self,
        email_address: EmailStr | None = None,
        phone_number: str | None = None,
        group_names: list[str] | None = None,
    ) -> BaseResponse:
        """Update workplace user groups.

        Args:
            email_address: Email address of the user (only one of email or phone is required)
            phone_number: Phone number of the user (only one of email or phone is required)
            group_names: List of group names to assign to the user

        Returns:
            WorkplaceUserGroupsResponse: Response containing operation result
        """
        validation_error = self._validate_email_phone_requirements(
            email_address, phone_number, "update_workplace_user_groups"
        )
        if validation_error:
            return validation_error

        if not group_names or len(group_names) == 0:
            return BaseResponse(
                success=False,
                message="Group names are required",
                operation="update_workplace_user_groups",
            )

        unique_groups = list(
            {name.strip() for name in group_names if name and name.strip()}
        )

        if unique_groups != group_names:
            return BaseResponse(
                success=False,
                message="Group names must be unique",
                operation="update_workplace_user_groups",
            )

        env_error = self._validate_environment("update_workplace_user_groups")
        if env_error:
            return env_error

        payload = self._build_user_identifier_payload(
            email_address, phone_number, {"groupNames": unique_groups}
        )

        logger.info(f"Updating workplace user groups with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workplace/updateWorkplaceUserGroups",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False,
                message=error_message,
                operation="update_workplace_user_groups",
            )

        return BaseResponse(
            success=True,
            message=f"Successfully updated workplace user groups to {', '.join(unique_groups)}",
            operation="update_workplace_user_groups",
            data=response_data,
        )

    def add_user_to_app(
        self,
        app_id: str,
        permissions: Permission,
        email_address: EmailStr | None = None,
        phone_number: str | None = None,
    ) -> AppUserResponse:
        """Add a user to an app."""
        validation_error = self._validate_email_phone_requirements(
            email_address, phone_number, "add_user_to_app"
        )
        if validation_error:
            return AppUserResponse(
                success=False,
                message=validation_error.message,
                app_id=app_id,
                operation="add_user_to_app",
            )

        env_error = self._validate_environment("add_user_to_app")
        if env_error:
            return AppUserResponse(
                success=False,
                message=env_error.message,
                app_id=app_id,
                operation="add_user_to_app",
            )

        dict_permissions = permissions.to_dict()

        payload = self._build_user_identifier_payload(
            email_address,
            phone_number,
            {
                "appId": app_id,
                "permissions": dict_permissions,
            },
        )

        logger.info(f"Adding user to app with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="app/addUserToApp",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppUserResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="add_user_to_app",
                permissions=dict_permissions,
            )

        return AppUserResponse(
            success=True,
            message=f"Successfully added user to app {app_id}",
            app_id=app_id,
            permissions=dict_permissions,
            operation="add_user_to_app",
            data=response_data,
        )

    def get_workplace_apps(self) -> BaseResponse:
        """Get all apps in the workplace.

        Returns:
            WorkplaceAppResponse: Response containing list of apps
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False,
                message=env_error,
                operation="get_workplace_apps",
            )

        logger.info("Getting workplace apps")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET",
            endpoint="workplace/getApps",
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False,
                message=error_message,
                operation="get_workplace_apps",
            )

        apps: list[AppMetaData] = []
        if response_data:
            for app_data in response_data:
                try:
                    json_data: dict[str, Any] = (
                        app_data if isinstance(app_data, dict) else {}
                    )
                    app = AppMetaData.from_json(json_data)
                    apps.append(app)
                except Exception as e:
                    logger.warning(f"Failed to parse app data: {e}")

            return BaseResponse(
                success=True,
                message="Successfully retrieved workplace apps",
                operation="get_workplace_apps",
                data=apps,
            )

        return BaseResponse(
            success=False,
            message="Failed to retrieve workplace apps",
            operation="get_workplace_apps",
            data=apps,
        )

    def get_workplace_user_apps(
        self,
        email_address: EmailStr | None = None,
        phone_number: str | None = None,
    ) -> BaseResponse:
        """Get apps for a specific workplace user.

        Args:
            email_address: Email address of the user (only one of email or phone is required)
            phone_number: Phone number of the user (only one of email or phone is required)

        Returns:
            WorkplaceUserAppsResponse: Response containing list of user's apps
        """
        validation_error = self._validate_email_phone_requirements(
            email_address, phone_number, "get_workplace_user_apps"
        )
        if validation_error:
            return validation_error

        env_error = self._validate_environment("get_workplace_user_apps")
        if env_error:
            return env_error

        params = self._build_user_identifier_payload(email_address, phone_number)

        logger.info(f"Getting workplace user apps with params: {params}")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET",
            endpoint="workplace/getUserApps",
            params=params,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False,
                message=error_message,
                operation="get_workplace_user_apps",
            )

        apps: list[AppUserMetaData] = []
        if response_data:
            for app_data in response_data:
                try:
                    json_data: dict[str, Any] = (
                        app_data if isinstance(app_data, dict) else {}
                    )
                    app = AppUserMetaData.from_json(json_data)
                    apps.append(app)
                except Exception as e:
                    logger.warning(f"Failed to parse app data: {e}")

            return BaseResponse(
                success=True,
                message="Successfully retrieved workplace user apps",
                operation="get_workplace_user_apps",
                data=apps,
            )
        return BaseResponse(
            success=False,
            message="Failed to retrieve workplace user apps",
            operation="get_workplace_user_apps",
            data=apps,
        )

    def get_workplace_users(
        self,
        page_size: int = 50,
        token: str | None = None,
    ) -> WorkplaceUsersResponse:
        """Get workplace users with pagination.

        Args:
            page_size: Number of users to retrieve per page
            token: Token for pagination

        Returns:
            WorkplaceUsersResponse: Response containing list of users and pagination token
        """
        env_valid, env_error = self.api_utils.validate_environment()

        if not env_valid:
            return WorkplaceUsersResponse(
                success=False,
                message=env_error,
                users=[],
                operation="get_workplace_users",
            )

        payload: dict[str, Any] = {
            "pageSize": page_size,
        }

        if token is not None:
            payload["token"] = token

        logger.info(f"Getting workplace users with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workplace/getWorkplaceUsers",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkplaceUsersResponse(
                success=False,
                message=error_message,
                users=[],
                operation="get_workplace_users",
            )

        users = []
        next_token = None

        if response_data and isinstance(response_data, dict):
            users_data = response_data.get("users", [])
            next_token = response_data.get("token")

            if isinstance(users_data, list):
                for user_data in users_data:
                    try:
                        user = WorkplaceUser(**user_data)
                        users.append(user)
                    except Exception as e:
                        logger.warning(f"Failed to parse user data: {e}")

        return WorkplaceUsersResponse(
            success=True,
            message="Successfully retrieved workplace users",
            users=users,
            token=next_token,
            operation="get_workplace_users",
            data=response_data,
        )


class WorkplaceAPIKeyClient(BaseAPIKeyClient, WorkplaceClient):
    """Client for managing Clappia workplace users with API key authentication.

    This client combines API key authentication with all workplace business logic.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize workplace client with API key.

        Args:
            api_key: Clappia API key.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAPIKeyClient.__init__(self, api_key, base_url, timeout)


class WorkplaceAuthTokenClient(BaseAuthTokenClient, WorkplaceClient):
    """Client for managing Clappia workplace users with auth token authentication.

    This client combines auth token authentication with all workplace business logic.
    """

    def __init__(
        self,
        auth_token: str,
        workplace_id: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize workplace client with auth token.

        Args:
            auth_token: Clappia Auth token.
            workplace_id: Clappia Workplace ID.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAuthTokenClient.__init__(self, auth_token, workplace_id, base_url, timeout)
