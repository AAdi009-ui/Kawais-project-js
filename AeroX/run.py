#!/usr/bin/env python3
"""
Run script for Cipher Discord Bot
Executes main.py
"""
import os
import sys
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the script directory to ensure relative imports work
    os.chdir(script_dir)
    
    # Get the path to main.py
    main_py = os.path.join(script_dir, "main.py")
    
    # Check if main.py exists
    if not os.path.exists(main_py):
        print(f"Error: main.py not found in {script_dir}")
        sys.exit(1)
    
    # Execute main.py
    try:
        # Use the same Python interpreter that's running this script
        subprocess.run([sys.executable, main_py], cwd=script_dir)
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error running main.py: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


