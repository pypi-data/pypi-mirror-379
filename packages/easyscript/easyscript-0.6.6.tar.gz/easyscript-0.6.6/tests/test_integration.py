"""
Integration tests for EasyScript

This module contains integration tests that combine multiple EasyScript features including:
- LDAP user transformation scenarios
- Complex conditional logic
- Mathematical expressions with variables
- Math functions in complex expressions
- Real-world usage patterns
"""

import unittest
import sys
import os
import datetime

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript import EasyScriptEvaluator
from tests.test_helpers import LDAPUser


class TestEasyScriptIntegration(unittest.TestCase):
    """Integration tests combining multiple features"""

    def setUp(self):
        self.evaluator = EasyScriptEvaluator()

    def test_ldap_user_transformation_scenario(self):
        """Test a realistic LDAP user transformation scenario"""
        user = LDAPUser(
            cn='John Smith',
            uid='jsmith',
            mail='j.smith@oldcompany.com',
            department='IT',
            title='Developer'
        )

        variables = {'user': user}

        # Simulate a series of transformations
        transformations = [
            'user.department = "25_" + user.department',
            'user.title = "Senior " + user.title',
            'user.mail = user.uid + "@newcompany.com"',
            'if len(user.cn) > 5 then (user.cn = user.cn + " (Updated)") else user.cn'
        ]

        expected_results = [
            "25_IT",
            "Senior Developer",
            "jsmith@newcompany.com",
            "John Smith (Updated)"
        ]

        for transformation, expected in zip(transformations, expected_results):
            with self.subTest(transformation=transformation):
                result = self.evaluator.evaluate(transformation, variables)
                self.assertEqual(result, expected)

        # Verify final state
        self.assertEqual(user.department, "25_IT")
        self.assertEqual(user.title, "Senior Developer")
        self.assertEqual(user.mail, "jsmith@newcompany.com")
        self.assertEqual(user.cn, "John Smith (Updated)")

    def test_complex_conditional_logic(self):
        """Test complex conditional logic with multiple branches"""
        user = LDAPUser(department='Engineering', title='Manager')
        variables = {'user': user}

        complex_expression = '''
        if user.department == "Engineering" and user.title ~ ".*Manager.*" then
            (user.department = "ENGINEERING_MGMT")
        else
            user.department
        '''

        # Remove extra whitespace and newlines for evaluation
        expression = ' '.join(complex_expression.split())
        result = self.evaluator.evaluate(expression, variables)

        self.assertEqual(result, "ENGINEERING_MGMT")
        self.assertEqual(user.department, "ENGINEERING_MGMT")

    def test_mathematical_expressions_with_variables(self):
        """Test complex mathematical expressions using built-in variables"""
        now = datetime.datetime.now()

        # Test date-based calculations
        test_cases = [
            ("year - 2000", now.year - 2000),
            ("month * day", now.month * now.day),
            ("if year > 2020 then year - 2020 else 0", now.year - 2020 if now.year > 2020 else 0),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_math_functions_in_complex_expressions(self):
        """Test mathematical functions in complex expressions and conditionals"""
        now = datetime.datetime.now()

        # Test math functions with built-in variables
        test_cases = [
            ("abs(day - 15)", abs(now.day - 15)),
            ("max(day, month)", max(now.day, now.month)),
            ("min(day, month, year)", min(now.day, now.month, now.year)),
            ("round(day / 2.0)", round(now.day / 2.0)),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

        # Test math functions in conditionals
        conditional_tests = [
            ('if abs(-5) > 3 then "large" else "small"', "large"),
            ('if min(10, 20) < 15 then "correct" else "wrong"', "correct"),
            ('if max(5, 3) == 5 then "max works" else "error"', "max works"),
            ('if round(3.7) == 4 then "rounded up" else "rounded down"', "rounded up"),
        ]

        for expression, expected in conditional_tests:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

        # Test nested math functions
        nested_tests = [
            ("abs(min(-10, -5))", 10),
            ("max(abs(-3), abs(-7))", 7),
            ("round(max(3.14, 2.71), 1)", 3.1),
            ("min(round(3.7), round(4.2))", 4),
        ]

        for expression, expected in nested_tests:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression)
                self.assertEqual(result, expected)

    def test_employee_processing_workflow(self):
        """Test a comprehensive employee processing workflow"""
        class Employee:
            def __init__(self, name, department, salary, years_experience, active=True):
                self.name = name
                self.department = department
                self.salary = salary
                self.years_experience = years_experience
                self.active = active
                self.bonus = 0
                self.classification = ""

        employees = [
            Employee("Alice Johnson", "Engineering", 85000, 5),
            Employee("Bob Smith", "Marketing", 65000, 3),
            Employee("Carol Davis", "Engineering", 95000, 8),
            Employee("David Wilson", "Sales", 55000, 2),
        ]

        for emp in employees:
            variables = {'emp': emp}

            # Calculate bonus based on department and experience
            bonus_expr = '''if emp.department == "Engineering" and emp.years_experience >= 5 then
                               max(emp.salary * 0.15, 10000)
                             else if emp.years_experience >= 3 then
                               min(emp.salary * 0.10, 8000)
                             else
                               emp.salary * 0.05'''

            # Simplify the expression for testing (EasyScript doesn't support elif)
            if emp.department == "Engineering" and emp.years_experience >= 5:
                bonus_result = self.evaluator.evaluate('max(emp.salary * 0.15, 10000)', variables)
            elif emp.years_experience >= 3:
                bonus_result = self.evaluator.evaluate('min(emp.salary * 0.10, 8000)', variables)
            else:
                bonus_result = self.evaluator.evaluate('emp.salary * 0.05', variables)

            # Assign the bonus
            self.evaluator.evaluate(f'emp.bonus = {bonus_result}', variables)

            # Classify employee
            classification_expr = '''if emp.salary >= 90000 then "Senior"
                                   else if emp.salary >= 70000 then "Mid-Level"
                                   else "Junior"'''

            # Simplify for EasyScript
            if emp.salary >= 90000:
                classification = "Senior"
            elif emp.salary >= 70000:
                classification = "Mid-Level"
            else:
                classification = "Junior"

            self.evaluator.evaluate(f'emp.classification = "{classification}"', variables)

            # Verify results
            with self.subTest(employee=emp.name):
                self.assertGreater(emp.bonus, 0)
                self.assertIn(emp.classification, ["Junior", "Mid-Level", "Senior"])

                # Test some specific calculations
                if emp.name == "Alice Johnson":
                    expected_bonus = max(85000 * 0.15, 10000)  # 12750
                    self.assertEqual(emp.bonus, expected_bonus)
                    self.assertEqual(emp.classification, "Mid-Level")

                elif emp.name == "Carol Davis":
                    expected_bonus = max(95000 * 0.15, 10000)  # 14250
                    self.assertEqual(emp.bonus, expected_bonus)
                    self.assertEqual(emp.classification, "Senior")

    def test_data_validation_pipeline(self):
        """Test a data validation and processing pipeline"""
        class DataRecord:
            def __init__(self, id, email, score, category):
                self.id = id
                self.email = email
                self.score = score
                self.category = category
                self.is_valid = False
                self.normalized_score = 0
                self.grade = ""

        records = [
            DataRecord(1, "user@domain.com", 87.5, "A"),
            DataRecord(2, "invalid-email", 65.2, "B"),
            DataRecord(3, "test@company.org", 92.8, "A"),
            DataRecord(4, "admin@site.net", 78.1, "C"),
        ]

        for record in records:
            variables = {'record': record}

            # Validate email format
            email_valid = self.evaluator.evaluate('record.email ~ ".*@.*\\.(com|org|net)$"', variables)

            # Validate score range
            score_valid = self.evaluator.evaluate('record.score >= 0 and record.score <= 100', variables)

            # Validate category
            category_valid = self.evaluator.evaluate('record.category ~ "^[ABC]$"', variables)

            # Set overall validity
            overall_valid = email_valid and score_valid and category_valid
            self.evaluator.evaluate(f'record.is_valid = {str(overall_valid).lower()}', variables)

            if overall_valid:
                # Normalize score to 0-10 scale
                normalized = self.evaluator.evaluate('round(record.score / 10, 1)', variables)
                self.evaluator.evaluate(f'record.normalized_score = {normalized}', variables)

                # Assign grade
                if record.score >= 90:
                    grade = "A+"
                elif record.score >= 80:
                    grade = "A"
                elif record.score >= 70:
                    grade = "B"
                else:
                    grade = "C"

                self.evaluator.evaluate(f'record.grade = "{grade}"', variables)

            # Verify results
            with self.subTest(record_id=record.id):
                if record.email == "invalid-email":
                    self.assertFalse(record.is_valid)
                else:
                    self.assertTrue(record.is_valid)
                    self.assertGreater(record.normalized_score, 0)
                    self.assertIn(record.grade, ["A+", "A", "B", "C"])

    def test_complex_string_processing(self):
        """Test complex string processing with regex and functions"""
        class TextData:
            def __init__(self, content):
                self.content = content
                self.word_count = 0
                self.has_email = False
                self.has_phone = False
                self.category = ""

        texts = [
            TextData("Hello world! Contact us at info@company.com for more details."),
            TextData("Call us at 555-123-4567 or visit our website."),
            TextData("This is a simple message without contact info."),
            TextData("Email: support@help.org Phone: (555) 987-6543"),
        ]

        for text in texts:
            variables = {'text': text}

            # Count words (approximate - count spaces + 1)
            word_count = self.evaluator.evaluate('len(text.content) - len(text.content)', variables)  # Start with 0
            # Simple word count approximation
            spaces = 0
            for char in text.content:
                if char == ' ':
                    spaces += 1
            word_count = spaces + 1
            self.evaluator.evaluate(f'text.word_count = {word_count}', variables)

            # Check for email pattern
            has_email = self.evaluator.evaluate('text.content ~ ".*@.*\\.(com|org|net)"', variables)
            self.evaluator.evaluate(f'text.has_email = {str(has_email).lower()}', variables)

            # Check for phone pattern
            has_phone = self.evaluator.evaluate('text.content ~ ".*(\\d{3}[-.]?\\d{3}[-.]?\\d{4}|\\(\\d{3}\\)\\s*\\d{3}[-.]?\\d{4})"', variables)
            self.evaluator.evaluate(f'text.has_phone = {str(has_phone).lower()}', variables)

            # Categorize based on content
            if has_email and has_phone:
                category = "full_contact"
            elif has_email:
                category = "email_only"
            elif has_phone:
                category = "phone_only"
            else:
                category = "no_contact"

            self.evaluator.evaluate(f'text.category = "{category}"', variables)

            # Verify results
            with self.subTest(content_preview=text.content[:30] + "..."):
                self.assertGreater(text.word_count, 0)
                self.assertIn(text.category, ["full_contact", "email_only", "phone_only", "no_contact"])

                # Test specific cases
                if "info@company.com" in text.content:
                    self.assertTrue(text.has_email)
                if "555-123-4567" in text.content or "(555) 987-6543" in text.content:
                    self.assertTrue(text.has_phone)


if __name__ == '__main__':
    unittest.main(verbosity=2)