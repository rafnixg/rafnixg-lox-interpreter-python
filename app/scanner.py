"""A module for scanning the Lox code."""

import sys
from app.token import Token, TokenType


class Scanner:
    """A class to scan the Lox code."""

    def __init__(self, source_code: str) -> None:
        self.source_code: str = source_code
        self.tokens: list[Token] = []
        self.start: int = 0
        self.current: int = 0
        self.line: int = 1
        self.error = False

    def error_message(self, message: str) -> None:
        """Print an error message."""
        self.report(self.line, "", message)

    def report(self, line: int, where: str, message: str) -> None:
        """Print an error message."""
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        self.error = True
        # exit(65)

    def is_at_end(self) -> bool:
        """Check if the scanner is at the end of the source code."""
        return self.current >= len(self.source_code)

    def advance(self) -> str:
        """Advance the scanner."""
        self.current += 1
        return self.source_code[self.current - 1]

    def add_token(self, token_type: TokenType, literal: object = None) -> None:
        """Add a token to the list of tokens."""
        text = self.source_code[self.start : self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def scan_tokens(self) -> None:
        """Scan the tokens."""
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))

    def scan_token(self) -> None:
        """Scan a token."""
        c = self.advance()
        match c:
            case "(":
                self.add_token(TokenType.LEFT_PAREN)
            case ")":
                self.add_token(TokenType.RIGHT_PAREN)
            case "{":
                self.add_token(TokenType.LEFT_BRACE)
            case "}":
                self.add_token(TokenType.RIGHT_BRACE)
            case ",":
                self.add_token(TokenType.COMMA)
            case ".":
                self.add_token(TokenType.DOT)
            case "-":
                self.add_token(TokenType.MINUS)
            case "+":
                self.add_token(TokenType.PLUS)
            case ";":
                self.add_token(TokenType.SEMICOLON)
            case "*":
                self.add_token(TokenType.STAR)
            case "=":
                self.add_token(
                    TokenType.EQUAL
                    if not self._match("=")
                    else TokenType.EQUAL_EQUAL
                )
            case "!":
                self.add_token(
                    TokenType.BANG
                    if not self._match("=")
                    else TokenType.BANG_EQUAL
                )
            case "<":
                self.add_token(
                    TokenType.LESS
                    if not self._match("=")
                    else TokenType.LESS_EQUAL
                )
            case ">":
                self.add_token(
                    TokenType.GREATER
                    if not self._match("=")
                    else TokenType.GREATER_EQUAL
                )
            case "/":
                if self._match("/"):
                    while self._peek() != "\n" and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case " ", "\r", "\t":
                pass
            case _:
                self.error_message(f"Unexpected character: {c}")

    def _peek(self) -> str:
        """Return the next character."""
        if self.is_at_end():
            return "\0"
        return self.source_code[self.current]

    def _match(self, expected: str) -> bool:
        """Check if the current character is equal to the expected character."""
        if self.is_at_end():
            return False
        if self.source_code[self.current] != expected:
            return False
        self.current += 1
        return True

    def print_tokens(self) -> None:
        """Print the tokens."""
        for token in self.tokens:
            print(token)

    def get_tokens(self) -> list[Token]:
        """Return the tokens."""
        return self.tokens
