"""
Django Easy Pagination
======================

A Django REST Framework library providing customizable pagination classes
with rich metadata and flexible configuration options.

Author: Casper
Email: cassymyo@gmail.com
License: MIT
"""

__version__ = "0.1.0"
__author__ = "Casper"
__email__ = "cassymyo@gmail.com"
__license__ = "MIT"

from .pagination import (
    CustomPageNumberPagination,
    LargeResultsPagination,
    NoPagination,
    SmallResultsPagination,
    StandardPagination,
    get_pagination_class,
)

__all__ = [
    "CustomPageNumberPagination",
    "StandardPagination",
    "SmallResultsPagination",
    "LargeResultsPagination",
    "NoPagination",
    "get_pagination_class",
    "__version__",
]
