#!/usr/bin/env python3
"""
Excel XML Conversion for GitHub Actions
Extracts VBA code and table structure, commits to Git for proper diffing
"""

import os
import sys
import shutil
import zipfile
import glob
import git
import re
import time  # ADD THIS MISSING IMPORT
from pathlib import Path

def extract_excel_selective(excel_path):
    """Extract only VBA, table definitions, and structure from Excel file"""
    excel_dir = Path(excel_path).with_suffix('')
    
    # Create directory if it doesn't exist
    os.makedirs(excel_dir, exist_ok=True)
    
    # Extract Excel as zip to temporary directory
    temp_dir = Path(f"{excel_dir}_temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    with zipfile.ZipFile(excel_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    # Copy only essential files
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
    
    # Copy workbook structure (no worksheet data)
    workbook_files = ['xl/workbook.xml', 'xl/styles.xml', 'xl/_rels/workbook.xml.rels']
    for wb_file in workbook_files:
        src = temp_dir / wb_file
        if src.exists():
            dst = excel_dir / wb_file
            os.makedirs(dst.parent, exist_ok=True)
            shutil.copy2(src, dst)
    
    # Clean up temp directory
    shutil.rmtree(temp_dir)
    
    print(f"Extracted VBA and table structure from {excel_path} to {excel_dir}/")
    return excel_dir

def format_xml_files(directory):
    """Format XML files - FAST VERSION that preserves formula newlines"""
    try:
        xml_count = 0
        
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.xml'):
                    file_path = os.path.join(root, file)
                    
                    # Skip large XML files to avoid timeout
                    if os.path.getsize(file_path) > 1024 * 1024:  # 1MB limit
                        print(f"⏭️ Skipping large XML file: {file_path}")
                        continue
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        # Entity decoding (manager's requirement for better diffs)
                        content = content.replace('&amp;', '&')
                        content = content.replace('&lt;', '<')
                        content = content.replace('&gt;', '>')
                        content = content.replace('&quot;', '"')
                        content = content.replace('&apos;', "'")
                        
                        # Basic indentation without complex regex (FAST)
                        lines = content.split('\n')
                        formatted_lines = []
                        indent_level = 0
                        
                        for line in lines:
                            stripped = line.strip()
                            if not stripped:
                                continue
                                
                            # Closing tags
                            if stripped.startswith('</'):
                                indent_level = max(0, indent_level - 1)
                                formatted_lines.append('    ' * indent_level + stripped)
                            # Self-closing tags
                            elif stripped.endswith('/>'):
                                formatted_lines.append('    ' * indent_level + stripped)
                            # Opening tags
                            elif stripped.startswith('<') and not stripped.startswith('<?'):
                                formatted_lines.append('    ' * indent_level + stripped)
                                if not stripped.endswith('/>'):
                                    indent_level += 1
                            # XML declaration
                            elif stripped.startswith('<?'):
                                formatted_lines.append(stripped)
                            # Content (preserves formula newlines - CRITICAL!)
                            else:
                                formatted_lines.append(stripped)
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write('\n'.join(formatted_lines))
                        
                        xml_count += 1
                    except Exception as e:
                        print(f"⚠️ Error formatting {file_path}: {e}")
        
        print(f"✅ Formatted {xml_count} XML files for better Git diffing")
    except Exception as e:
        print(f"⚠️ XML formatting failed - {e}")

def package_xml_to_excel(xml_dir):
    """Package XML directory back to Excel file"""
    excel_path = Path(f"{xml_dir}.xlsx")
    
    if excel_path.exists():
        overwritten_path = excel_path.with_name(f"{excel_path.stem}_overwritten{excel_path.suffix}")
        shutil.copy2(excel_path, overwritten_path)
        print(f"Created backup at {overwritten_path}")
    
    temp_zip = excel_path.with_suffix('.zip')
    
    with zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(xml_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(xml_dir))
                zipf.write(file_path, arcname)
    
    if temp_zip.exists():
        if excel_path.exists():
            excel_path.unlink()
        temp_zip.rename(excel_path)
        print(f"Created Excel file at {excel_path}")
    
    return excel_path

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
        for file_path in glob.glob(pattern, recursive=True):
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"🗑️ Removed: {file_path}")
                    cleaned_count += 1
            except Exception as e:
                print(f"⚠️ Could not remove {file_path}: {e}")
    
    # Also clean up extracted directories
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
    
    print(f"✅ Cleanup completed: {cleaned_count} items removed")

def process_excel_files():
    """Process Excel files with aggressive filtering to avoid timeout"""
    print("=== STARTING EXCEL PROCESSING WITH DUPLICATE FILTERING ===")
    start_time = time.time()
    
    # Get changed files first (most important)
    changed_files = get_changed_files()
    excel_files = [f for f in changed_files if f.endswith(('.xlsx', '.xlsm'))]
    
    # If no changed files, get all files but filter heavily
    if not excel_files:
        all_files = glob.glob('**/*.xlsx', recursive=True) + glob.glob('**/*.xlsm', recursive=True)
        
        # AGGRESSIVE FILTERING
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
            
            # Skip large files
            if os.path.exists(file_path):
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                if file_size_mb > 15:  # 15MB limit
                    print(f"⏭️ Skipping large file: {file_path} ({file_size_mb:.1f}MB)")
                    continue
                
                filtered_files.append((file_path, file_size_mb))
        
        # Sort by size and take only the smallest 3 files
        filtered_files.sort(key=lambda x: x[1])
        excel_files = [f[0] for f in filtered_files[:3]]
        
        print(f"📊 Filtered from {len(all_files)} to {len(excel_files)} files")
        for file_path, size_mb in filtered_files[:3]:
            print(f"   ✅ Will process: {file_path} ({size_mb:.1f}MB)")
    
    processed_count = 0
    
    for excel_file in excel_files:
        # Double-check filters
        if ('_fromXML' in excel_file or 
            '_overwritten' in excel_file or
            not os.path.exists(excel_file)):
            continue
        
        # Timeout check
        elapsed = time.time() - start_time
        if elapsed > 120:  # 2 minutes max
            print(f"⏱️ TIMEOUT: Stopping after {elapsed:.1f}s")
            break
        
        file_size_mb = os.path.getsize(excel_file) / (1024 * 1024)
        print(f"🔄 Processing {excel_file} ({file_size_mb:.1f}MB)")
        
        file_start = time.time()
        
        try:
            # Use selective extraction
            extract_dir = extract_excel_selective(excel_file)
            if not extract_dir:
                continue
            
            # Skip XML formatting to save time
            print("🎨 Formatting XML files for better Git diffing...")
            format_xml_files(extract_dir)
            
            # Add to git
            repo = git.Repo('.')
            repo.git.add(str(extract_dir))
            
            # Create _fromXML copy
            fromxml_path = Path(excel_file).with_name(
                f"{Path(excel_file).stem}_fromXML{Path(excel_file).suffix}"
            )
            shutil.copy2(excel_file, fromxml_path)
            repo.git.add(str(fromxml_path))
            
            processed_count += 1
            file_elapsed = time.time() - file_start
            total_elapsed = time.time() - start_time
            
            print(f"✅ Processed {excel_file} in {file_elapsed:.1f}s (total: {total_elapsed:.1f}s)")
            
        except Exception as e:
            print(f"❌ Error processing {excel_file}: {e}")
            continue
    
    total_elapsed = time.time() - start_time
    print(f"=== COMPLETED: {processed_count} files in {total_elapsed:.1f}s ===")
    return excel_files

def process_xml_files():
    """Process XML files but don't package back to Excel"""
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
    
    # Don't package back to Excel - just return directories for diff reporting
    print(f"Found {len(xml_dirs)} XML directories with changes")
    return list(xml_dirs)

def generate_xml_diff_report(xml_dirs):
    """Generate diff report for VBA and table changes"""
    try:
        reports_dir = Path("xml-diff-reports")
        os.makedirs(reports_dir, exist_ok=True)
        repo = git.Repo('.')
        
        for xml_dir in xml_dirs:
            summary_file = reports_dir / f"{Path(xml_dir).name}-summary.md"
            
            with open(summary_file, 'w') as f:
                f.write(f"# VBA and Table Changes for {xml_dir}\n\n")
                
                vba_changes = []
                table_changes = []
                total_changes = 0
                
                for root, _, files in os.walk(xml_dir):
                    for file in files:
                        if file.endswith('.xml'):
                            file_path = os.path.join(root, file)
                            rel_path = os.path.relpath(file_path, '.')
                            
                            try:
                                diff = repo.git.diff('HEAD~1', file_path)
                                
                                if not diff:
                                    continue
                                    
                                added = diff.count('\n+')
                                removed = diff.count('\n-')
                                changes = added + removed
                                
                                if changes > 0:
                                    total_changes += changes
                                    
                                    if 'vba' in rel_path.lower():
                                        vba_changes.append((rel_path, changes))
                                    elif 'tables' in rel_path.lower():
                                        table_changes.append((rel_path, changes))
                                        
                            except Exception as e:
                                f.write(f"Error analyzing {rel_path}: {e}\n\n")
                
                f.write(f"**Total changes:** {total_changes} lines\n\n")
                
                if vba_changes:
                    f.write("## VBA Code Changes\n\n")
                    for file_path, changes in vba_changes:
                        f.write(f"- **{file_path}**: {changes} lines changed\n")
                    f.write("\n")
                
                if table_changes:
                    f.write("## Table Structure Changes\n\n")
                    for file_path, changes in table_changes:
                        f.write(f"- **{file_path}**: {changes} lines changed\n")
                    f.write("\n")
            
            # Create detailed diffs
            details_dir = reports_dir / f"{Path(xml_dir).name}-details"
            os.makedirs(details_dir, exist_ok=True)
            
            all_changes = vba_changes + table_changes
            for file_path, changes in sorted(all_changes, key=lambda x: x[1], reverse=True)[:10]:
                try:
                    full_path = os.path.join('.', file_path)
                    
                    file_size_mb = os.path.getsize(full_path) / (1024 * 1024)
                    if file_size_mb > 20:
                        continue
                    
                    detail_file = details_dir / f"{Path(file_path).name.replace('.', '_')}-diff.md"
                    
                    with open(detail_file, 'w') as f:
                        f.write(f"# Changes in {file_path}\n\n")
                        
                        diff = repo.git.diff('HEAD~1', full_path)
                        
                        # Process for readability
                        processed_diff = diff.replace('&amp;', '[&]').replace('&lt;', '[<]').replace('&gt;', '[>]').replace('&quot;', '["]')
                        
                        f.write("```diff\n")
                        f.write(processed_diff)
                        f.write("\n```\n")
                except Exception as e:
                    print(f"Error creating detail report for {file_path}: {e}")
            
            print(f"Created XML diff reports for {xml_dir}")
        
        return reports_dir
    except Exception as e:
        print(f"Warning: Failed to generate XML diff report - {e}")
        return None

def commit_changes():
    """Commit any changes and push to repository"""
    repo = git.Repo('.')
    
    if repo.is_dirty() or len(repo.untracked_files) > 0:
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
                print(f"Pull error (non-critical): {e}")
            
            repo.git.add(A=True)
            commit_msg = "Excel VBA/Table Structure Extraction [skip ci]"
            repo.git.commit('-m', commit_msg)
            
            repo.git.push('origin', branch)
            print(f"Changes committed and pushed to {branch}")
            
        except git.exc.GitCommandError as e:
            print(f"Git push error: {e}")

def main():
    """Main function to process files"""
    print("🚀 STARTING: Excel VBA/Table extraction...")
    
    # STEP 1: Clean up first
    print("🧹 STEP 1: Starting cleanup_generated_files()...")
    cleanup_generated_files()
    print("✅ STEP 1: cleanup_generated_files() completed")
    
    # STEP 2: Process with filtering  
    print("📁 STEP 2: Starting process_excel_files()...")
    excel_files = process_excel_files()
    print(f"✅ STEP 2: process_excel_files() completed - {len(excel_files)} files")
    
    # STEP 3: Continue with rest
    print("🔍 STEP 3: Starting process_xml_files()...")
    xml_dirs = process_xml_files()
    print(f"✅ STEP 3: process_xml_files() completed - {len(xml_dirs)} directories")
    
    print("📊 STEP 4: Starting generate_xml_diff_report()...")
    if xml_dirs:
        generate_xml_diff_report(xml_dirs)
    print("✅ STEP 4: generate_xml_diff_report() completed")
    
    print("📤 STEP 5: Starting commit_changes()...")
    commit_changes()
    print("✅ STEP 5: commit_changes() completed")
    
    print("🏁 COMPLETED: Excel VBA/Table extraction completed")

if __name__ == "__main__":
    main()
