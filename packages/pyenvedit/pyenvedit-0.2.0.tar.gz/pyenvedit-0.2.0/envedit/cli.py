#!/usr/bin/env python3
"""
envedit - CLI tool for editing .env files
"""

import argparse
import os
import sys
from pathlib import Path
from .env_parser import EnvParser
from .tui import EnvEditTUI


def display_env_file(env_path):
    """Display the contents of an env file"""
    parser = EnvParser(env_path)
    env_vars = parser.parse()

    if not env_vars:
        print(f"No environment variables found in {env_path}")
        return

    print(f"Environment variables in {env_path}:")
    print("-" * 40)
    for key, value in env_vars.items():
        print(f"{key}={value}")


def add_env_variable(env_path, key_value_pair):
    """Add a new environment variable to the file"""
    try:
        key, value = key_value_pair.split('=', 1)
    except ValueError:
        print("Error: Invalid format. Use KEY=VALUE")
        return False

    parser = EnvParser(env_path)
    if parser.add_variable(key, value):
        print(f"Added {key}={value} to {env_path}")
        return True
    else:
        print(f"Variable {key} already exists. Use --edit to modify it.")
        return False


def edit_env_variable(env_path, key_value_pair):
    """Edit an existing environment variable"""
    try:
        key, value = key_value_pair.split('=', 1)
    except ValueError:
        print("Error: Invalid format. Use KEY=VALUE")
        return False

    parser = EnvParser(env_path)
    if parser.edit_variable(key, value):
        print(f"Updated {key}={value} in {env_path}")
        return True
    else:
        print(f"Variable {key} not found in {env_path}")
        return False


def remove_env_variable(env_path, key):
    """Remove an environment variable from the file"""
    parser = EnvParser(env_path)
    if parser.remove_variable(key):
        print(f"Removed {key} from {env_path}")
        return True
    else:
        print(f"Variable {key} not found in {env_path}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Edit .env files with ease',
        prog='pyenvedit'
    )

    parser.add_argument(
        'env_file',
        nargs='?',
        default='.env',
        help='Path to the .env file (default: .env)'
    )

    parser.add_argument(
        '--add',
        metavar='KEY=VALUE',
        help='Add a new environment variable'
    )

    parser.add_argument(
        '--edit',
        metavar='KEY=VALUE',
        help='Edit an existing environment variable'
    )

    parser.add_argument(
        '--remove',
        metavar='KEY',
        help='Remove an environment variable'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.2.0'
    )

    args = parser.parse_args()

    try:
        env_path = Path(args.env_file)

        # If no flags are provided, either display the file or launch TUI
        if not args.add and not args.edit and not args.remove:
            if env_path.exists():
                # If file exists and we just have the filename, display it
                display_env_file(env_path)
            else:
                # Launch TUI mode for interactive editing
                app = EnvEditTUI(env_path)
                app.run()
            return

        # Ensure the directory exists
        env_path.parent.mkdir(parents=True, exist_ok=True)

        # Handle add operation
        if args.add:
            if not add_env_variable(env_path, args.add):
                sys.exit(1)

        # Handle edit operation
        if args.edit:
            if not edit_env_variable(env_path, args.edit):
                sys.exit(1)

        # Handle remove operation
        if args.remove:
            if not remove_env_variable(env_path, args.remove):
                sys.exit(1)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied accessing {env_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()