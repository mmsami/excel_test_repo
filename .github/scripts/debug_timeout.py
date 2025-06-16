#!/usr/bin/env python3
"""
Debugging version to find what's causing the timeout
Add this to your script to identify the bottleneck
"""

import os
import sys
import time
import glob
from pathlib import Path

def debug_file_discovery():
    """Debug what files are being discovered and their sizes"""
    print("=== FILE DISCOVERY DEBUG ===")
    start_time = time.time()
    
    # Check what Excel files exist
    xlsx_files = glob.glob('**/*.xlsx', recursive=True)
    xlsm_files = glob.glob('**/*.xlsm', recursive=True)
    all_excel = xlsx_files + xlsm_files
    
    discovery_time = time.time() - start_time
    print(f"File discovery took {discovery_time:.2f}s")
    print(f"Found {len(all_excel)} Excel files:")
    
    total_size = 0
    large_files = []
    
    for excel_file in all_excel:
        if os.path.exists(excel_file):
            size_mb = os.path.getsize(excel_file) / (1024 * 1024)
            total_size += size_mb
            print(f"  📄 {excel_file}: {size_mb:.1f}MB")
            
            if size_mb > 10:  # Files larger than 10MB
                large_files.append((excel_file, size_mb))
        else:
            print(f"  ❌ {excel_file}: FILE NOT FOUND")
    
    print(f"\n📊 SUMMARY:")
    print(f"   Total files: {len(all_excel)}")
    print(f"   Total size: {total_size:.1f}MB")
    print(f"   Large files (>10MB): {len(large_files)}")
    
    if large_files:
        print(f"\n🚨 LARGE FILES:")
        for file_path, size in sorted(large_files, key=lambda x: x[1], reverse=True):
            print(f"   {file_path}: {size:.1f}MB")
    
    return all_excel, large_files

def debug_git_operations():
    """Debug git operations that might be slow"""
    print("\n=== GIT OPERATIONS DEBUG ===")
    start_time = time.time()
    
    try:
        import git
        repo = git.Repo('.')
        
        # Test git.diff - this can be VERY slow on large repos
        diff_start = time.time()
        try:
            if len(repo.heads) > 0:
                diffs = repo.git.diff('HEAD~1', '--name-only').split('\n')
            else:
                diffs = repo.git.ls_files().split('\n')
            diff_time = time.time() - diff_start
            print(f"Git diff took {diff_time:.2f}s")
            print(f"Found {len(diffs)} changed files")
            
            # Show changed files
            excel_changes = [f for f in diffs if f.endswith(('.xlsx', '.xlsm'))]
            if excel_changes:
                print(f"Excel files in changes: {excel_changes}")
            else:
                print("No Excel files in git changes")
                
        except Exception as e:
            print(f"Git diff error: {e}")
            
    except Exception as e:
        print(f"Git setup error: {e}")
    
    git_time = time.time() - start_time
    print(f"Total git operations took {git_time:.2f}s")

def debug_single_file_processing(excel_file):
    """Debug processing of a single Excel file"""
    print(f"\n=== PROCESSING DEBUG: {excel_file} ===")
    
    if not os.path.exists(excel_file):
        print(f"❌ File doesn't exist: {excel_file}")
        return
    
    file_size = os.path.getsize(excel_file) / (1024 * 1024)
    print(f"📁 File size: {file_size:.1f}MB")
    
    # Test extraction step by step
    excel_dir = Path(excel_file).with_suffix('')
    temp_dir = Path(f"{excel_dir}_temp")
    
    # Step 1: Directory creation
    step_start = time.time()
    os.makedirs(excel_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    print(f"✅ Directory creation: {time.time() - step_start:.2f}s")
    
    # Step 2: ZIP extraction (THIS IS OFTEN THE BOTTLENECK!)
    step_start = time.time()
    try:
        import zipfile
        with zipfile.ZipFile(excel_file, 'r') as zip_ref:
            # Count entries first
            entry_count = len(zip_ref.namelist())
            print(f"📦 ZIP contains {entry_count} entries")
            
            # Extract (this can be VERY slow for large files)
            zip_ref.extractall(temp_dir)
        
        extraction_time = time.time() - step_start
        print(f"✅ ZIP extraction: {extraction_time:.2f}s")
        
        if extraction_time > 60:  # More than 1 minute
            print(f"🚨 BOTTLENECK FOUND: ZIP extraction is taking {extraction_time:.1f}s!")
            
    except Exception as e:
        print(f"❌ ZIP extraction failed: {e}")
        return
    
    # Step 3: File copying
    step_start = time.time()
    try:
        # Check what was extracted
        extracted_files = list(temp_dir.rglob('*'))
        print(f"📂 Extracted {len(extracted_files)} files/folders")
        
        # Check for large extracted files
        large_extracted = []
        for extracted_file in extracted_files:
            if extracted_file.is_file():
                size_mb = extracted_file.stat().st_size / (1024 * 1024)
                if size_mb > 5:  # Files larger than 5MB
                    large_extracted.append((str(extracted_file), size_mb))
        
        if large_extracted:
            print(f"🚨 Large extracted files:")
            for file_path, size in sorted(large_extracted, key=lambda x: x[1], reverse=True)[:5]:
                rel_path = os.path.relpath(file_path, temp_dir)
                print(f"   {rel_path}: {size:.1f}MB")
        
        copy_time = time.time() - step_start
        print(f"✅ File analysis: {copy_time:.2f}s")
        
    except Exception as e:
        print(f"❌ File copying failed: {e}")
    
    # Cleanup
    try:
        import shutil
        shutil.rmtree(temp_dir)
        shutil.rmtree(excel_dir, ignore_errors=True)
        print(f"✅ Cleanup completed")
    except Exception as e:
        print(f"⚠️ Cleanup warning: {e}")

def main_debug():
    """Main debug function"""
    print("🔍 EXCEL PROCESSING TIMEOUT DEBUGGER")
    print("=" * 50)
    
    overall_start = time.time()
    
    # Step 1: File discovery
    all_excel, large_files = debug_file_discovery()
    
    # Step 2: Git operations
    debug_git_operations()
    
    # Step 3: Test processing one file
    if all_excel:
        test_file = all_excel[0]  # Test the first file
        print(f"\n🧪 TESTING SINGLE FILE PROCESSING...")
        debug_single_file_processing(test_file)
    
    total_time = time.time() - overall_start
    print(f"\n⏱️ TOTAL DEBUG TIME: {total_time:.2f}s")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS:")
    if large_files:
        print(f"1. 🚨 LARGE FILES DETECTED - Consider excluding files > 50MB")
        for file_path, size in large_files[:3]:
            if size > 50:
                print(f"   Exclude: {file_path} ({size:.1f}MB)")
    
    if len(all_excel) > 10:
        print(f"2. 📊 MANY FILES - {len(all_excel)} Excel files found")
        print(f"   Consider processing only changed files")
    
    if total_time > 30:
        print(f"3. ⏱️ SLOW PROCESSING - Even debug took {total_time:.1f}s")
        print(f"   Real processing will definitely timeout")

if __name__ == "__main__":
    main_debug()
