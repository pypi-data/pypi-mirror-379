"""Query optimization for field selection and performance"""

from typing import Dict, List, Set, Any
from django.db.models import Prefetch, QuerySet
from .utils import extract_relationships, validate_field_name
from .exceptions import InvalidFieldError

class FieldSelector:
    """Handles GraphQL-like field selection"""
    
    def __init__(self, query_params: Dict[str, str], model=None, allowed_fields: List[str] = None):
        self.query_params = query_params
        self.model = model
        self.allowed_fields = set(allowed_fields) if allowed_fields else None
    
    def get_selected_fields(self) -> Dict[str, Any]:
        """Parse fields parameter into structured field selection"""
        fields_param = self.query_params.get('fields', '').strip()
        include_param = self.query_params.get('include', '').strip()
        exclude_param = self.query_params.get('exclude', '').strip()
        
        if fields_param:
            selection = self._parse_fields_param(fields_param)
            return self._validate_field_selection(selection)
        else:
            return {
                'include': self._parse_list_param(include_param),
                'exclude': self._parse_list_param(exclude_param)
            }
    
    def _parse_fields_param(self, fields_str: str) -> Dict[str, Any]:
        """Parse GraphQL-like fields syntax"""
        if not fields_str:
            return {}
        
        # Remove whitespace for easier parsing
        clean_str = re.sub(r'\s+', '', fields_str)
        return self._parse_fields_recursive(clean_str)
    
    def _parse_fields_recursive(self, fields_str: str) -> Dict[str, Any]:
        """Recursively parse fields string"""
        fields = {}
        i = 0
        current_field = ''
        buffer = ''
        
        while i < len(fields_str):
            char = fields_str[i]
            
            if char == '{':
                # Start of nested fields
                if current_field:
                    # Find matching closing brace
                    brace_count = 1
                    j = i + 1
                    while j < len(fields_str) and brace_count > 0:
                        if fields_str[j] == '{':
                            brace_count += 1
                        elif fields_str[j] == '}':
                            brace_count -= 1
                        j += 1
                    
                    nested_str = fields_str[i+1:j-1]
                    fields[current_field] = self._parse_fields_recursive(nested_str)
                    i = j
                    current_field = ''
                else:
                    buffer += char
                    i += 1
                    
            elif char == '}':
                # Should be handled by brace matching
                buffer += char
                i += 1
                
            elif char == ',':
                if current_field:
                    fields[current_field] = {}
                elif buffer:
                    fields[buffer] = {}
                current_field = ''
                buffer = ''
                i += 1
                
            else:
                if not current_field and buffer and char.isalnum():
                    current_field = buffer
                    buffer = char
                else:
                    buffer += char
                i += 1
        
        # Handle remaining buffer
        if current_field:
            fields[current_field] = {}
        elif buffer:
            fields[buffer] = {}
            
        return fields
    
    def _validate_field_selection(self, selection: Dict) -> Dict:
        """Validate that selected fields are allowed"""
        if not self.model or not self.allowed_fields:
            return selection
            
        validated = {}
        for field, subfields in selection.items():
            if validate_field_name(field, self.model, self.allowed_fields):
                if subfields:
                    # For nested fields, we need to get the related model
                    # Simplified validation - in practice, you'd need model introspection
                    validated[field] = self._validate_field_selection(subfields)
                else:
                    validated[field] = {}
                    
        return validated
    
    def _parse_list_param(self, param_str: str) -> List[str]:
        """Parse comma-separated list parameters"""
        if not param_str:
            return []
        return [field.strip() for field in param_str.split(',') if field.strip()]

class QueryOptimizer:
    """Optimizes queries based on field selection and relationships"""
    
    def __init__(self, field_selection: Dict, model=None):
        self.field_selection = field_selection
        self.model = model
    
    def optimize_queryset(self, queryset: QuerySet) -> QuerySet:
        """Apply select_related and prefetch_related optimizations"""
        if not self.field_selection or not self.model:
            return queryset
            
        relationships = self._analyze_relationships()
        
        # Apply select_related for foreign keys and one-to-one
        if relationships['select_related']:
            queryset = queryset.select_related(*relationships['select_related'])
        
        # Apply prefetch_related for many-to-many and reverse relations
        for prefetch in relationships['prefetch_related']:
            if isinstance(prefetch, str):
                queryset = queryset.prefetch_related(prefetch)
            else:
                queryset = queryset.prefetch_related(prefetch)
                
        return queryset
    
    def _analyze_relationships(self) -> Dict[str, List]:
        """Analyze field selection to determine relationships"""
        select_related = set()
        prefetch_related = set()
        
        if isinstance(self.field_selection, dict):
            self._analyze_fields_recursive(self.field_selection, '', select_related, prefetch_related)
        
        return {
            'select_related': list(select_related),
            'prefetch_related': list(prefetch_related)
        }
    
    def _analyze_fields_recursive(self, fields: Dict, prefix: str, 
                                select_related: Set, prefetch_related: Set):
        """Recursively analyze fields for relationships"""
        for field, subfields in fields.items():
            full_path = f"{prefix}__{field}" if prefix else field
            
            if subfields:  # This field has nested selections - it's a relationship
                # Simple heuristic: singular field names are likely FK/O2O
                if self._is_foreign_key_like(field):
                    select_related.add(field)
                    self._analyze_fields_recursive(subfields, field, select_related, prefetch_related)
                else:
                    # Likely a reverse relation or M2M
                    prefetch_related.add(field)
    
    def _is_foreign_key_like(self, field_name: str) -> bool:
        """Heuristic to determine if a field is likely a foreign key"""
        # Simple heuristic - in practice, you'd inspect the model
        return not field_name.endswith('s')  # Plural often indicates many relationship

def optimize_query(queryset: QuerySet, field_selection: Dict, model=None) -> QuerySet:
    """Convenience function to optimize a queryset"""
    optimizer = QueryOptimizer(field_selection, model)
    return optimizer.optimize_queryset(queryset)