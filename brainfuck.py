"""
Brainfuck Interpreter (Python 3)
Reads and executes Brainfuck code from a file, with optional debug printing.
"""
import sys

DEBUG = False
DEBUG_FILE = "helloML.bf"
BYTE_MIN = 0
BYTE_MAX = 255
MEMORY_SIZE = 30000

# global vars
memory = [0] * MEMORY_SIZE
pointer = 0


def clean_brainfuck_code(dirty_code):
    """
    Takes in dirty brainfuck code with whitespace and comments and returns clean brainfuck
    Only returns valid Brainfuck commands: []<>+-,.
    """

    lines = dirty_code.splitlines()
    code_no_comments = []

    for line in lines:
        code_no_comments.append(line.split(';')[0])

    allowed = "[]<>+-,."

    code = ''.join(code_no_comments)
    code = ''.join(c for c in code if c in allowed)
    debug_print(code)
    return code


def find_matching_brackets(code):
    """
    Return sorted list of matching bracket index pairs in Brainfuck code.

    Raises SyntaxError on unmatched brackets.
    """
    pairs = []
    stack = []

    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)  # adds the position of the opening bracket on the stack 
        elif c == ']':
            if not stack:
                raise SyntaxError(f"Unmatched ']' at position {i}")
            open_index = stack.pop()  # pops the position of the last opening bracket from the stack
            pairs.append((open_index, i))  # collect pairs (open index from stack, and i is current closing bracket)

    if stack:
        raise SyntaxError(f"Unmatched '[' at position {stack.pop()}")

    # sort pairs by opening bracket index
    pairs.sort()

    return pairs


def find_closing_bracket(pairs, start_index):
    for open_idx, close_idx in pairs:
        if open_idx == start_index:
            return close_idx
    return None  # or raise an exception if not found


def execute_brainfuck(code, pairs):
    """
    Execute brainfuck code on the given memory and pointer.

    Todo:
        implement input or ','

    Note:
        looping by anything other than -1 is not supported.
    """
    global memory, pointer
    for index, char in enumerate(code):
        #debug_print(char)
        if char == '+':
            if memory[pointer] < BYTE_MAX:
                memory[pointer] += 1
        elif char == '-':
            if memory[pointer] > BYTE_MIN:
                memory[pointer] -= 1
        elif char == '>':
                if pointer + 1 >= MEMORY_SIZE:
                    raise IndexError(f"Pointer would go out of bounds: {pointer + 1}")
                pointer += 1
        elif char == '<':
                if pointer - 1 < 0:
                    raise IndexError(f"Pointer would go out of bounds: {pointer - 1}")
                pointer -= 1
        elif char == '[':
            end = find_closing_bracket(pairs, index)
            loopcode = code[index+1:end]
            #debug_print(loopcode)
            # listen here person unfortunate to read this, this code is fucked, but works, don't touch it.
            # probably buggy in edge cases but what are you gonna do refactor it? didn't think so.
            while memory[pointer] != 1:
                #debug_print(memory[:5])
                execute_brainfuck(loopcode, pairs)
                # red hot patch for looping by even numbers
                if memory[pointer] == 0:
                    break
        elif char == '.':
            print(chr(memory[pointer]), end="")


def debug_print(*args):
    """
    Prints messages only if DEBUG flag is True.
    Accepts any arguments like the built-in print().
    """
    if DEBUG:
        print(*args)


def run_interpreter(code):
    """
    Runs the brainfuck interpreter on clean code
    you have to provide clean brainfuck, use clean_brainfuck_code to remove whitespace and comments
    """
    global memory, pointer
    memory = [0] * MEMORY_SIZE
    pointer = 0

    pairs = find_matching_brackets(code)
    debug_print(pairs)

    execute_brainfuck(code, pairs)
    debug_print(memory[:5])


def run_brainfuck_from_file(filename):
    """
    Runs the brainfuck interpreter and code from file
    it reads file, cleans the brainfuck code of any whitespace, and runs it.
    """
    with open(filename, "r") as f:
        dirty_code = f.read()
    code = clean_brainfuck_code(dirty_code)
    run_interpreter(code)


def main():
    if DEBUG:
        filename = DEBUG_FILE
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
        if not filename.endswith(".bf"):
            filename += ".bf"
    else:
        filename = input("Enter path to .bf file: ").strip()
        if not filename.endswith(".bf"):
            filename += ".bf"

    with open(filename, "r") as f:
        dirty_code = f.read()

    code = clean_brainfuck_code(dirty_code)
    run_interpreter(code)


if __name__ == "__main__":
    main()
