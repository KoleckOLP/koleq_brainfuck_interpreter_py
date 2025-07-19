code = "++++++++++[>++++++++++<-]>+."
tape = [0]*30000
p = 0
i = 0
while i < len(code):
    c = code[i]
    if c == '>': p += 1
    elif c == '<': p -= 1
    elif c == '+': tape[p] = (tape[p] + 1) % 256
    elif c == '-': tape[p] = (tape[p] - 1) % 256
    elif c == '.': print(chr(tape[p]), end='')
    elif c == ',': tape[p] = ord(input()[0])
    elif c == '[' and tape[p] == 0:
        open = 1
        while open:
            i += 1
            if code[i] == '[': open += 1
            elif code[i] == ']': open -= 1
    elif c == ']' and tape[p] != 0:
        close = 1
        while close:
            i -= 1
            if code[i] == ']': close += 1
            elif code[i] == '[': close -= 1
    i += 1