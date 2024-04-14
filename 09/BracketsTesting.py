
''' Jesse Higgins
    CS5001
    Test case for Stack Bracket Application
'''

from Brackets import brackets
import unittest
from unittest.mock import patch
from io import StringIO

class TestBracketsFunction(unittest.TestCase):
    @patch('builtins.input', return_value='[]{}()')

    def test_valid_brackets(self, mock_input):
        expected_output = "pop() returned -- [\npop() returned -- {\npop() returned -- (\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            brackets()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value='({])')

    def test_invalid_brackets(self, mock_input):
        expected_output = "invalid string\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            brackets()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value='')

    def test_empty_brackets(self, mock_input):
        expected_output = "invalid string\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            brackets()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

def main():

    unittest.main()
if __name__ == "__main__":
    main()