#!/usr/bin/env python3
"""
Excel XML Conversion for GitHub Actions
Extracts VBA code and table structure for diffing, generates artifact reports
"""

import os
import sys
import shutil
import zipfile
import glob
import git
import re
from pathlib import Path

def extract_excel_selective(excel_path, output_dir):
    """Extract only VBA, table definitions, and structure from Excel file"""
    # Create directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract Excel as zip to temporary directory
    temp_dir = Path(f"{output_dir}_temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    with zipfile.ZipFile(excel_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    # Copy only the files we care about
    # First, essential files for Excel structure
    essential_files = [
        '[Content_Types].xml',
        'Content_Types.xml',
        '_rels/.rels',
    ]
    
    for file in essential_files:
        src = temp_dir / file
        if src.exists():
            # Create parent directories if needed
            dst = output_dir / file
            os.makedirs(dst.parent, exist_ok=True)
            shutil.copy2(src, dst)
    
    # Copy all VBA-related files
    vba_paths = ['xl/vbaProject.bin', 'xl/_rels/vbaProject.bin.rels', 'xl/vba/']
    for vba_path in vba_paths:
        src = temp_dir / vba_path
        if src.exists():
            if src.is_dir():
                dst = output_dir / vba_path
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                dst = output_dir / vba_path
                os.makedirs(dst.parent, exist_ok=True)
                shutil.copy2(src, dst)
    
    # Copy all table definitions
    tables_dir = temp_dir / 'xl/tables'
    if tables_dir.exists():
        dst_tables = output_dir / 'xl/tables'
        shutil.copytree(tables_dir, dst_tables, dirs_exist_ok=True)
    
    # Copy worksheet structure files, but remove data
    worksheets_dir = temp_dir / 'xl/worksheets'
    if worksheets_dir.exists():
        # Create destination directory
        dst_worksheets = output_dir / 'xl/worksheets'
        os.makedirs(dst_worksheets, exist_ok=True)
        
        # Process each worksheet
        for sheet_file in worksheets_dir.glob('*.xml'):
            # Process the worksheet to remove data but keep structure
            process_worksheet_structure(sheet_file, dst_worksheets / sheet_file.name)
    
    # Clean up temp directory
    shutil.rmtree(temp_dir)
    
    print(f"Extracted code and structure from {excel_path} to {output_dir}/")
    return output_dir

def process_worksheet_structure(src_file, dst_file):
    """Extract worksheet structure without data"""
    try:
        # Read the worksheet XML
        with open(src_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Use regex to remove data cells but keep structure
        # This pattern matches <c> tags (cells) that aren't defining structure
        data_pattern = r'<c r="[^"]+">.*?</c>'
        structure_only = re.sub(data_pattern, '', content)
        
        # Write the structure-only content
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(structure_only)
    except Exception as e:
        print(f"Error processing worksheet {src_file}: {e}")
        # Fallback: just copy the file as is
        shutil.copy2(src_file, dst_file)

def format_xml_files(directory):
    """Format XML files with attributes on separate lines for better diffing"""
    try:
        xml_count = 0
        
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.xml'):
                    file_path = os.path.join(root, file)
                    try:
                        # Use a simple string replacement approach which is faster
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        # Process opening tags with regex - more efficient than char-by-char
                        import re
                        
                        # This pattern finds opening tags with attributes
                        pattern = r'<([a-zA-Z0-9_:-]+)(\s+[^>]+)>'
                        
                        def format_attributes(match):
                            tag_name = match.group(1)
                            attributes = match.group(2).strip()
                            
                            # If no attributes or very simple, return as is
                            if not attributes or ' ' not in attributes:
                                return f"<{tag_name} {attributes}>"
                            
                            # Add line breaks between attributes
                            formatted_attrs = ""
                            attr_indent = "  "
                            
                            # Match each attribute
                            attr_pattern = r'([a-zA-Z0-9_:-]+)="([^"]*)"'
                            attr_matches = re.findall(attr_pattern, attributes)
                            
                            for attr_name, attr_value in attr_matches:
                                formatted_attrs += f"\n{attr_indent}{attr_name}=\"{attr_value}\""
                            
                            return f"<{tag_name}{formatted_attrs}\n>"
                        
                        # Apply the formatting to opening tags
                        formatted_content = re.sub(pattern, format_attributes, content)
                        
                        # Add indentation to make it more readable
                        lines = formatted_content.split('\n')
                        indented_lines = []
                        indent_level = 0
                        
                        for line in lines:
                            stripped = line.strip()
                            
                            # Adjust indent for closing tags
                            if stripped.startswith('</'):
                                indent_level = max(0, indent_level - 1)
                                
                            # Add the indented line if it's not empty
                            if stripped:
                                # Don't re-indent lines that are already indented attributes
                                if '=' in stripped and not stripped.startswith('<'):
                                    indented_lines.append(line)  # Keep original indentation
                                else:
                                    indented_lines.append('  ' * indent_level + stripped)
                            
                            # Increase indent after opening tag
                            if stripped.startswith('<') and not stripped.startswith('</') and not stripped.endswith('/>') and not stripped.startswith('<?'):
                                indent_level += 1
                        
                        # Write the formatted content back
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write('\n'.join(indented_lines))
                        
                        xml_count += 1
                    except Exception as e:
                        print(f"Error formatting {file_path}: {e}")
        
        print(f"Formatted {xml_count} XML files in {directory} with attributes on separate lines")
    except Exception as e:
        print(f"Warning: XML formatting failed - {e}")
        print("Continuing without XML formatting...")

def get_changed_files():
    """Get list of changed files from the most recent commit"""
    repo = git.Repo('.')
    
    try:
        # Get list of changed files from the most recent commit
        if len(repo.heads) > 0:  # Check if there are any branches
            diffs = repo.git.diff('HEAD~1', '--name-only').split('\n')
        else:
            # First commit in repo
            diffs = repo.git.ls_files().split('\n')
        return diffs
    except git.exc.GitCommandError:
        # Handle case where HEAD~1 doesn't exist (first commit)
        return repo.git.ls_files().split('\n')

def process_excel_files():
    """Process Excel files and extract code and structure to XML"""
    # Get all changed files
    changed_files = get_changed_files()
    
    # Filter for Excel files
    excel_files = [f for f in changed_files if f.endswith(('.xlsx', '.xlsm'))]
    
    # If no changed Excel files found, get all Excel files in repository
    if not excel_files:
        excel_files = glob.glob('**/*.xlsx', recursive=True) + glob.glob('**/*.xlsm', recursive=True)
    
    # Create a directory for extracted files (not committed to Git)
    extraction_dir = Path(".excel-extractions")
    if extraction_dir.exists():
        shutil.rmtree(extraction_dir)  # Clean up from previous runs
    os.makedirs(extraction_dir, exist_ok=True)
    
    # Dictionary to track original file paths and their extraction directories
    processed_files = {}
    
    # Process each Excel file
    for excel_file in excel_files:
        # Skip any files that have _fromXML or _overwritten in their name
        if '_fromXML' in excel_file or '_overwritten' in excel_file:
            continue
            
        # Skip files that don't exist (may have been deleted)
        if not os.path.exists(excel_file):
            continue
            
        # Skip files that are inside extracted directories
        if any(part.endswith('_fromXML') for part in Path(excel_file).parts):
            print(f"Skipping {excel_file} - inside extracted directory")
            continue
            
        # Check file size - skip very large files
        file_size_mb = os.path.getsize(excel_file) / (1024 * 1024)
        if file_size_mb > 90:
            print(f"Skipping {excel_file} - size {file_size_mb:.2f}MB exceeds GitHub's limit")
            continue
            
        # Extract only VBA and table structure to a temporary directory
        safe_name = re.sub(r'[^\w\-\.]', '_', str(Path(excel_file).stem))
        file_extraction_dir = extraction_dir / safe_name
        extract_excel_selective(excel_file, file_extraction_dir)
        
        # Format XML files for better diffing
        format_xml_files(file_extraction_dir)
        
        # Track the mapping of original file to extraction directory
        processed_files[excel_file] = file_extraction_dir
    
    return processed_files

def generate_xml_diff_report(processed_files):
    """Generate human-readable XML diff report with smart truncation"""
    try:
        reports_dir = Path("xml-diff-reports")
        if reports_dir.exists():
            shutil.rmtree(reports_dir)  # Clean up from previous runs
        os.makedirs(reports_dir, exist_ok=True)
        
        # Create an index file
        index_file = reports_dir / "index.md"
        with open(index_file, 'w') as f:
            f.write("# Excel File Diff Reports\n\n")
            f.write("| Excel File | VBA Changes | Table Structure Changes | Last Modified |\n")
            f.write("|------------|-------------|-------------------------|---------------|\n")
        
        repo = git.Repo('.')
        
        for original_file, extraction_dir in processed_files.items():
            # Create summary report file
            excel_name = Path(original_file).name
            summary_file = reports_dir / f"{Path(extraction_dir).name}-summary.md"
            
            # Track different types of changes
            vba_changes = []
            table_changes = []
            structure_changes = []
            
            # Create the summary file
            with open(summary_file, 'w') as f:
                f.write(f"# Changes in {excel_name}\n\n")
                
                # Calculate file stats
                try:
                    file_stats = repo.git.log('-1', '--format=%ad', '--date=relative', '--', original_file)
                except:
                    file_stats = "Unknown"
                
                f.write(f"Last modified: {file_stats}\n\n")
                
                # Track total changes across all files
                total_changes = 0
                important_files = []
                
                # Process each XML file
                for root, _, files in os.walk(extraction_dir):
                    for file in files:
                        if file.endswith('.xml'):
                            file_path = os.path.join(root, file)
                            rel_path = os.path.relpath(file_path, extraction_dir)
                            
                            try:
                                # Get the diff - compare with previous commit's version
                                # First, need to check if this is a new file
                                is_new_file = True
                                try:
                                    # Check if the file path exists in the previous commit
                                    is_new_file = False
                                    diff = repo.git.diff('HEAD', file_path)
                                except:
                                    # If error, it's likely a new file
                                    is_new_file = True
                                
                                if is_new_file:
                                    # For new files, just count the lines
                                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as content_file:
                                        content = content_file.read()
                                        changes = content.count('\n')
                                        diff = content
                                else:
                                    # Not a new file, get diff
                                    diff = repo.git.diff('HEAD', file_path)
                                    # Skip files with no changes
                                    if not diff:
                                        continue
                                    
                                    # Count added/removed lines
                                    added = diff.count('\n+')
                                    removed = diff.count('\n-')
                                    changes = added + removed
                                
                                if changes > 0:
                                    total_changes += changes
                                    
                                    # Record changes by type
                                    if 'vba' in rel_path.lower():
                                        vba_changes.append((rel_path, changes))
                                    elif 'tables' in rel_path.lower():
                                        table_changes.append((rel_path, changes))
                                    else:
                                        structure_changes.append((rel_path, changes))
                                    
                                    # Record important files (those with significant changes)
                                    importance = "HIGH" if changes > 10 else "MEDIUM" if changes > 3 else "LOW"
                                    important_files.append((rel_path, changes, importance))
                            except Exception as e:
                                f.write(f"Error analyzing {rel_path}: {e}\n\n")
                
                # Write summary sections
                f.write(f"**Total changes:** {total_changes} lines modified\n\n")
                
                # VBA Changes
                if vba_changes:
                    f.write("## VBA Code Changes\n\n")
                    f.write("| File | Changes |\n")
                    f.write("|------|--------|\n")
                    for file_path, changes in sorted(vba_changes, key=lambda x: x[1], reverse=True):
                        f.write(f"| {file_path} | {changes} |\n")
                    f.write("\n")
                
                # Table Changes
                if table_changes:
                    f.write("## Table Structure Changes\n\n")
                    f.write("| Table | Changes |\n")
                    f.write("|-------|--------|\n")
                    for file_path, changes in sorted(table_changes, key=lambda x: x[1], reverse=True):
                        f.write(f"| {file_path} | {changes} |\n")
                    f.write("\n")
                
                # Other Structure Changes
                if structure_changes:
                    f.write("## Other Structure Changes\n\n")
                    f.write("| File | Changes |\n")
                    f.write("|------|--------|\n")
                    for file_path, changes in sorted(structure_changes, key=lambda x: x[1], reverse=True):
                        f.write(f"| {file_path} | {changes} |\n")
                    f.write("\n")
                
                f.write("## Details\n\n")
                f.write("For detailed changes in specific files, see the detailed reports below.\n")
            
            # Create detailed reports directory 
            details_dir = reports_dir / f"{Path(extraction_dir).name}-details"
            os.makedirs(details_dir, exist_ok=True)
            
            # Process most important files first
            for file_path, changes, _ in sorted(important_files, key=lambda x: x[1], reverse=True)[:20]:
                try:
                    # Get the full file path
                    full_path = os.path.join(extraction_dir, file_path)
                    
                    # Skip very large files
                    file_size_mb = os.path.getsize(full_path) / (1024 * 1024)
                    if file_size_mb > 40:
                        print(f"Skipping detailed diff for {file_path} - size {file_size_mb:.2f}MB exceeds size limits")
                        continue
                    
                    # Create detail file
                    detail_file = details_dir / f"{Path(file_path).name.replace('.', '_')}-diff.md"
                    
                    with open(detail_file, 'w') as f:
                        f.write(f"# Changes in {file_path}\n\n")
                        
                        # Get diff
                        try:
                            diff = repo.git.diff('HEAD', full_path)
                        except:
                            # If error, it's likely a new file - show the whole content
                            with open(full_path, 'r', encoding='utf-8', errors='ignore') as content_file:
                                diff = content_file.read()
                        
                        # Limit diff size (GitHub's recommended file size)
                        if len(diff) > 40 * 1024 * 1024:  # 40MB
                            truncated_diff = diff[:40 * 1024 * 1024] + "\n\n... (truncated due to size limits) ...\n"
                            diff = truncated_diff
                        
                        # Process diff for readability
                        processed_diff = diff.replace('&amp;', '[&]').replace('&lt;', '[<]').replace('&gt;', '[>]').replace('&quot;', '["]')
                        
                        f.write("```diff\n")
                        f.write(processed_diff)
                        f.write("\n```\n")
                except Exception as e:
                    print(f"Error creating detail report for {file_path}: {e}")
            
            # Update the index file
            with open(index_file, 'a') as f:
                vba_count = len(vba_changes)
                table_count = len(table_changes)
                f.write(f"| [{excel_name}]({Path(extraction_dir).name}-summary.md) | {vba_count} | {table_count} | {file_stats} |\n")
            
            print(f"Created XML diff reports for {original_file}")
        
        return reports_dir
    except Exception as e:
        print(f"Warning: Failed to generate XML diff report - {e}")
        return None

def main():
    """Main function to process files"""
    print("Starting Excel-XML conversion...")
    
    # Process Excel files (extract to XML but don't commit)
    processed_files = process_excel_files()
    print(f"Processed {len(processed_files)} Excel files")
    
    # Generate XML diff reports
    if processed_files:
        generate_xml_diff_report(processed_files)
    
    # No need to commit any changes - reports are uploaded as artifacts only
    print("Excel-XML conversion completed. Diff reports created as artifacts.")

if __name__ == "__main__":
    main()
