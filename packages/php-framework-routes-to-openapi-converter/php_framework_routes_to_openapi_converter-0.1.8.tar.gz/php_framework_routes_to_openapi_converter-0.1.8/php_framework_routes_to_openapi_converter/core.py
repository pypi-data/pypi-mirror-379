"""Core API for PHP framework routes to OpenAPI conversion."""
from collections.abc import Iterable
from typing import Any

from php_framework_detector.core.models import FrameworkType

from php_framework_routes_to_openapi_converter.converters import CakePHPConverter
from php_framework_routes_to_openapi_converter.converters import CodeIgniterConverter
from php_framework_routes_to_openapi_converter.converters import DrupalConverter
from php_framework_routes_to_openapi_converter.converters import DrushConverter
from php_framework_routes_to_openapi_converter.converters import FastRouteConverter
from php_framework_routes_to_openapi_converter.converters import FatFreeConverter
from php_framework_routes_to_openapi_converter.converters import FuelConverter
from php_framework_routes_to_openapi_converter.converters import LaminasConverter
from php_framework_routes_to_openapi_converter.converters import LaravelConverter
from php_framework_routes_to_openapi_converter.converters import PhalconConverter
from php_framework_routes_to_openapi_converter.converters import PhpixieConverter
from php_framework_routes_to_openapi_converter.converters import PopPHPConverter
from php_framework_routes_to_openapi_converter.converters import RouteConverter
from php_framework_routes_to_openapi_converter.converters import SlimConverter
from php_framework_routes_to_openapi_converter.converters import SymfonyConverter
from php_framework_routes_to_openapi_converter.converters import ThinkPHPConverter
from php_framework_routes_to_openapi_converter.converters import YiiConverter
from php_framework_routes_to_openapi_converter.converters import ZendFrameworkConverter


def get_converter(framework: str, parameters_file: str | None = None) -> RouteConverter:
    """Get the appropriate converter for the framework.

    Args:
        framework: The PHP framework name (case-insensitive)
        parameters_file: Optional path to static analysis parameters file

    Returns:
        RouteConverter: The appropriate converter instance

    Raises:
        ValueError: If the framework is not supported

    Example:
        >>> converter = get_converter("laravel")
        >>> isinstance(converter, LaravelConverter)
        True
    """
    converters = {
        FrameworkType.LARAVEL: LaravelConverter(parameters_file),
        FrameworkType.SYMFONY: SymfonyConverter(parameters_file),
        FrameworkType.CODEIGNITER: CodeIgniterConverter(parameters_file),
        FrameworkType.CAKEPHP: CakePHPConverter(parameters_file),
        FrameworkType.YII: YiiConverter(parameters_file),
        FrameworkType.THINKPHP: ThinkPHPConverter(parameters_file),
        FrameworkType.SLIM: SlimConverter(parameters_file),
        FrameworkType.FATFREE: FatFreeConverter(parameters_file),
        FrameworkType.FASTROUTE: FastRouteConverter(parameters_file),
        FrameworkType.FUEL: FuelConverter(parameters_file),
        FrameworkType.PHALCON: PhalconConverter(parameters_file),
        FrameworkType.PHPIXIE: PhpixieConverter(parameters_file),
        FrameworkType.POPPHP: PopPHPConverter(parameters_file),
        FrameworkType.LAMINAS: LaminasConverter(parameters_file),
        FrameworkType.ZENDFRAMEWORK: ZendFrameworkConverter(parameters_file),
        FrameworkType.DRUPAL: DrupalConverter(parameters_file),
        FrameworkType.DRUSH: DrushConverter(parameters_file),
    }
    return converters[FrameworkType(framework)]


def convert_routes_to_openapi(
    routes: Iterable,
    framework: str,
    parameters_file: str | None = None,
) -> dict[str, Any]:
    """Convert routes to OpenAPI specification using framework-specific converter.

    Args:
        routes: Route structure from the framework
            - For Laravel/CodeIgniter: List[Dict[str, Any]]
            - For Symfony: Dict[str, Dict[str, Any]]
        framework: The PHP framework name
        parameters_file: Optional path to static analysis parameters file

    Returns:
        Dict containing the complete OpenAPI 3.0 specification

    Raises:
        ValueError: If the framework is not supported

    Example:
        >>> routes = [{"uri": "/users", "methods": ["GET"], "name": "users.index"}]
        >>> spec = convert_routes_to_openapi(routes, "laravel")
        >>> spec["openapi"]
        '3.0.0'
    """
    return get_converter(framework, parameters_file).convert(routes)


def get_supported_frameworks() -> list[str]:
    """Get list of supported PHP frameworks.

    Returns:
        List of supported framework names in lowercase

    Example:
        >>> frameworks = get_supported_frameworks()
        >>> "laravel" in frameworks
        True
    """
    return ['laravel', 'symfony', 'codeigniter']


def validate_framework(framework: str) -> bool:
    """Validate if a framework is supported.

    Args:
        framework: The framework name to validate

    Returns:
        True if the framework is supported, False otherwise

    Example:
        >>> validate_framework("laravel")
        True
        >>> validate_framework("unknown")
        False
    """
    return framework.lower() in get_supported_frameworks()
