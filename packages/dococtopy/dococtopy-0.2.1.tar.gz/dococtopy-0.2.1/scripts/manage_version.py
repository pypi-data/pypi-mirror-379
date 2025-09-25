#!/usr/bin/env python3
"""Version management script for DocOctopy.

This script provides commands to manage version consistency across the project.
"""

import argparse
import re
import sys
from pathlib import Path


def get_current_version() -> str:
    """Get the current version from _version.py."""
    # Get the project root (parent of scripts directory)
    project_root = Path(__file__).parent.parent
    version_file = project_root / "src" / "dococtopy" / "_version.py"
    content = version_file.read_text()
    match = re.search(r'__version__ = "([^"]+)"', content)
    if not match:
        raise ValueError("Could not find version in _version.py")
    return match.group(1)


def set_version(new_version: str) -> None:
    """Set the version in _version.py."""
    # Get the project root (parent of scripts directory)
    project_root = Path(__file__).parent.parent
    version_file = project_root / "src" / "dococtopy" / "_version.py"
    content = version_file.read_text()

    # Validate version format (semantic versioning)
    if not re.match(r"^\d+\.\d+\.\d+$", new_version):
        raise ValueError(
            f"Invalid version format: {new_version}. Expected format: X.Y.Z"
        )

    # Update version
    new_content = re.sub(
        r'__version__ = "[^"]+"', f'__version__ = "{new_version}"', content
    )

    version_file.write_text(new_content)
    print(f"✅ Updated version to {new_version}")


def update_tests(new_version: str) -> None:
    """Update version references in test files."""
    # Get the project root (parent of scripts directory)
    project_root = Path(__file__).parent.parent
    test_files = [
        "tests/test_cli_basic.py",
        "tests/integration/test_cli_commands.py",
    ]

    for test_file in test_files:
        file_path = project_root / test_file
        if file_path.exists():
            content = file_path.read_text()
            # Update version assertions
            new_content = re.sub(
                r'assert "[^"]*" in result\.stdout',
                f'assert "{new_version}" in result.stdout',
                content,
            )
            file_path.write_text(new_content)
            print(f"✅ Updated {test_file}")


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(description="DocOctopy version management")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Show current version
    show_parser = subparsers.add_parser("show", help="Show current version")

    # Set new version
    set_parser = subparsers.add_parser("set", help="Set new version")
    set_parser.add_argument("version", help="New version (format: X.Y.Z)")

    # Bump version
    bump_parser = subparsers.add_parser("bump", help="Bump version")
    bump_group = bump_parser.add_mutually_exclusive_group(required=True)
    bump_group.add_argument("--major", action="store_true", help="Bump major version")
    bump_group.add_argument("--minor", action="store_true", help="Bump minor version")
    bump_group.add_argument("--patch", action="store_true", help="Bump patch version")

    args = parser.parse_args()

    if args.command == "show":
        try:
            version = get_current_version()
            print(f"Current version: {version}")
        except ValueError as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "set":
        try:
            set_version(args.version)
            update_tests(args.version)
            print(f"🎉 Version updated to {args.version}")
            print("💡 Don't forget to commit the changes and create a git tag!")
        except ValueError as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "bump":
        try:
            current_version = get_current_version()
            major, minor, patch = map(int, current_version.split("."))

            if args.major:
                new_version = f"{major + 1}.0.0"
            elif args.minor:
                new_version = f"{major}.{minor + 1}.0"
            elif args.patch:
                new_version = f"{major}.{minor}.{patch + 1}"

            set_version(new_version)
            update_tests(new_version)
            print(f"🎉 Version bumped to {new_version}")
            print("💡 Don't forget to commit the changes and create a git tag!")
        except ValueError as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
