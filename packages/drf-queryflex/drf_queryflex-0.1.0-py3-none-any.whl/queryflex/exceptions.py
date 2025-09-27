"""Custom exceptions for drf-queryflex"""

from rest_framework.exceptions import APIException
from rest_framework import status

class QueryFlexException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Query parsing error'
    default_code = 'query_parsing_error'

class InvalidFieldError(QueryFlexException):
    default_detail = 'Invalid field specified'
    default_code = 'invalid_field'

class InvalidOperatorError(QueryFlexException):
    default_detail = 'Invalid operator specified'
    default_code = 'invalid_operator'

class RelationshipDepthError(QueryFlexException):
    default_detail = 'Relationship depth exceeds maximum allowed'
    default_code = 'relationship_depth_exceeded'

class QuerySyntaxError(QueryFlexException):
    default_detail = 'Invalid query syntax'
    default_code = 'invalid_syntax'

class SecurityError(QueryFlexException):
    default_detail = 'Query contains potentially unsafe operations'
    default_code = 'security_error'