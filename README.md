# Django Easy Pagination

A Django REST Framework library providing customizable pagination classes with rich metadata and flexible configuration options.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-3.2+-green.svg)](https://www.djangoproject.com/)
[![DRF Version](https://img.shields.io/badge/drf-3.12+-orange.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Features

**Rich Metadata**: Get comprehensive pagination information including total pages, current page, and page size  
**Multiple Pagination Classes**: Pre-configured classes for different use cases  
**Highly Customizable**: Easy to customize page sizes and behavior  
**Client Control**: Allow clients to specify page size via query parameters  
**Production Ready**: Includes comprehensive test suite  
**Well Documented**: Clear documentation and examples

## Installation

Install using pip:

```bash
pip install easy_pagination
```

Or install from source:

```bash
git clone https://github.com/digitaltouchcode/easy-pagination.git
cd easy-pagination
pip install -e .
```

## Quick Start

### 1. Add to your Django REST Framework view:

```python
from rest_framework import viewsets
from easy_pagination import StandardPagination

class MyViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    pagination_class = StandardPagination
```

### 2. Get paginated responses with rich metadata:

```json
{
    "count": 100,
    "next": "http://api.example.com/items/?page=3",
    "previous": "http://api.example.com/items/?page=1",
    "total_pages": 10,
    "current_page": 2,
    "page_size": 10,
    "results": [...]
}
```

## Available Pagination Classes

### StandardPagination
Default pagination for most list views.
- **Default page size**: 20 items
- **Max page size**: 100 items
- **Best for**: General purpose API endpoints

```python
from easy_pagination import StandardPagination

class MyViewSet(viewsets.ModelViewSet):
    pagination_class = StandardPagination
```

### SmallResultsPagination
Optimized for small, quick-loading lists.
- **Default page size**: 10 items
- **Max page size**: 50 items
- **Best for**: Dropdown lists, autocomplete, quick searches

```python
from easy_pagination import SmallResultsPagination

class QuickListViewSet(viewsets.ModelViewSet):
    pagination_class = SmallResultsPagination
```

### LargeResultsPagination
Designed for large datasets and reports.
- **Default page size**: 50 items
- **Max page size**: 500 items
- **Best for**: Reports, data exports, admin interfaces

```python
from easy_pagination import LargeResultsPagination

class ReportViewSet(viewsets.ModelViewSet):
    pagination_class = LargeResultsPagination
```

### NoPagination
Disable pagination for specific views.
- **Returns**: All results without pagination
- **Best for**: Small datasets, configuration endpoints
- **Warning**: Use carefully with large datasets!

```python
from easy_pagination import NoPagination

class ConfigViewSet(viewsets.ModelViewSet):
    pagination_class = NoPagination
```

## Advanced Usage

### Custom Pagination Class

Create your own pagination class by extending `CustomPageNumberPagination`:

```python
from easy_pagination import CustomPageNumberPagination

class MyCustomPagination(CustomPageNumberPagination):
    page_size = 25
    max_page_size = 200
    page_size_query_param = 'page_size'
```

### Dynamic Pagination

Use the factory function to create pagination classes on the fly:

```python
from easy_pagination import get_pagination_class

class MyViewSet(viewsets.ModelViewSet):
    pagination_class = get_pagination_class(page_size=30, max_page_size=200)
```

### Client-Controlled Page Size

Clients can control page size using query parameters:

```bash
# Get 50 items per page
GET /api/items/?page_size=50

# Navigate to page 3
GET /api/items/?page=3

# Combine both
GET /api/items/?page=3&page_size=50
```

### Global Configuration

Set a default pagination class for all views in your Django settings:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'easy_pagination.StandardPagination',
    'PAGE_SIZE': 20
}
```

## Response Schema

All pagination classes return responses with the following structure:

| Field | Type | Description |
|-------|------|-------------|
| `count` | integer | Total number of items across all pages |
| `next` | string/null | URL to the next page (null if on last page) |
| `previous` | string/null | URL to the previous page (null if on first page) |
| `total_pages` | integer | Total number of pages |
| `current_page` | integer | Current page number (1-indexed) |
| `page_size` | integer | Number of items per page |
| `results` | array | Array of serialized objects for current page |

## Requirements

- Python >= 3.7
- Django >= 3.2
- djangorestframework >= 3.12

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/digitaltouchcode/easy-pagination.git
cd easy-pagination

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=easy_pagination

# Run specific test file
pytest tests/test_pagination.py
```

### Code Quality

```bash
# Format code with black
black easy_pagination/

# Sort imports
isort easy_pagination/

# Lint with flake8
flake8 easy_pagination/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Casper**
- Email: cassymyo@gmail.com
- GitHub: [@casperspec-1](https://github.com/digitaltouchcoode)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/casperspec-1/easy-pagination/issues) on GitHub.

## Acknowledgments

Built with ❤️ using Django REST Framework.
