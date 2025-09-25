"""Tests for DG208RaisesSectionFormat rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG208RaisesSectionFormat


class TestDG208RaisesSectionFormat:
    """Test cases for DG208RaisesSectionFormat rule."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        import ast

        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind=(
                            "function"
                            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                            else "class"
                        ),
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=docstring,
                        ast_node=node,
                    )
                )

        return symbols

    def test_raises_section_with_proper_format_passes(self):
        """Test that Raises section with proper format passes."""
        code = '''
def example_function():
    """Example function with proper Raises section format.

    Raises:
        ValueError: When invalid input is provided.
        TypeError: When wrong type is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_raises_section_with_missing_description_fails(self):
        """Test that Raises section with missing description fails."""
        code = '''
def example_function():
    """Example function with missing Raises description.

    Raises:
        ValueError:
        TypeError: When wrong type is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert (
            "Exception 'ValueError' in Raises section is missing description"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_raises_section_with_lowercase_description_fails(self):
        """Test that Raises section with lowercase description fails."""
        code = '''
def example_function():
    """Example function with lowercase Raises description.

    Raises:
        ValueError: when invalid input is provided.
        TypeError: When wrong type is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert (
            "Exception 'ValueError' description should start with capital letter"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_raises_section_with_multiple_format_issues_fails(self):
        """Test that Raises section with multiple format issues fails."""
        code = '''
def example_function():
    """Example function with multiple Raises format issues.

    Raises:
        ValueError:
        TypeError: when wrong type is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG208" for f in findings)
        assert any(
            "Exception 'ValueError' in Raises section is missing description"
            in f.message
            for f in findings
        )
        assert any(
            "Exception 'TypeError' description should start with capital letter"
            in f.message
            for f in findings
        )

    def test_raises_section_with_empty_description_fails(self):
        """Test that Raises section with empty description fails."""
        code = '''
def example_function():
    """Example function with empty Raises description.

    Raises:
        ValueError:   
        TypeError: When wrong type is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert (
            "Exception 'ValueError' in Raises section is missing description"
            in findings[0].message
        )

    def test_raises_section_with_whitespace_only_description_fails(self):
        """Test that Raises section with whitespace-only description fails."""
        code = '''
def example_function():
    """Example function with whitespace-only Raises description.

    Raises:
        ValueError: \t\n   
        TypeError: When wrong type is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert (
            "Exception 'ValueError' in Raises section is missing description"
            in findings[0].message
        )

    def test_raises_section_with_proper_capitalization_passes(self):
        """Test that Raises section with proper capitalization passes."""
        code = '''
def example_function():
    """Example function with proper capitalization.

    Raises:
        ValueError: When invalid input is provided.
        TypeError: When wrong type is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_raises_section_with_numbers_at_start_passes(self):
        """Test that Raises section with numbers at start of description passes."""
        code = '''
def example_function():
    """Example function with numbers at start of description.

    Raises:
        ValueError: 1st error condition.
        TypeError: 2nd error condition.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_raises_section_with_special_characters_at_start_passes(self):
        """Test that Raises section with special characters at start passes."""
        code = '''
def example_function():
    """Example function with special characters at start.

    Raises:
        ValueError: @error description.
        TypeError: #error description.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_raises_section_passes(self):
        """Test that functions without Raises section pass."""
        code = '''
def example_function():
    """Example function without Raises section."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring_passes(self):
        """Test that functions without docstrings pass."""
        code = """
def example_function():
    raise ValueError("Invalid input")
"""
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_raises_section_format_issues_fails(self):
        """Test that classes with Raises section format issues fail."""
        code = '''
class ExampleClass:
    """Example class with Raises section format issues.

    Raises:
        ValueError: when invalid input is provided.
    """
    def __init__(self):
        raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert (
            "Exception 'ValueError' description should start with capital letter"
            in findings[0].message
        )

    def test_async_function_with_raises_section_format_issues_fails(self):
        """Test that async functions with Raises section format issues fail."""
        code = '''
async def async_function():
    """Async function with Raises section format issues.

    Raises:
        ValueError: when invalid input is provided.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert (
            "Exception 'ValueError' description should start with capital letter"
            in findings[0].message
        )

    def test_raises_section_with_custom_exception_class_passes(self):
        """Test that Raises section with custom exception class passes."""
        code = '''
class CustomError(Exception):
    pass

def example_function():
    """Example function with custom exception class.

    Raises:
        CustomError: When custom error occurs.
    """
    raise CustomError("Custom error")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_raises_section_with_imported_exception_passes(self):
        """Test that Raises section with imported exception passes."""
        code = '''
def example_function():
    """Example function with imported exception.

    Raises:
        ImportError: When import fails.
    """
    raise ImportError("Import failed")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_raises_section_with_multiple_exceptions_passes(self):
        """Test that Raises section with multiple exceptions passes."""
        code = '''
def example_function():
    """Example function with multiple exceptions.

    Raises:
        ValueError: When invalid input is provided.
        TypeError: When wrong type is provided.
        KeyError: When key is not found.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_raises_section_format_issues(self):
        """Test that multiple functions with Raises section format issues are all detected."""
        code = '''
def function1():
    """Function with Raises section format issues.

    Raises:
        ValueError: when invalid input is provided.
    """
    raise ValueError("Invalid input")

def function2():
    """Another function with Raises section format issues.

    Raises:
        TypeError: when wrong type is provided.
    """
    raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG208" for f in findings)
        assert any(
            "Exception 'ValueError' description should start with capital letter"
            in f.message
            for f in findings
        )
        assert any(
            "Exception 'TypeError' description should start with capital letter"
            in f.message
            for f in findings
        )

    def test_raises_section_with_long_description_passes(self):
        """Test that Raises section with long description passes."""
        code = '''
def example_function():
    """Example function with long Raises description.

    Raises:
        ValueError: This is a very long description that explains when this exception is raised in detail.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_raises_section_with_multiline_description_passes(self):
        """Test that Raises section with multiline description passes."""
        code = '''
def example_function():
    """Example function with multiline Raises description.

    Raises:
        ValueError: This is a multiline description that explains
            when this exception is raised in detail.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
