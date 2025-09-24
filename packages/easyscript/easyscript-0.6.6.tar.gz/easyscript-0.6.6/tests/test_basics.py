"""
Basic functionality tests for EasyScript

This module contains tests for core EasyScript functionality including:
- Arithmetic operations
- String operations
- Comparison operations
- Boolean operations
- Built-in variables and functions
- Conditional statements
- Complex expressions
"""

import unittest
import sys
import os
import io
import contextlib

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript import EasyScriptEvaluator


class TestEasyScriptBasics(unittest.TestCase):
    """Test basic EasyScript functionality"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.evaluator = EasyScriptEvaluator()

    def test_arithmetic_operations(self):
        """Test basic arithmetic operations"""
        test_cases = [
            ("3+3", 6),
            ("10-4", 6),
            ("2*3", 6),
            ("12/2", 6.0),
            ("2 + 3 * 4", 14),  # Order of operations
            ("(2 + 3) * 4", 20),  # Parentheses
            ("10 / 2 + 3", 8.0),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_string_operations(self):
        """Test string operations and concatenation"""
        test_cases = [
            ('"hello" + "world"', "helloworld"),
            ('"hello" + 123', "hello123"),
            ('123 + "world"', "123world"),
            ('"hello " + "world"', "hello world"),
            ('"Value: " + 42', "Value: 42"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_comparison_operations(self):
        """Test comparison operations"""
        test_cases = [
            ("5 > 3", True),
            ("3 > 5", False),
            ("5 >= 5", True),
            ("4 >= 5", False),
            ("3 < 5", True),
            ("5 < 3", False),
            ("5 <= 5", True),
            ("6 <= 5", False),
            ("5 == 5", True),
            ("5 == 3", False),
            ("5 != 3", True),
            ("5 != 5", False),
            ('"hello" == "hello"', True),
            ('"hello" == "world"', False),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_boolean_operations(self):
        """Test boolean operations"""
        test_cases = [
            ("true", True),
            ("false", False),
            ("True", True),
            ("False", False),
            ("null", None),  # Test null keyword
            ("true and true", True),
            ("true and false", False),
            ("false and true", False),
            ("false and false", False),
            ("true or true", True),
            ("true or false", True),
            ("false or true", True),
            ("false or false", False),
            # Test with null
            ("null and true", None),
            ("null or true", True),
            ("true and null", None),
            ("null or false", False),
            # Test not operator
            ("not true", False),
            ("not false", True),
            ("not True", False),
            ("not False", True),
            ("not null", True),
            # Test not with expressions
            ("not (3 > 5)", True),
            ("not (5 > 3)", False),
            # Test double not
            ("not not true", True),
            ("not not false", False),
            ("not not null", False),
            # Test not with other operators (precedence)
            ("not true and false", False),  # Should be (not true) and false
            ("not true or false", False),   # Should be (not true) or false
            ("true and not false", True),   # Should be true and (not false)
            ("not (true and false)", True), # Should be not (true and false)
            ("not (true or false)", False), # Should be not (true or false)
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_not_operator_with_data_types(self):
        """Test not operator with different data types"""
        test_cases = [
            # Numbers (0 is falsy, non-zero is truthy)
            ("not 0", True),
            ("not 1", False),
            ("not -1", False),
            ("not 42", False),
            ("not 0.0", True),
            ("not 3.14", False),
            # Strings (empty string is falsy, non-empty is truthy)
            ('not ""', True),
            ('not "hello"', False),
            ('not " "', False),  # Space is not empty
            # Null value (null is falsy)
            ("not null", True),
            ("null", None),  # Test that null evaluates to None
            # Complex expressions
            ("not (5 - 5)", True),   # 5 - 5 = 0, which is falsy
            ("not (3 + 2)", False),  # 3 + 2 = 5, which is truthy
            ('not len("")', True),   # len("") = 0, which is falsy
            ('not len("hi")', False), # len("hi") = 2, which is truthy
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_builtin_variables(self):
        """Test built-in variables"""
        import datetime
        now = datetime.datetime.now()

        self.assertEqual(self.evaluator.evaluate("day"), now.day)
        self.assertEqual(self.evaluator.evaluate("month"), now.month)
        self.assertEqual(self.evaluator.evaluate("year"), now.year)

        # Test using variables in expressions
        self.assertEqual(self.evaluator.evaluate("day + 0"), now.day)
        self.assertEqual(self.evaluator.evaluate("month * 1"), now.month)

    def test_builtin_functions(self):
        """Test built-in functions"""
        # Test len function
        test_cases = [
            ('len("hello")', 5),
            ('len("test")', 4),
            ('len("")', 0),
            ('len("unicode: 🎉")', 10),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_math_functions(self):
        """Test mathematical functions"""
        # Test abs function
        test_cases = [
            ('abs(5)', 5),
            ('abs(-5)', 5),
            ('abs(0)', 0),
            ('abs(3.14)', 3.14),
            ('abs(-3.14)', 3.14),
            ('abs(-0.5)', 0.5),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

        # Test min function
        min_test_cases = [
            ('min(5, 3)', 3),
            ('min(10, 20)', 10),
            ('min(-5, -10)', -10),
            ('min(3.14, 2.71)', 2.71),
            ('min(5, 3, 8, 1)', 1),
            ('min(10, 5, 15, 2, 8)', 2),
            ('min("apple", "banana")', "apple"),  # String comparison
        ]

        for expression, expected in min_test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

        # Test max function
        max_test_cases = [
            ('max(5, 3)', 5),
            ('max(10, 20)', 20),
            ('max(-5, -10)', -5),
            ('max(3.14, 2.71)', 3.14),
            ('max(5, 3, 8, 1)', 8),
            ('max(10, 5, 15, 2, 8)', 15),
            ('max("apple", "banana")', "banana"),  # String comparison
        ]

        for expression, expected in max_test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

        # Test round function
        round_test_cases = [
            ('round(3.14)', 3),
            ('round(3.6)', 4),
            ('round(3.5)', 4),  # Python's banker's rounding
            ('round(2.5)', 2),  # Python's banker's rounding
            ('round(-3.14)', -3),
            ('round(-3.6)', -4),
            ('round(3.14159, 2)', 3.14),
            ('round(3.14159, 3)', 3.142),
            ('round(123.456, 1)', 123.5),
            ('round(123.456, 0)', 123),
            ('round(123.456, -1)', 120),  # Round to nearest 10
        ]

        for expression, expected in round_test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_random_function(self):
        """Test random() built-in with 0,1,2 args and error cases"""
        import random as py_random

        # No-arg deterministic test by seeding
        py_random.seed(1)
        expected = py_random.random()
        py_random.seed(1)
        result = self.evaluator.evaluate('random()')
        self.assertEqual(result, expected)

        # Single-arg upper bound
        py_random.seed(2)
        expected = py_random.random() * 10
        py_random.seed(2)
        result = self.evaluator.evaluate('random(10)')
        self.assertEqual(result, expected)

        # Two-arg lower and upper
        py_random.seed(3)
        r = py_random.random()
        expected = 5 + r * (10 - 5)
        py_random.seed(3)
        result = self.evaluator.evaluate('random(5, 10)')
        self.assertEqual(result, expected)

        # Type errors
        with self.assertRaises(TypeError):
            self.evaluator.evaluate('random("a")')

        with self.assertRaises(TypeError):
            self.evaluator.evaluate('random(1, "b")')

    def test_log_function(self):
        """Test log function (capture output)"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = self.evaluator.evaluate('log("test message")')

        output = f.getvalue().strip()
        self.assertEqual(output, "test message")
        self.assertEqual(result, "test message")  # log returns the value

    def test_regex_operator(self):
        """Test regex matching operator"""
        test_cases = [
            ('"hello" ~ "h.*o"', True),
            ('"hello" ~ "x.*"', False),
            ('"test123" ~ "[0-9]+"', True),
            ('"test" ~ "[0-9]+"', False),
            ('"abc" ~ "^[a-c]*$"', True),
            ('"xyz" ~ "^[a-c]*$"', False),
            ('"email@domain.com" ~ ".*@.*"', True),
            ('"invalid-email" ~ ".*@.*"', False),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_conditional_statements(self):
        """Test if statements"""
        test_cases = [
            ('if true then "yes" else null', "yes"),
            ('if false then "yes" else null', None),
            ('if null then "yes" else null', None),  # null is falsy
            ('if 5 > 3 then "greater" else null', "greater"),
            ('if 3 > 5 then "greater" else null', None),
            ('if true then "returned" else null', "returned"),
            ('if len("hello") > 3 then "long" else null', "long"),
            ('if len("hi") > 3 then "long" else null', None),
            # Test with null in conditions
            ('if not null then "not null" else null', "not null"),
            ('if null or true then "truthy" else null', "truthy"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_complex_expressions(self):
        """Test complex nested expressions"""
        test_cases = [
            ('if 3 > 1 and len("hello") > 3 then True else False', True),
            ('if (5 + 3) > 6 and "test" ~ "t.*" then "match" else "no match"', "match"),
            ('"Result: " + (2 * 3 + 4)', "Result: 10"),
            ('len("hello") + len("world")', 10),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)


class TestEasyScriptEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""

    def setUp(self):
        self.evaluator = EasyScriptEvaluator()

    def test_empty_string(self):
        """Test operations with empty strings"""
        self.assertEqual(self.evaluator.evaluate('""'), "")
        self.assertEqual(self.evaluator.evaluate('len("")'), 0)
        self.assertEqual(self.evaluator.evaluate('"" + "hello"'), "hello")

    def test_zero_values(self):
        """Test operations with zero"""
        self.assertEqual(self.evaluator.evaluate("0"), 0)
        self.assertEqual(self.evaluator.evaluate("0 + 5"), 5)
        self.assertEqual(self.evaluator.evaluate("0 * 100"), 0)

    def test_whitespace_handling(self):
        """Test expressions with various whitespace"""
        test_cases = [
            ("  3  +  3  ", 6),
            ("\t5\t>\t3\t", True),
            ("\n\"hello\"\n", "hello"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=repr(expression)):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_nested_parentheses(self):
        """Test deeply nested expressions"""
        test_cases = [
            ("((3 + 2) * (4 - 1))", 15),
            ("(((5)))", 5),
            ('(("hello" + "world"))', "helloworld"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_boolean_edge_cases(self):
        """Test boolean edge cases"""
        # Test truthy/falsy behavior
        self.assertEqual(self.evaluator.evaluate("true and true and true"), True)
        self.assertEqual(self.evaluator.evaluate("false or false or false"), False)
        self.assertEqual(self.evaluator.evaluate("true and false or true"), True)

    def test_string_with_special_characters(self):
        """Test strings with special characters"""
        test_cases = [
            ('"hello\tworld"', "hello\tworld"),
            ('"line1\nline2"', "line1\nline2"),
            ('"quote: \'"', 'quote: \''),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(self.evaluator.evaluate("1000000 + 1"), 1000001)
        self.assertEqual(self.evaluator.evaluate("999999999 * 1"), 999999999)

    def test_float_precision(self):
        """Test floating point operations"""
        result = self.evaluator.evaluate("0.1 + 0.2")
        self.assertAlmostEqual(result, 0.3, places=10)


if __name__ == '__main__':
    unittest.main(verbosity=2)