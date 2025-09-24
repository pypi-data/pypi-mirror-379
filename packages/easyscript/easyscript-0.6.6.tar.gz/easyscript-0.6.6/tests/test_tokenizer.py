"""
Tokenizer tests for EasyScript

This module contains tests for the EasyScript tokenizer functionality including:
- Number tokenization
- String tokenization
- Identifier tokenization
- Keyword tokenization
- Operator tokenization
- Punctuation tokenization
"""

import unittest
import sys
import os

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript import EasyScriptEvaluator
from easyscript.easyscript import TokenType


class TestEasyScriptTokenizer(unittest.TestCase):
    """Test the tokenizer functionality"""

    def setUp(self):
        self.evaluator = EasyScriptEvaluator()

    def test_number_tokenization(self):
        """Test tokenization of numbers"""
        tokens = self.evaluator.tokenize("123 45.67 0")

        # Filter out EOF token
        number_tokens = [t for t in tokens if t.type == TokenType.NUMBER]

        self.assertEqual(len(number_tokens), 3)
        self.assertEqual(number_tokens[0].value, 123)
        self.assertEqual(number_tokens[1].value, 45.67)
        self.assertEqual(number_tokens[2].value, 0)

    def test_string_tokenization(self):
        """Test tokenization of strings"""
        tokens = self.evaluator.tokenize('"hello" "world with spaces" ""')

        string_tokens = [t for t in tokens if t.type == TokenType.STRING]

        self.assertEqual(len(string_tokens), 3)
        self.assertEqual(string_tokens[0].value, "hello")
        self.assertEqual(string_tokens[1].value, "world with spaces")
        self.assertEqual(string_tokens[2].value, "")

    def test_identifier_tokenization(self):
        """Test tokenization of identifiers"""
        tokens = self.evaluator.tokenize("variable user_name test123 _private")

        identifier_tokens = [t for t in tokens if t.type == TokenType.IDENTIFIER]

        self.assertEqual(len(identifier_tokens), 4)
        self.assertEqual(identifier_tokens[0].value, "variable")
        self.assertEqual(identifier_tokens[1].value, "user_name")
        self.assertEqual(identifier_tokens[2].value, "test123")
        self.assertEqual(identifier_tokens[3].value, "_private")

    def test_keyword_tokenization(self):
        """Test tokenization of keywords"""
        tokens = self.evaluator.tokenize("if and or not True False true false")

        keyword_tokens = [t for t in tokens if t.type == TokenType.KEYWORD]

        expected_keywords = ["if", "and", "or", "not", "True", "False", "true", "false"]
        actual_keywords = [t.value for t in keyword_tokens]

        self.assertEqual(actual_keywords, expected_keywords)

    def test_operator_tokenization(self):
        """Test tokenization of operators"""
        tokens = self.evaluator.tokenize("+ - * / > < >= <= == != ~ =")

        operator_tokens = [t for t in tokens if t.type == TokenType.OPERATOR]

        expected_operators = ["+", "-", "*", "/", ">", "<", ">=", "<=", "==", "!=", "~", "="]
        actual_operators = [t.value for t in operator_tokens]

        self.assertEqual(actual_operators, expected_operators)

    def test_punctuation_tokenization(self):
        """Test tokenization of punctuation"""
        tokens = self.evaluator.tokenize("( ) : , .")

        punct_tokens = [t for t in tokens if t.type in [TokenType.LPAREN, TokenType.RPAREN,
                                                        TokenType.COLON, TokenType.COMMA, TokenType.DOT]]

        expected_types = [TokenType.LPAREN, TokenType.RPAREN, TokenType.COLON, TokenType.COMMA, TokenType.DOT]
        actual_types = [t.type for t in punct_tokens]

        self.assertEqual(actual_types, expected_types)

    def test_mixed_tokenization(self):
        """Test tokenization of mixed expressions"""
        tokens = self.evaluator.tokenize('if user.age > 18 then "adult" else "minor"')

        # Check that we get the expected token types in sequence
        expected_sequence = [
            TokenType.KEYWORD,     # if
            TokenType.IDENTIFIER,  # user
            TokenType.DOT,         # .
            TokenType.IDENTIFIER,  # age
            TokenType.OPERATOR,    # >
            TokenType.NUMBER,      # 18
            TokenType.KEYWORD,     # then
            TokenType.STRING,      # "adult"
            TokenType.KEYWORD,     # else
            TokenType.STRING,      # "minor"
            TokenType.EOF          # EOF
        ]

        actual_sequence = [t.type for t in tokens]
        self.assertEqual(actual_sequence, expected_sequence)

    def test_special_characters_in_strings(self):
        """Test tokenization of strings with special characters"""
        tokens = self.evaluator.tokenize(r'"hello\nworld" "tab\there" "quote\"inside"')

        string_tokens = [t for t in tokens if t.type == TokenType.STRING]

        self.assertEqual(len(string_tokens), 3)
        self.assertEqual(string_tokens[0].value, "hello\nworld")
        self.assertEqual(string_tokens[1].value, "tab\there")
        self.assertEqual(string_tokens[2].value, 'quote"inside')

    def test_comments_handling(self):
        """Test that comments are properly ignored during tokenization"""
        # Python-style comments
        tokens1 = self.evaluator.tokenize("5 + 3 # This is a comment")
        non_eof_tokens1 = [t for t in tokens1 if t.type != TokenType.EOF]
        expected_types1 = [TokenType.NUMBER, TokenType.OPERATOR, TokenType.NUMBER]
        actual_types1 = [t.type for t in non_eof_tokens1]
        self.assertEqual(actual_types1, expected_types1)

        # JavaScript-style comments
        tokens2 = self.evaluator.tokenize("5 + 3 // This is also a comment")
        non_eof_tokens2 = [t for t in tokens2 if t.type != TokenType.EOF]
        expected_types2 = [TokenType.NUMBER, TokenType.OPERATOR, TokenType.NUMBER]
        actual_types2 = [t.type for t in non_eof_tokens2]
        self.assertEqual(actual_types2, expected_types2)

    def test_complex_expression_tokenization(self):
        """Test tokenization of complex expressions"""
        expression = 'max(abs(user.score - 100), min(day, month)) >= round(3.14159, 2)'
        tokens = self.evaluator.tokenize(expression)

        # Verify we get reasonable tokens (not testing exact sequence, just major components)
        token_values = [t.value for t in tokens if t.type != TokenType.EOF]

        # Should contain function names
        self.assertIn("max", token_values)
        self.assertIn("abs", token_values)
        self.assertIn("min", token_values)
        self.assertIn("round", token_values)

        # Should contain object property access
        self.assertIn("user", token_values)
        self.assertIn("score", token_values)

        # Should contain operators and numbers
        self.assertIn(">=", token_values)
        self.assertIn(100, token_values)
        self.assertIn(3.14159, token_values)
        self.assertIn(2, token_values)


if __name__ == '__main__':
    unittest.main(verbosity=2)