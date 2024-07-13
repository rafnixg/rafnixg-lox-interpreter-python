"""A module to interpret the Lox code."""
import sys
from app.scanner import Scanner


class Interpreter:
    """A class to interpret the Lox code."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_contents = None
        self.command = None
        self.read_file()

    def read_file(self) -> None:
        """Read the file contents."""
        with open(self.filename) as file:
            self.file_contents = file.read()

    def run(self, command: str) -> None:
        """Run the interpreter."""
        self.command = command
        command_func = getattr(self, command, self.default_command)
        command_func()

    def default_command(self) -> None:
        """Print an error message for an unknown command."""
        print(f"Unknown command: {self.command}", file=sys.stderr)
        exit(1)

    def tokenize(self) -> None:
        """Tokenize the Lox code."""
        scanner = Scanner(self.file_contents)
        scanner.scan_tokens()
        scanner.print_tokens()
