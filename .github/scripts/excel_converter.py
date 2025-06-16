#!/usr/bin/env python3
"""
MINIMAL TEST SCRIPT - Find what's crashing
"""

print("🚀 SCRIPT STARTED")

try:
    print("📦 Testing imports...")
    import os
    print("✅ os imported")
    
    import sys
    print("✅ sys imported")
    
    import shutil
    print("✅ shutil imported")
    
    import zipfile
    print("✅ zipfile imported")
    
    import glob
    print("✅ glob imported")
    
    import git
    print("✅ git imported")
    
    import re
    print("✅ re imported")
    
    import time
    print("✅ time imported")
    
    from pathlib import Path
    print("✅ pathlib imported")
    
    print("🎉 ALL IMPORTS SUCCESSFUL")
    
except Exception as e:
    print(f"💥 IMPORT ERROR: {e}")
    import traceback
    traceback.print_exc()

try:
    print("🔍 Testing basic operations...")
    
    # Test current directory
    current_dir = os.getcwd()
    print(f"📂 Current directory: {current_dir}")
    
    # Test git repo
    print("📊 Testing git repo...")
    repo = git.Repo('.')
    print(f"📊 Git repo found: {repo}")
    
    # Test file listing
    print("📋 Testing file listing...")
    all_files = os.listdir('.')
    print(f"📋 Found {len(all_files)} files in current directory")
    
    # Test glob
    print("🔍 Testing glob...")
    excel_files = glob.glob('**/*.xlsx', recursive=True)
    print(f"🔍 Found {len(excel_files)} Excel files")
    
    print("🎉 ALL BASIC OPERATIONS SUCCESSFUL")
    
except Exception as e:
    print(f"💥 OPERATION ERROR: {e}")
    import traceback
    traceback.print_exc()

print("✅ SCRIPT COMPLETED SUCCESSFULLY")
