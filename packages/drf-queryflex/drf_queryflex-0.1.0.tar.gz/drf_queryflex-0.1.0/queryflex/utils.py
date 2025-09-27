"""Utility functions for drf-queryflex"""

import re
import json
from typing import Any, Dict, List, Set
from django.db import models
from django.core.exceptions import FieldError
from .constants import OPERATORS, RESERVED_PARAMS
from .exceptions import InvalidFieldError, SecurityError

def validate_field_name(field_name: str, model: models.Model, allowed_fields: Set[str] = None) -> bool:
    """
    Validate that a field exists on the model and is allowed
    """
    if allowed_fields and field_name not in allowed_fields:
        return False
    
    try:
        # Split field path to handle relationships
        parts = field_name.split('__')
        current_model = model
        
        for part in parts:
            if hasattr(current_model, part):
                field = getattr(current_model, part)
                if hasattr(field, 'field'):
                    current_model = field.field.related_model
                else:
                    # Check if it's a manager (reverse relation)
                    if hasattr(field, 'related'):
                        current_model = field.related.related_model
                    else:
                        return False
            else:
                # Check if it's a direct field
                if not hasattr(current_model, '_meta') or part not in [f.name for f in current_model._meta.get_fields()]:
                    return False
        return True
    except (AttributeError, FieldError):
        return False

def parse_value(value: str) -> Any:
    """
    Parse string values into appropriate Python types
    """
    if not isinstance(value, str):
        return value
        
    value = value.strip()
    
    # Boolean values
    if value.lower() in ('true', 'false'):
        return value.lower() == 'true'
    
    # Null values
    if value.lower() == 'null':
        return None
    
    # Numbers
    if value.isdigit():
        return int(value)
    
    # Floating point numbers
    if re.match(r'^-?\d+\.\d+$', value):
        return float(value)
    
    # Scientific notation
    if re.match(r'^-?\d+\.?\d*[eE][+-]?\d+$', value):
        return float(value)
    
    # Lists (comma-separated)
    if ',' in value and not (value.startswith('"') and value.endswith('"')):
        return [parse_value(v.strip()) for v in value.split(',')]
    
    # Remove quotes from strings
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    
    return value

def build_lookup_expression(field: str, operator: str, value: Any) -> str:
    """
    Build Django lookup expression from field, operator, and value
    """
    if operator == 'ne':
        # Handle not equal specially
        return f"{field}__{OPERATORS['eq']}"
    
    if operator in OPERATORS:
        return f"{field}__{OPERATORS[operator]}"
    
    raise InvalidOperatorError(f"Unknown operator: {operator}")

def sanitize_field_path(field_path: str, max_depth: int = 5) -> bool:
    """
    Sanitize field path to prevent security issues
    """
    if field_path.count('__') > max_depth:
        return False
    
    # Prevent common injection patterns
    unsafe_patterns = [
        r'\.\.',  # Directory traversal
        r'[\(\)]',  # Function calls
        r';',  # Command injection
        r'`',  # Command injection
        r'\$',  # Variable injection
    ]
    
    for pattern in unsafe_patterns:
        if re.search(pattern, field_path):
            return False
    
    return True

def get_model_fields(model: models.Model) -> List[str]:
    """
    Get all field names for a model
    """
    return [f.name for f in model._meta.get_fields()]

def extract_relationships(field_path: str) -> List[str]:
    """
    Extract relationship path from field path
    """
    parts = field_path.split('__')
    relationships = []
    
    for i in range(len(parts) - 1):
        relationships.append('__'.join(parts[:i+1]))
    
    return relationships