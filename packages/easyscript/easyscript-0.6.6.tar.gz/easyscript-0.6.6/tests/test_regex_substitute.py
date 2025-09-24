"""
Tests for EasyScript regex substitute expressions

This module contains tests for the Perl-style substitute expressions using the ~ operator
with s/pattern/replacement/flags syntax.
"""

import unittest
import sys
import os

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript import EasyScriptEvaluator


class TestRegexSubstituteExpressions(unittest.TestCase):
    """Test Perl-style substitute expressions"""

    def setUp(self):
        self.evaluator = EasyScriptEvaluator()

    def test_basic_substitution(self):
        """Test basic substitution without flags"""
        test_cases = [
            # Simple replacement
            ('"hello world" ~ "s/world/universe/"', "hello universe"),
            ('"test string" ~ "s/test/demo/"', "demo string"),
            ('"abc def ghi" ~ "s/def/xyz/"', "abc xyz ghi"),

            # Replace first occurrence only (no 'g' flag)
            ('"test test test" ~ "s/test/demo/"', "demo test test"),

            # No match
            ('"hello world" ~ "s/xyz/abc/"', "hello world"),

            # Empty replacement
            ('"hello world" ~ "s/world//"', "hello "),
            ('"test123test" ~ "s/123//"', "testtest"),

            # Unquoted substitute expressions
            ('"hello world" ~ s/world/universe/', "hello universe"),
            ('"test string" ~ s/test/demo/', "demo string"),
            ('"test test test" ~ s/test/demo/', "demo test test"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_global_substitution(self):
        """Test global substitution with 'g' flag"""
        test_cases = [
            # Replace all occurrences (quoted)
            ('"test test test" ~ "s/test/demo/g"', "demo demo demo"),
            ('"abc abc abc" ~ "s/abc/xyz/g"', "xyz xyz xyz"),
            ('"hello hello world hello" ~ "s/hello/hi/g"', "hi hi world hi"),

            # Replace all occurrences (unquoted)
            ('"test test test" ~ s/test/demo/g', "demo demo demo"),
            ('"abc abc abc" ~ s/abc/xyz/g', "xyz xyz xyz"),
            ('"hello hello world hello" ~ s/hello/hi/g', "hi hi world hi"),

            # Mixed case
            ('"Test test TEST" ~ "s/test/demo/g"', "Test demo TEST"),  # Case sensitive
            ('"Test test TEST" ~ s/test/demo/g', "Test demo TEST"),  # Case sensitive
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_case_insensitive_substitution(self):
        """Test case-insensitive substitution with 'i' flag"""
        test_cases = [
            # Case insensitive matching
            ('"Hello WORLD" ~ "s/hello/hi/i"', "hi WORLD"),
            ('"Test test TEST" ~ "s/test/demo/i"', "demo test TEST"),  # Only first match
            ('"Test test TEST" ~ "s/test/demo/gi"', "demo demo demo"),  # All matches
            ('"ABC abc Abc" ~ "s/abc/xyz/gi"', "xyz xyz xyz"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_multiline_flag(self):
        """Test multiline flag 'm'"""
        test_cases = [
            # ^ and $ match line boundaries
            ('"line1\\nline2\\nline3" ~ "s/^line/LINE/m"', "LINE1\nline2\nline3"),
            ('"line1\\nline2\\nline3" ~ "s/^line/LINE/gm"', "LINE1\nLINE2\nLINE3"),
            ('"test\\nend" ~ "s/end$/END/m"', "test\nEND"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_dotall_flag(self):
        """Test dotall flag 's' (dot matches newline)"""
        test_cases = [
            # . matches newline characters
            ('"hello\\nworld" ~ "s/hello.world/hi universe/s"', "hi universe"),
            ('"start\\nmiddle\\nend" ~ "s/start.*end/replaced/s"', "replaced"),

            # Without 's' flag, . shouldn't match newline
            ('"hello\\nworld" ~ "s/hello.world/hi universe/"', "hello\nworld"),  # No match
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_combined_flags(self):
        """Test combinations of flags"""
        test_cases = [
            # Global + case insensitive
            ('"Test test TEST" ~ "s/test/demo/gi"', "demo demo demo"),

            # Global + multiline
            ('"line1\\nline2\\nline3" ~ "s/^line/LINE/gm"', "LINE1\nLINE2\nLINE3"),

            # Case insensitive + multiline (first occurrence only, no 'g' flag)
            ('"Test\\ntest\\nTEST" ~ "s/^test$/demo/im"', "demo\ntest\nTEST"),

            # All flags (with 's' flag, .* matches across newlines)
            ('"Test\\ntest line\\nTEST" ~ "s/test.*/demo/gims"', "demo"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_regex_groups(self):
        """Test regex groups and backreferences"""
        test_cases = [
            # Simple group reference
            ('"hello world" ~ "s/(hello) (world)/$2 $1/"', "world hello"),
            ('"John Doe" ~ "s/(\\w+) (\\w+)/$2, $1/"', "Doe, John"),

            # Multiple groups
            ('"2023-12-25" ~ "s/(\\d{4})-(\\d{2})-(\\d{2})/$3\\/$2\\/$1/"', "25/12/2023"),

            # Repeated groups
            ('"test123test" ~ "s/(test)(\\d+)(test)/$1_$2_$3/"', "test_123_test"),

            # Groups with global replacement
            ('"a1 b2 c3" ~ "s/(\\w)(\\d)/$1_$2/g"', "a_1 b_2 c_3"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_complex_patterns(self):
        """Test complex regex patterns"""
        test_cases = [
            # Word boundaries
            ('"testing test tested" ~ "s/\\btest\\b/exam/g"', "testing exam tested"),

            # Character classes
            ('"abc 123 xyz" ~ "s/[0-9]+/NUM/g"', "abc NUM xyz"),
            ('"Hello World!" ~ "s/[A-Z]/L/g"', "Lello Lorld!"),

            # Quantifiers
            ('"aaa bbb ccc" ~ "s/a+/X/g"', "X bbb ccc"),
            ('"test1 test22 test333" ~ "s/test\\d*/ITEM/g"', "ITEM ITEM ITEM"),

            # Non-greedy matching
            ('"<tag>content</tag>" ~ "s/<.*?>/[]/g"', "[]content[]"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_escaped_delimiters(self):
        """Test escaped delimiters in patterns and replacements"""
        test_cases = [
            # Escaped forward slash in pattern
            ('"http://example.com" ~ "s/http:\\/\\//https:\\/\\//"', "https://example.com"),

            # Escaped forward slash in replacement
            ('"test" ~ "s/test/path\\/to\\/file/"', "path/to/file"),

            # Both pattern and replacement with slashes
            ('"a/b" ~ "s/a\\/b/c\\/d/"', "c/d"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_error_cases(self):
        """Test error handling for invalid substitute expressions"""
        error_cases = [
            # Missing delimiters
            '"test" ~ "s/pattern"',
            '"test" ~ "s/pattern/"',
            '"test" ~ "spattern/replacement/"',

            # Invalid regex patterns
            '"test" ~ "s/[/replacement/"',  # Unclosed character class
            '"test" ~ "s/*/replacement/"',  # Nothing to repeat

            # Unknown flags
            '"test" ~ "s/pattern/replacement/x"',
            '"test" ~ "s/pattern/replacement/gix"',
        ]

        for expression in error_cases:
            with self.subTest(expression=expression):
                with self.assertRaises((ValueError, SyntaxError)):
                    self.evaluator.evaluate(expression)

    def test_mixed_regex_operations(self):
        """Test mixing regular regex matching with substitute expressions"""
        # Regular regex matching (returns boolean)
        result1 = self.evaluator.evaluate('"hello world" ~ "world"')
        self.assertTrue(result1)

        result2 = self.evaluator.evaluate('"hello world" ~ "xyz"')
        self.assertFalse(result2)

        # Substitute expressions (returns string)
        result3 = self.evaluator.evaluate('"hello world" ~ "s/world/universe/"')
        self.assertEqual(result3, "hello universe")

        # Ensure they can be used in the same context
        result4 = self.evaluator.evaluate('if "test" ~ "s/test/demo/" == "demo" then "success" else "failure"')
        self.assertEqual(result4, "success")

    def test_real_world_examples(self):
        """Test real-world usage examples"""
        test_cases = [
            # Email domain replacement
            ('"user@olddomain.com" ~ "s/@olddomain\\.com/@newdomain.com/"', "user@newdomain.com"),

            # Phone number formatting
            ('"1234567890" ~ "s/(\\d{3})(\\d{3})(\\d{4})/$1-$2-$3/"', "123-456-7890"),

            # Remove HTML tags
            ('"<p>Hello <b>world</b>!</p>" ~ "s/<[^>]*>//g"', "Hello world!"),

            # Convert camelCase to snake_case
            ('"camelCaseVariable" ~ "s/([a-z])([A-Z])/$1_$2/g"', "camel_Case_Variable"),

            # Clean whitespace
            ('"  hello   world  " ~ "s/^\\s+|\\s+$//g"', "hello   world"),  # Trim ends
            ('"hello    world" ~ "s/\\s+/ /g"', "hello world"),  # Normalize spaces
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)