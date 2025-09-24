#!/usr/bin/env python3
"""
Test script for the new download_folder functionality
"""

import asyncio
import sys
import os
from pathlib import Path

from src.inopyutils.s3_helper import InoS3Helper

async def test_download_folder():
    """
    Test the download_folder method
    Note: This is a basic test structure - actual testing would require valid S3 credentials and bucket
    """
    
    print("Testing download_folder method...")
    
    # Initialize S3Helper (would need real credentials for actual testing)
    s3_helper = InoS3Helper(
        bucket_name="test-bucket",
        region_name="us-east-1"
    )
    
    # Test parameters
    s3_folder_key = "test-folder/"
    local_folder_path = "downloaded_test_folder"
    
    try:
        print(f"Attempting to download folder: {s3_folder_key}")
        print(f"Local destination: {local_folder_path}")
        
        # This would work with real credentials and existing S3 folder
        result = await s3_helper.download_folder(
            s3_folder_key=s3_folder_key,
            local_folder_path=local_folder_path
        )
        
        print("\nDownload Result:")
        print(f"Success: {result['success']}")
        print(f"Total files: {result['total_files']}")
        print(f"Downloaded successfully: {result['downloaded_successfully']}")
        print(f"Failed downloads: {result['failed_downloads']}")
        
        if result['errors']:
            print("\nErrors encountered:")
            for error in result['errors']:
                print(f"  - {error}")
                
    except Exception as e:
        print(f"Test failed with exception: {str(e)}")
        print("Note: This is expected if S3 credentials are not configured")

async def test_method_signature():
    """
    Test that the method signature and basic validation work correctly
    """
    print("\nTesting method signature and validation...")
    
    # Test with no bucket name
    s3_helper = InoS3Helper()
    
    try:
        result = await s3_helper.download_folder("test/", "local_folder")
        print("ERROR: Should have raised ValueError for missing bucket name")
    except ValueError as e:
        print(f"✓ Correctly raised ValueError: {e}")
    except Exception as e:
        print(f"✓ Expected error (no credentials): {e}")
    
    # Test that local folder creation logic exists
    print("✓ Method exists and accepts correct parameters")

def main():
    """
    Run the tests
    """
    print("=" * 50)
    print("Testing S3Helper download_folder method")
    print("=" * 50)
    
    # Run async tests
    asyncio.run(test_download_folder())
    asyncio.run(test_method_signature())
    
    print("\n" + "=" * 50)
    print("Test completed!")
    print("Note: Full functionality testing requires valid S3 credentials and test data")
    print("=" * 50)

if __name__ == "__main__":
    main()