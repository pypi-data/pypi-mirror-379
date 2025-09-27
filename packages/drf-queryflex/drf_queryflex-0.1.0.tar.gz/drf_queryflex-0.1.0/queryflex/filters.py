"""Main filter backend for drf-queryflex"""

from django.db.models import Q
from rest_framework import filters
from rest_framework.request import Request
from rest_framework.views import APIView

from .parsers import QueryParser
from .optimizers import FieldSelector, QueryOptimizer
from .exceptions import InvalidFieldError, RelationshipDepthError, SecurityError
from .constants import DEFAULT_CONFIG

class QueryFlexFilterBackend(filters.BaseFilterBackend):
    """Advanced filtering backend with GraphQL-like syntax"""
    
    def filter_queryset(self, request: Request, queryset, view: APIView):
        # Get configuration from view
        config = self._get_config(view)
        model = getattr(queryset, 'model', None)
        
        try:
            # Parse and apply filters
            parser = QueryParser(
                request.query_params,
                model=model,
                allowed_fields=getattr(view, 'queryflex_allowed_fields', None),
                config=config
            )
            
            q_object = parser.parse_filters()
            if q_object:
                queryset = queryset.filter(q_object)
            
            # Apply field selection and optimization
            if config.get('enable_field_selection', True):
                queryset = self._apply_field_optimization(queryset, request, view, model)
                
        except Exception as e:
            if getattr(view, 'queryflex_raise_exceptions', True):
                raise
            # Log error but don't break the request
            # In production, you might want to log this
            pass
            
        return queryset
    
    def _get_config(self, view: APIView) -> Dict:
        """Get configuration from view with defaults"""
        config = DEFAULT_CONFIG.copy()
        
        # Update with view-specific configuration
        view_config = getattr(view, 'queryflex_config', {})
        config.update(view_config)
        
        # Set individual attributes if they exist
        if hasattr(view, 'queryflex_max_depth'):
            config['max_depth'] = view.queryflex_max_depth
        if hasattr(view, 'queryflex_allowed_operators'):
            config['allowed_operators'] = view.queryflex_allowed_operators
            
        return config
    
    def _apply_field_optimization(self, queryset, request: Request, view: APIView, model):
        """Apply field selection and query optimization"""
        field_selector = FieldSelector(
            request.query_params,
            model=model,
            allowed_fields=getattr(view, 'queryflex_allowed_fields', None)
        )
        
        field_selection = field_selector.get_selected_fields()
        
        if field_selection:
            optimizer = QueryOptimizer(field_selection, model)
            queryset = optimizer.optimize_queryset(queryset)
            
            # TODO: Apply actual field selection to serializers
            # This would require modifying the serializer context
            # or using a custom serializer mixin
            
        return queryset
    
    def get_schema_operation_parameters(self, view: APIView):
        """Provide OpenAPI schema parameters"""
        parameters = [
            {
                'name': 'filter',
                'in': 'query',
                'required': False,
                'description': 'GraphQL-like filter expression',
                'schema': {
                    'type': 'string',
                },
            },
            {
                'name': 'q',
                'in': 'query',
                'required': False,
                'description': 'Simplified filter syntax: field:operator:value',
                'schema': {
                    'type': 'string',
                },
            },
            {
                'name': 'fields',
                'in': 'query',
                'required': False,
                'description': 'Field selection like GraphQL',
                'schema': {
                    'type': 'string',
                },
            },
            {
                'name': 'include',
                'in': 'query',
                'required': False,
                'description': 'Fields to include',
                'schema': {
                    'type': 'string',
                },
            },
            {
                'name': 'exclude',
                'in': 'query',
                'required': False,
                'description': 'Fields to exclude',
                'schema': {
                    'type': 'string',
                },
            },
        ]
        
        return parameters