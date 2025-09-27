#!/usr/bin/env python3
"""
Development setup script for mkdocs-excel-plugin.
"""

import subprocess
import sys
import os


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"📦 {description}...")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ {description} completed")
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        sys.exit(1)


def main():
    """Main development setup."""
    print("🚀 Setting up mkdocs-excel-plugin development environment\n")

    # Install development dependencies
    run_command("pip install -r requirements-dev.txt", "Installing development dependencies")

    # Install package in development mode
    run_command("pip install -e .", "Installing package in development mode")

    # Run code formatting
    run_command("black mkdocs_excel tests", "Formatting code with Black")
    run_command("isort mkdocs_excel tests", "Sorting imports with isort")

    # Run linting
    run_command("flake8 mkdocs_excel", "Running flake8 linting")

    # Run tests
    run_command("pytest tests/ -v", "Running tests")

    print("\n🎉 Development environment setup complete!")
    print("\nNext steps:")
    print("1. Make your changes to the code")
    print("2. Run 'python dev-setup.py' to test changes")
    print("3. Run 'python build-release.py' to build for release")


if __name__ == "__main__":
    main()