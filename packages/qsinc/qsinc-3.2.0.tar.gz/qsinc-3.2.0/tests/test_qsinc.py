"""
Qsinc Unit Tests
================

Basic unit tests for Qsinc compression library to ensure functionality
works correctly across different use cases.

Author: YOUR_NAME_HERE  # 🔴 REPLACE WITH YOUR NAME
"""

import pytest
import sys
import os
import time

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import qsinc

class TestBasicCompression:
    """Test basic compression and decompression functionality"""

    def test_simple_compression(self):
        """Test basic compress/decompress cycle"""
        data = b"Hello, World!" * 100
        compressor = qsinc.Qsinc(level=5)

        # Compress
        result = compressor.compress(data)

        # Verify result structure
        assert isinstance(result, dict)
        assert result['original_size'] == len(data)
        assert result['compressed_size'] > 0
        assert result['ratio'] > 0
        assert 'timestamp' in result
        assert 'compressed_data' in result

        # Decompress
        decompressed = compressor.decompress(result)

        # Verify integrity
        assert decompressed == data
        assert len(decompressed) == len(data)

    def test_empty_data(self):
        """Test compression of empty data"""
        data = b""
        compressor = qsinc.Qsinc(level=5)

        result = compressor.compress(data)
        assert result['original_size'] == 0
        assert result['ratio'] == 1.0

        decompressed = compressor.decompress(result)
        assert decompressed == data

    def test_compression_levels(self):
        """Test different compression levels"""
        data = b"Test data for compression level testing. " * 200

        for level in [1, 5, 11]:
            compressor = qsinc.Qsinc(level=level)
            result = compressor.compress(data)

            # Verify compression worked
            assert result['compression_level'] == level
            assert result['original_size'] == len(data)

            # Verify decompression works
            decompressed = compressor.decompress(result)
            assert decompressed == data

class TestSpecialModes:
    """Test special compression modes (infinity, burn-after-time)"""

    def test_infinity_compression(self):
        """Test infinity timestamp compression"""
        data = b"Permanent archive data"

        # Compress with infinity timestamp
        result = qsinc.compress_infinity(data)

        # Verify infinity mode
        assert result['infinity_mode'] == True
        assert result['timestamp'] == qsinc.TIMESTAMP_INFINITY

        # Test decryption with infinity timestamp
        decrypted = qsinc.decompress_qsinc(result, verify_timestamp=qsinc.TIMESTAMP_INFINITY)
        assert decrypted == data

        # Test decryption without explicit timestamp (should work)
        decrypted2 = qsinc.decompress_qsinc(result)
        assert decrypted2 == data

    def test_burn_after_time(self):
        """Test burn-after-time functionality"""
        data = b"Secret message for testing"

        # Compress with 5-minute burn time
        result = qsinc.compress_and_burn(data, expire_minutes=5)

        # Verify burn mode
        assert result['burn_after_minutes'] == 5
        assert 'burns_at' in result
        assert 'warning' in result

        # Should work immediately (within burn window)
        decrypted = qsinc.decompress_qsinc(result)
        assert decrypted == data

        # Check burn status
        status = qsinc.check_burn_status(result)
        assert status['is_burn_mode'] == True
        assert status['is_burned'] == False  # Should not be burned yet

    def test_timestamp_validation(self):
        """Test timestamp validation"""
        data = b"Test data"
        compressor = qsinc.Qsinc(level=5)

        # Compress with specific timestamp
        custom_timestamp = int(time.time())
        result = compressor.compress(data, timestamp=custom_timestamp)

        # Should work with correct timestamp
        decrypted = compressor.decompress(result, verify_timestamp=custom_timestamp)
        assert decrypted == data

        # Should work without verification (uses original)
        decrypted2 = compressor.decompress(result)
        assert decrypted2 == data

class TestUtilityFunctions:
    """Test utility functions"""

    def test_file_compression(self):
        """Test file compression utilities"""
        # Create test file
        test_content = b"This is test file content for compression testing." * 100
        test_file = 'test_input.txt'
        compressed_file = 'test_output.qsinc'
        recovered_file = 'test_recovered.txt'

        try:
            # Write test file
            with open(test_file, 'wb') as f:
                f.write(test_content)

            # Compress file
            result = qsinc.compress_file(test_file, compressed_file, level=5)

            # Verify compression result
            assert result['input_file'] == test_file
            assert result['output_file'] == compressed_file
            assert result['original_size'] == len(test_content)
            assert os.path.exists(compressed_file)

            # Decompress file
            qsinc.decompress_file(compressed_file, recovered_file)

            # Verify recovered file
            with open(recovered_file, 'rb') as f:
                recovered_content = f.read()

            assert recovered_content == test_content

        finally:
            # Clean up test files
            for filename in [test_file, compressed_file, recovered_file]:
                if os.path.exists(filename):
                    os.remove(filename)

    def test_compression_info(self):
        """Test compression info utility"""
        data = b"Test data"
        compressor = qsinc.Qsinc(level=5)
        result = compressor.compress(data)

        # Get info about compressed data
        info = qsinc.get_compression_info(result['compressed_data'])

        assert info['valid'] == True
        assert info['format'] == 'Qsinc'
        assert info['version'] == '3.2'
        assert info['magic_header'] == 'QSINC32'

class TestErrorHandling:
    """Test error handling and edge cases"""

    def test_invalid_compression_level(self):
        """Test invalid compression level handling"""
        with pytest.raises(ValueError):
            qsinc.Qsinc(level=0)  # Too low

        with pytest.raises(ValueError):
            qsinc.Qsinc(level=15)  # Too high

    def test_invalid_file_paths(self):
        """Test file operation error handling"""
        with pytest.raises(FileNotFoundError):
            qsinc.compress_file('nonexistent.txt', 'output.qsinc')

        with pytest.raises(FileNotFoundError):
            qsinc.decompress_file('nonexistent.qsinc', 'output.txt')

    def test_invalid_qsinc_format(self):
        """Test invalid format detection"""
        # Test with non-Qsinc data
        fake_result = {
            'compressed_data': b'not_qsinc_data',
            'timestamp': int(time.time())
        }

        compressor = qsinc.Qsinc()
        with pytest.raises(ValueError, match="Invalid Qsinc"):
            compressor.decompress(fake_result)

    def test_burn_time_validation(self):
        """Test burn-after-time validation"""
        data = b"test"

        with pytest.raises(ValueError):
            qsinc.compress_and_burn(data, expire_minutes=0)  # Invalid time

        with pytest.raises(ValueError):
            qsinc.compress_and_burn(data, expire_minutes=-5)  # Negative time

def test_import_functionality():
    """Test that all main functions can be imported"""
    # Test main class
    assert hasattr(qsinc, 'Qsinc')

    # Test utility functions
    assert hasattr(qsinc, 'compress_file')
    assert hasattr(qsinc, 'compress_infinity')
    assert hasattr(qsinc, 'compress_and_burn')
    assert hasattr(qsinc, 'decompress_qsinc')

    # Test constants
    assert hasattr(qsinc, 'TIMESTAMP_INFINITY')

    # Test version info
    assert hasattr(qsinc, '__version__')
    assert qsinc.__version__ == '3.2.0'

def test_large_data_handling():
    """Test handling of larger data sets"""
    # Create larger test data (1MB)
    large_data = b"Large data testing pattern. " * 40000  # ~1MB

    compressor = qsinc.Qsinc(level=5)

    # Should handle large data without issues
    result = compressor.compress(large_data)
    assert result['original_size'] == len(large_data)
    assert result['compressed_size'] > 0

    # Decompression should work correctly
    decompressed = compressor.decompress(result)
    assert decompressed == large_data
    assert len(decompressed) == len(large_data)

if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, '-v'])
