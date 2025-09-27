#!/usr/bin/env python3
"""
Qsinc Setup Configuration for PyPI Distribution
===============================================

This setup script configures Qsinc for distribution on PyPI (Python Package Index).
It includes all necessary metadata, dependencies, and configuration options.

Author: Ankit Singh 
"""

from setuptools import setup, find_packages
import os
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements from requirements.txt
def read_requirements():
    requirements = []
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return requirements

setup(
    # Basic package information
    name="qsinc",
    version="3.2.0",
    description="Revolutionary Quaternary Compression with Built-in Security",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Author information
    author="Ankit Singh",
    author_email="ankitsingh9717@gmail.com", 
    maintainer="Ankit Singh",
    maintainer_email="ankitsingh9717@gmail.com",

    # URLs
    url="https://github.com/YOUR_ankitsinc/qsinc",
    project_urls={
        "Homepage": "https://github.com/YOUR_ankitsinc/qsinc",
        "Documentation": "https://github.com/YOUR_ankitsinc/qsinc#readme",
        "Source Code": "https://github.com/YOUR_ankitsinc/qsinc",
        "Bug Reports": "https://github.com/YOUR_ankitsinc/qsinc/issues",
        "Feature Requests": "https://github.com/YOUR_ankitsinc/qsinc/issues",
        "Discussions": "https://github.com/YOUR_ankitsinc/qsinc/discussions",
    },

    # Package structure
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,

    # Dependencies
    install_requires=read_requirements(),
    python_requires=">=3.8",

    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0", 
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
            "twine>=3.4.0",
            "build>=0.3.0"
        ],
        "fast": [
            "numpy>=1.20.0",
            "cython>=0.29.0"
        ],
        "benchmark": [
            "lz4>=3.1.0",
            "zstandard>=0.15.0", 
            "brotli>=1.0.9"
        ],
        "all": [
            "numpy>=1.20.0",
            "cython>=0.29.0",
            "lz4>=3.1.0", 
            "zstandard>=0.15.0",
            "brotli>=1.0.9",
            "pytest>=6.0.0",
            "black>=21.0.0"
        ]
    },

    # Console scripts
    entry_points={
        "console_scripts": [
            "qsinc-compress=qsinc.cli:compress_main",
            "qsinc-decompress=qsinc.cli:decompress_main",
            "qsinc-info=qsinc.cli:info_main",
        ],
    },

    # Package classification for PyPI
    classifiers=[
        # Development status
        "Development Status :: 4 - Beta",

        # Intended audience
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology", 
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",

        # License
        "License :: OSI Approved :: MIT License",

        # Operating systems
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",

        # Programming languages
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",

        # Topics
        "Topic :: System :: Archiving :: Compression",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],

    # Keywords for PyPI search
    keywords=[
        "compression", "quaternary", "security", "encryption", 
        "temporal", "infinity", "burn-after-time", "fast", "efficient",
        "lossless", "data", "archive", "backup", "space-saving"
    ],

    # License
    license="MIT",

    # Platform support
    platforms=["any"],

    # Package metadata
    package_data={
        "qsinc": ["py.typed"],  # Type hints support
    },
)
