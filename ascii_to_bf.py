def text_to_bf_no_loops(text):
    bf_code = []

    for i, char in enumerate(text):
        ascii_val = ord(char)
        bf_code.append('+' * ascii_val)  # increment to ASCII
        bf_code.append('.')              # output
        if i != len(text) - 1:
            bf_code.append('>')          # move to next cell unless last char

    return ''.join(bf_code)

# Example usage
text = "Hello, World!"
bf_program = text_to_bf_no_loops(text)
print(bf_program)
