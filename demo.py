#!/usr/bin/env python3
"""
Demo script to showcase Django Easy Pagination functionality.
Run this script to see the library in action.
"""

import os
import sys
import django
from django.conf import settings

# Configure Django settings
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='demo-key-for-testing',
        INSTALLED_APPS=[
            'rest_framework',
        ],
        USE_TZ=True,
    )
    django.setup()

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from easy_pagination import (
    StandardPagination,
    SmallResultsPagination,
    LargeResultsPagination,
    NoPagination,
    get_pagination_class,
)

def demo_pagination_classes():
    """Demonstrate different pagination classes"""
    print(" Django Easy Pagination Demo")
    print("=" * 50)

    # Create test data
    test_data = list(range(1, 101))  # 100 items
    factory = APIRequestFactory()

    # Test StandardPagination
    print("\ StandardPagination (20 items/page, max 100)")
    pagination = StandardPagination()
    request = factory.get('/')
    drf_request = Request(request)
    paginated_data = pagination.paginate_queryset(test_data, drf_request)
    response = pagination.get_paginated_response(paginated_data)

    print(f"  Total items: {response.data['count']}")
    print(f"  Total pages: {response.data['total_pages']}")
    print(f"  Current page: {response.data['current_page']}")
    print(f"  Page size: {response.data['page_size']}")
    print(f"  Items on this page: {len(response.data['results'])}")

    # Test SmallResultsPagination
    print("\n SmallResultsPagination (10 items/page, max 50)")
    pagination = SmallResultsPagination()
    paginated_data = pagination.paginate_queryset(test_data, drf_request)
    response = pagination.get_paginated_response(paginated_data)

    print(f"  Page size: {response.data['page_size']}")
    print(f"  Items on this page: {len(response.data['results'])}")

    # Test LargeResultsPagination
    print("\n LargeResultsPagination (50 items/page, max 500)")
    pagination = LargeResultsPagination()
    paginated_data = pagination.paginate_queryset(test_data, drf_request)
    response = pagination.get_paginated_response(paginated_data)

    print(f"  Page size: {response.data['page_size']}")
    print(f"  Items on this page: {len(response.data['results'])}")

    # Test NoPagination
    print("\n NoPagination (all items)")
    pagination = NoPagination()
    paginated_data = pagination.paginate_queryset(test_data, drf_request)
    print(f"  Paginated data: {paginated_data}")  # Should be None

    # Test custom pagination
    print("\n📄 Custom Pagination (factory function)")
    CustomPagination = get_pagination_class(page_size=15, max_page_size=75)
    pagination = CustomPagination()
    paginated_data = pagination.paginate_queryset(test_data, drf_request)
    response = pagination.get_paginated_response(paginated_data)

    print(f"  Page size: {response.data['page_size']}")
    print(f"  Items on this page: {len(response.data['results'])}")

    # Test client-controlled page size
    print("\n Client-controlled page size")
    request = factory.get('/?page_size=30')
    drf_request = Request(request)
    pagination = StandardPagination()
    paginated_data = pagination.paginate_queryset(test_data, drf_request)
    response = pagination.get_paginated_response(paginated_data)

    print(f"  Requested page size: 30")
    print(f"  Actual page size: {response.data['page_size']}")
    print(f"  Items on this page: {len(response.data['results'])}")
    print("\n Demo completed successfully!")
    print("\n our Django Easy Pagination library is ready to use!")
    print("   Install it in any Django project with: pip install django-easy-pagination")

if __name__ == "__main__":
    demo_pagination_classes()
