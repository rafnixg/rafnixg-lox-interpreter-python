# Lox Interpreter in Python

[![progress-banner](https://backend.codecrafters.io/progress/interpreter/9459789f-a865-4088-928d-d1d8b4816a8f)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

A Python implementation of the **Lox** interpreter, built as part of the
["Build Your Own Interpreter" Challenge](https://app.codecrafters.io/courses/interpreter/overview) on [CodeCrafters](https://codecrafters.io).

Lox is a simple, dynamically-typed language described in the book
[Crafting Interpreters](https://craftinginterpreters.com/) by Robert Nystrom.

---

## Prerequisites

- Python 3.12+
- [Pipenv](https://pipenv.pypa.io/)

## Installation

```bash
# Install dependencies
pipenv install
```

## Usage

Run the interpreter using the provided shell script:

```bash
./your_program.sh <command> <path_to_lox_file>
```

### Available commands

| Command    | Description                          |
|------------|--------------------------------------|
| `tokenize` | Scan and print all tokens in a file  |

### Example

```bash
$ ./your_program.sh tokenize test.lox
IDENTIFIER foo null
IDENTIFIER bar null
IDENTIFIER _hello null
EOF  null
```

---

## Project Structure

```
.
├── app/
│   ├── main.py          # Entry point — parses CLI arguments
│   ├── interpreter.py   # Orchestrates command execution
│   ├── scanner.py       # Lexer / tokenizer
│   └── token.py         # Token and TokenType definitions
├── test.lox             # Sample Lox source file
├── your_program.sh      # Local run script
├── codecrafters.yml     # CodeCrafters configuration
└── Pipfile              # Python dependencies
```

---

## Implementation Status

| Feature                                     | Status |
|---------------------------------------------|--------|
| Scanning / Tokenizing                       | ✅ Done |
| Parsing                                     | 🔲 Pending |
| Evaluating expressions                      | 🔲 Pending |
| Evaluating statements                       | 🔲 Pending |
| Arithmetic operations                       | 🔲 Pending |
| Variables                                   | 🔲 Pending |
| Control flow (`if` / `while` / `for`)       | 🔲 Pending |
| Functions                                   | 🔲 Pending |
| Standard library functions (e.g. `clock()`) | 🔲 Pending |
| Classes                                     | 🔲 Pending |

---

## References

- [Crafting Interpreters](https://craftinginterpreters.com/) — the book this project is based on
- [CodeCrafters — Build Your Own Interpreter](https://app.codecrafters.io/courses/interpreter/overview)
