#!/usr/bin/env python3
"""Entry point for cerb command"""
import os
import sys
import subprocess
from pathlib import Path

def main():
    """Run the launch.sh script"""
    # Find the launch script in the same directory as kerberos.py
    script_dir = Path(__file__).parent
    launch_script = script_dir / "launch.sh"

    if not launch_script.exists():
        print(f"Error: launch.sh not found at {launch_script}")
        print(f"Searching in: {script_dir}")
        sys.exit(1)

    # Execute the launch script
    try:
        subprocess.run(["/bin/bash", str(launch_script)], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()