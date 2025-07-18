# Brainfuck Interpreter in Python

## About

A simple Brainfuck interpreter written in Python, designed to run Brainfuck code from the command line with zero dependencies beyond Python itself.
For detailed API docs and usage, check out doc.txt.

## Features

- Brainfuck code execution
- Two copies of the runtime, better one (chat_execute_brainfuck) and worse one (execute_brainfuck)
- Basic command-line interface
- Pure Python, no external libs required (brainfuck.py uses sys, unittest_brainfuck.py uses os, unittest, brainfuc)
- Unit tests included
- Actually fixed recursive looping
- Examples included (Some examples are not valid brainfuck and were used for testing edge cases)
- Lazy make file

## Usage

```bash
python brainfuck.py yourcode.bf
```

For more info, see doc.txt.

## Requirements

- Python 3.x

## License

No license specified. Use at your own risk.
