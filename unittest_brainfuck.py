import unittest
import brainfuck

class TestBrainfuck(unittest.TestCase):

    # clean brainfuck code
    def test001_clean_brainfuck_code(self):
        dirty_code = "++++               ; in cell 0 add 4\n[                  ; loop until cell 0 = 0\n    > +++++ +++++  ; move to cell 1 and add 10\n    < -            ; move to cell 0 and remove 1\n]\n> +++++ ++++       ; add 9 to cell 1\n.                  ; print cell 1"
        code = brainfuck.clean_brainfuck_code(dirty_code)
        self.assertEqual(code, "++++[>++++++++++<-]>+++++++++.")

    # find matching brackets

    # find closint brackets

    # region execute brainfuck
    def test01_addition_to_cell_zero(self):
        code = "+++>+++++[<+>-]<"  # 3 + 5 = 8 into cell[0]

        # reset memory and pointer
        brainfuck.memory = [0] * brainfuck.MEMORY_SIZE
        brainfuck.pointer = 0

        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        # executing brainfuck code
        brainfuck.execute_brainfuck(code, pairs)

        self.assertEqual(brainfuck.memory[0], 8)

    def test02_print_char_1(self):
        code = "++++[>++++++++++<-]>+++++++++."

        # reset memory and pointer
        brainfuck.memory = [0] * brainfuck.MEMORY_SIZE
        brainfuck.pointer = 0

        from contextlib import redirect_stdout
        import io
        f = io.StringIO()
        
        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        
        with redirect_stdout(f):
            # executing brainfuck code
            brainfuck.execute_brainfuck(code, pairs)
        self.assertEqual(f.getvalue().strip(), "1")

    def test03_hello_world_single_loop(self):
        code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."

        # reset memory and pointer
        brainfuck.memory = [0] * brainfuck.MEMORY_SIZE
        brainfuck.pointer = 0

        from contextlib import redirect_stdout
        import io
        f = io.StringIO()
        
        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        
        with redirect_stdout(f):
            # executing brainfuck code
            brainfuck.execute_brainfuck(code, pairs)
        self.assertEqual(f.getvalue().strip(), "Hello World!")

    def test04_hello_world_multiple_loops(self):
        code = ">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++."
        
        # reset memory and pointer
        brainfuck.memory = [0] * brainfuck.MEMORY_SIZE
        brainfuck.pointer = 0
        
        from contextlib import redirect_stdout
        import io
        f = io.StringIO()
        
        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        
        with redirect_stdout(f):
            # executing brainfuck code
            brainfuck.execute_brainfuck(code, pairs)
        self.assertEqual(f.getvalue().strip(), "Hello world!")

    def test05_looping_with_even_numebers(self):
        code = "++++++[--]"  # adds 6 and loops by -2 until 0

        # reset memory and pointer
        brainfuck.memory = [0] * brainfuck.MEMORY_SIZE
        brainfuck.pointer = 0

        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        # executing brainfuck code
        brainfuck.execute_brainfuck(code, pairs)

        self.assertEqual(brainfuck.memory[0], 0)
    # endregion

    # run interpreter

    # run brainfuck from file

if __name__ == "__main__":
    unittest.main()
