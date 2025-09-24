"""
Slice operation tests for EasyScript

This module contains tests for EasyScript slice operator functionality including:
- String slicing operations
- List slicing operations
- Complex slice expressions with variables
- Chained operations with slicing
- Slice error handling
"""

import unittest
import sys
import os

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript import EasyScriptEvaluator


class TestSliceOperations(unittest.TestCase):
    """Test slice operator functionality"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.evaluator = EasyScriptEvaluator()

    def test_string_slicing(self):
        """Test string slicing operations"""
        test_string = "hello world"
        variables = {"text": test_string}

        test_cases = [
            # Basic indexing
            ("text[0]", "h"),
            ("text[1]", "e"),
            ("text[-1]", "d"),
            ("text[6]", "w"),

            # Slice with start and end
            ("text[0:5]", "hello"),
            ("text[6:11]", "world"),
            ("text[1:4]", "ell"),
            ("text[0:2]", "he"),
            ("text[1:-1]", "ello worl"),  # From index 1 to second-to-last

            # Slice with no start ([:end])
            ("text[:5]", "hello"),
            ("text[:2]", "he"),
            ("text[:0]", ""),

            # Slice with no end ([start:])
            ("text[6:]", "world"),
            ("text[1:]", "ello world"),
            ("text[0:]", "hello world"),

            # Full slice
            ("text[:]", "hello world"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_list_slicing(self):
        """Test list slicing operations"""
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        variables = {"numbers": test_list}

        test_cases = [
            # Basic indexing
            ("numbers[0]", 1),
            ("numbers[4]", 5),
            ("numbers[-1]", 10),
            ("numbers[9]", 10),

            # Slice with start and end
            ("numbers[0:3]", [1, 2, 3]),
            ("numbers[2:5]", [3, 4, 5]),
            ("numbers[1:4]", [2, 3, 4]),
            ("numbers[1:-1]", [2, 3, 4, 5, 6, 7, 8, 9]),  # From index 1 to second-to-last

            # Slice with no start ([:end])
            ("numbers[:3]", [1, 2, 3]),
            ("numbers[:5]", [1, 2, 3, 4, 5]),
            ("numbers[:0]", []),

            # Slice with no end ([start:])
            ("numbers[7:]", [8, 9, 10]),
            ("numbers[3:]", [4, 5, 6, 7, 8, 9, 10]),
            ("numbers[0:]", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),

            # Full slice
            ("numbers[:]", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_complex_slice_expressions(self):
        """Test slicing with complex expressions for indices"""
        variables = {
            "text": "programming",
            "numbers": [10, 20, 30, 40, 50],
            "start": 2,
            "end": 7,
            "index": 3
        }

        test_cases = [
            # Using variables as indices
            ("text[start]", "o"),
            ("text[start:end]", "ogram"),
            ("text[:end]", "program"),
            ("text[start:]", "ogramming"),
            ("numbers[index]", 40),
            ("numbers[start:end]", [30, 40, 50]),

            # Using expressions as indices
            ("text[1+1]", "o"),  # text[2]
            ("text[start*2:end+1]", "ramm"),  # text[4:8]
            ("numbers[index-1]", 30),  # numbers[2]
            ("numbers[1:end-4]", [20, 30]),  # numbers[1:3]
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_chained_operations(self):
        """Test slicing combined with other operations"""
        variables = {
            "words": ["hello", "world", "python", "programming"],
            "text": "EasyScript"
        }

        test_cases = [
            # Length of slice
            ('len(text[2:6])', 4),  # len("yScr")
            ('len(words[:2])', 2),  # len(["hello", "world"])

            # Slice of slice (chained slicing)
            ('text[1:8][2:5]', "ySc"),  # "asyScri"[2:5]
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_slice_error_handling(self):
        """Test error handling for slice operations"""
        variables = {"text": "hello", "numbers": [1, 2, 3]}

        # Test cases that should raise errors
        error_cases = [
            ("text[", SyntaxError),  # Incomplete syntax
            ("text[1", SyntaxError),  # Missing closing bracket
            ("5[0]", TypeError),  # Cannot index numbers
        ]

        for expression, expected_error in error_cases:
            with self.subTest(expression=expression):
                with self.assertRaises(expected_error):
                    self.evaluator.evaluate(expression, variables)

    def test_slice_with_math_functions(self):
        """Test slicing with mathematical functions"""
        variables = {
            "data": [10, -5, 23, -8, 15, 7, -12, 20],
            "text": "abcdefghijklmnop"
        }

        test_cases = [
            # Use math functions to determine slice bounds
            ('data[abs(-2):abs(-6)]', [23, -8, 15, 7]),  # data[2:6]
            ('data[min(1, 3):max(5, 3)]', [-5, 23, -8, 15]),  # data[1:5]
            ('text[round(2.7):round(7.2)]', "defg"),  # text[3:7]

            # Apply math functions to individual sliced elements
            ('abs(data[3])', 8),  # abs(-8) = 8
            ('data[2]', 23),  # data[2] = 23
            ('round(len(text[5:10]) / 2.0)', 2),  # round(5 / 2.0) = round(2.5) = 2
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_slice_in_conditionals(self):
        """Test slice operations in conditional expressions"""
        variables = {
            "message": "Hello, World!",
            "scores": [85, 92, 78, 96, 88],
            "threshold": 90
        }

        test_cases = [
            # Use slices in conditions
            ('if len(message[0:5]) == 5 then "correct" else "wrong"', "correct"),
            ('if message[:5] == "Hello" then "greeting" else "other"', "greeting"),
            ('if scores[1] > threshold then "high" else "low"', "high"),  # scores[1] = 92 > 90
            ('if scores[2] < 80 then "low_found" else "all_high"', "low_found"),  # scores[2] = 78 < 80

            # Conditional slicing
            ('if len(message) > 10 then message[:10] else message', "Hello, Wor"),
            ('if scores[0] > threshold then scores[1:] else scores[:4]', [85, 92, 78, 96]),  # 85 <= 90, so scores[:4]
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_slice_with_regex(self):
        """Test slice operations combined with regex matching"""
        variables = {
            "emails": ["user@domain.com", "invalid-email", "admin@site.org", "test@company.net"],
            "text": "The quick brown fox jumps over the lazy dog"
        }

        test_cases = [
            # Check if slice matches pattern
            ('text[0:3] ~ "^The$"', True),  # "The" matches "^The$"
            ('text[4:9] ~ "qu.*k"', True),  # "quick" matches "qu.*k"
            ('text[-3:] ~ "dog"', True),   # "dog" matches "dog"

            # Use regex on array elements via slicing
            ('emails[0] ~ ".*@.*\\.(com|org)$"', True),  # user@domain.com matches
            ('emails[2] ~ ".*@.*\\.(com|org)$"', True),  # admin@site.org matches
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_edge_cases_slicing(self):
        """Test edge cases for slice operations"""
        variables = {
            "empty_list": [],
            "empty_string": "",
            "single_char": "a",
            "single_item": [42]
        }

        test_cases = [
            # Empty containers
            ('len(empty_list[:])', 0),
            ('len(empty_string[:])', 0),

            # Single element containers
            ('single_char[0]', "a"),
            ('single_char[:]', "a"),
            ('single_item[0]', 42),
            ('single_item[:]', [42]),

            # Out of bounds handling (should work with Python's slice behavior)
            ('single_char[:10]', "a"),  # Beyond end
            ('single_item[:10]', [42]),  # Beyond end
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)