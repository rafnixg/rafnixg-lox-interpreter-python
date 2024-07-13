"""The main module for the program."""

import sys
from app.interpreter import Interpreter


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

    Interpreter(filename).run(command)


if __name__ == "__main__":
    main()
