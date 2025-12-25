# Installation Guide

This guide will help you install and use Django Easy Pagination in your project.

## Installation Methods

### Method 1: Install from PyPI (Recommended - when published)

```bash
pip install easy_pagination
```

### Method 2: Install from Source (Current)

```bash
# Clone the repository
git clone https://github.com/digitaltoouchcode/easy-pagination.git
cd easy-pagination

# Install in development mode (editable)
pip install -e .

# Or install normally
pip install .
```

### Method 3: Install from GitHub

```bash
pip install git+https://github.com/digitaltouch/easy-pagination.git
```

### Method 4: Install with Development Dependencies

```bash
# For development work
pip install -e ".[dev]"

# Or using requirements files
pip install -r requirements-dev.txt
```

## Verification

After installation, verify it works:

```python
# In Python shell or script
from drf_easy_pagination import StandardPagination
print(StandardPagination.page_size)  # Should print: 20
```

## Quick Setup in Django Project

1. **Install the package** (using any method above)

2. **Add to your Django REST Framework settings** (optional - for global configuration):

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'easy_pagination.StandardPagination',
    'PAGE_SIZE': 20
}
```

3. **Use in your views**:

```python
# views.py
from rest_framework import viewsets
from easy_pagination import StandardPagination

class MyViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    pagination_class = StandardPagination
```

## Building Distribution Packages

If you want to build the package yourself:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# This creates:
# - dist/django-easy-pagination-0.1.0.tar.gz (source distribution)
# - dist/django_easy_pagination-0.1.0-py3-none-any.whl (wheel)
```

## Publishing to PyPI (For Maintainers)

```bash
# Test on TestPyPI first
twine upload --repository testpypi dist/*

# Then upload to PyPI
twine upload dist/*
```

## Troubleshooting

### Import Error

If you get `ModuleNotFoundError: No module named 'easy_pagination'`:

1. Make sure the package is installed: `pip list | grep easy-pagination`
2. Check your Python environment is correct
3. Try reinstalling: `pip uninstall django-easy-pagination && pip install django-easy-pagination`

### Django/DRF Not Found

Make sure Django and Django REST Framework are installed:

```bash
pip install Django>=4.0 djangorestframework>=3.12
```

### Version Conflicts

If you have version conflicts:

```bash
# Check installed versions
pip show Django djangorestframework

# Upgrade if needed
pip install --upgrade Django djangorestframework
```

## Uninstallation

```bash
pip uninstall easy_pagination
```

## Next Steps

- Read the [README.md](README.md) for usage examples
- Check out the [tests](tests/test_pagination.py) for more examples
- See [CHANGELOG.md](CHANGELOG.md) for version history
