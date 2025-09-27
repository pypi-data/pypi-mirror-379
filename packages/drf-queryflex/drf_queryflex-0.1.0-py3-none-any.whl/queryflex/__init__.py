"""DRF QueryFlex - Advanced filtering with GraphQL-like syntax for Django REST Framework"""
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.1.0"
    
__author__ = "Sifat Ali"
__email__ = "sifat.de.com"

from .filters import QueryFlexFilterBackend
from .parsers import QueryParser
from .optimizers import FieldSelector, QueryOptimizer
from .exceptions import (
    QueryFlexException,
    InvalidFieldError,
    InvalidOperatorError,
    RelationshipDepthError,
    QuerySyntaxError
)

__all__ = [
    'QueryFlexFilterBackend',
    'QueryParser',
    'FieldSelector',
    'QueryOptimizer',
    'QueryFlexException',
    'InvalidFieldError',
    'InvalidOperatorError',
    'RelationshipDepthError',
    'QuerySyntaxError',
]