"""
Interactive TUI for editing .env files using Textual
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Header, Footer, Button, Input, Label, DataTable, Static
from textual.screen import ModalScreen
from textual import events
from textual.reactive import reactive
from pathlib import Path

from .env_parser import EnvParser


class AddVariableModal(ModalScreen):
    """Modal screen for adding a new environment variable"""

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Add New Environment Variable", classes="modal-title"),
            Label("Key:"),
            Input(placeholder="Enter variable name", id="key-input"),
            Label("Value:"),
            Input(placeholder="Enter variable value", id="value-input"),
            Horizontal(
                Button("Add", variant="primary", id="add-btn"),
                Button("Cancel", variant="default", id="cancel-btn"),
                classes="button-row"
            ),
            classes="modal-content"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-btn":
            key_input = self.query_one("#key-input", Input)
            value_input = self.query_one("#value-input", Input)
            key = key_input.value.strip()
            value = value_input.value.strip()

            if key and value:
                self.dismiss((key, value))
            else:
                # TODO: Show validation error
                pass
        elif event.button.id == "cancel-btn":
            self.dismiss(None)


class EditVariableModal(ModalScreen):
    """Modal screen for editing an existing environment variable"""

    def __init__(self, key: str, current_value: str):
        super().__init__()
        self.key = key
        self.current_value = current_value

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label(f"Edit Environment Variable: {self.key}", classes="modal-title"),
            Label("Value:"),
            Input(value=self.current_value, id="value-input"),
            Horizontal(
                Button("Save", variant="primary", id="save-btn"),
                Button("Cancel", variant="default", id="cancel-btn"),
                classes="button-row"
            ),
            classes="modal-content"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save-btn":
            value_input = self.query_one("#value-input", Input)
            new_value = value_input.value.strip()
            self.dismiss((self.key, new_value))
        elif event.button.id == "cancel-btn":
            self.dismiss(None)


class EnvEditTUI(App):
    """Main TUI application for editing .env files"""

    CSS = """
    .modal-content {
        background: $surface;
        border: solid $primary;
        width: 60;
        height: auto;
        padding: 1;
    }

    .modal-title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    .button-row {
        height: auto;
        align: center middle;
        margin-top: 1;
    }

    .button-row Button {
        margin: 0 1;
    }

    .status-bar {
        dock: bottom;
        height: 1;
        background: $primary;
        color: white;
        padding: 0 1;
    }

    DataTable {
        height: 1fr;
    }

    .controls {
        dock: bottom;
        height: auto;
        background: $surface-lighten-1;
        padding: 1;
    }

    .controls Horizontal {
        height: auto;
        align: center middle;
    }

    .controls Button {
        margin: 0 1;
    }
    """

    def __init__(self, env_file_path):
        super().__init__()
        self.env_file_path = Path(env_file_path)
        self.parser = EnvParser(self.env_file_path)
        self.env_vars = {}

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        yield VerticalScroll(
            DataTable(id="env-table", zebra_stripes=True),
        )
        yield Vertical(
            Horizontal(
                Button("Add Variable", id="add-btn", variant="primary"),
                Button("Edit Selected", id="edit-btn", variant="default"),
                Button("Delete Selected", id="delete-btn", variant="error"),
                Button("Refresh", id="refresh-btn"),
                Button("Quit", id="quit-btn"),
                classes="controls-row"
            ),
            Static(f"Editing: {self.env_file_path}", classes="status-bar"),
            classes="controls"
        )

    def on_mount(self) -> None:
        """Initialize the application"""
        self.title = f"EnvEdit - {self.env_file_path.name}"
        self.refresh_table()

    def refresh_table(self) -> None:
        """Refresh the data table with current environment variables"""
        table = self.query_one("#env-table", DataTable)
        table.clear(columns=True)

        # Set up columns
        table.add_columns("Key", "Value")

        # Load and display environment variables
        self.env_vars = self.parser.parse()

        for key, value in self.env_vars.items():
            # Truncate long values for display
            display_value = value[:50] + "..." if len(value) > 50 else value
            table.add_row(key, display_value, key=key)

        if not self.env_vars:
            table.add_row("No variables found", "Use 'Add Variable' to get started")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses"""
        if event.button.id == "add-btn":
            self.push_screen(AddVariableModal(), self.on_add_variable)
        elif event.button.id == "edit-btn":
            self.edit_selected_variable()
        elif event.button.id == "delete-btn":
            self.delete_selected_variable()
        elif event.button.id == "refresh-btn":
            self.refresh_table()
        elif event.button.id == "quit-btn":
            self.exit()

    def edit_selected_variable(self) -> None:
        """Edit the currently selected variable"""
        table = self.query_one("#env-table", DataTable)
        if table.cursor_row is None:
            return

        try:
            row_key = table.get_row_at(table.cursor_row)
            if row_key and len(row_key) >= 2:
                key = str(row_key[0])
                if key in self.env_vars:
                    current_value = self.env_vars[key]
                    self.push_screen(EditVariableModal(key, current_value), self.on_edit_variable)
        except Exception:
            # Handle case where no row is selected or table is empty
            pass

    def delete_selected_variable(self) -> None:
        """Delete the currently selected variable"""
        table = self.query_one("#env-table", DataTable)
        if table.cursor_row is None:
            return

        try:
            row_key = table.get_row_at(table.cursor_row)
            if row_key and len(row_key) >= 2:
                key = str(row_key[0])
                if key in self.env_vars:
                    if self.parser.remove_variable(key):
                        self.refresh_table()
        except Exception:
            # Handle case where no row is selected or table is empty
            pass

    def on_add_variable(self, result) -> None:
        """Handle result from add variable modal"""
        if result:
            key, value = result
            if self.parser.add_variable(key, value):
                self.refresh_table()
            else:
                # Variable already exists - could show an error message
                pass

    def on_edit_variable(self, result) -> None:
        """Handle result from edit variable modal"""
        if result:
            key, new_value = result
            if self.parser.edit_variable(key, new_value):
                self.refresh_table()

    def action_quit(self) -> None:
        """Handle quit action"""
        self.exit()