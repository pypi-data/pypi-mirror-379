"""
Modern Wikipedia API Client

A production-ready, async Wikipedia API client with advanced features.
"""

from .client import WikipediaClient
from .config import ClientConfig
from .models import (
    SearchResult,
    WikiPage,
    PageSummary,
    Coordinates,
    Language,
    GeoSearchResult,
)
from .exceptions import (
    WikipediaException,
    PageNotFoundError,
    DisambiguationError,
    RedirectError,
    RateLimitError,
    TimeoutError,
    NetworkError,
)

from .helpers import (
    SectionNode,
    SectionResult,
)

__version__ = "0.6.0"
__all__ = [
    "WikipediaClient",
    "ClientConfig",
    "SearchResult",
    "WikiPage",
    "PageSummary",
    "Coordinates",
    "Language",
    "GeoSearchResult",
    "WikipediaException",
    "PageNotFoundError",
    "DisambiguationError",
    "RedirectError",
    "RateLimitError",
    "TimeoutError",
    "NetworkError",
    "SectionNode",
    "SectionResult",
]
