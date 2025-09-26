from abc import ABC

from clappia_api_tools.enums import ChartType
from clappia_api_tools.models.request import (
    UpsertBarChartDefinitionRequest,
    UpsertDataTableChartDefinitionRequest,
    UpsertDoughnutChartDefinitionRequest,
    UpsertGanttChartDefinitionRequest,
    UpsertLineChartDefinitionRequest,
    UpsertMapChartDefinitionRequest,
    UpsertPieChartDefinitionRequest,
    UpsertSummaryChartDefinitionRequest,
)
from clappia_api_tools.models.response import BaseResponse, ChartResponse
from clappia_api_tools.utils.logging_utils import get_logger

from .base_client import BaseAPIKeyClient, BaseAuthTokenClient, BaseClappiaClient

ChartDefinitionRequestUnion = (
    UpsertSummaryChartDefinitionRequest
    | UpsertBarChartDefinitionRequest
    | UpsertPieChartDefinitionRequest
    | UpsertDoughnutChartDefinitionRequest
    | UpsertLineChartDefinitionRequest
    | UpsertDataTableChartDefinitionRequest
    | UpsertMapChartDefinitionRequest
    | UpsertGanttChartDefinitionRequest
)

logger = get_logger(__name__)


class AnalyticsClient(BaseClappiaClient, ABC):
    """Abstract client for managing Clappia analytics and charts.

    This client handles retrieving and managing analytics configurations, including
    adding charts, removing charts, updating charts, and reordering charts.
    """

    def add(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: ChartDefinitionRequestUnion,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        if isinstance(request, UpsertSummaryChartDefinitionRequest):
            return self._add_summary_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        elif isinstance(request, UpsertBarChartDefinitionRequest):
            return self._add_bar_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        elif isinstance(request, UpsertPieChartDefinitionRequest):
            return self._add_pie_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        elif isinstance(request, UpsertDoughnutChartDefinitionRequest):
            return self._add_doughnut_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        elif isinstance(request, UpsertLineChartDefinitionRequest):
            return self._add_line_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        elif isinstance(request, UpsertDataTableChartDefinitionRequest):
            return self._add_data_table_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        elif isinstance(request, UpsertMapChartDefinitionRequest):
            return self._add_map_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        elif isinstance(request, UpsertGanttChartDefinitionRequest):
            return self._add_gantt_chart(
                app_id, chart_index, chart_title, request, version_variable_name
            )
        else:
            raise ValueError(
                f"Unsupported chart definition request type: {type(request)}"
            )

    def update(
        self,
        app_id: str,
        chart_index: int,
        request: ChartDefinitionRequestUnion,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        if isinstance(request, UpsertSummaryChartDefinitionRequest):
            return self._update_summary_chart(
                app_id, chart_index, request, version_variable_name
            )
        elif isinstance(request, UpsertBarChartDefinitionRequest):
            return self._update_bar_chart(
                app_id, chart_index, request, version_variable_name
            )
        elif isinstance(request, UpsertPieChartDefinitionRequest):
            return self._update_pie_chart(
                app_id, chart_index, request, version_variable_name
            )
        elif isinstance(request, UpsertDoughnutChartDefinitionRequest):
            return self._update_doughnut_chart(
                app_id, chart_index, request, version_variable_name
            )
        elif isinstance(request, UpsertLineChartDefinitionRequest):
            return self._update_line_chart(
                app_id, chart_index, request, version_variable_name
            )
        elif isinstance(request, UpsertDataTableChartDefinitionRequest):
            return self._update_data_table_chart(
                app_id, chart_index, request, version_variable_name
            )
        elif isinstance(request, UpsertMapChartDefinitionRequest):
            return self._update_map_chart(
                app_id, chart_index, request, version_variable_name
            )
        elif isinstance(request, UpsertGanttChartDefinitionRequest):
            return self._update_gantt_chart(
                app_id, chart_index, request, version_variable_name
            )
        else:
            raise ValueError(
                f"Unsupported chart definition request type: {type(request)}"
            )

    def _add_summary_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertSummaryChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a summary chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used
        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_summary_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.SUMMARY_CARD.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Adding summary chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_summary_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added summary chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_summary_chart",
            data=response_data,
        )

    def _update_summary_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertSummaryChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a summary chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used
        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_summary_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.SUMMARY_CARD.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating summary chart for app_id: {app_id} at index {chart_index}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_summary_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated summary chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_summary_chart",
            data=response_data,
        )

    def _add_bar_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertBarChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a bar chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used
        Returns:
            ChartResponse: Response containing the result of the operation
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_bar_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.BAR_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding bar chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_bar_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added bar chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_bar_chart",
            data=response_data,
        )

    def _update_bar_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertBarChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a bar chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_bar_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.BAR_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating bar chart for app_id: {app_id} at index {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_bar_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated bar chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_bar_chart",
            data=response_data,
        )

    def _add_pie_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertPieChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a pie chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_pie_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.PIE_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding pie chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_pie_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added pie chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_pie_chart",
            data=response_data,
        )

    def _update_pie_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertPieChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a pie chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_pie_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.PIE_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating pie chart for app_id: {app_id} at index {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_pie_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated pie chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_pie_chart",
            data=response_data,
        )

    def _add_doughnut_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertDoughnutChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a doughnut chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_doughnut_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.DOUGHNUT_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding doughnut chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_doughnut_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added doughnut chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_doughnut_chart",
            data=response_data,
        )

    def _update_doughnut_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertDoughnutChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a doughnut chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_doughnut_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.DOUGHNUT_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating doughnut chart for app_id: {app_id} at index {chart_index}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_doughnut_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated doughnut chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_doughnut_chart",
            data=response_data,
        )

    def _add_line_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertLineChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a line chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_line_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.LINE_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding line chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_line_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added line chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_line_chart",
            data=response_data,
        )

    def _update_line_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertLineChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a line chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_line_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.LINE_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating line chart for app_id: {app_id} at index {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_line_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated line chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_line_chart",
            data=response_data,
        )

    def _add_data_table_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertDataTableChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a data table chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_data_table_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.DATA_TABLE.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding data table chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_data_table_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added data table chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_data_table_chart",
            data=response_data,
        )

    def _update_data_table_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertDataTableChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a data table chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_data_table_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.DATA_TABLE.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(
            f"Updating data table chart for app_id: {app_id} at index {chart_index}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_data_table_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated data table chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_data_table_chart",
            data=response_data,
        )

    def _add_map_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertMapChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a map chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_map_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.MAP_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding map chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_map_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added map chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_map_chart",
            data=response_data,
        )

    def _update_map_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertMapChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a map chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_map_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.MAP_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating map chart for app_id: {app_id} at index {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_map_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated map chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_map_chart",
            data=response_data,
        )

    def _add_gantt_chart(
        self,
        app_id: str,
        chart_index: int,
        chart_title: str,
        request: UpsertGanttChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Add a Gantt chart to an app.

        Args:
            app_id: The ID of the app to add the chart to
            chart_index: The index of the chart to add
            chart_title: The title of the chart
            request: The request object containing the chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_gantt_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartTitle": chart_title,
            "chartType": ChartType.GANTT_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Adding Gantt chart for app_id: {app_id} at index {chart_index} with title {chart_title}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="add_gantt_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully added Gantt chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="add_gantt_chart",
            data=response_data,
        )

    def _update_gantt_chart(
        self,
        app_id: str,
        chart_index: int,
        request: UpsertGanttChartDefinitionRequest,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        """Update a Gantt chart in an app.

        Args:
            app_id: The ID of the app containing the chart
            chart_index: The index of the chart to update
            request: The request object containing the updated chart configuration
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            ChartResponse: Response containing the result of the operation
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_gantt_chart",
            )

        payload = {
            "appId": app_id,
            "chartIndex": chart_index,
            "chartType": ChartType.GANTT_CHART.value,
            **request.to_json(),
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name
        logger.info(f"Updating Gantt chart for app_id: {app_id} at index {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="update_gantt_chart",
            )

        return ChartResponse(
            success=True,
            message="Successfully updated Gantt chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="update_gantt_chart",
            data=response_data,
        )

    def reorder_chart(
        self,
        app_id: str,
        source_index: int,
        target_index: int,
        version_variable_name: str | None = None,
    ) -> ChartResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="reorder",
            )

        payload = {
            "appId": app_id,
            "sourceIndex": source_index,
            "targetIndex": target_index,
        }
        if version_variable_name is not None:
            payload["versionVariableName"] = version_variable_name

        logger.info(
            f"Reordering chart for app_id: {app_id} from index {source_index} to {target_index}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/reorderChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                version_variable_name=version_variable_name,
                operation="reorder",
            )

        return ChartResponse(
            success=True,
            message="Successfully reordered chart",
            app_id=app_id,
            version_variable_name=version_variable_name,
            operation="reorder",
            data=response_data,
        )

    def get_charts(
        self, app_id: str, version_variable_name: str | None = None
    ) -> BaseResponse:
        """Get all charts for a specific app.

        Args:
            app_id: The ID of the app to get charts for
            version_variable_name: The variable name representing the app version. If not specified, the live version is used

        Returns:
            BaseResponse : Response containing the list of charts
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False, message=env_error, operation="get_charts"
            )
        params = {
            "appId": app_id,
        }
        if version_variable_name is not None:
            params["versionVariableName"] = version_variable_name

        logger.info(f"Getting charts for app_id: {app_id}")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET", endpoint="analytics/getAppCharts", params=params
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False, message=error_message, operation="get_charts"
            )
        return BaseResponse(
            success=True,
            message="Successfully retrieved charts",
            operation="get_charts",
            data=response_data,
        )


class AnalyticsAPIKeyClient(BaseAPIKeyClient, AnalyticsClient):
    """Client for managing Clappia analytics and charts with API key authentication.

    This client combines API key authentication with all analytics business logic.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize analytics client with API key.

        Args:
            api_key: Clappia API key.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAPIKeyClient.__init__(self, api_key, base_url, timeout)


class AnalyticsAuthTokenClient(BaseAuthTokenClient, AnalyticsClient):
    """Client for managing Clappia analytics and charts with auth token authentication.

    This client combines auth token authentication with all analytics business logic.
    """

    def __init__(
        self,
        auth_token: str,
        workplace_id: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize analytics client with auth token.

        Args:
            auth_token: Clappia Auth token.
            workplace_id: Clappia Workplace ID.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAuthTokenClient.__init__(self, auth_token, workplace_id, base_url, timeout)
