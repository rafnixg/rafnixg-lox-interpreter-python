"""The main module for the program."""

import sys
from enum import Enum, auto


class Interpreter:
    """A class to interpret the Lox code."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_contents = None
        self.run()

    def read_file(self) -> None:
        """Read the file contents."""
        with open(self.filename) as file:
            self.file_contents = file.read()

    def run(self) -> None:
        """Run the interpreter."""
        self.read_file()
        scanner = Scanner(self.file_contents)
        scanner.scan_tokens()
        scanner.print_tokens()


class TokenType(Enum):
    """An enumeration of the token types."""

    # Single-character tokens
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()

    # One or two character tokens
    BANG = auto()
    BANG_EQUAL = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    # Literals
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    # Keywords
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FUN = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()

    EOF = auto()


class Token:
    """A class to represent a token."""

    def __init__(
        self, token_type: TokenType, lexeme: str, literal: object, line: int
    ) -> None:
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self) -> str:
        return f"{self.token_type.name} {self.lexeme} {self.literal}"

    def __repr__(self) -> str:
        return self.__str__()


class Scanner:
    """A class to scan the Lox code."""

    def __init__(self, source_code: str) -> None:
        self.source_code: str = source_code
        self.tokens: list[Token] = []

    def scan_tokens(self) -> None:
        """Scan the tokens."""
        line = 1
        self.scan_token(0)
        self.tokens.append(Token(TokenType.EOF, "", 'null', line))

    def scan_token(self, start: int) -> None:
        """Scan a token."""
        # TODO: Implement the scanner

    def print_tokens(self) -> None:
        """Print the tokens."""
        for token in self.tokens:
            print(token)

    def get_tokens(self) -> list[Token]:
        """Return the tokens."""
        return self.tokens


def main():
    """Main function for the program."""

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    Interpreter(filename)


if __name__ == "__main__":
    main()
