#!/usr/bin/env python3
"""
MINIMAL VERSION - Test if this works
If this works, then the problem is in the functions we're not including
"""

print("🚀 SCRIPT STARTED - Testing minimal version")

# SAFE IMPORTS
import os
import sys
import shutil
import zipfile
import glob
import git
import re
import time
from pathlib import Path

print("✅ All imports successful")

# MINIMAL MAIN FUNCTION
def main():
    print("📋 Starting main function...")
    
    # Just do the absolute minimum
    try:
        repo = git.Repo('.')
        print("✅ Git repo accessed")
        
        excel_files = glob.glob('**/*.xlsx', recursive=True)
        print(f"✅ Found {len(excel_files)} Excel files")
        
        print("✅ Basic operations successful")
        
    except Exception as e:
        print(f"❌ Error in main: {e}")

print("🔧 About to call main function...")

# CRITICAL: Only run main if this script is executed directly
if __name__ == "__main__":
    print("✅ Running in main block")
    main()
    print("🏁 Script completed successfully")
else:
    print("⚠️ Script was imported, not executed directly")
