"""
Brainfuck Interpreter (Python 3)
Reads and executes Brainfuck code from a file, with optional debug printing.
"""
import sys

BYTE_MIN = 0
BYTE_MAX = 255
MEMORY_SIZE = 30000
MIN_INDEX = 5

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


# This is an improved version by ChatGPT (thx babe) this actually skips over loop that has been ran.
def chat_execute_brainfuck(code, pairs):
    global memory, pointer
    index = 0
    while index < len(code):
        char = code[index]
        if char == '+':
            if memory[pointer] < BYTE_MAX:
                memory[pointer] += 1
        elif char == '-':
            if memory[pointer] > BYTE_MIN:
                memory[pointer] -= 1
        elif char == '>':
            if pointer + 1 >= MEMORY_SIZE:
                raise IndexError(f"Pointer out of bounds: {pointer + 1}")
            pointer += 1
        elif char == '<':
            if pointer - 1 < 0:
                raise IndexError(f"Pointer out of bounds: {pointer - 1}")
            pointer -= 1
        elif char == '[':
            end = find_closing_bracket(pairs, index)
            loopcode = code[index+1:end]
            while memory[pointer] != 0:
                execute_brainfuck(loopcode, pairs)
            index = end  # Skip over the loop body after finishing
        elif char == '.':
            print(chr(memory[pointer]), end="")
        index += 1


# This is my version that is correct but goes over loop code after running it without running it when it's done looping.
def execute_brainfuck(code, pairs):
    """
    Execute brainfuck code on the given memory and pointer.

    Todo:
        implement input or ','
    """
    loop = False
    global memory, pointer
    for index, char in enumerate(code):
        if not loop:
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
                while memory[pointer] != 0:
                    execute_brainfuck(loopcode, pairs)
                    loop = True
            elif char == '.':
                print(chr(memory[pointer]), end="")
        else:
            if char == ']':
                loop = False


def run_interpreter(code):
    """
    Runs the brainfuck interpreter on clean code
    you have to provide clean brainfuck, use clean_brainfuck_code to remove whitespace and comments
    """
    global memory, pointer
    memory = [0] * MEMORY_SIZE
    pointer = 0

    pairs = find_matching_brackets(code)

    execute_brainfuck(code, pairs)


def run_brainfuck_from_file(filename):
    """
    Runs the brainfuck interpreter and code from file
    it reads file, cleans the brainfuck code of any whitespace, and runs it.
    """
    with open(filename, "r") as f:
        dirty_code = f.read()
    code = clean_brainfuck_code(dirty_code)
    run_interpreter(code)


def reset_state():
    global memory, pointer
    memory = [0] * MEMORY_SIZE
    pointer = 0


def last_nonzero_index(lst):
    """
    Returns the length to consider for the memory tape:
    - The index of last non-zero element + 1 (to count length),
    - or min_length if the last non-zero index is less than min_length - 1,
    - or min_length if all zeros.
    """
    for index in range(len(lst) - 1, -1, -1):
        if lst[index] != 0:
            return max(index + 1, MIN_INDEX)
    return MIN_INDEX


def print_memory(memory, pointer, fmt="dec"):
    """
    Prints the memory tape slice based on last non-zero index or min_index.
    fmt: 'dec', 'hex', or 'char' - output format
    pointer: current tape pointer (int)
    """
    length_to_show = last_nonzero_index(memory)
    visible = memory[:length_to_show]

    # Format cells according to fmt
    if fmt == "dec":
        formatted = [f"{c:4}" for c in visible]
    elif fmt == "hex":
        formatted = [f"0x{c:02X}" for c in visible]
    elif fmt == "char":
        def to_char(c):
            if 32 <= c <= 126:  # printable ASCII range
                return f" '{chr(c)}'"
            else:
                return " '.'"
        formatted = [to_char(c) for c in visible]
    else:
        raise ValueError("Invalid fmt: choose 'dec', 'hex', or 'char'")

    # Print in chunks of 10
    chunk_size = 10
    for i in range(0, length_to_show, chunk_size):
        chunk = formatted[i:i+chunk_size]
        line_str = " ".join(chunk)
        print(f"{line_str}")


def main():
    if len(sys.argv) > 1:
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
