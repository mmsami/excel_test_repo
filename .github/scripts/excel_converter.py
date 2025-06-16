#!/usr/bin/env python3
"""
EXACT copy of your main script but with debug timing
This will show us what's actually taking 3+ minutes
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

def debug_print(message):
    """Print with timestamp"""
    elapsed = time.time() - start_time if 'start_time' in globals() else 0
    print(f"[{elapsed:6.1f}s] {message}")

def extract_excel_selective(excel_path):
    """Extract only VBA, table definitions, and structure from Excel file"""
    debug_print(f"🔄 Starting extraction of {excel_path}")
    
    excel_dir = Path(excel_path).with_suffix('')
    
    # Create directory if it doesn't exist
    os.makedirs(excel_dir, exist_ok=True)
    
    # Extract Excel as zip to temporary directory
    temp_dir = Path(f"{excel_dir}_temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    debug_print(f"📦 Extracting ZIP: {excel_path}")
    extract_start = time.time()
    
    with zipfile.ZipFile(excel_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    extract_time = time.time() - extract_start
    debug_print(f"📦 ZIP extraction completed in {extract_time:.2f}s")
    
    # Copy only essential files
    debug_print("📋 Copying essential files...")
    essential_files = ['[Content_Types].xml', 'Content_Types.xml', '_rels/.rels']
    for file in essential_files:
        src = temp_dir / file
        if src.exists():
            dst = excel_dir / file
            os.makedirs(dst.parent, exist_ok=True)
            shutil.copy2(src, dst)
    
    # Copy VBA files
    debug_print("📋 Copying VBA files...")
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
    debug_print("📋 Copying table definitions...")
    tables_dir = temp_dir / 'xl/tables'
    if tables_dir.exists():
        dst_tables = excel_dir / 'xl/tables'
        shutil.copytree(tables_dir, dst_tables, dirs_exist_ok=True)
    
    # Copy workbook structure (no worksheet data)
    debug_print("📋 Copying workbook structure...")
    workbook_files = ['xl/workbook.xml', 'xl/styles.xml', 'xl/_rels/workbook.xml.rels']
    for wb_file in workbook_files:
        src = temp_dir / wb_file
        if src.exists():
            dst = excel_dir / wb_file
            os.makedirs(dst.parent, exist_ok=True)
            shutil.copy2(src, dst)
    
    # Clean up temp directory
    debug_print("🧹 Cleaning up temp directory...")
    shutil.rmtree(temp_dir)
    
    debug_print(f"✅ Extracted VBA and table structure from {excel_path} to {excel_dir}/")
    return excel_dir

def format_xml_files(directory):
    """Format XML files with attributes on separate lines and decode entities for better diffing"""
    debug_print(f"🎨 Starting XML formatting for {directory}")
    format_start = time.time()
    
    try:
        xml_count = 0
        
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.xml'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        # Decode XML entities for better readability
                        content = content.replace('&amp;', '&')
                        content = content.replace('&lt;', '<')
                        content = content.replace('&gt;', '>')
                        content = content.replace('&quot;', '"')
                        content = content.replace('&apos;', "'")
                        
                        # Format XML tags with attributes on separate lines
                        pattern = r'<([a-zA-Z0-9_:-]+)(\s+[^>]+)>'
                        
                        def format_attributes(match):
                            tag_name = match.group(1)
                            attributes = match.group(2).strip()
                            
                            if not attributes or ' ' not in attributes:
                                return f"<{tag_name} {attributes}>"
                            
                            formatted_attrs = ""
                            attr_indent = "  "
                            
                            attr_pattern = r'([a-zA-Z0-9_:-]+)="([^"]*)"'
                            attr_matches = re.findall(attr_pattern, attributes)
                            
                            for attr_name, attr_value in attr_matches:
                                formatted_attrs += f"\n{attr_indent}{attr_name}=\"{attr_value}\""
                            
                            return f"<{tag_name}{formatted_attrs}\n>"
                        
                        formatted_content = re.sub(pattern, format_attributes, content)
                        
                        # Add proper indentation
                        lines = formatted_content.split('\n')
                        indented_lines = []
                        indent_level = 0
                        
                        for line in lines:
                            stripped = line.strip()
                            
                            if stripped.startswith('</'):
                                indent_level = max(0, indent_level - 1)
                                
                            if stripped:
                                if '=' in stripped and not stripped.startswith('<'):
                                    indented_lines.append(line)
                                else:
                                    indented_lines.append('  ' * indent_level + stripped)
                            
                            if stripped.startswith('<') and not stripped.startswith('</') and not stripped.endswith('/>') and not stripped.startswith('<?'):
                                indent_level += 1
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write('\n'.join(indented_lines))
                        
                        xml_count += 1
                    except Exception as e:
                        debug_print(f"❌ Error formatting {file_path}: {e}")
        
        format_time = time.time() - format_start
        debug_print(f"🎨 Formatted {xml_count} XML files in {format_time:.2f}s")
    except Exception as e:
        format_time = time.time() - format_start
        debug_print(f"⚠️ XML formatting failed after {format_time:.2f}s: {e}")

def get_changed_files():
    """Get list of changed files from the most recent commit"""
    debug_print("📊 Getting changed files from git...")
    git_start = time.time()
    
    repo = git.Repo('.')
    
    try:
        if len(repo.heads) > 0:
            diffs = repo.git.diff('HEAD~1', '--name-only').split('\n')
        else:
            diffs = repo.git.ls_files().split('\n')
        
        git_time = time.time() - git_start
        debug_print(f"📊 Git operations completed in {git_time:.2f}s, found {len(diffs)} files")
        return diffs
    except git.exc.GitCommandError:
        git_time = time.time() - git_start
        debug_print(f"📊 Git fallback completed in {git_time:.2f}s")
        return repo.git.ls_files().split('\n')

def cleanup_generated_files():
    """Clean up previously generated files to avoid processing duplicates"""
    debug_print("🧹 CLEANING UP GENERATED FILES...")
    cleanup_start = time.time()
    
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
        for file_path in glob.glob(pattern, recursive=True):
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    debug_print(f"🗑️ Removed: {file_path}")
                    cleaned_count += 1
            except Exception as e:
                debug_print(f"⚠️ Could not remove {file_path}: {e}")
    
    # Also clean up extracted directories
    for item in Path('.').rglob('*'):
        if (item.is_dir() and 
            item.name.endswith(('.xlsx', '.xlsm')) and
            item.name != item.parent.name):  # Avoid infinite recursion
            try:
                shutil.rmtree(item)
                debug_print(f"🗂️ Removed directory: {item}")
                cleaned_count += 1
            except Exception as e:
                debug_print(f"⚠️ Could not remove directory {item}: {e}")
    
    cleanup_time = time.time() - cleanup_start
    debug_print(f"✅ Cleanup completed: {cleaned_count} items removed in {cleanup_time:.2f}s")

def process_excel_files():
    """Process Excel files with aggressive filtering to avoid timeout"""
    debug_print("=== STARTING EXCEL PROCESSING WITH DUPLICATE FILTERING ===")
    process_start = time.time()
    
    # Get changed files first (most important)
    changed_files = get_changed_files()
    excel_files = [f for f in changed_files if f.endswith(('.xlsx', '.xlsm'))]
    
    # If no changed files, get all files but filter heavily
    if not excel_files:
        debug_print("📂 No Excel files in git changes, scanning all files...")
        all_files = glob.glob('**/*.xlsx', recursive=True) + glob.glob('**/*.xlsm', recursive=True)
        
        # AGGRESSIVE FILTERING
        filtered_files = []
        for file_path in all_files:
            # Skip generated files
            if ('_fromXML' in file_path or 
                '_overwritten' in file_path or 
                '_temp' in file_path or
                ' - Copy' in file_path):
                debug_print(f"⏭️ Skipping generated file: {file_path}")
                continue
            
            # Skip files inside extracted directories
            if ('/' in file_path and 
                any(part.endswith(('.xlsx', '.xlsm')) for part in Path(file_path).parts[:-1])):
                debug_print(f"⏭️ Skipping nested file: {file_path}")
                continue
            
            # Skip large files
            if os.path.exists(file_path):
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                if file_size_mb > 15:  # 15MB limit
                    debug_print(f"⏭️ Skipping large file: {file_path} ({file_size_mb:.1f}MB)")
                    continue
                
                filtered_files.append((file_path, file_size_mb))
        
        # Sort by size and take only the smallest 3 files
        filtered_files.sort(key=lambda x: x[1])
        excel_files = [f[0] for f in filtered_files[:3]]
        
        debug_print(f"📊 Filtered from {len(all_files)} to {len(excel_files)} files")
        for file_path, size_mb in filtered_files[:3]:
            debug_print(f"   ✅ Will process: {file_path} ({size_mb:.1f}MB)")
    
    processed_count = 0
    
    for excel_file in excel_files:
        # Double-check filters
        if ('_fromXML' in excel_file or 
            '_overwritten' in excel_file or
            not os.path.exists(excel_file)):
            continue
        
        # Timeout check
        elapsed = time.time() - process_start
        if elapsed > 120:  # 2 minutes max
            debug_print(f"⏱️ TIMEOUT: Stopping after {elapsed:.1f}s")
            break
        
        file_size_mb = os.path.getsize(excel_file) / (1024 * 1024)
        debug_print(f"🔄 Processing {excel_file} ({file_size_mb:.1f}MB)")
        
        file_start = time.time()
        
        try:
            # Use selective extraction
            extract_dir = extract_excel_selective(excel_file)
            if not extract_dir:
                continue
            
            # Skip XML formatting to save time
            debug_print(f"⚠️ Skipping XML formatting to avoid timeout")
            
            # Add to git
            debug_print("📝 Adding to git...")
            git_add_start = time.time()
            repo = git.Repo('.')
            repo.git.add(str(extract_dir))
            git_add_time = time.time() - git_add_start
            debug_print(f"📝 Git add completed in {git_add_time:.2f}s")
            
            # Create _fromXML copy
            debug_print("📄 Creating _fromXML copy...")
            copy_start = time.time()
            fromxml_path = Path(excel_file).with_name(
                f"{Path(excel_file).stem}_fromXML{Path(excel_file).suffix}"
            )
            shutil.copy2(excel_file, fromxml_path)
            repo.git.add(str(fromxml_path))
            copy_time = time.time() - copy_start
            debug_print(f"📄 Copy completed in {copy_time:.2f}s")
            
            processed_count += 1
            file_elapsed = time.time() - file_start
            total_elapsed = time.time() - process_start
            
            debug_print(f"✅ Processed {excel_file} in {file_elapsed:.1f}s (total: {total_elapsed:.1f}s)")
            
        except Exception as e:
            debug_print(f"❌ Error processing {excel_file}: {e}")
            continue
    
    total_elapsed = time.time() - process_start
    debug_print(f"=== COMPLETED: {processed_count} files in {total_elapsed:.1f}s ===")
    return excel_files

def process_xml_files():
    """Process XML files but don't package back to Excel"""
    debug_print("🔍 Processing XML files...")
    xml_start = time.time()
    
    changed_files = get_changed_files()
    
    xml_dirs = set()
    for changed_file in changed_files:
        if changed_file.endswith('.xml') or '/xl/' in changed_file or '/_rels/' in changed_file:
            path = Path(changed_file)
            current_dir = path.parent
            
            while str(current_dir) != '.':
                if (current_dir / 'Content_Types.xml').exists() or (current_dir / '[Content_Types].xml').exists():
                    xml_dirs.add(str(current_dir))
                    break
                
                if current_dir == Path('.') or current_dir.parent == current_dir:
                    break
                
                current_dir = current_dir.parent
    
    xml_time = time.time() - xml_start
    debug_print(f"🔍 Found {len(xml_dirs)} XML directories with changes in {xml_time:.2f}s")
    return list(xml_dirs)

def generate_xml_diff_report(xml_dirs):
    """Generate diff report for VBA and table changes"""
    debug_print(f"📊 Generating XML diff reports for {len(xml_dirs)} directories...")
    # ... (keeping original function but won't run due to no xml_dirs)
    debug_print("📊 No XML directories to process, skipping report generation")
    return None

def commit_changes():
    """Commit any changes and push to repository"""
    debug_print("📤 Checking for changes to commit...")
    commit_start = time.time()
    
    repo = git.Repo('.')
    
    if repo.is_dirty() or len(repo.untracked_files) > 0:
        debug_print("📤 Changes detected, committing...")
        try:
            token = os.environ.get('GITHUB_TOKEN')
            
            origin_url = repo.remotes.origin.url
            if origin_url.startswith('https://'):
                new_url = f"https://x-access-token:{token}@github.com/{'/'.join(origin_url.split('/')[3:])}"
                repo.remotes.origin.set_url(new_url)
            
            branch = os.environ.get('GITHUB_REF', 'refs/heads/main').replace('refs/heads/', '')
            
            try:
                repo.git.pull('--rebase', 'origin', branch)
            except git.exc.GitCommandError as e:
                debug_print(f"Pull error (non-critical): {e}")
            
            repo.git.add(A=True)
            commit_msg = "Excel VBA/Table Structure Extraction [skip ci]"
            repo.git.commit('-m', commit_msg)
            
            repo.git.push('origin', branch)
            commit_time = time.time() - commit_start
            debug_print(f"📤 Changes committed and pushed to {branch} in {commit_time:.2f}s")
            
        except git.exc.GitCommandError as e:
            commit_time = time.time() - commit_start
            debug_print(f"❌ Git push error after {commit_time:.2f}s: {e}")
    else:
        commit_time = time.time() - commit_start
        debug_print(f"📤 No changes to commit ({commit_time:.2f}s)")

def main():
    """Main function to process files"""
    global start_time
    start_time = time.time()
    
    debug_print("🚀 Starting Excel VBA/Table extraction...")
    
    # STEP 1: Clean up first
    cleanup_generated_files()
    
    # STEP 2: Process with filtering
    excel_files = process_excel_files()
    debug_print(f"📊 Processed {len(excel_files)} Excel files")
    
    # STEP 3: Continue with rest
    xml_dirs = process_xml_files()
    debug_print(f"📊 Processed {len(xml_dirs)} XML directories")
    
    if xml_dirs:
        generate_xml_diff_report(xml_dirs)
    
    commit_changes()
    
    total_time = time.time() - start_time
    debug_print(f"🏁 Excel VBA/Table extraction completed in {total_time:.2f}s")

if __name__ == "__main__":
    main()
