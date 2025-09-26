# D:\HotReload\HotReload\src\hotreload\main.py
import sys
import subprocess
import os

def main():
    script_path = os.path.join(os.path.dirname(__file__), "HotReload.py")
    # Alle Argumente, die nach "hotreload" in der CLI kommen, weitergeben
    args = [sys.executable, script_path] + sys.argv[1:]
    subprocess.run(args)
