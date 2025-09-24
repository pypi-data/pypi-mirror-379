from .easyscript import EasyScriptEvaluator


class EasyScriptREPL:
    """Simple REPL implementation for EasyScript"""

    def __init__(self):
        self.evaluator = EasyScriptEvaluator()
        self.variables = {}

    def print_welcome(self):
        """Print welcome message"""
        print("EasyScript REPL v0.6.5")
        print("A simple language combining Python and JavaScript syntax")
        print("Type 'exit', 'quit', or press Ctrl+C to exit")
        print("Type 'help' for available commands")
        print()

    def print_help(self):
        """Print help message"""
        print("EasyScript REPL Commands:")
        print("  exit, quit    - Exit the REPL")
        print("  help          - Show this help message")
        print("  clear         - Clear all variables")
        print("  vars          - Show all defined variables")
        print()
        print("EasyScript Features:")
        print("  Arithmetic:   5 + 3 * 2, (10 - 4) / 2")
        print("  Strings:      \"hello\" + \" world\", len(\"test\")")
        print("  Booleans:     true and false, not true")
        print("  Comparisons:  5 > 3, \"a\" == \"a\"")
        print("  Conditionals: if 5 > 3 then \"yes\" else \"no\"")
        print("  Math:         abs(-5), min(1, 2), max(3, 4), round(3.7), random()")
        print("  Regex:        \"hello\" ~ \"h.*o\"")
        print("  Variables:    Built-in: day, month, year")
        print()

    def format_result(self, result):
        """Format result for display"""
        if result is None:
            return "null"
        elif isinstance(result, bool):
            return "true" if result else "false"
        elif isinstance(result, str):
            return f'"{result}"'
        elif isinstance(result, list):
            formatted_items = [self.format_result(item) for item in result]
            return f"[{', '.join(formatted_items)}]"
        else:
            return str(result)

    def show_variables(self):
        """Show all variables in scope"""
        # Built-in variables
        import datetime
        now = datetime.datetime.now()
        builtin_vars = {
            'day': now.day,
            'month': now.month,
            'year': now.year
        }

        print("Built-in variables:")
        for name, value in builtin_vars.items():
            print(f"  {name} = {self.format_result(value)}")

        # User-defined variables (if we had them)
        if self.variables:
            print("User variables:")
            for name, value in self.variables.items():
                print(f"  {name} = {self.format_result(value)}")
        else:
            print("No user variables defined")
        print()

    def clear_variables(self):
        """Clear all user-defined variables"""
        self.variables.clear()
        print("Variables cleared")

    def run(self):
        """Run the REPL"""
        self.print_welcome()

        while True:
            try:
                # Read input
                try:
                    expression = input(">> ").strip()
                except EOFError:
                    print("\nGoodbye!")
                    break

                # Skip empty lines
                if not expression:
                    continue

                # Handle special commands
                if expression.lower() in ('exit', 'quit'):
                    print("Goodbye!")
                    break
                elif expression.lower() == 'help':
                    self.print_help()
                    continue
                elif expression.lower() == 'clear':
                    self.clear_variables()
                    continue
                elif expression.lower() == 'vars':
                    self.show_variables()
                    continue

                # Evaluate expression
                try:
                    result = self.evaluator.evaluate(expression, self.variables)

                    # Only print result if it's not None (to avoid printing for statements like assignments)
                    if result is not None:
                        print(self.format_result(result))

                except Exception as e:
                    print(f"Error: {e}")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")


def start_repl():
    """Start the EasyScript REPL"""
    repl = EasyScriptREPL()
    repl.run()


if __name__ == '__main__':
    start_repl()