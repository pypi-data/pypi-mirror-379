"""
Object handling tests for EasyScript

This module contains tests for EasyScript object property access and manipulation including:
- Property access (reading)
- Property assignment (writing)
- Property usage in expressions
- Conditional assignments
- Multiple object injection
"""

import unittest
import sys
import os

# Add the parent directory to the path to import easyscript
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from easyscript import EasyScriptEvaluator
from tests.test_helpers import LDAPUser


class TestEasyScriptObjectHandling(unittest.TestCase):
    """Test object property access and manipulation"""

    def setUp(self):
        self.evaluator = EasyScriptEvaluator()
        self.test_user = LDAPUser(
            cn='John Doe',
            uid='jdoe',
            mail='john.doe@company.com',
            givenName='John',
            sn='Doe',
            department='Engineering',
            title='Senior Developer'
        )
        self.user_variables = {'user': self.test_user}

    def test_property_access(self):
        """Test reading object properties"""
        test_cases = [
            ("user.cn", "John Doe"),
            ("user.uid", "jdoe"),
            ("user.mail", "john.doe@company.com"),
            ("user.givenName", "John"),
            ("user.sn", "Doe"),
            ("user.department", "Engineering"),
            ("user.title", "Senior Developer"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, self.user_variables)
                self.assertEqual(result, expected)

    def test_property_in_expressions(self):
        """Test using object properties in expressions"""
        test_cases = [
            ('len(user.cn)', 8),
            ('"Hello " + user.givenName', "Hello John"),
            ('user.givenName + " " + user.sn', "John Doe"),
            ('len(user.mail) > 10', True),
            ('user.department == "Engineering"', True),
            ('user.mail ~ ".*@.*"', True),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, self.user_variables)
                self.assertEqual(result, expected)

    def test_property_assignment(self):
        """Test assigning values to object properties"""
        # Test basic assignment
        result = self.evaluator.evaluate('user.department = "IT"', self.user_variables)
        self.assertEqual(result, "IT")
        self.assertEqual(self.test_user.department, "IT")

        # Test assignment with expression
        result = self.evaluator.evaluate('user.title = "Senior " + user.title', self.user_variables)
        self.assertEqual(result, "Senior Senior Developer")
        self.assertEqual(self.test_user.title, "Senior Senior Developer")

        # Test assignment with concatenation
        result = self.evaluator.evaluate('user.uid = user.uid + "_new"', self.user_variables)
        self.assertEqual(result, "jdoe_new")
        self.assertEqual(self.test_user.uid, "jdoe_new")

    def test_conditional_assignment(self):
        """Test assignments within conditional statements"""
        # Reset user for clean test
        self.test_user.department = "Engineering"

        # Use a conditional expression that assigns and returns the new value
        result = self.evaluator.evaluate('if len(user.department) > 5 then (user.department = "ENGINEERING") else user.department', self.user_variables)
        self.assertEqual(result, "ENGINEERING")
        self.assertEqual(self.test_user.department, "ENGINEERING")

    def test_multiple_object_injection(self):
        """Test working with multiple injected objects"""
        class Config:
            def __init__(self):
                self.debug = True
                self.version = "1.0"

        config = Config()
        variables = {'user': self.test_user, 'config': config}

        # Test accessing different objects
        self.assertEqual(self.evaluator.evaluate("user.cn", variables), "John Doe")
        self.assertEqual(self.evaluator.evaluate("config.debug", variables), True)
        self.assertEqual(self.evaluator.evaluate("config.version", variables), "1.0")

        # Test assignment to different objects
        self.evaluator.evaluate('config.version = "2.0"', variables)
        self.assertEqual(config.version, "2.0")

    def test_object_properties_in_math_functions(self):
        """Test using object properties with mathematical functions"""
        # Create a user with numeric properties for testing
        class NumericUser:
            def __init__(self):
                self.age = 25
                self.score = -15
                self.rating = 4.7

        numeric_user = NumericUser()
        variables = {'user': numeric_user}

        test_cases = [
            ('abs(user.score)', 15),
            ('max(user.age, 30)', 30),
            ('min(user.age, 30)', 25),
            ('round(user.rating)', 5),
            ('round(user.rating, 1)', 4.7),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_property_chains(self):
        """Test accessing properties through chains (nested objects)"""
        class Address:
            def __init__(self):
                self.street = "123 Main St"
                self.city = "Anytown"

        class UserWithAddress:
            def __init__(self):
                self.name = "Jane Smith"
                self.address = Address()

        user_with_address = UserWithAddress()
        variables = {'user': user_with_address}

        # Test nested property access
        self.assertEqual(self.evaluator.evaluate("user.name", variables), "Jane Smith")
        self.assertEqual(self.evaluator.evaluate("user.address.street", variables), "123 Main St")
        self.assertEqual(self.evaluator.evaluate("user.address.city", variables), "Anytown")

        # Test nested property in expressions
        self.assertEqual(self.evaluator.evaluate('user.name + " lives on " + user.address.street', variables), "Jane Smith lives on 123 Main St")

        # Test nested property assignment
        self.evaluator.evaluate('user.address.city = "New City"', variables)
        self.assertEqual(user_with_address.address.city, "New City")

    def test_dynamic_property_access_patterns(self):
        """Test various patterns of property access"""
        class TestObject:
            def __init__(self):
                self.simple_prop = "simple"
                self.camelCase = "camel"
                self.snake_case = "snake"
                self.NumberProp1 = "number1"
                self._private = "private"

        test_obj = TestObject()
        variables = {'obj': test_obj}

        test_cases = [
            ("obj.simple_prop", "simple"),
            ("obj.camelCase", "camel"),
            ("obj.snake_case", "snake"),
            ("obj.NumberProp1", "number1"),
            ("obj._private", "private"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)

    def test_object_properties_in_conditionals(self):
        """Test object properties in complex conditional expressions"""
        class Employee:
            def __init__(self):
                self.name = "Alice"
                self.department = "Engineering"
                self.salary = 75000
                self.active = True

        employee = Employee()
        variables = {'emp': employee}

        test_cases = [
            ('if emp.active then "Active" else "Inactive"', "Active"),
            ('if emp.salary > 70000 then "High" else "Low"', "High"),
            ('if emp.department == "Engineering" and emp.salary > 60000 then "Senior Engineer" else "Other"', "Senior Engineer"),
            ('if len(emp.name) > 3 and emp.active then emp.name else "Unknown"', "Alice"),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = self.evaluator.evaluate(expression, variables)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)