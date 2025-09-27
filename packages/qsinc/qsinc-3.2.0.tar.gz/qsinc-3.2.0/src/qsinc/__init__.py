"""
Qsinc - Revolutionary Quaternary Compression with Built-in Security
==================================================================

The world's first practical quaternary compression system featuring:
- Built-in temporal encryption
- Infinity timestamps (permanent encryption)  
- Burn-after-time functionality
- Patent-protected quaternary encoding
- Competitive performance with leading algorithms

Quick Start:
-----------
>>> import qsinc
>>> data = b"Hello, World!" * 1000
>>> compressor = qsinc.Qsinc(level=5)
>>> result = compressor.compress(data)
>>> print(f"Compressed {result['ratio']:.2f}:1")
>>> original = compressor.decompress(result)
>>> assert original == data  # ✅ Perfect integrity

Advanced Features:
-----------------
>>> # Permanent encryption (never expires)
>>> result = qsinc.compress_infinity(data, level=7)

>>> # Self-destructing data (burns after time)  
>>> result = qsinc.compress_and_burn(data, expire_minutes=30)
"""

# Import main classes and functions
from .core import Qsinc
from .utils import (
    compress_file,
    compress_infinity,
    compress_and_burn,
    decompress_qsinc,
    TIMESTAMP_INFINITY
)

# Version info
__version__ = "3.2.0"
__author__ = "Ankit Singh" 
__email__ = "ankitsingh9717@gmail.com" 
__license__ = "MIT"

# Public API
__all__ = [
    "Qsinc",
    "compress_file",
    "compress_infinity", 
    "compress_and_burn",
    "decompress_qsinc",
    "TIMESTAMP_INFINITY",
    "__version__",
]

print(f"🚀 Qsinc v{__version__} loaded - Revolutionary Quaternary Compression")
