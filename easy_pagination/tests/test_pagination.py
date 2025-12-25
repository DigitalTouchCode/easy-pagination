"""
Tests for pagination functionality.

Run with: python manage.py test easy_pagination.tests.test_pagination
Or: pytest tests/test_pagination.py
"""

import pytest
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
import os
import sys
import pytest
from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from .. import (
    StandardPagination,
    LargeResultsPagination,
    SmallResultsPagination,
    NoPagination,
    get_pagination_class
)


class PaginationTestCase(TestCase):
    """Test pagination classes"""

    def setUp(self):
        """Set up test fixtures"""
        self.factory = APIRequestFactory()

    def test_standard_pagination_defaults(self):
        """Test StandardPagination default values"""
        pagination = StandardPagination()
        self.assertEqual(pagination.page_size, 20)
        self.assertEqual(pagination.max_page_size, 100)
        self.assertEqual(pagination.page_size_query_param, "page_size")

    def test_small_results_pagination_defaults(self):
        """Test SmallResultsPagination default values"""
        pagination = SmallResultsPagination()
        self.assertEqual(pagination.page_size, 10)
        self.assertEqual(pagination.max_page_size, 50)

    def test_large_results_pagination_defaults(self):
        """Test LargeResultsPagination default values"""
        pagination = LargeResultsPagination()
        self.assertEqual(pagination.page_size, 50)
        self.assertEqual(pagination.max_page_size, 500)

    def test_no_pagination(self):
        """Test NoPagination returns None"""
        pagination = NoPagination()
        request = self.factory.get("/")
        result = pagination.paginate_queryset([], request)
        self.assertIsNone(result)

    def test_dynamic_pagination_factory(self):
        """Test get_pagination_class factory function"""
        CustomPagination = get_pagination_class(page_size=30, max_page_size=200)
        pagination = CustomPagination()
        self.assertEqual(pagination.page_size, 30)
        self.assertEqual(pagination.max_page_size, 200)

    def test_pagination_response_structure(self):
        """Test paginated response has correct structure"""
        pagination = StandardPagination()

        # Create a mock request
        request = self.factory.get("/")
        drf_request = Request(request)

        # Mock queryset with 100 items
        mock_queryset = list(range(100))

        # Paginate
        paginated_data = pagination.paginate_queryset(mock_queryset, drf_request)

        # Get response
        response = pagination.get_paginated_response(paginated_data)

        # Check response structure
        self.assertIn("count", response.data)
        self.assertIn("next", response.data)
        self.assertIn("previous", response.data)
        self.assertIn("total_pages", response.data)
        self.assertIn("current_page", response.data)
        self.assertIn("page_size", response.data)
        self.assertIn("results", response.data)

        # Check values
        self.assertEqual(response.data["count"], 100)
        self.assertEqual(response.data["total_pages"], 5)  # 100 items / 20 per page
        self.assertEqual(response.data["current_page"], 1)
        self.assertEqual(response.data["page_size"], 20)
        self.assertEqual(len(response.data["results"]), 20)


class PaginationIntegrationTestCase(TestCase):
    """Integration tests for pagination with views"""

    def test_pagination_query_params(self):
        """Test pagination with custom query parameters"""
        pagination = StandardPagination()

        # Test custom page size
        request = self.factory.get("/?page_size=50")
        drf_request = Request(request)

        mock_queryset = list(range(100))
        paginated_data = pagination.paginate_queryset(mock_queryset, drf_request)

        self.assertEqual(len(paginated_data), 50)

    def test_pagination_max_page_size_limit(self):
        """Test that max_page_size is enforced"""
        pagination = StandardPagination()

        # Try to request more than max_page_size (100)
        request = self.factory.get("/?page_size=200")
        drf_request = Request(request)

        mock_queryset = list(range(200))
        paginated_data = pagination.paginate_queryset(mock_queryset, drf_request)

        # Should be limited to max_page_size
        self.assertEqual(len(paginated_data), 100)

    def test_pagination_page_navigation(self):
        """Test navigating between pages"""
        pagination = StandardPagination()

        # Get page 2
        request = self.factory.get("/?page=2")
        drf_request = Request(request)

        mock_queryset = list(range(100))
        paginated_data = pagination.paginate_queryset(mock_queryset, drf_request)

        response = pagination.get_paginated_response(paginated_data)

        self.assertEqual(response.data["current_page"], 2)
        self.assertIsNotNone(response.data["previous"])
        self.assertIsNotNone(response.data["next"])


if __name__ == "__main__":
    import django

    django.setup()
    from django.conf import settings
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["easy_pagination.tests.test_pagination"])
