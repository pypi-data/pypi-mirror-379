"""FatFree framework route converter."""
from collections.abc import Iterable
from typing import Any

from php_framework_routes_to_openapi_converter.converters.base import RouteConverter
from php_framework_routes_to_openapi_converter.models import OpenAPIPathItem
from php_framework_routes_to_openapi_converter.utils.parameter_analyzer import ParameterAnalyzer


class FatFreeConverter(RouteConverter):
    """FatFree framework route converter."""

    def __init__(self, parameters_file: str | None = None):
        """Initialize FatFree converter with optional parameters file.

        Args:
            parameters_file: Path to static analysis parameters file
        """
        self.parameter_analyzer = None
        if parameters_file:
            self.parameter_analyzer = ParameterAnalyzer(parameters_file)

    def _path_items_generator(self, routes: Iterable) -> Iterable[OpenAPIPathItem]:
        """Generate path items from FatFree routes."""
        for route in routes:
            path = self._get_path(route)
            if not path:
                continue

            methods = self._get_methods(route)
            summary = self._get_summary(route)
            tags = self._get_tags(route)

            # Get parameters and request body if analyzer is available
            parameters = None
            request_body = None

            if self.parameter_analyzer:
                action = route.get('action')
                if action:
                    # Extract class and method from action
                    if '@' in action:
                        parts = action.split('@', 1)
                        if len(parts) == 2:
                            class_path, method = parts
                            # Extract class name from full path
                            class_parts = class_path.split('\\')
                            # Get the last part (class name)
                            class_name = class_parts[-1]
                            method_key = f"{class_name}::{method}"

                            method_params = self.parameter_analyzer.get_parameters_for_method(
                                method_key,
                            )
                            if method_params:
                                parameters = self.parameter_analyzer.convert_to_openapi_parameters(
                                    method_params,
                                )
                                request_body = self.parameter_analyzer.get_request_body_schema(
                                    method_params,
                                )

            yield OpenAPIPathItem(
                path=path,
                methods=methods,
                summary=summary,
                tags=tags,
                parameters=parameters,
                request_body=request_body,
            )

    def _get_path(self, route: dict[str, Any]) -> str:
        return route.get('uri', '')

    def _get_methods(self, route: dict[str, Any]) -> list[str]:
        return route.get('methods', [])

    def _get_summary(self, route: dict[str, Any]) -> str:
        return route.get('name', '')

    def _get_tags(self, route: dict[str, Any]) -> list[str]:
        return route.get('tags', [])
