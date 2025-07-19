import os
import brainfuck

#reads brainfuck file
with open(f"examples{os.path.sep}hello1L.bf", 'r') as f:
    dirty_code = f.read()

# here you can paste your dirty code, if you don't want to read file (remove triple single quotes)
'''
dirty_code = """
paste your multiline code here!
"""
'''

print("dirty code: \n" + dirty_code)

code = brainfuck.clean_brainfuck_code(dirty_code)

# here you can paste clean code, if you don't want to read file or paste dirty code
code = "++++++++++[>++++++++++<-]>+." #"++++++[>+<--]"

print("\nclean code: " + code)

pairs = brainfuck.find_matching_brackets(code)

print("\nsquare bracket pairs: " + str(pairs))

# clears the memory "tape" and pointer
brainfuck.reset_state()

'''
index = brainfuck.last_nonzero_index(brainfuck.memory)

print("\nmemory before: " + str(brainfuck.memory[:index]))
'''

print("\nmemory before: ", end="")
brainfuck.print_memory(brainfuck.memory, brainfuck.pointer, "hex")
print("memory before: ", end="")
brainfuck.print_memory(brainfuck.memory, brainfuck.pointer, "dec")
print("memory before: ", end="")
brainfuck.print_memory(brainfuck.memory, brainfuck.pointer, "char")

print("\nbrainfuck output:")

# executes the code in the better engine
#brainfuck.chat_execute_brainfuck(code, pairs)

# executes the code in the worse engine
brainfuck.execute_brainfuck(code, pairs)

'''
index = brainfuck.last_nonzero_index(brainfuck.memory)
print("\n\nmemory after: " + str(brainfuck.memory[:index]))
'''

print("\n\nmemory after: ", end="")
brainfuck.print_memory(brainfuck.memory, brainfuck.pointer, "hex")
print("memory after: ", end="")
brainfuck.print_memory(brainfuck.memory, brainfuck.pointer, "dec")
print("memory after: ", end="")
brainfuck.print_memory(brainfuck.memory, brainfuck.pointer, "char")
