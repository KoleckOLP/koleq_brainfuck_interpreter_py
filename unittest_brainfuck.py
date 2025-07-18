import os
import unittest
import brainfuck

class TestBrainfuck(unittest.TestCase):

    # reset state
    def test000_reset_state(self):
        brainfuck.reset_state()
        correct_memory = [0] * 30000
        correct_pointer = 0
        self.assertEqual((brainfuck.memory, brainfuck.pointer), (correct_memory, correct_pointer))

    # clean brainfuck code
    def test001_clean_brainfuck_code(self):
        with open(f"examples{os.path.sep}one.bf", 'r') as f:
            dirty_code = f.read()
        code = brainfuck.clean_brainfuck_code(dirty_code)
        self.assertEqual(code, "++++[>++++++++++<-]>+++++++++.")

    # find matching brackets
    def test002_find_matching_brackets(self):
        code = "+[[>+<-][>++<-]]."
        pairs = brainfuck.find_matching_brackets(code)
        self.assertEqual(pairs, [(1, 15), (2, 7), (8, 14)])

    # find closing bracket
    def test003_find_closing_bracket(self):
        code = "+[[>+<-][>++<-]]."
        pairs = brainfuck.find_matching_brackets(code)
        closing_bracket = brainfuck.find_closing_bracket(pairs, 2)
        self.assertEqual(closing_bracket, 7)

    # region execute brainfuck
    def test004_addition_to_cell_zero(self):
        code = "+++>+++++[<+>-]<"  # 3 + 5 = 8 into cell[0]

        # reset memory and pointer
        brainfuck.reset_state()

        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        # executing brainfuck code
        brainfuck.execute_brainfuck(code, pairs)

        self.assertEqual(brainfuck.memory[0], 8)

    def test005_print_char_1(self):
        code = "++++[>++++++++++<-]>+++++++++."

        # reset memory and pointer
        brainfuck.reset_state()

        from contextlib import redirect_stdout
        import io
        f = io.StringIO()
        
        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        
        with redirect_stdout(f):
            # executing brainfuck code
            brainfuck.execute_brainfuck(code, pairs)
        self.assertEqual(f.getvalue().strip(), "1")

    def test006_hello_world_single_loop(self):
        code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."

        # reset memory and pointer
        brainfuck.reset_state()

        from contextlib import redirect_stdout
        import io
        f = io.StringIO()
        
        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        
        with redirect_stdout(f):
            # executing brainfuck code
            brainfuck.execute_brainfuck(code, pairs)
        self.assertEqual(f.getvalue().strip(), "Hello World!")

    def test007_hello_world_multiple_loops(self):
        code = ">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++."
        
        # reset memory and pointer
        brainfuck.reset_state()
        
        from contextlib import redirect_stdout
        import io
        f = io.StringIO()
        
        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        
        with redirect_stdout(f):
            # executing brainfuck code
            brainfuck.execute_brainfuck(code, pairs)
        self.assertEqual(f.getvalue().strip(), "Hello world!")

    def test008_looping_with_even_numebers(self):
        code = "++++++[>+<--]"  # adds 6 and loops by -2 until 0

        # reset memory and pointer
        brainfuck.reset_state()

        # you need to find bracket pairs before executing brainfuck.
        pairs = brainfuck.find_matching_brackets(code)
        # executing brainfuck code
        brainfuck.execute_brainfuck(code, pairs)

        self.assertEqual((brainfuck.memory[0], brainfuck.memory[1]), (0, 3))
    # endregion

    # run interpreter
    def test009_run_interpreter(self):
        code = "+++>+++++[<+>-]<"  # 3 + 5 = 8 into cell[0]
        brainfuck.run_interpreter(code)
        self.assertEqual(brainfuck.memory[0], 8)
        
    # run brainfuck from file
    def test010_run_brainfuck_from_file(self):
        brainfuck.run_brainfuck_from_file(f"examples{os.path.sep}addcell0.bf")
        self.assertEqual(brainfuck.memory[0], 8)

if __name__ == "__main__":
    unittest.main()
