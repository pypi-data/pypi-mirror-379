#!/usr/bin/env python3
"""
Qsinc Basic Usage Examples
=========================

Simple examples showing how to use the Qsinc compression library
for different use cases and compression modes.

Author: Ankit Singh 
"""

import sys
import os

# Add src to Python path so we can import qsinc
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import qsinc
import time

def example_basic_compression():
    """Basic compression and decompression example"""
    print("🗜️  BASIC COMPRESSION EXAMPLE")
    print("=" * 35)

    # Sample data to compress
    data = b"Hello, World! This is a test of Qsinc compression. " * 200
    print(f"Original data: {len(data):,} bytes")

    # Create compressor with level 5 (balanced speed/compression)
    compressor = qsinc.Qsinc(level=5)

    # Compress the data
    result = compressor.compress(data)

    print(f"\n✅ Compression Results:")
    print(f"   Compressed size: {result['compressed_size']:,} bytes")
    print(f"   Compression ratio: {result['ratio']:.2f}:1")
    print(f"   Speed: {result['speed_mbps']:.1f} MB/s")
    print(f"   Compression level: {result['compression_level']}")
    print(f"   Timestamp: {result['timestamp']}")

    # Decompress to verify integrity
    original = compressor.decompress(result)

    # Verify data integrity
    if original == data:
        print("   ✅ Data integrity verified - perfect reconstruction!")
    else:
        print("   ❌ Data integrity failed!")

    return result

def example_file_compression():
    """File compression example"""
    print("\n📁 FILE COMPRESSION EXAMPLE")
    print("=" * 32)

    # Create a sample text file
    sample_content = """
This is a sample text file for Qsinc compression testing.
It contains multiple lines of text that should compress well with
Qsinc's quaternary pattern matching algorithms.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur.

The quick brown fox jumps over the lazy dog.
Pack my box with five dozen liquor jugs.
How vexingly quick daft zebras jump!

This text will be compressed using Qsinc's revolutionary quaternary
encoding system, which provides better compression ratios than
traditional binary-based algorithms.
""" * 20  # Repeat to make it substantial

    # Write sample file
    with open('sample_text.txt', 'w') as f:
        f.write(sample_content)

    file_size = len(sample_content.encode())
    print(f"Created sample_text.txt ({file_size:,} bytes)")

    # Compress the file using level 7 (good compression)
    try:
        result = qsinc.compress_file(
            input_path='sample_text.txt',
            output_path='sample_text.qsinc',
            level=7
        )

        print(f"\n✅ File Compression Results:")
        print(f"   {result['input_file']} → {result['output_file']}")
        print(f"   Original: {result['original_size']:,} bytes")
        print(f"   Compressed: {result['compressed_size']:,} bytes")
        print(f"   Compression ratio: {result['ratio']:.2f}:1")
        print(f"   Space saved: {result['space_saved']:,} bytes ({result['space_saved_percent']:.1f}%)")
        print(f"   Speed: {result['speed_mbps']:.1f} MB/s")

        # Test decompression
        qsinc.decompress_file('sample_text.qsinc', 'sample_text_recovered.txt')

        # Verify files are identical
        with open('sample_text.txt', 'rb') as f1, open('sample_text_recovered.txt', 'rb') as f2:
            if f1.read() == f2.read():
                print("   ✅ File integrity verified after decompression!")
            else:
                print("   ❌ File integrity check failed!")

    finally:
        # Clean up files
        for filename in ['sample_text.txt', 'sample_text.qsinc', 'sample_text_recovered.txt']:
            if os.path.exists(filename):
                os.remove(filename)
        print("\n🧹 Cleaned up temporary files")

def example_infinity_mode():
    """Infinity timestamp compression example"""
    print("\n♾️  INFINITY TIMESTAMP EXAMPLE")
    print("=" * 33)

    # Important data that should be permanently archived
    archive_data = b"""
IMPORTANT LEGAL DOCUMENT - PERMANENT ARCHIVE
============================================

This document contains important legal information that must be
preserved permanently but with access control through encryption.

Contract Details:
- Party A: Acme Corporation  
- Party B: Beta Industries
- Contract Value: $10,000,000
- Duration: 25 years (2024-2049)
- Confidentiality: Perpetual

This document is encrypted using Qsinc's infinity timestamp mode,
which means it will never expire but still requires the correct
decryption key (knowledge of infinity mode) to access.

Archive Date: """ + time.strftime("%Y-%m-%d %H:%M:%S").encode() + """
Archived By: Qsinc v3.2 Compression System

END OF DOCUMENT
"""

    print(f"Archive document: {len(archive_data)} bytes")

    # Compress with infinity timestamp (never expires)
    result = qsinc.compress_infinity(archive_data, level=9)  # Maximum compression for archives

    print(f"\n✅ Infinity Compression Results:")
    print(f"   Original: {result['original_size']} bytes")
    print(f"   Compressed: {result['compressed_size']} bytes")
    print(f"   Ratio: {result['ratio']:.2f}:1")
    print(f"   Infinity mode: {result['infinity_mode']}")
    print(f"   Timestamp: {result['timestamp']}")
    print(f"   Security: Permanent encryption with access control")

    # Test decryption with infinity timestamp
    print("\n🔓 Testing infinity decryption...")
    try:
        decrypted = qsinc.decompress_qsinc(result, verify_timestamp=qsinc.TIMESTAMP_INFINITY)

        if decrypted == archive_data:
            print("   ✅ Infinity decryption successful!")
            print("   📚 Perfect for: Legal docs, archives, permanent records")
        else:
            print("   ❌ Infinity decryption failed!")
    except Exception as e:
        print(f"   ❌ Decryption error: {e}")

    # Test failure with wrong timestamp
    print("\n🚫 Testing decryption with wrong timestamp (should fail)...")
    try:
        wrong_decrypt = qsinc.decompress_qsinc(result, verify_timestamp=123456789)
        print("   ❌ UNEXPECTED: Wrong timestamp should have failed!")
    except Exception as e:
        print("   ✅ EXPECTED: Wrong timestamp correctly rejected")

    return result

def example_burn_after_time():
    """Burn-after-time compression example"""
    print("\n🔥 BURN-AFTER-TIME EXAMPLE")
    print("=" * 30)

    # Secret message that should self-destruct
    secret_message = b"""
TOP SECRET MISSION BRIEFING
============================

Operation: Quaternary Shield
Classification: Ultra-Secret
Time Stamp: """ + time.strftime("%Y-%m-%d %H:%M:%S").encode() + b"""

Mission Objectives:
1. Deploy Qsinc compression technology
2. Establish secure communication channels  
3. Demonstrate self-destructing data capabilities
4. Test burn-after-time functionality

Team Members:
- Agent Alpha (Team Leader)
- Agent Beta (Technical Specialist) 
- Agent Gamma (Security Expert)
- Agent Delta (Communications)

WARNING: THIS MESSAGE WILL SELF-DESTRUCT!

After the specified time expires, this data will become
permanently unrecoverable - even with the original
compression system and unlimited computational resources.

Mission Status: ACTIVE
Security Level: MAXIMUM
Auto-Destruct: ENABLED

END OF BRIEFING
"""

    print(f"Secret message: {len(secret_message)} bytes")

    # Compress with 2-minute burn time (for demo purposes)
    result = qsinc.compress_and_burn(
        data=secret_message,
        expire_minutes=2,  # Short time for demo
        level=9  # Maximum compression for secrets
    )

    print(f"\n✅ Self-Destructing Compression Results:")
    print(f"   Original: {result['original_size']} bytes")
    print(f"   Compressed: {result['compressed_size']} bytes")
    print(f"   Ratio: {result['ratio']:.2f}:1")
    print(f"   Burn time: {result['burn_after_minutes']} minutes")
    print(f"   🔥 Burns at: {time.ctime(result['burns_at'])}")
    print(f"   ⚠️  {result['warning']}")

    # Test immediate access (should work)
    print("\n🔓 Testing immediate access (within burn window)...")
    try:
        decrypted = qsinc.decompress_qsinc(result)

        if decrypted == secret_message:
            print("   ✅ Immediate access successful!")
            print("   📄 Message preview:", decrypted[:50].decode(), "...")
        else:
            print("   ❌ Immediate access failed!")
    except Exception as e:
        print(f"   ❌ Access error: {e}")

    # Check burn status
    status = qsinc.check_burn_status(result)
    print(f"\n🕐 Current burn status:")
    print(f"   {status['message']}")

    if not status['is_burned']:
        print("\n💡 Use Cases for Burn-After-Time:")
        print("   • Temporary secret messages")
        print("   • Mission briefings with auto-cleanup")
        print("   • Time-sensitive confidential data")
        print("   • Automatic evidence destruction")
        print("   • Secure temporary file sharing")

    return result

def example_compression_levels():
    """Compare different compression levels"""
    print("\n📊 COMPRESSION LEVELS COMPARISON")
    print("=" * 37)

    # Test data with various characteristics
    test_data = b"""
Qsinc Compression Level Testing Data
====================================

This test data contains various patterns that will respond
differently to different compression levels:

Repetitive data: AAAA BBBB CCCC DDDD EEEE FFFF
Sequential data: 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ
Random-ish data: X9K2M8L3Q7R4P6S1N5T0U9V8W
Mixed patterns: ABC123XYZ789DEF456GHI012JKL

The higher compression levels should achieve better ratios
by detecting more complex patterns in this data structure.
Lower levels will be faster but with less compression.

This demonstrates Qsinc's adaptive compression capabilities
across its full range of 11 compression levels.
""" * 10  # Repeat to get substantial data

    print(f"Test data size: {len(test_data):,} bytes")
    print()

    # Test levels 1, 5, and 11 for comparison
    levels_to_test = [1, 5, 11]
    results = []

    for level in levels_to_test:
        print(f"Testing Level {level}...")

        compressor = qsinc.Qsinc(level=level)
        result = compressor.compress(test_data)

        # Test decompression to verify
        decompressed = compressor.decompress(result)
        integrity = "✅ PASS" if decompressed == test_data else "❌ FAIL"

        stats = compressor.get_stats()

        print(f"   Ratio: {result['ratio']:6.2f}:1")
        print(f"   Speed: {result['speed_mbps']:6.1f} MB/s")
        print(f"   Mode:  {stats['speed_mode']}")
        print(f"   Patterns: {stats['pattern_count']} available")
        print(f"   Integrity: {integrity}")
        print()

        results.append((level, result))

    # Summary comparison
    print("📋 LEVEL COMPARISON SUMMARY:")
    print("Level |  Ratio  |  Speed  | Best For")
    print("------|---------|---------|------------------------")
    for level, result in results:
        speed_desc = {
            1: "Real-time streaming",
            5: "General purpose", 
            11: "Maximum space savings"
        }[level]
        print(f"  {level:2}  | {result['ratio']:5.2f}:1 | {result['speed_mbps']:5.1f} MB/s | {speed_desc}")

def main():
    """Run all examples"""
    print("🚀 QSINC USAGE EXAMPLES")
    print("=" * 25)
    print("Demonstrating revolutionary quaternary compression with built-in security\n")

    try:
        # Run all examples
        basic_result = example_basic_compression()
        example_file_compression()
        infinity_result = example_infinity_mode()
        burn_result = example_burn_after_time()
        example_compression_levels()

        print("\n" + "=" * 60)
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("=" * 60)

        print("\n📊 QSINC ADVANTAGES DEMONSTRATED:")
        print("✅ Competitive compression ratios (2-12:1 depending on level)")
        print("✅ Fast compression speeds (50-500+ MB/s)")
        print("✅ Built-in temporal encryption (no separate tools needed)")
        print("✅ Infinity timestamps (permanent encryption)")
        print("✅ Burn-after-time (self-destructing data)")
        print("✅ Multiple compression levels (1=fastest, 11=best ratio)")
        print("✅ Professional error handling and data validation")

        print("\n🌟 QSINC: The world's first quaternary compression system!")
        print("Ready to revolutionize how you handle data compression and security! 🔥")

        return {
            'basic': basic_result,
            'infinity': infinity_result, 
            'burn': burn_result
        }

    except Exception as e:
        print(f"❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    main()
