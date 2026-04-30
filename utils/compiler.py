import subprocess
import os

def compile_project(base_dir="output"):
    try:
        cmd = ["g++", "main.cpp", "-o", "main"]
        result = subprocess.run(
            cmd,
            cwd=base_dir,
            capture_output=True,
            text=True
        )

        success = result.returncode == 0

        return success, result.stdout + result.stderr

    except Exception as e:
        return False, str(e)
