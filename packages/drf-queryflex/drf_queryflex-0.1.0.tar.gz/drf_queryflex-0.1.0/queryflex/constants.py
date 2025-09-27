"""Constants and configuration for drf-queryflex"""

# Supported operators
OPERATORS = {
    'eq': 'exact',
    'ne': 'exact',  # Handled specially for negation
    'gt': 'gt',
    'gte': 'gte',
    'lt': 'lt',
    'lte': 'lte',
    'contains': 'contains',
    'icontains': 'icontains',
    'startswith': 'startswith',
    'istartswith': 'istartswith',
    'endswith': 'endswith',
    'iendswith': 'iendswith',
    'in': 'in',
    'isnull': 'isnull',
    'regex': 'regex',
    'iregex': 'iregex',
    'search': 'search',  # Full-text search
}

# Reverse mapping for Django lookups to friendly names
LOOKUP_NAMES = {v: k for k, v in OPERATORS.items()}

# Reserved query parameters
RESERVED_PARAMS = {'fields', 'include', 'exclude', 'sort', 'page', 'page_size', 'format'}

# Maximum depth for nested relationships
MAX_RELATION_DEPTH = 5

# Default configuration
DEFAULT_CONFIG = {
    'max_depth': MAX_RELATION_DEPTH,
    'allowed_operators': list(OPERATORS.keys()),
    'enable_field_selection': True,
    'enable_complex_operations': True,
}