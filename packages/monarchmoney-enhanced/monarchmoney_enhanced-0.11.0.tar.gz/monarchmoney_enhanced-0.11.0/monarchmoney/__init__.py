"""
monarchmoney

A Python API for interacting with MonarchMoney.
"""

# Import new exception hierarchy
from .exceptions import (
    AuthenticationError,
    ClientError,
    ConfigurationError,
    DataError,
    GraphQLError,
    InvalidMFAError,
    MFARequiredError,
    MonarchMoneyError,
    NetworkError,
    RateLimitError,
    ServerError,
    SessionExpiredError,
    ValidationError,
)
from .monarchmoney import (  # Legacy exceptions for backward compatibility
    LoginFailedException,
    MonarchMoney,
    MonarchMoneyEndpoints,
    RequestFailedException,
    RequireMFAException,
)
from .utils import (
    batch_items,
    flatten_dict,
    format_date_for_api,
    normalize_amount,
    safe_get,
    truncate_string,
)

# GraphQL Optimizations (optional)
try:
    from .optimizations import (
        CacheStrategy,
        OptimizedMonarchMoney,
        QueryCache,
        RequestDeduplicator,
    )
    from .graphql import (
        FRAGMENTS,
        QueryVariants,
        QueryBuilder,
        BatchedGraphQLClient,
    )
    _OPTIMIZATIONS_AVAILABLE = True
except ImportError:
    _OPTIMIZATIONS_AVAILABLE = False

__version__ = "0.11.0"
__author__ = "keithah"
