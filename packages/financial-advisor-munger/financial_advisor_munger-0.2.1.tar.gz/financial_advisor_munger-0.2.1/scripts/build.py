#!/usr/bin/env python3
"""
Build script for financial-advisor-munger package
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ {description} failed:")
        print(result.stderr)
        sys.exit(1)
    else:
        print(f"✅ {description} completed")
        if result.stdout.strip():
            print(result.stdout)

def main():
    """Main build process"""

    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ pyproject.toml not found. Run from package root directory.")
        sys.exit(1)

    print("🎯 Building financial-advisor-munger package")
    print("=" * 50)

    # Clean previous builds
    run_command("rm -rf dist/ build/ *.egg-info/", "Cleaning previous builds")

    # Install build dependencies
    run_command("pip install build twine", "Installing build tools")

    # Build package
    run_command("python -m build", "Building package")

    # Check package
    run_command("twine check dist/*", "Checking package integrity")

    print("\n🎉 Build completed successfully!")
    print("\n📦 Package files:")
    for file in Path("dist").glob("*"):
        print(f"  - {file}")

    print("\n📤 To publish to PyPI:")
    print("  pip install twine")
    print("  twine upload dist/*")

    print("\n🐳 To build Docker image:")
    print("  docker build -t financial-advisor-munger .")

    print("\n🧪 To test locally:")
    print("  pip install dist/*.whl")
    print("  munger-web --help")

if __name__ == "__main__":
    main()