"""
Modern Wikipedia API Client

A production-ready, async Wikipedia API client with advanced features.
"""

from wikipedia_async.client import WikipediaClient
from wikipedia_async.config import ClientConfig
from wikipedia_async.models import (
    SearchResult,
    WikiPage,
    PageSummary,
    Coordinates,
    Language,
    GeoSearchResult,
)
from wikipedia_async.exceptions import (
    WikipediaException,
    PageNotFoundError,
    DisambiguationError,
    RedirectError,
    RateLimitError,
    TimeoutError,
    NetworkError,
)

from wikipedia_async.helpers.section_helpers import (
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
