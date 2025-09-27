"""
Qsinc Utility Functions
======================

Convenience functions for common Qsinc operations including file compression,
infinity timestamps, and burn-after-time functionality.

Author: Ankit Singh  
"""

import os
import time
from typing import Dict, Union, Optional, Any
from .core import Qsinc, TIMESTAMP_INFINITY

def compress_file(input_path: str, output_path: str, level: int = 5, 
                 timestamp: Optional[Union[int, float]] = None) -> Dict[str, Any]:
    """
    Compress a file using Qsinc

    Args:
        input_path: Path to input file
        output_path: Path to output .qsinc file
        level: Compression level 1-11
        timestamp: Custom timestamp (None=current, TIMESTAMP_INFINITY=permanent)

    Returns:
        Dict with compression results and file information

    Example:
        >>> result = compress_file('data.txt', 'data.qsinc', level=7)
        >>> print(f"File compressed {result['ratio']:.2f}:1")
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    print(f"📁 Compressing file: {input_path}")

    # Read input file
    with open(input_path, 'rb') as f:
        data = f.read()

    print(f"   File size: {len(data):,} bytes")

    # Compress data
    compressor = Qsinc(level=level)
    result = compressor.compress(data, timestamp=timestamp)

    # Write compressed file
    with open(output_path, 'wb') as f:
        f.write(result['compressed_data'])

    # Add file information to result
    result['input_file'] = input_path
    result['output_file'] = output_path
    result['space_saved'] = result['original_size'] - result['compressed_size']
    result['space_saved_percent'] = (result['space_saved'] / result['original_size']) * 100

    print(f"✅ File compressed successfully:")
    print(f"   {input_path} → {output_path}")
    print(f"   {result['ratio']:.2f}:1 compression ratio")
    print(f"   Saved {result['space_saved']:,} bytes ({result['space_saved_percent']:.1f}%)")

    return result

def decompress_file(input_path: str, output_path: str, 
                   verify_timestamp: Optional[Union[int, float]] = None) -> Dict[str, Any]:
    """
    Decompress a Qsinc file

    Args:
        input_path: Path to .qsinc compressed file
        output_path: Path to output decompressed file
        verify_timestamp: Timestamp for decryption verification

    Returns:
        Dict with decompression results
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Compressed file not found: {input_path}")

    print(f"📂 Decompressing file: {input_path}")

    # Read compressed file
    with open(input_path, 'rb') as f:
        compressed_data = f.read()

    # Create result object for decompression
    result = {
        'compressed_data': compressed_data,
        'timestamp': verify_timestamp or int(time.time())
    }

    # Decompress
    compressor = Qsinc()
    decompressed = compressor.decompress(result, verify_timestamp=verify_timestamp)

    # Write decompressed file
    with open(output_path, 'wb') as f:
        f.write(decompressed)

    print(f"✅ File decompressed successfully:")
    print(f"   {input_path} → {output_path}")
    print(f"   Recovered {len(decompressed):,} bytes")

    return {
        'input_file': input_path,
        'output_file': output_path,
        'decompressed_size': len(decompressed)
    }

def compress_infinity(data: bytes, level: int = 5) -> Dict[str, Any]:
    """
    Compress data with infinity timestamp (never expires)

    This creates permanently encrypted data that can be decrypted at any time
    by anyone who knows it uses infinity mode.

    Args:
        data: Data to compress
        level: Compression level 1-11

    Returns:
        Dict with compression results (infinity_mode=True)

    Example:
        >>> archive = compress_infinity(b"Important document", level=9)
        >>> # Can decrypt anytime with:
        >>> original = decompress_qsinc(archive, verify_timestamp=TIMESTAMP_INFINITY)
    """
    print(f"♾️  Compressing with INFINITY timestamp (never expires)")

    compressor = Qsinc(level=level)
    result = compressor.compress(data, timestamp=TIMESTAMP_INFINITY)

    print(f"✅ Infinity compression complete:")
    print(f"   Ratio: {result['ratio']:.2f}:1")
    print(f"   Mode: Permanent encryption (never expires)")
    print(f"   Security: Requires knowledge of infinity mode to decrypt")

    return result

def compress_and_burn(data: bytes, expire_minutes: int, level: int = 5) -> Dict[str, Any]:
    """
    Compress data with burn-after-time (self-destructing)

    Data becomes permanently unrecoverable after the specified time.

    Args:
        data: Data to compress
        expire_minutes: Minutes until data becomes unrecoverable
        level: Compression level 1-11

    Returns:
        Dict with compression results and burn information

    Example:
        >>> secret = compress_and_burn(b"Mission briefing", expire_minutes=30)
        >>> print(f"🔥 {secret['warning']}")
        >>> # After 30 minutes: data is permanently unrecoverable!
    """
    if expire_minutes <= 0:
        raise ValueError("expire_minutes must be positive")

    expire_timestamp = int(time.time()) + (expire_minutes * 60)

    print(f"🔥 Compressing with BURN-AFTER-TIME ({expire_minutes} minutes)")

    compressor = Qsinc(level=level)
    result = compressor.compress(data, timestamp=expire_timestamp)

    # Add burn-specific information
    result['burn_after_minutes'] = expire_minutes
    result['burns_at'] = expire_timestamp
    result['current_time'] = int(time.time())
    result['time_remaining_minutes'] = expire_minutes
    result['warning'] = f"⚠️  Data will become PERMANENTLY UNRECOVERABLE after {expire_minutes} minutes!"

    print(f"✅ Self-destructing compression complete:")
    print(f"   Ratio: {result['ratio']:.2f}:1")
    print(f"   🔥 Burns at: {time.ctime(expire_timestamp)}")
    print(f"   ⚠️  Warning: {result['warning']}")

    return result

def decompress_qsinc(result: Dict[str, Any], 
                    verify_timestamp: Optional[Union[int, float]] = None) -> bytes:
    """
    Universal decompression function for Qsinc data

    Works with any Qsinc compressed data regardless of compression mode.

    Args:
        result: Result dictionary from any compress function
        verify_timestamp: Timestamp for verification (None = use original)

    Returns:
        Original decompressed data

    Example:
        >>> # Works with any compression mode:
        >>> original = decompress_qsinc(standard_result)
        >>> original = decompress_qsinc(infinity_result, verify_timestamp=TIMESTAMP_INFINITY)
        >>> original = decompress_qsinc(burn_result)  # Only if not expired
    """
    compressor = Qsinc()
    return compressor.decompress(result, verify_timestamp=verify_timestamp)

def check_burn_status(result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check the burn status of self-destructing data

    Args:
        result: Result from compress_and_burn()

    Returns:
        Dict with burn status information
    """
    if 'burns_at' not in result:
        return {'is_burn_mode': False, 'message': 'Not a burn-after-time compression'}

    current_time = int(time.time())
    burns_at = result['burns_at']
    time_remaining = burns_at - current_time

    if time_remaining > 0:
        minutes_remaining = time_remaining // 60
        seconds_remaining = time_remaining % 60

        return {
            'is_burn_mode': True,
            'is_burned': False,
            'time_remaining_seconds': time_remaining,
            'time_remaining_minutes': minutes_remaining,
            'message': f"⏱️  Data expires in {minutes_remaining}m {seconds_remaining}s",
            'warning': "Data will become permanently unrecoverable when timer expires!"
        }
    else:
        return {
            'is_burn_mode': True,
            'is_burned': True,
            'time_remaining_seconds': 0,
            'message': "🔥 Data has BURNED - permanently unrecoverable!",
            'warning': "This data can never be recovered."
        }

def get_compression_info(compressed_data: bytes) -> Dict[str, Any]:
    """
    Get information about compressed data without decompressing

    Args:
        compressed_data: Raw compressed data bytes

    Returns:
        Dict with file format information
    """
    if not compressed_data:
        return {'valid': False, 'error': 'No data provided'}

    if not compressed_data.startswith(b'QSINC32'):
        return {'valid': False, 'error': 'Not a Qsinc file (invalid magic header)'}

    return {
        'valid': True,
        'format': 'Qsinc',
        'version': '3.2',
        'magic_header': compressed_data[:7].decode(),
        'total_size': len(compressed_data),
        'header_size': 7,
        'payload_size': len(compressed_data) - 7,
        'created_by': 'Qsinc v3.2 - Revolutionary Quaternary Compression'
    }

# Convenience aliases for common operations
compress = compress_file
decompress = decompress_file
