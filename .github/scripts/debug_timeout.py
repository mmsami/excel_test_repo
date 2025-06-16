#!/usr/bin/env python3
"""
Comprehensive Debug Script - Find the Exact Bottleneck
This will run the EXACT same logic as your main script but with detailed timing
"""

import os
import sys
import shutil
import zipfile
import glob
import git
import re
import time
from pathlib import Path

def debug_step(step_name, func, *args, **kwargs):
    """Debug wrapper that times each step"""
    print(f"\n🔍 STARTING: {step_name}")
    start_time = time.time()
    
    try:
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"✅ COMPLETED: {step_name} in {elapsed:.2f}s")
        return result
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"❌ FAILED: {step_name} after {elapsed:.2f}s - Error: {e}")
        raise

def get_changed_files():
    """Get list of changed files from the most recent commit"""
    repo = git.Repo('.')
    
    try:
        if len(repo.heads) > 0:
            diffs = repo.git.diff('HEAD~1', '--name-only').split('\n')
        else:
            diffs = repo.git.ls_files().split('\n')
        return diffs
    except git.exc.GitCommandError:
        return repo.git.ls_files().split('\n')

def cleanup_generated_files():
    """Clean up previously generated files to avoid processing duplicates"""
    print("🧹 CLEANING UP GENERATED FILES...")
    
    cleanup_patterns = [
        '**/*_fromXML.xlsx',
        '**/*_fromXML.xlsm', 
        '**/*_overwritten.xlsx',
        '**/*_overwritten.xlsm',
        '**/*_temp*',
        '**/* - Copy*.xlsx',
        '**/* - Copy*.xlsm'
    ]
    
    cleaned_count = 0
    for pattern in cleanup_patterns:
        pattern_start = time.time()
        matches = glob.glob(pattern, recursive=True)
        pattern_time = time.time() - pattern_start
        
        print(f"   Pattern '{pattern}' found {len(matches)} files in {pattern_time:.2f}s")
        
        for file_path in matches:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"🗑️ Removed: {file_path}")
                    cleaned_count += 1
            except Exception as e:
                print(f"⚠️ Could not remove {file_path}: {e}")
    
    # Also clean up extracted directories
    print("   Scanning for extracted directories...")
    dir_scan_start = time.time()
    
    for item in Path('.').rglob('*'):
        if (item.is_dir() and 
            item.name.endswith(('.xlsx', '.xlsm')) and
            item.name != item.parent.name):  # Avoid infinite recursion
            try:
                shutil.rmtree(item)
                print(f"🗂️ Removed directory: {item}")
                cleaned_count += 1
            except Exception as e:
                print(f"⚠️ Could not remove directory {item}: {e}")
    
    dir_scan_time = time.time() - dir_scan_start
    print(f"   Directory scan completed in {dir_scan_time:.2f}s")
    print(f"✅ Cleanup completed: {cleaned_count} items removed")

def debug_file_discovery():
    """Debug file discovery with detailed timing"""
    print("=== DETAILED FILE DISCOVERY ===")
    
    # Test glob performance
    print("📂 Testing glob patterns...")
    
    glob_start = time.time()
    xlsx_files = glob.glob('**/*.xlsx', recursive=True)
    xlsx_time = time.time() - glob_start
    print(f"   Found {len(xlsx_files)} .xlsx files in {xlsx_time:.2f}s")
    
    glob_start = time.time()
    xlsm_files = glob.glob('**/*.xlsm', recursive=True)
    xlsm_time = time.time() - glob_start
    print(f"   Found {len(xlsm_files)} .xlsm files in {xlsm_time:.2f}s")
    
    all_files = xlsx_files + xlsm_files
    print(f"📊 Total Excel files: {len(all_files)}")
    
    # Test file filtering
    print("\n🔍 Testing file filtering...")
    filter_start = time.time()
    
    filtered_files = []
    for file_path in all_files:
        # Skip generated files
        if ('_fromXML' in file_path or 
            '_overwritten' in file_path or 
            '_temp' in file_path or
            ' - Copy' in file_path):
            print(f"⏭️ Skipping generated file: {file_path}")
            continue
        
        # Skip files inside extracted directories
        if ('/' in file_path and 
            any(part.endswith(('.xlsx', '.xlsm')) for part in Path(file_path).parts[:-1])):
            print(f"⏭️ Skipping nested file: {file_path}")
            continue
        
        # Check file size
        if os.path.exists(file_path):
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if file_size_mb > 15:  # 15MB limit
                print(f"⏭️ Skipping large file: {file_path} ({file_size_mb:.1f}MB)")
                continue
            
            filtered_files.append((file_path, file_size_mb))
        else:
            print(f"❌ File not found: {file_path}")
    
    filter_time = time.time() - filter_start
    print(f"🔍 Filtering completed in {filter_time:.2f}s")
    print(f"📊 Filtered from {len(all_files)} to {len(filtered_files)} files")
    
    # Sort by size
    filtered_files.sort(key=lambda x: x[1])
    selected_files = filtered_files[:3]
    
    print(f"\n📋 Files selected for processing:")
    for file_path, size_mb in selected_files:
        print(f"   ✅ {file_path} ({size_mb:.1f}MB)")
    
    return [f[0] for f in selected_files]

def test_single_file_extraction(excel_file):
    """Test extraction of a single file with detailed timing"""
    print(f"\n🧪 TESTING EXTRACTION: {excel_file}")
    
    if not os.path.exists(excel_file):
        print(f"❌ File not found: {excel_file}")
        return None
    
    file_size_mb = os.path.getsize(excel_file) / (1024 * 1024)
    print(f"📁 File size: {file_size_mb:.1f}MB")
    
    # Setup directories
    excel_dir = Path(excel_file).with_suffix('')
    temp_dir = Path(f"{excel_dir}_temp")
    
    step_start = time.time()
    os.makedirs(excel_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    setup_time = time.time() - step_start
    print(f"📂 Directory setup: {setup_time:.2f}s")
    
    # ZIP extraction (THE LIKELY BOTTLENECK)
    step_start = time.time()
    try:
        with zipfile.ZipFile(excel_file, 'r') as zip_ref:
            entry_count = len(zip_ref.namelist())
            print(f"📦 ZIP contains {entry_count} entries")
            
            # Extract with progress
            zip_ref.extractall(temp_dir)
            
        extraction_time = time.time() - step_start
        print(f"📦 ZIP extraction: {extraction_time:.2f}s")
        
        if extraction_time > 30:
            print(f"🚨 BOTTLENECK DETECTED: ZIP extraction took {extraction_time:.1f}s!")
            
    except Exception as e:
        extraction_time = time.time() - step_start
        print(f"❌ ZIP extraction failed after {extraction_time:.2f}s: {e}")
        return None
    
    # File copying
    step_start = time.time()
    
    # Copy essential files
    essential_files = ['[Content_Types].xml', 'Content_Types.xml', '_rels/.rels']
    for file in essential_files:
        src = temp_dir / file
        if src.exists():
            dst = excel_dir / file
            os.makedirs(dst.parent, exist_ok=True)
            shutil.copy2(src, dst)
    
    # Copy VBA files
    for vba_path in ['xl/vbaProject.bin', 'xl/_rels/vbaProject.bin.rels', 'xl/vba/']:
        src = temp_dir / vba_path
        if src.exists():
            dst = excel_dir / vba_path
            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                os.makedirs(dst.parent, exist_ok=True)
                shutil.copy2(src, dst)
    
    # Copy table definitions
    tables_dir = temp_dir / 'xl/tables'
    if tables_dir.exists():
        dst_tables = excel_dir / 'xl/tables'
        shutil.copytree(tables_dir, dst_tables, dirs_exist_ok=True)
    
    # Copy workbook structure
    workbook_files = ['xl/workbook.xml', 'xl/styles.xml', 'xl/_rels/workbook.xml.rels']
    for wb_file in workbook_files:
        src = temp_dir / wb_file
        if src.exists():
            dst = excel_dir / wb_file
            os.makedirs(dst.parent, exist_ok=True)
            shutil.copy2(src, dst)
    
    copy_time = time.time() - step_start
    print(f"📋 File copying: {copy_time:.2f}s")
    
    # Cleanup
    step_start = time.time()
    shutil.rmtree(temp_dir)
    cleanup_time = time.time() - step_start
    print(f"🧹 Cleanup: {cleanup_time:.2f}s")
    
    return excel_dir

def debug_git_operations():
    """Debug git operations with timing"""
    print("\n=== GIT OPERATIONS DEBUG ===")
    
    step_start = time.time()
    changed_files = get_changed_files()
    git_time = time.time() - step_start
    
    print(f"📊 Git operations took {git_time:.2f}s")
    print(f"📊 Found {len(changed_files)} changed files")
    
    excel_changes = [f for f in changed_files if f.endswith(('.xlsx', '.xlsm'))]
    if excel_changes:
        print(f"📊 Excel files in changes: {excel_changes}")
    else:
        print("📊 No Excel files in git changes")
    
    return changed_files

def main_debug():
    """Main debug function that follows the exact same logic as your script"""
    print("🔍 COMPREHENSIVE EXCEL PROCESSING DEBUG")
    print("=" * 60)
    
    overall_start = time.time()
    max_time = 180  # 3 minutes like GitHub Actions
    
    try:
        # STEP 1: Cleanup (like your script)
        cleanup_result = debug_step("Cleanup Generated Files", cleanup_generated_files)
        
        # Check timeout
        elapsed = time.time() - overall_start
        if elapsed > max_time:
            print(f"⏱️ TIMEOUT during cleanup after {elapsed:.1f}s")
            return
        
        # STEP 2: Git operations
        changed_files = debug_step("Git Operations", debug_git_operations)
        
        # Check timeout
        elapsed = time.time() - overall_start
        if elapsed > max_time:
            print(f"⏱️ TIMEOUT during git operations after {elapsed:.1f}s")
            return
        
        # STEP 3: File discovery (like your script)
        excel_files = debug_step("File Discovery and Filtering", debug_file_discovery)
        
        # Check timeout
        elapsed = time.time() - overall_start
        if elapsed > max_time:
            print(f"⏱️ TIMEOUT during file discovery after {elapsed:.1f}s")
            return
        
        # STEP 4: Process first file (the likely bottleneck)
        if excel_files:
            test_file = excel_files[0]
            extraction_result = debug_step(f"Extract {test_file}", test_single_file_extraction, test_file)
            
            # Check timeout
            elapsed = time.time() - overall_start
            if elapsed > max_time:
                print(f"⏱️ TIMEOUT during extraction after {elapsed:.1f}s")
                return
        
        total_time = time.time() - overall_start
        print(f"\n⏱️ TOTAL DEBUG TIME: {total_time:.2f}s")
        
        # Analysis
        print(f"\n💡 ANALYSIS:")
        if total_time > 60:
            print(f"🚨 SLOW PROCESSING: Debug took {total_time:.1f}s")
            print("   Real processing will definitely timeout")
        
        if len(excel_files) > 5:
            print(f"📊 TOO MANY FILES: {len(excel_files)} files to process")
        
        print(f"\n🎯 NEXT STEPS:")
        print("1. Look for steps that took >30s")
        print("2. Focus on the slowest operation")
        print("3. Consider processing only 1 file at a time")
        
    except Exception as e:
        elapsed = time.time() - overall_start
        print(f"💥 CRITICAL ERROR after {elapsed:.1f}s: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main_debug()
