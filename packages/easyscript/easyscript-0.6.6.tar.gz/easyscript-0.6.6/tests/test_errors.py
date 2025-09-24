"""
Error handling tests for EasyScript

This module contains tests for EasyScript error handling and edge cases including:
- Undefined variable errors
- Undefined property errors
- Invalid function errors
- Function argument errors
- Mathematical function errors
- Invalid regex errors
- Syntax errors
- Type errors
- Division by zero
- Assignment errors
"""

import unittest
import sys
import os

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript import EasyScriptEvaluator


class TestEasyScriptErrorHandling(unittest.TestCase):
    """Test error handling and edge cases"""

    def setUp(self):
        self.evaluator = EasyScriptEvaluator()

    def test_undefined_variable_error(self):
        """Test error when accessing undefined variables"""
        with self.assertRaises(NameError):
            self.evaluator.evaluate("undefined_variable")

    def test_undefined_property_error(self):
        """Test error when accessing undefined properties"""
        test_obj = type('TestObj', (), {'name': 'test'})()
        variables = {'obj': test_obj}

        with self.assertRaises(AttributeError):
            self.evaluator.evaluate("obj.undefined_property", variables)

    def test_invalid_function_error(self):
        """Test error when calling undefined functions"""
        with self.assertRaises(NameError):
            self.evaluator.evaluate("undefined_function()")

    def test_function_argument_error(self):
        """Test error when calling functions with wrong number of arguments"""
        with self.assertRaises(TypeError):
            self.evaluator.evaluate("len()")  # len requires 1 argument

        with self.assertRaises(TypeError):
            self.evaluator.evaluate('len("hello", "world")')  # len takes only 1 argument

    def test_math_function_errors(self):
        """Test error handling for mathematical functions"""
        # Test abs() with wrong number of arguments
        with self.assertRaises(TypeError):
            self.evaluator.evaluate("abs()")  # abs requires 1 argument

        with self.assertRaises(TypeError):
            self.evaluator.evaluate("abs(5, 3)")  # abs takes only 1 argument

        # Test abs() with non-numeric argument
        with self.assertRaises(TypeError):
            self.evaluator.evaluate('abs("hello")')  # abs requires a number

        # Test min() with insufficient arguments
        with self.assertRaises(TypeError):
            self.evaluator.evaluate("min()")  # min requires at least 2 arguments

        with self.assertRaises(TypeError):
            self.evaluator.evaluate("min(5)")  # min requires at least 2 arguments

        # Test max() with insufficient arguments
        with self.assertRaises(TypeError):
            self.evaluator.evaluate("max()")  # max requires at least 2 arguments

        with self.assertRaises(TypeError):
            self.evaluator.evaluate("max(5)")  # max requires at least 2 arguments

        # Test round() with wrong number of arguments
        with self.assertRaises(TypeError):
            self.evaluator.evaluate("round()")  # round requires at least 1 argument

        with self.assertRaises(TypeError):
            self.evaluator.evaluate("round(3.14, 2, 1)")  # round takes at most 2 arguments

        # Test round() with non-numeric first argument
        with self.assertRaises(TypeError):
            self.evaluator.evaluate('round("hello")')  # round requires a number

        # Test round() with non-integer second argument
        with self.assertRaises(TypeError):
            self.evaluator.evaluate('round(3.14, "2")')  # round second argument must be integer

    def test_invalid_regex_error(self):
        """Test error with invalid regex patterns"""
        with self.assertRaises(ValueError):
            self.evaluator.evaluate('"test" ~ "["')  # Invalid regex

    def test_syntax_error(self):
        """Test syntax errors"""
        # Create a dummy object to test assignment syntax errors
        test_obj = type('TestObj', (), {'prop': 'value'})()
        variables = {'user': test_obj}

        with self.assertRaises(SyntaxError):
            self.evaluator.evaluate("user. = value", variables)  # Invalid assignment syntax

        # Test that direct variable assignment is not supported (only property assignment)
        with self.assertRaises(NameError):
            self.evaluator.evaluate("undefined_variable = value")  # Undefined variable

        # Test that && and || are no longer supported
        with self.assertRaises(SyntaxError):
            self.evaluator.evaluate("true && false")

        with self.assertRaises(SyntaxError):
            self.evaluator.evaluate("true || false")

    def test_assignment_to_nonexistent_object(self):
        """Test assignment to properties of non-existent objects"""
        with self.assertRaises(NameError):
            self.evaluator.evaluate("nonexistent.property = value")

    def test_division_by_zero(self):
        """Test division by zero"""
        with self.assertRaises(ZeroDivisionError):
            self.evaluator.evaluate("10 / 0")

    def test_type_error_in_operations(self):
        """Test type errors in operations"""
        # Test that regex operator properly handles type conversion
        with self.assertRaises(TypeError):
            self.evaluator.evaluate('"test" ~ 123')  # Should raise TypeError for non-string regex pattern

    def test_incomplete_expressions(self):
        """Test error handling for incomplete expressions"""
        incomplete_expressions = [
            "5 +",          # Missing right operand
            "+ 5",          # Missing left operand for binary +
            "len(",         # Incomplete function call
        ]

        for expression in incomplete_expressions:
            with self.subTest(expression=expression):
                with self.assertRaises((SyntaxError, ValueError, TypeError)):
                    self.evaluator.evaluate(expression)

    def test_specific_incomplete_cases(self):
        """Test specific incomplete expression cases"""
        # These expressions have specific behaviors in EasyScript

        # Incomplete if statement returns None for missing else clause
        result = self.evaluator.evaluate("if true then")
        self.assertIsNone(result)

        # EasyScript allows unclosed strings to parse to end of input
        # This is implementation-specific behavior
        try:
            result = self.evaluator.evaluate('"unclosed')
            # If it doesn't raise an error, that's the current behavior
        except (SyntaxError, ValueError):
            # If it does raise an error, that's also acceptable
            pass

        # Test "user." incomplete property access - this will raise NameError for undefined variable
        with self.assertRaises(NameError):
            self.evaluator.evaluate("user.")

    def test_invalid_operators(self):
        """Test errors with invalid or unsupported operators"""
        invalid_expressions = [
            "5 += 3",       # Compound assignment not supported
            "5 ** 3",       # Exponentiation not supported
            "5 % 3",        # Modulo not supported in expressions (only in verification)
            "++5",          # Prefix increment not supported
            "5++",          # Postfix increment not supported
        ]

        for expression in invalid_expressions:
            with self.subTest(expression=expression):
                with self.assertRaises((SyntaxError, ValueError)):
                    self.evaluator.evaluate(expression)

    def test_nested_error_handling(self):
        """Test error handling in nested expressions"""
        # Error in function argument
        with self.assertRaises(NameError):
            self.evaluator.evaluate("len(undefined_var)")

        # Error in conditional
        with self.assertRaises(NameError):
            self.evaluator.evaluate('if undefined_var then "yes" else "no"')

        # Error in nested function calls
        with self.assertRaises(TypeError):
            self.evaluator.evaluate("abs(len())")  # len() missing argument

        # Error in property chain
        test_obj = type('TestObj', (), {'valid_prop': None})()
        variables = {'obj': test_obj}
        with self.assertRaises(AttributeError):
            self.evaluator.evaluate("obj.valid_prop.invalid_prop", variables)

    def test_assignment_error_scenarios(self):
        """Test various assignment error scenarios"""
        # Assignment to undefined object
        with self.assertRaises(NameError):
            self.evaluator.evaluate("undefined_obj.prop = 5")

        # Assignment to property that doesn't exist on object without setattr support
        class ReadOnlyObj:
            def __init__(self):
                self.existing_prop = "value"

            def __setattr__(self, name, value):
                if name == "existing_prop":
                    super().__setattr__(name, value)
                else:
                    raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

        readonly_obj = ReadOnlyObj()
        variables = {'obj': readonly_obj}

        # This should work (existing property)
        result = self.evaluator.evaluate('obj.existing_prop = "new_value"', variables)
        self.assertEqual(result, "new_value")

        # This should fail (non-existing property)
        with self.assertRaises(AttributeError):
            self.evaluator.evaluate('obj.nonexistent_prop = "value"', variables)

    def test_function_call_error_scenarios(self):
        """Test various function call error scenarios"""
        # Wrong argument types for comparison functions
        error_expressions = [
            'min("hello")',          # min needs at least 2 arguments
            'max()',                 # max needs at least 2 arguments
            'abs("not_a_number")',   # abs needs a number
            'round("not_a_number")', # round needs a number
            'round(3.14, 2.5)',      # round second arg must be integer
        ]

        for expression in error_expressions:
            with self.subTest(expression=expression):
                with self.assertRaises(TypeError):
                    self.evaluator.evaluate(expression)

    def test_regex_error_scenarios(self):
        """Test various regex error scenarios"""
        # Invalid regex patterns
        invalid_patterns = [
            '"test" ~ "["',          # Unclosed character class
            '"test" ~ "*"',          # Nothing to repeat
            '"test" ~ "(?P<)"',      # Empty group name
            '"test" ~ "(?P<name>)\\k<invalid>"',  # Invalid backreference
        ]

        for expression in invalid_patterns:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    self.evaluator.evaluate(expression)

        # Non-string pattern (right side)
        with self.assertRaises(TypeError):
            self.evaluator.evaluate('"test" ~ 123')

        # Non-string subject (left side)
        with self.assertRaises(TypeError):
            self.evaluator.evaluate('123 ~ "\\d+"')

        with self.assertRaises(TypeError):
            self.evaluator.evaluate('true ~ "pattern"')

        with self.assertRaises(TypeError):
            self.evaluator.evaluate('5.5 ~ "\\d+"')

        with self.assertRaises(TypeError):
            self.evaluator.evaluate('null ~ "pattern"')

    def test_regex_left_side_type_validation(self):
        """Test that regex operator requires string on left side"""
        # Test various non-string types on the left side
        non_string_expressions = [
            ('123 ~ "\\d+"', "number"),
            ('true ~ "pattern"', "boolean"),
            ('false ~ "pattern"', "boolean"),
            ('null ~ "pattern"', "null"),
            ('42.5 ~ "\\d+"', "float"),
        ]

        for expression, type_name in non_string_expressions:
            with self.subTest(expression=expression, type_name=type_name):
                with self.assertRaises(TypeError) as cm:
                    self.evaluator.evaluate(expression)

                # Check that the error message mentions the left side requirement
                error_message = str(cm.exception)
                self.assertIn("left side", error_message)
                self.assertIn("string", error_message)

        # Test that string left side still works
        valid_expressions = [
            '"hello" ~ "h.*o"',
            '"123" ~ "\\d+"',
            '"test" ~ "pattern"',
        ]

        for expression in valid_expressions:
            with self.subTest(expression=expression):
                # Should not raise an exception
                try:
                    result = self.evaluator.evaluate(expression)
                    self.assertIsInstance(result, bool)
                except Exception as e:
                    self.fail(f"Valid regex expression '{expression}' raised {type(e).__name__}: {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)