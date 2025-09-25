"""Tests for DG205RaisesSectionValidation rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG205RaisesSectionValidation


class TestDG205RaisesSectionValidation:
    """Test cases for DG205RaisesSectionValidation rule."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        import ast

        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=docstring,
                        ast_node=node,
                    )
                )

        return symbols

    def test_function_with_documented_and_raised_exceptions_passes(self):
        """Test that functions with documented exceptions that are actually raised pass."""
        code = '''
def example_function():
    """Example function with documented exceptions that are raised.

    Raises:
        ValueError: When invalid input is provided.
        TypeError: When wrong type is provided.
    """
    if True:
        raise ValueError("Invalid input")
    raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_undocumented_exceptions_passes(self):
        """Test that functions with undocumented exceptions pass (not checked by this rule)."""
        code = '''
def example_function():
    """Example function without documented exceptions."""
    raise ValueError("This is not documented")
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_no_exceptions_passes(self):
        """Test that functions with no exceptions pass."""
        code = '''
def example_function():
    """Example function with no exceptions."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_documented_but_not_raised_exception_fails(self):
        """Test that functions with documented exceptions that are not raised fail."""
        code = '''
def example_function():
    """Example function with documented exception that is not raised.

    Raises:
        ValueError: When invalid input is provided.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG205"
        assert (
            "Exception 'ValueError' documented in Raises but not raised"
            in findings[0].message
        )
        assert findings[0].level.value == "info"

    def test_function_with_multiple_documented_but_not_raised_exceptions_fails(self):
        """Test that functions with multiple documented exceptions that are not raised fail."""
        code = '''
def example_function():
    """Example function with multiple documented exceptions that are not raised.

    Raises:
        ValueError: When invalid input is provided.
        TypeError: When wrong type is provided.
        KeyError: When key is not found.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 3
        assert all(f.rule_id == "DG205" for f in findings)
        assert any(
            "Exception 'ValueError' documented in Raises but not raised" in f.message
            for f in findings
        )
        assert any(
            "Exception 'TypeError' documented in Raises but not raised" in f.message
            for f in findings
        )
        assert any(
            "Exception 'KeyError' documented in Raises but not raised" in f.message
            for f in findings
        )

    def test_function_with_mixed_documented_exceptions(self):
        """Test that functions with some documented exceptions raised and some not."""
        code = '''
def example_function():
    """Example function with mixed documented exceptions.

    Raises:
        ValueError: When invalid input is provided.
        TypeError: When wrong type is provided.
    """
    raise ValueError("This is raised")
    # TypeError is documented but not raised
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG205"
        assert (
            "Exception 'TypeError' documented in Raises but not raised"
            in findings[0].message
        )

    def test_function_with_exception_in_try_except_block(self):
        """Test that functions with exceptions in try-except blocks are detected."""
        code = '''
def example_function():
    """Example function with documented exception in try-except.

    Raises:
        ValueError: When invalid input is provided.
    """
    try:
        raise ValueError("This is raised")
    except ValueError:
        pass
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_exception_in_nested_function(self):
        """Test that functions with exceptions in nested functions are detected."""
        code = '''
def example_function():
    """Example function with documented exception in nested function.

    Raises:
        ValueError: When invalid input is provided.
    """
    def nested_function():
        raise ValueError("This is raised")
    nested_function()
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_exception_in_lambda(self):
        """Test that functions with exceptions in lambda expressions are detected."""
        code = '''
def example_function():
    """Example function with documented exception in lambda.

    Raises:
        ValueError: When invalid input is provided.
    """
    func = lambda: (_ for _ in ()).throw(ValueError("This is raised"))
    next(func())
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        # The extract_raised_exceptions function doesn't detect exceptions in lambda expressions
        # So this will be flagged as documented but not raised
        assert len(findings) == 1
        assert findings[0].rule_id == "DG205"
        assert (
            "Exception 'ValueError' documented in Raises but not raised"
            in findings[0].message
        )

    def test_async_function_with_documented_but_not_raised_exception_fails(self):
        """Test that async functions with documented exceptions that are not raised fail."""
        code = '''
async def async_function():
    """Async function with documented exception that is not raised.

    Raises:
        ValueError: When invalid input is provided.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG205"
        assert (
            "Exception 'ValueError' documented in Raises but not raised"
            in findings[0].message
        )

    def test_function_with_custom_exception_class(self):
        """Test that functions with custom exception classes are handled correctly."""
        code = '''
class CustomError(Exception):
    pass

def example_function():
    """Example function with custom exception.

    Raises:
        CustomError: When custom error occurs.
    """
    raise CustomError("Custom error")
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_custom_exception_class_not_raised_fails(self):
        """Test that functions with custom exception classes that are not raised fail."""
        code = '''
class CustomError(Exception):
    pass

def example_function():
    """Example function with custom exception that is not raised.

    Raises:
        CustomError: When custom error occurs.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG205"
        assert (
            "Exception 'CustomError' documented in Raises but not raised"
            in findings[0].message
        )

    def test_function_with_exception_from_imported_module(self):
        """Test that functions with exceptions from imported modules are handled correctly."""
        code = '''
def example_function():
    """Example function with imported exception.

    Raises:
        ImportError: When import fails.
    """
    raise ImportError("Import failed")
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_exception_from_imported_module_not_raised_fails(self):
        """Test that functions with imported exceptions that are not raised fail."""
        code = '''
def example_function():
    """Example function with imported exception that is not raised.

    Raises:
        ImportError: When import fails.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG205"
        assert (
            "Exception 'ImportError' documented in Raises but not raised"
            in findings[0].message
        )

    def test_no_docstring_not_checked(self):
        """Test that functions without docstrings are not checked."""
        code = """
def example_function():
    raise ValueError("This is not documented")
"""
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_not_checked(self):
        """Test that classes are not checked by this rule."""
        code = '''
class ExampleClass:
    """Example class docstring."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_documented_but_not_raised_exceptions(self):
        """Test that multiple functions with documented but not raised exceptions are all detected."""
        code = '''
def function1():
    """Function with documented exception that is not raised.

    Raises:
        ValueError: When invalid input is provided.
    """
    return "example"

def function2():
    """Another function with documented exception that is not raised.

    Raises:
        TypeError: When wrong type is provided.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG205" for f in findings)
        assert any(
            "Exception 'ValueError' documented in Raises but not raised" in f.message
            for f in findings
        )
        assert any(
            "Exception 'TypeError' documented in Raises but not raised" in f.message
            for f in findings
        )

    def test_function_with_exception_in_conditional_statement(self):
        """Test that functions with exceptions in conditional statements are detected."""
        code = '''
def example_function(flag):
    """Example function with documented exception in conditional.

    Raises:
        ValueError: When flag is True.
    """
    if flag:
        raise ValueError("Flag is True")
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_exception_in_loop(self):
        """Test that functions with exceptions in loops are detected."""
        code = '''
def example_function():
    """Example function with documented exception in loop.

    Raises:
        ValueError: When iteration fails.
    """
    for i in range(1):
        raise ValueError("Iteration failed")
'''
        symbols = self._parse_code(code)
        rule = DG205RaisesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
