"""
Tests for EasyScript REPL functionality

This module contains tests for the REPL (Read-Eval-Print Loop) interface.
"""

import unittest
import sys
import os
import subprocess
import io
from unittest.mock import patch, MagicMock

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript.repl import EasyScriptREPL


class TestEasyScriptREPL(unittest.TestCase):
    """Test the REPL functionality"""

    def setUp(self):
        self.repl = EasyScriptREPL()

    def test_repl_initialization(self):
        """Test REPL initializes properly"""
        self.assertIsNotNone(self.repl.evaluator)
        self.assertEqual(self.repl.variables, {})

    def test_format_result(self):
        """Test result formatting"""
        # Test None
        self.assertEqual(self.repl.format_result(None), "null")

        # Test booleans
        self.assertEqual(self.repl.format_result(True), "true")
        self.assertEqual(self.repl.format_result(False), "false")

        # Test strings
        self.assertEqual(self.repl.format_result("hello"), '"hello"')
        self.assertEqual(self.repl.format_result(""), '""')

        # Test numbers
        self.assertEqual(self.repl.format_result(42), "42")
        self.assertEqual(self.repl.format_result(3.14), "3.14")

        # Test lists
        self.assertEqual(self.repl.format_result([1, 2, 3]), "[1, 2, 3]")
        self.assertEqual(self.repl.format_result(["a", "b"]), '["a", "b"]')
        self.assertEqual(self.repl.format_result([]), "[]")

    def test_format_nested_list(self):
        """Test formatting of nested lists"""
        nested = [1, [2, 3], "test"]
        expected = '[1, [2, 3], "test"]'
        self.assertEqual(self.repl.format_result(nested), expected)

    @patch('builtins.print')
    def test_print_welcome(self, mock_print):
        """Test welcome message printing"""
        self.repl.print_welcome()

        # Check that print was called multiple times
        self.assertTrue(mock_print.called)
        calls = mock_print.call_args_list

        # Check for key content in the welcome message
        welcome_text = " ".join([str(call[0][0]) for call in calls if call[0]])
        self.assertIn("EasyScript REPL", welcome_text)
        self.assertIn("exit", welcome_text)

    @patch('builtins.print')
    def test_print_help(self, mock_print):
        """Test help message printing"""
        self.repl.print_help()

        # Check that print was called
        self.assertTrue(mock_print.called)
        calls = mock_print.call_args_list

        # Check for key content in the help message
        help_text = " ".join([str(call[0][0]) for call in calls if call[0]])
        self.assertIn("Commands", help_text)
        self.assertIn("exit", help_text)
        self.assertIn("help", help_text)
        self.assertIn("Arithmetic", help_text)

    @patch('builtins.print')
    def test_show_variables(self, mock_print):
        """Test showing variables"""
        self.repl.show_variables()

        # Check that print was called
        self.assertTrue(mock_print.called)
        calls = mock_print.call_args_list

        # Check for built-in variables
        vars_text = " ".join([str(call[0][0]) for call in calls if call[0]])
        self.assertIn("day", vars_text)
        self.assertIn("month", vars_text)
        self.assertIn("year", vars_text)

    def test_clear_variables(self):
        """Test clearing variables"""
        # Add some test variables
        self.repl.variables['test'] = 42
        self.assertEqual(len(self.repl.variables), 1)

        # Clear variables
        with patch('builtins.print') as mock_print:
            self.repl.clear_variables()

        # Check variables are cleared
        self.assertEqual(len(self.repl.variables), 0)
        mock_print.assert_called_with("Variables cleared")

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_basic_expressions(self, mock_print, mock_input):
        """Test REPL with basic expressions"""
        # Mock input sequence: expression, then exit
        mock_input.side_effect = ["5 + 3", "exit"]

        self.repl.run()

        # Check that the result was printed
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        results = [str(call[0][0]) for call in print_calls]

        # Should contain welcome message and result
        self.assertTrue(any("EasyScript REPL" in result for result in results))
        self.assertTrue(any("8" in result for result in results))

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_help_command(self, mock_print, mock_input):
        """Test REPL help command"""
        mock_input.side_effect = ["help", "exit"]

        self.repl.run()

        # Check that help was displayed
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        help_text = " ".join([str(call[0][0]) for call in print_calls])
        self.assertIn("Commands", help_text)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_vars_command(self, mock_print, mock_input):
        """Test REPL vars command"""
        mock_input.side_effect = ["vars", "exit"]

        self.repl.run()

        # Check that variables were displayed
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        vars_text = " ".join([str(call[0][0]) for call in print_calls])
        self.assertIn("Built-in variables", vars_text)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_clear_command(self, mock_print, mock_input):
        """Test REPL clear command"""
        mock_input.side_effect = ["clear", "exit"]

        self.repl.run()

        # Check that clear was executed
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        clear_text = " ".join([str(call[0][0]) for call in print_calls])
        self.assertIn("Variables cleared", clear_text)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_error_handling(self, mock_print, mock_input):
        """Test REPL error handling"""
        mock_input.side_effect = ["undefined_function()", "exit"]

        self.repl.run()

        # Check that error was displayed
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        error_text = " ".join([str(call[0][0]) for call in print_calls])
        self.assertIn("Error", error_text)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_empty_input(self, mock_print, mock_input):
        """Test REPL with empty input"""
        mock_input.side_effect = ["", "  ", "5 + 3", "exit"]

        self.repl.run()

        # Should handle empty input gracefully and still process valid input
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        results = [str(call[0][0]) for call in print_calls]
        self.assertTrue(any("8" in result for result in results))

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_keyboard_interrupt(self, mock_print, mock_input):
        """Test REPL keyboard interrupt handling"""
        mock_input.side_effect = KeyboardInterrupt()

        self.repl.run()

        # Should handle Ctrl+C gracefully
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        goodbye_text = " ".join([str(call[0][0]) for call in print_calls])
        self.assertIn("Goodbye", goodbye_text)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_repl_eof_handling(self, mock_print, mock_input):
        """Test REPL EOF handling"""
        mock_input.side_effect = EOFError()

        self.repl.run()

        # Should handle EOF gracefully
        print_calls = [call for call in mock_print.call_args_list if call[0]]
        goodbye_text = " ".join([str(call[0][0]) for call in print_calls])
        self.assertIn("Goodbye", goodbye_text)


class TestREPLIntegration(unittest.TestCase):
    """Integration tests for the REPL"""

    def test_repl_subprocess(self):
        """Test REPL through subprocess"""
        try:
            # Start REPL process
            proc = subprocess.Popen(
                [sys.executable, "-m", "easyscript"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            )

            # Send simple commands
            input_text = "5 + 3\nexit\n"
            stdout, stderr = proc.communicate(input=input_text, timeout=5)

            # Check output
            self.assertIn("EasyScript REPL", stdout)
            self.assertIn("8", stdout)
            self.assertEqual(proc.returncode, 0)

        except subprocess.TimeoutExpired:
            proc.kill()
            self.fail("REPL subprocess test timed out")
        except Exception as e:
            self.fail(f"REPL subprocess test failed: {e}")

    def test_cli_help(self):
        """Test CLI help message"""
        try:
            proc = subprocess.run(
                [sys.executable, "-m", "easyscript", "--help"],
                capture_output=True,
                text=True,
                timeout=5,
                cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            )

            self.assertIn("REPL", proc.stdout)
            self.assertIn("file", proc.stdout)
            self.assertEqual(proc.returncode, 0)

        except subprocess.TimeoutExpired:
            self.fail("CLI help test timed out")
        except Exception as e:
            self.fail(f"CLI help test failed: {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)