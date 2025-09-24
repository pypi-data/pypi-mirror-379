"""Data models for PHP framework routes to OpenAPI conversion."""
from dataclasses import dataclass
from typing import Any


@dataclass
class OpenAPIPathItem:
    """Represents an OpenAPI path item.

    Attributes:
        path: The URL path of the endpoint
        methods: List of HTTP methods (GET, POST, etc.)
        summary: Human-readable description of the endpoint
        tags: List of tags for grouping endpoints
        parameters: Optional parameters for the endpoint
        request_body: Optional request body schema
        responses: Optional response definitions
    """
    path: str
    methods: list[str]
    summary: str
    tags: list[str]
    parameters: list[dict[str, Any]] | None = None
    request_body: dict[str, Any] | None = None
    responses: dict[str, Any] | None = None

    def openapi(self) -> dict[str, Any]:
        """Convert this path item to OpenAPI path item format.

        Returns:
            Dict containing the OpenAPI path item structure
        """
        path_item = {}

        for method in self.methods:
            method_lower = method.lower()
            operation: dict[str, Any] = {
                'summary': self.summary,
                'tags': self.tags,
                'responses': self.responses or {'200': {'description': 'Success'}},
            }

            if self.parameters:
                operation['parameters'] = self.parameters

            if self.request_body and method_lower in ['post', 'put', 'patch']:
                operation['requestBody'] = self.request_body

            path_item[method_lower] = operation

        return path_item
