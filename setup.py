from setuptools import setup, find_packages
import os

# Read the README file
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

setup(
    name="easy_pagination",
    version="0.1.0",
    description="Custom pagination classes for Django REST Framework",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="Casper",
    author_email="cassymyo@gmail.com",
    url="https://github.com/casperspec-1/easy-pagination",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        'Django>=3.2',
        'djangorestframework>=3.12',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-django>=4.5',
            'black>=22.0',
            'flake8>=4.0',
            'isort>=5.10',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords=[
        'django',
        'rest-framework',
        'pagination',
        'api',
        'drf',
        'django-rest-framework',
    ],
    license='MIT',
    project_urls={
        'Bug Reports': 'https://github.com/casperspec-1/easy-pagination/issues',
        'Source': 'https://github.com/casperspec-1/easy-pagination',
        'Documentation': 'https://github.com/casperspec-1/easy-pagination#readme',
    },
    include_package_data=True,
    zip_safe=False,
)
