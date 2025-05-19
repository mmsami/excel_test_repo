#!/usr/bin/env python3
"""
Excel XML Conversion for GitHub Actions
Handles both extraction and packaging in a single script
"""

import os
import sys
import shutil
import zipfile
import glob
import git
from pathlib import Path

def extract_excel(excel_path):
    """Extract Excel file to directory with same name"""
    excel_dir = Path(excel_path).with_suffix('')
    
    # Create directory if it doesn't exist
    os.makedirs(excel_dir, exist_ok=True)
    
    # Extract Excel as zip to directory
    with zipfile.ZipFile(excel_path, 'r') as zip_ref:
        zip_ref.extractall(excel_dir)
    
    print(f"Extracted {excel_path} to {excel_dir}/")
    return excel_dir

def format_xml_files(directory):
    """Format XML files for better diffing"""
    try:
        # Try to import xmlformatter, install if not available
        try:
            from xmlformatter import Formatter
        except ImportError:
            import subprocess
            print("Installing xmlformatter...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "xmlformatter"])
            from xmlformatter import Formatter
        
        # Use only supported parameters
        formatter = Formatter(indent="  ")
        
        xml_count = 0
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.xml'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'rb') as f:
                            content = f.read()
                        
                        formatted_content = formatter.format_string(content)
                        
                        with open(file_path, 'wb') as f:
                            f.write(formatted_content)
                            
                        xml_count += 1
                    except Exception as e:
                        print(f"Error formatting {file_path}: {e}")
        
        print(f"Formatted {xml_count} XML files in {directory}")
    except Exception as e:
        print(f"Warning: XML formatting failed - {e}")
        print("Continuing without XML formatting...")

def package_xml_to_excel(xml_dir):
    """Package XML directory back to Excel file"""
    excel_path = Path(f"{xml_dir}.xlsx")
    
    # If excel already exists, create _overwritten backup
    if excel_path.exists():
        overwritten_path = excel_path.with_name(f"{excel_path.stem}_overwritten{excel_path.suffix}")
        shutil.copy2(excel_path, overwritten_path)
        print(f"Created backup at {overwritten_path}")
    
    # Create a temporary zip file
    temp_zip = excel_path.with_suffix('.zip')
    
    with zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(xml_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(xml_dir))
                zipf.write(file_path, arcname)
    
    # Rename zip to Excel
    if temp_zip.exists():
        if excel_path.exists():
            excel_path.unlink()  # Remove existing Excel file
        temp_zip.rename(excel_path)
        print(f"Created Excel file at {excel_path}")
    
    return excel_path

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
    """Process Excel files and extract to XML"""
    # Get all changed files
    changed_files = get_changed_files()
    
    # Filter for Excel files
    excel_files = [f for f in changed_files if f.endswith(('.xlsx', '.xlsm'))]
    
    # If no changed Excel files found, get all Excel files in repository
    if not excel_files:
        excel_files = glob.glob('**/*.xlsx', recursive=True) + glob.glob('**/*.xlsm', recursive=True)
    
    # Process each Excel file
    for excel_file in excel_files:
        # Skip any files that have _fromXML or _overwritten in their name
        if '_fromXML' in excel_file or '_overwritten' in excel_file:
            continue
            
        # Skip files that don't exist (may have been deleted)
        if not os.path.exists(excel_file):
            continue
            
        # Extract Excel to directory
        extract_dir = extract_excel(excel_file)
        
        # Format XML files for better diffing
        format_xml_files(extract_dir)
        
        # Add the extracted files to git
        repo = git.Repo('.')
        repo.git.add(str(extract_dir))
        
        # Create a _fromXML version for verification
        fromxml_path = Path(excel_file).with_name(
            f"{Path(excel_file).stem}_fromXML{Path(excel_file).suffix}"
        )
        shutil.copy2(excel_file, fromxml_path)
        repo.git.add(str(fromxml_path))
    
    return excel_files

def process_xml_files():
    """Process XML files and package to Excel"""
    # Get all changed files
    changed_files = get_changed_files()
    
    # Find directories that contain XML changes
    xml_dirs = set()
    for changed_file in changed_files:
        if changed_file.endswith('.xml') or '/xl/' in changed_file or '/_rels/' in changed_file:
            # Find the directory containing Content_Types.xml or [Content_Types].xml
            path = Path(changed_file)
            current_dir = path.parent
            
            # Walk up the directory tree until we find the content types file
            while str(current_dir) != '.':
                # Check for both possible filenames (with and without brackets)
                if (current_dir / 'Content_Types.xml').exists() or (current_dir / '[Content_Types].xml').exists():
                    xml_dirs.add(str(current_dir))
                    break
                
                if current_dir == Path('.') or current_dir.parent == current_dir:
                    break  # Avoid infinite loop at root
                
                current_dir = current_dir.parent
    
    # Process each XML directory
    for xml_dir in xml_dirs:
        # Package XML directory to Excel
        excel_path = package_xml_to_excel(xml_dir)
        
        # Add the new Excel file to git
        repo = git.Repo('.')
        repo.git.add(str(excel_path))
        
        # If we created an _overwritten backup, add that too
        overwritten_path = excel_path.with_name(f"{excel_path.stem}_overwritten{excel_path.suffix}")
        if overwritten_path.exists():
            repo.git.add(str(overwritten_path))
    
    return list(xml_dirs)

def generate_xml_diff_report(xml_dirs):
    """Generate human-readable XML diff report with smart truncation"""
    try:
        reports_dir = Path("xml-diff-reports")
        os.makedirs(reports_dir, exist_ok=True)
        repo = git.Repo('.')
        
        for xml_dir in xml_dirs:
            # Create summary and detailed reports
            summary_file = reports_dir / f"{Path(xml_dir).name}-summary.md"
            
            with open(summary_file, 'w') as f:
                f.write(f"# XML Changes Summary for {xml_dir}\n\n")
                
                # Track total changes across all files
                total_changes = 0
                important_files = []
                
                # Process each XML file
                for root, _, files in os.walk(xml_dir):
                    for file in files:
                        if file.endswith('.xml'):
                            file_path = os.path.join(root, file)
                            rel_path = os.path.relpath(file_path, '.')
                            
                            try:
                                # Get the diff
                                diff = repo.git.diff('HEAD~1', file_path)
                                
                                # Skip files with no changes
                                if not diff:
                                    continue
                                    
                                # Count added/removed lines
                                added = diff.count('\n+')
                                removed = diff.count('\n-')
                                changes = added + removed
                                
                                if changes > 0:
                                    total_changes += changes
                                    
                                    # Record important files (those with significant changes)
                                    importance = "HIGH" if changes > 10 else "MEDIUM" if changes > 3 else "LOW"
                                    important_files.append((rel_path, changes, importance))
                            except Exception as e:
                                f.write(f"Error analyzing {rel_path}: {e}\n\n")
                
                # Write summary
                f.write(f"**Total changes:** {total_changes} lines modified\n\n")
                f.write("## Modified Files\n\n")
                f.write("| File | Changes | Importance |\n")
                f.write("|------|---------|------------|\n")
                
                for file_path, changes, importance in sorted(important_files, key=lambda x: x[1], reverse=True):
                    f.write(f"| {file_path} | {changes} | {importance} |\n")
                
                f.write("\n## Details\n\n")
                f.write("For detailed changes in specific files, see subdirectories in this report.\n")
            
            # Create detailed reports directory 
            details_dir = reports_dir / f"{Path(xml_dir).name}-details"
            os.makedirs(details_dir, exist_ok=True)
            
            # Process most important files first
            for file_path, changes, _ in sorted(important_files, key=lambda x: x[1], reverse=True)[:10]:
                try:
                    # Get the full file path
                    full_path = os.path.join('.', file_path)
                    
                    # Create detail file
                    detail_file = details_dir / f"{Path(file_path).name}-diff.md"
                    
                    with open(detail_file, 'w') as f:
                        f.write(f"# Changes in {file_path}\n\n")
                        
                        # Get diff
                        diff = repo.git.diff('HEAD~1', full_path)
                        
                        # Process diff for readability
                        processed_diff = diff.replace('&amp;', '[&]').replace('&lt;', '[<]').replace('&gt;', '[>]')
                        
                        f.write("```diff\n")
                        f.write(processed_diff)
                        f.write("\n```\n")
                except Exception as e:
                    print(f"Error creating detail report for {file_path}: {e}")
            
            print(f"Created XML diff reports for {xml_dir}")
        
        # Add the reports to git
        repo.git.add(str(reports_dir))
        
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
            
            # Construct the correct remote URL with token
            origin_url = repo.remotes.origin.url
            if origin_url.startswith('https://'):
                # Format: https://x-access-token:TOKEN@github.com/user/repo.git
                new_url = f"https://x-access-token:{token}@github.com/{'/'.join(origin_url.split('/')[3:])}"
                repo.remotes.origin.set_url(new_url)
            
            # Get branch name from GITHUB_REF environment variable
            branch = os.environ.get('GITHUB_REF', 'refs/heads/main').replace('refs/heads/', '')
            
            # Commit changes
            repo.git.add(A=True)  # Add all changes
            commit_msg = "Excel-XML Conversion [skip ci]"
            repo.git.commit('-m', commit_msg)
            
            # Push changes
            repo.git.push('origin', branch)
            print(f"Changes committed and pushed to {branch}")
            
        except git.exc.GitCommandError as e:
            print(f"Git push error: {e}")
            print("Continuing with conversion...")

def main():
    """Main function to process files"""
    print("Starting Excel-XML conversion...")
    
    # Process Excel files (extract to XML)
    excel_files = process_excel_files()
    print(f"Processed {len(excel_files)} Excel files")
    
    # Process XML files (package to Excel)
    xml_dirs = process_xml_files()
    print(f"Processed {len(xml_dirs)} XML directories")
    
    # Generate XML diff report
    if xml_dirs:
        generate_xml_diff_report(xml_dirs)
    
    # Commit and push changes
    commit_changes()
    
    print("Excel-XML conversion completed")

if __name__ == "__main__":
    main()
