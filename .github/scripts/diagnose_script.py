#!/usr/bin/env python3
"""
DIAGNOSTIC WRAPPER
This will run your exact script but with timeout and monitoring
"""

import subprocess
import sys
import time
import threading
import signal
import os

def monitor_process():
    """Monitor the subprocess and kill it if it hangs"""
    global process, timed_out
    time.sleep(180)  # 3 minutes
    if process and process.poll() is None:
        print(f"🚨 TIMEOUT: Script has been running for 3 minutes, terminating...")
        timed_out = True
        try:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        except:
            try:
                process.terminate()
                time.sleep(2)
                if process.poll() is None:
                    process.kill()
            except:
                pass

def run_with_monitoring():
    """Run the main script with monitoring"""
    global process, timed_out
    process = None
    timed_out = False
    
    print("🔍 DIAGNOSTIC: Testing your excel_converter.py")
    print("=" * 60)
    
    # Test 1: Check file exists and is readable
    print("📋 Test 1: File existence and permissions")
    script_path = ".github/scripts/excel_converter.py"
    
    if not os.path.exists(script_path):
        print(f"❌ Script not found: {script_path}")
        return
    
    file_size = os.path.getsize(script_path)
    print(f"✅ Script found: {script_path} ({file_size} bytes)")
    
    # Test 2: Check file contents (first few lines)
    print("\n📋 Test 2: File contents (first 10 lines)")
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= 10:
                    break
                print(f"   {i+1:2d}: {line.rstrip()}")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    # Test 3: Python syntax check
    print("\n📋 Test 3: Python syntax validation")
    try:
        with open(script_path, 'r') as f:
            code = f.read()
        compile(code, script_path, 'exec')
        print("✅ Syntax is valid")
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        print(f"   Line {e.lineno}: {e.text}")
        return
    except Exception as e:
        print(f"❌ Compilation error: {e}")
        return
    
    # Test 4: Import test (dry run)
    print("\n📋 Test 4: Import testing")
    test_imports = [
        "import os",
        "import sys", 
        "import shutil",
        "import zipfile",
        "import glob",
        "import git",
        "import re",
        "import time",
        "from pathlib import Path"
    ]
    
    for import_stmt in test_imports:
        try:
            exec(import_stmt)
            print(f"✅ {import_stmt}")
        except Exception as e:
            print(f"❌ {import_stmt} - Error: {e}")
    
    # Test 5: Run the actual script with monitoring
    print("\n📋 Test 5: Running script with 3-minute timeout")
    print("🚀 Starting your excel_converter.py...")
    
    start_time = time.time()
    
    # Start monitoring thread
    monitor_thread = threading.Thread(target=monitor_process, daemon=True)
    monitor_thread.start()
    
    try:
        # Run the script with subprocess
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1,
            preexec_fn=os.setsid  # Create new process group
        )
        
        # Read output in real-time
        output_lines = []
        while True:
            if timed_out:
                print("🚨 SCRIPT TIMED OUT!")
                break
                
            line = process.stdout.readline()
            if line:
                print(f"[SCRIPT] {line.rstrip()}")
                output_lines.append(line.rstrip())
            elif process.poll() is not None:
                # Process finished
                break
            else:
                time.sleep(0.1)
        
        # Get final status
        return_code = process.poll()
        elapsed = time.time() - start_time
        
        if timed_out:
            print(f"⏱️ RESULT: Script timed out after {elapsed:.1f}s")
            print(f"📊 Output lines received: {len(output_lines)}")
            if output_lines:
                print("📋 Last few lines of output:")
                for line in output_lines[-5:]:
                    print(f"   {line}")
            else:
                print("❌ NO OUTPUT RECEIVED - Script hung immediately")
        elif return_code == 0:
            print(f"✅ RESULT: Script completed successfully in {elapsed:.1f}s")
        else:
            print(f"❌ RESULT: Script failed with return code {return_code} after {elapsed:.1f}s")
    
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"💥 EXCEPTION: {e} after {elapsed:.1f}s")
    
    # Test 6: Compare with debug script
    print("\n📋 Test 6: Size comparison with debug script")
    debug_path = ".github/scripts/debug_timeout.py"
    if os.path.exists(debug_path):
        debug_size = os.path.getsize(debug_path)
        main_size = os.path.getsize(script_path)
        print(f"   Debug script: {debug_size} bytes")
        print(f"   Main script:  {main_size} bytes")
        print(f"   Difference:   {main_size - debug_size:+d} bytes")
    
    print("\n💡 ANALYSIS:")
    if timed_out and len(output_lines) == 0:
        print("🚨 DIAGNOSIS: Script hangs immediately at startup")
        print("   Likely causes:")
        print("   - Infinite loop in global scope")
        print("   - Blocking import or module initialization") 
        print("   - Deadlock in class/function definition")
    elif timed_out and len(output_lines) > 0:
        print("🚨 DIAGNOSIS: Script starts but hangs during execution")
        print("   Last output can help identify where it hangs")
    
    print("\n🔧 SUGGESTED FIXES:")
    print("1. Compare your script with the working debug_timeout.py")
    print("2. Look for differences in imports or global code")
    print("3. Add print statements at the very beginning of your script")

if __name__ == "__main__":
    run_with_monitoring()
