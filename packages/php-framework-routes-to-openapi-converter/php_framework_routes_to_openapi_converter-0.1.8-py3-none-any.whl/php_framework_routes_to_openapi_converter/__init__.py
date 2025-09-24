"""PHP Framework Routes to OpenAPI Converter.

A Python library and CLI tool for converting PHP framework routes
to OpenAPI 3.0 specifications.

Supported frameworks:
- Laravel
- Symfony
- CodeIgniter

Example:
    >>> from php_framework_routes_to_openapi_converter import convert_routes_to_openapi
    >>> routes = [{"uri": "/users", "methods": ["GET"], "name": "users.index"}]
    >>> spec = convert_routes_to_openapi(routes, "laravel")
    >>> print(spec["openapi"])
    3.0.0
"""
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
from php_framework_routes_to_openapi_converter.core import convert_routes_to_openapi
from php_framework_routes_to_openapi_converter.core import get_converter
from php_framework_routes_to_openapi_converter.core import get_supported_frameworks
from php_framework_routes_to_openapi_converter.core import validate_framework

__version__ = '0.1.0'

__all__ = [
    # Core API functions
    'convert_routes_to_openapi',
    'get_converter',
    'get_supported_frameworks',
    'validate_framework',

    # Converter classes
    'RouteConverter',
    'LaravelConverter',
    'SymfonyConverter',
    'CodeIgniterConverter',
    'CakePHPConverter',
    'DrupalConverter',
    'DrushConverter',
    'FastRouteConverter',
    'FatFreeConverter',
    'FuelConverter',
    'LaminasConverter',
    'PhalconConverter',
    'PhpixieConverter',
    'PopPHPConverter',
    'SlimConverter',
    'ThinkPHPConverter',
    'YiiConverter',
    'ZendFrameworkConverter',
]
