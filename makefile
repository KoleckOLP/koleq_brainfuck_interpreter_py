PYTHON=python
TEST_FILE=unittest_brainfuck.py
MAIN_FILE=brainfuck

.PHONY: test run

test:
	$(PYTHON) -m unittest -v $(TEST_FILE)

run:
	$(PYTHON) $(MAIN_FILE).py

doc:
	$(PYTHON) -m pydoc $(MAIN_FILE) > doc.txt
