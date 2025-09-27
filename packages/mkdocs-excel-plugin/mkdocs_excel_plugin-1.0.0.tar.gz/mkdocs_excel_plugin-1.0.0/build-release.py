#!/usr/bin/env python3
"""
Release build and publish script for mkdocs-excel-plugin.
"""

import subprocess
import sys
import os
import shutil


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        sys.exit(1)


def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning build artifacts...")
    dirs_to_clean = ['build', 'dist', 'mkdocs_excel.egg-info']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}")


def main():
    """Main release process."""
    print("🚀 Building mkdocs-excel-plugin for release\n")

    # Clean previous builds
    clean_build()

    # Run quality checks
    run_command("black --check mkdocs_excel tests", "Checking code formatting")
    run_command("isort --check-only mkdocs_excel tests", "Checking import sorting")
    run_command("flake8 mkdocs_excel", "Running linting")

    # Run tests
    run_command("pytest tests/ -v --cov=mkdocs_excel", "Running tests with coverage")

    # Build the package
    run_command("python -m build", "Building wheel and source distribution")

    # Check the built package
    run_command("twine check dist/*", "Checking built package")

    print("\n🎉 Build completed successfully!")
    print("\nBuild artifacts:")
    if os.path.exists('dist'):
        for file in os.listdir('dist'):
            print(f"  📦 dist/{file}")

    print("\nNext steps:")
    print("1. Test the package: pip install dist/*.whl")
    print("2. Test upload: twine upload --repository testpypi dist/*")
    print("3. Production upload: twine upload dist/*")

    # Ask if user wants to upload to TestPyPI
    response = input("\nUpload to TestPyPI? (y/N): ").lower().strip()
    if response == 'y':
        run_command("twine upload --repository testpypi dist/*", "Uploading to TestPyPI")
        print("\n✅ Uploaded to TestPyPI!")
        print("Test installation: pip install --index-url https://test.pypi.org/simple/ mkdocs-excel-plugin")

        # Ask about production upload
        response = input("\nUpload to production PyPI? (y/N): ").lower().strip()
        if response == 'y':
            run_command("twine upload dist/*", "Uploading to PyPI")
            print("\n🎉 Published to PyPI!")
            print("Install: pip install mkdocs-excel-plugin")


if __name__ == "__main__":
    main()