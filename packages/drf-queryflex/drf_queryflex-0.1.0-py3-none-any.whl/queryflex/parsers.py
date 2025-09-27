"""Query parsing logic for drf-queryflex"""

import json
import re
from typing import Dict, List, Any, Union, Tuple
from django.db.models import Q
from .constants import OPERATORS, RESERVED_PARAMS
from .exceptions import InvalidOperatorError, QuerySyntaxError, SecurityError
from .utils import parse_value, sanitize_field_path, build_lookup_expression

class QueryParser:
    """Parses various query syntax formats into standardized filters"""
    
    def __init__(self, query_params: Dict[str, str], model=None, allowed_fields: List[str] = None, config: Dict = None):
        self.query_params = {k: v for k, v in query_params.items() if k not in RESERVED_PARAMS}
        self.model = model
        self.allowed_fields = set(allowed_fields) if allowed_fields else None
        self.config = config or {}
        self.max_depth = self.config.get('max_depth', 5)
    
    def parse_filters(self) -> Q:
        """Parse query parameters into Django Q object"""
        q_object = Q()
        
        if not self.query_params:
            return q_object
            
        # Try different syntax formats in order of preference
        if 'filter' in self.query_params:
            filters = self._parse_filter_param(self.query_params['filter'])
        elif 'q' in self.query_params:
            filters = self._parse_q_param(self.query_params['q'])
        else:
            filters = self._parse_individual_params()
        
        # Convert filters to Q object
        for field_path, condition in filters.items():
            if not sanitize_field_path(field_path, self.max_depth):
                raise SecurityError(f"Field path '{field_path}' is not allowed")
                
            q_object &= self._build_q_expression(field_path, condition)
            
        return q_object
    
    def _parse_filter_param(self, filter_str: str) -> Dict[str, Any]:
        """Parse GraphQL-like filter syntax"""
        try:
            # Support both JSON and simplified syntax
            if filter_str.startswith('{') and filter_str.endswith('}'):
                return self._parse_json_syntax(filter_str)
            else:
                return self._parse_simplified_syntax(filter_str)
        except (json.JSONDecodeError, ValueError) as e:
            raise QuerySyntaxError(f"Invalid filter syntax: {str(e)}")
    
    def _parse_json_syntax(self, filter_str: str) -> Dict[str, Any]:
        """Parse JSON filter syntax"""
        try:
            filters = json.loads(filter_str)
            return self._normalize_json_filters(filters)
        except json.JSONDecodeError as e:
            raise QuerySyntaxError(f"Invalid JSON: {str(e)}")
    
    def _normalize_json_filters(self, filters: Dict, prefix: str = '') -> Dict:
        """Normalize JSON filters into flat structure"""
        normalized = {}
        
        for key, value in filters.items():
            current_path = f"{prefix}__{key}" if prefix else key
            
            if isinstance(value, dict):
                if 'and' in value or 'or' in value:
                    # Complex condition
                    normalized[current_path] = value
                else:
                    # Nested field conditions
                    normalized.update(self._normalize_json_filters(value, current_path))
            else:
                normalized[current_path] = value
                
        return normalized
    
    def _parse_simplified_syntax(self, filter_str: str) -> Dict[str, Any]:
        """Parse simplified filter syntax"""
        filters = {}
        
        # Split by commas but respect quoted strings and parentheses
        conditions = self._smart_split(filter_str)
        
        for condition in conditions:
            condition = condition.strip()
            if not condition:
                continue
                
            # Parse condition
            field, operator, value = self._parse_condition(condition)
            filters[field] = value
            
        return filters
    
    def _smart_split(self, text: str) -> List[str]:
        """Split text by commas, respecting quotes and parentheses"""
        parts = []
        current = []
        paren_depth = 0
        in_quotes = False
        quote_char = None
        
        for char in text:
            if char in ('"', "'") and not in_quotes:
                in_quotes = True
                quote_char = char
                current.append(char)
            elif char == quote_char and in_quotes:
                in_quotes = False
                quote_char = None
                current.append(char)
            elif char == '(' and not in_quotes:
                paren_depth += 1
                current.append(char)
            elif char == ')' and not in_quotes:
                paren_depth -= 1
                current.append(char)
            elif char == ',' and not in_quotes and paren_depth == 0:
                parts.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        
        if current:
            parts.append(''.join(current).strip())
            
        return parts
    
    def _parse_condition(self, condition: str) -> Tuple[str, str, Any]:
        """Parse a single condition into field, operator, value"""
        # Operator patterns (order matters for multi-character operators)
        operators = [
            ('>=', 'gte'), ('<=', 'lte'), ('!=', 'ne'),
            ('>', 'gt'), ('<', 'lt'), ('=', 'eq'),
            (':', 'eq')  # Default operator for q syntax
        ]
        
        for op_symbol, op_name in operators:
            if op_symbol in condition:
                parts = condition.split(op_symbol, 1)
                if len(parts) == 2:
                    field = parts[0].strip()
                    value_str = parts[1].strip()
                    value = parse_value(value_str)
                    return field, op_name, value
        
        # If no operator found, treat as existence check
        return condition.strip(), 'isnull', False
    
    def _parse_q_param(self, q_str: str) -> Dict[str, Any]:
        """Parse field:operator:value syntax"""
        filters = {}
        conditions = self._smart_split(q_str)
        
        for condition in conditions:
            parts = condition.split(':', 2)
            if len(parts) == 3:
                field, operator, value_str = parts
            elif len(parts) == 2:
                field, value_str = parts
                operator = 'eq'
            else:
                continue
                
            field = field.strip()
            operator = operator.strip()
            value = parse_value(value_str.strip())
            
            if operator not in OPERATORS:
                raise InvalidOperatorError(f"Unknown operator: {operator}")
                
            filters[field] = value
            
        return filters
    
    def _parse_individual_params(self) -> Dict[str, Any]:
        """Parse individual query parameters"""
        filters = {}
        
        for param, value in self.query_params.items():
            if param in RESERVED_PARAMS:
                continue
                
            # Handle field__operator syntax
            if '__' in param:
                field_parts = param.split('__')
                if field_parts[-1] in OPERATORS.values():
                    filters[param] = parse_value(value)
                else:
                    # Default to exact match
                    filters[f"{param}__exact"] = parse_value(value)
            else:
                # Default to exact match
                filters[f"{param}__exact"] = parse_value(value)
                
        return filters
    
    def _build_q_expression(self, field_path: str, condition: Any) -> Q:
        """Build Q object from field path and condition"""
        if isinstance(condition, dict):
            return self._build_complex_q(field_path, condition)
        else:
            lookup = build_lookup_expression(field_path, 'eq', condition)
            return Q(**{lookup: condition})
    
    def _build_complex_q(self, field_path: str, conditions: Dict) -> Q:
        """Build Q object for complex conditions"""
        q_object = Q()
        
        if 'and' in conditions:
            for condition in conditions['and']:
                for sub_field, sub_value in condition.items():
                    full_path = f"{field_path}__{sub_field}" if sub_field else field_path
                    q_object &= self._build_q_expression(full_path, sub_value)
        
        elif 'or' in conditions:
            or_q = Q()
            for condition in conditions['or']:
                for sub_field, sub_value in condition.items():
                    full_path = f"{field_path}__{sub_field}" if sub_field else field_path
                    or_q |= self._build_q_expression(full_path, sub_value)
            q_object &= or_q
        
        else:
            # Treat as simple key-value pairs
            for sub_field, sub_value in conditions.items():
                full_path = f"{field_path}__{sub_field}"
                q_object &= self._build_q_expression(full_path, sub_value)
                
        return q_object