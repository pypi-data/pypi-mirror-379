"""
Environment file parser for reading and writing .env files
"""

import re
from pathlib import Path
from typing import Dict, Optional


class EnvParser:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.lines = []
        self.env_vars = {}
        self._load_file()

    def _load_file(self):
        """Load the env file and parse it"""
        try:
            if self.file_path.exists():
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    self.lines = f.readlines()
            else:
                self.lines = []
        except (OSError, UnicodeDecodeError) as e:
            raise RuntimeError(f"Error reading {self.file_path}: {e}")

    def parse(self) -> Dict[str, str]:
        """Parse the env file and return a dictionary of variables"""
        env_vars = {}

        for line in self.lines:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue

            # Match KEY=VALUE pattern
            match = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$', line)
            if match:
                key = match.group(1)
                value = match.group(2)

                # Remove quotes if present
                if (value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]

                env_vars[key] = value

        self.env_vars = env_vars
        return env_vars

    def add_variable(self, key: str, value: str) -> bool:
        """Add a new environment variable"""
        # Validate key format
        if not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', key):
            raise ValueError(f"Invalid variable name '{key}'. Must start with letter or underscore, followed by letters, numbers, or underscores.")

        current_vars = self.parse()

        # Check if variable already exists
        if key in current_vars:
            return False

        # Add the new variable
        new_line = f"{key}={value}\n"
        self.lines.append(new_line)

        # Save the file
        self._save_file()
        return True

    def edit_variable(self, key: str, new_value: str) -> bool:
        """Edit an existing environment variable"""
        current_vars = self.parse()

        # Check if variable exists
        if key not in current_vars:
            return False

        # Find and replace the line
        for i, line in enumerate(self.lines):
            line = line.strip()
            if line and not line.startswith('#'):
                match = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$', line)
                if match and match.group(1) == key:
                    self.lines[i] = f"{key}={new_value}\n"
                    break

        # Save the file
        self._save_file()
        return True

    def remove_variable(self, key: str) -> bool:
        """Remove an environment variable"""
        current_vars = self.parse()

        # Check if variable exists
        if key not in current_vars:
            return False

        # Find and remove the line
        new_lines = []
        for line in self.lines:
            line_stripped = line.strip()
            if line_stripped and not line_stripped.startswith('#'):
                match = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$', line_stripped)
                if match and match.group(1) == key:
                    continue  # Skip this line
            new_lines.append(line)

        self.lines = new_lines
        self._save_file()
        return True

    def _save_file(self):
        """Save the current lines to the file"""
        try:
            # Ensure parent directory exists
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.writelines(self.lines)
        except OSError as e:
            raise RuntimeError(f"Error writing to {self.file_path}: {e}")