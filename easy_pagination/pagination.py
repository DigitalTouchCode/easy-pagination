"""
Global Pagination Classes for Django REST Framework

This module provides reusable pagination classes that can be used across
the entire project. These classes provide rich metadata and are easily
customizable per view.

Usage:
    # In your viewset:
    from utils.pagination import StandardPagination

    class MyViewSet(viewsets.ModelViewSet):
        pagination_class = StandardPagination
        # ... rest of your viewset
"""

from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    """
    Base pagination class with rich metadata.

    Response format:
    {
        "count": 100,
        "next": "http://api.example.com/items/?page=3",
        "previous": "http://api.example.com/items/?page=1",
        "total_pages": 10,
        "current_pagejm
        "page_size": 10,
        "results": [...]
    }
    """

    # Allow client to override page size using query parameter
    page_size_query_param = "page_size"

    # Maximum page size that client can request
    max_page_size = 1000

    def get_paginated_response(self, data):
        """
        Return paginated response with additional metadata.
        """
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("total_pages", self.page.paginator.num_pages),
                    ("current_page", self.page.number),
                    ("page_size", self.page.paginator.per_page),
                    ("results", data),
                ]
            )
        )

    def get_paginated_response_schema(self, schema):
        """
        Schema for paginated response (for API documentation).
        """
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "example": 123,
                    "description": "Total number of items",
                },
                "next": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?page=4",
                    "description": "URL to next page",
                },
                "previous": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?page=2",
                    "description": "URL to previous page",
                },
                "total_pages": {
                    "type": "integer",
                    "example": 10,
                    "description": "Total number of pages",
                },
                "current_page": {
                    "type": "integer",
                    "example": 3,
                    "description": "Current page number",
                },
                "page_size": {
                    "type": "integer",
                    "example": 10,
                    "description": "Number of items per page",
                },
                "results": schema,
            },
        }


class StandardPagination(CustomPageNumberPagination):
    """
    Standard pagination for most list views.

    Default: 20 items per page
    Client can request up to 100 items per page using ?page_size=100

    Usage:
        class MyViewSet(viewsets.ModelViewSet):
            pagination_class = StandardPagination
    """

    page_size = 20
    max_page_size = 100


class SmallResultsPagination(CustomPageNumberPagination):
    """
    Pagination for small, quick-loading lists.

    Default: 10 items per page
    Client can request up to 50 items per page

    Usage:
        class QuickListViewSet(viewsets.ModelViewSet):
            pagination_class = SmallResultsPagination
    """

    page_size = 10
    max_page_size = 50


class LargeResultsPagination(CustomPageNumberPagination):
    """
    Pagination for large datasets or reports.

    Default: 50 items per page
    Client can request up to 500 items per page

    Usage:
        class ReportViewSet(viewsets.ModelViewSet):
            pagination_class = LargeResultsPagination
    """

    page_size = 50
    max_page_size = 500


class NoPagination(PageNumberPagination):
    """
    Disable pagination for specific views.

    Use this when you need to return all results without pagination.
    Be careful with large datasets!

    Usage:
        class AllItemsViewSet(viewsets.ModelViewSet):
            pagination_class = NoPagination
    """

    page_size = None

    def paginate_queryset(self, queryset, request, view=None):
        """
        Return None to indicate no pagination.
        """
        return None


# Convenience function for dynamic pagination
def get_pagination_class(page_size=20, max_page_size=100):
    """
    Factory function to create custom pagination class with specific sizes.

    Args:
        page_size (int): Default number of items per page
        max_page_size (int): Maximum items client can request per page

    Returns:
        CustomPageNumberPagination: Configured pagination class

    Usage:
        class MyViewSet(viewsets.ModelViewSet):
            pagination_class = get_pagination_class(page_size=30, max_page_size=200)
    """

    class DynamicPagination(CustomPageNumberPagination):
        pass

    DynamicPagination.page_size = page_size
    DynamicPagination.max_page_size = max_page_size

    return DynamicPagination
