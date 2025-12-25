# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-12-22

### Added
- Initial release of Django Easy Pagination
- `CustomPageNumberPagination` base class with rich metadata
- `StandardPagination` class (20 items per page, max 100)
- `SmallResultsPagination` class (10 items per page, max 50)
- `LargeResultsPagination` class (50 items per page, max 500)
- `NoPagination` class for disabling pagination
- `get_pagination_class()` factory function for dynamic pagination
- Comprehensive test suite
- Full documentation and examples
- Support for Django 3.2+ and Django REST Framework 3.12+
- Support for Python 3.7+

### Features
- Rich pagination metadata including total_pages, current_page, and page_size
- Client-controlled page size via query parameters
- Configurable maximum page sizes
- OpenAPI/Swagger schema support
- Easy integration with Django REST Framework viewsets

[0.1.0]: https://github.com/casperspec-1/easy-pagination/releases/tag/v0.1.0
