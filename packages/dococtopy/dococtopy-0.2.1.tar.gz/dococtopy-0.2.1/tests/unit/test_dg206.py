"""Tests for DG206ArgsSectionFormat rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG206ArgsSectionFormat


class TestDG206ArgsSectionFormat:
    """Test cases for DG206ArgsSectionFormat rule."""

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

    def test_args_section_with_proper_format_passes(self):
        """Test that Args section with proper format passes."""
        code = '''
def example_function(param1, param2):
    """Example function with proper Args section format.

    Args:
        param1: First parameter description.
        param2: Second parameter description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_args_section_with_missing_description_fails(self):
        """Test that Args section with missing description fails."""
        code = '''
def example_function(param1, param2):
    """Example function with missing parameter description.

    Args:
        param1: First parameter description.
        param2:
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG206"
        assert (
            "Parameter 'param2' in Args section is missing description"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_args_section_with_lowercase_description_fails(self):
        """Test that Args section with lowercase description fails."""
        code = '''
def example_function(param1, param2):
    """Example function with lowercase parameter description.

    Args:
        param1: first parameter description.
        param2: Second parameter description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG206"
        assert (
            "Parameter 'param1' description should start with capital letter"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_args_section_with_multiple_format_issues_fails(self):
        """Test that Args section with multiple format issues fails."""
        code = '''
def example_function(param1, param2, param3):
    """Example function with multiple format issues.

    Args:
        param1: first parameter description.
        param2:
        param3: Third parameter description.
    """
    return f"{param1} {param2} {param3}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG206" for f in findings)
        assert any(
            "Parameter 'param1' description should start with capital letter"
            in f.message
            for f in findings
        )
        assert any(
            "Parameter 'param2' in Args section is missing description" in f.message
            for f in findings
        )

    def test_args_section_with_empty_description_fails(self):
        """Test that Args section with empty description fails."""
        code = '''
def example_function(param1, param2):
    """Example function with empty parameter description.

    Args:
        param1: First parameter description.
        param2:   
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG206"
        assert (
            "Parameter 'param2' in Args section is missing description"
            in findings[0].message
        )

    def test_args_section_with_whitespace_only_description_fails(self):
        """Test that Args section with whitespace-only description fails."""
        code = '''
def example_function(param1, param2):
    """Example function with whitespace-only parameter description.

    Args:
        param1: First parameter description.
        param2: \t\n   
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG206"
        assert (
            "Parameter 'param2' in Args section is missing description"
            in findings[0].message
        )

    def test_args_section_with_proper_capitalization_passes(self):
        """Test that Args section with proper capitalization passes."""
        code = '''
def example_function(param1, param2):
    """Example function with proper capitalization.

    Args:
        param1: First parameter description.
        param2: Second parameter description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_args_section_with_numbers_at_start_passes(self):
        """Test that Args section with numbers at start of description passes."""
        code = '''
def example_function(param1, param2):
    """Example function with numbers at start of description.

    Args:
        param1: 1st parameter description.
        param2: 2nd parameter description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_args_section_with_special_characters_at_start_passes(self):
        """Test that Args section with special characters at start passes."""
        code = '''
def example_function(param1, param2):
    """Example function with special characters at start.

    Args:
        param1: @param1 description.
        param2: #param2 description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_args_section_passes(self):
        """Test that functions without Args section pass."""
        code = '''
def example_function():
    """Example function without Args section."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring_passes(self):
        """Test that functions without docstrings pass."""
        code = """
def example_function(param1, param2):
    return f"{param1} {param2}"
"""
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_args_section_format_issues_fails(self):
        """Test that classes with Args section format issues fail."""
        code = '''
class ExampleClass:
    """Example class with Args section format issues.

    Args:
        param1: first parameter description.
        param2:
    """
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG206" for f in findings)
        assert any(
            "Parameter 'param1' description should start with capital letter"
            in f.message
            for f in findings
        )
        assert any(
            "Parameter 'param2' in Args section is missing description" in f.message
            for f in findings
        )

    def test_async_function_with_args_section_format_issues_fails(self):
        """Test that async functions with Args section format issues fail."""
        code = '''
async def async_function(param1, param2):
    """Async function with Args section format issues.

    Args:
        param1: first parameter description.
        param2:
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG206" for f in findings)
        assert any(
            "Parameter 'param1' description should start with capital letter"
            in f.message
            for f in findings
        )
        assert any(
            "Parameter 'param2' in Args section is missing description" in f.message
            for f in findings
        )

    def test_args_section_with_type_annotations_passes(self):
        """Test that Args section with type annotations passes."""
        code = '''
def example_function(param1: str, param2: int):
    """Example function with type annotations.

    Args:
        param1: First parameter description.
        param2: Second parameter description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_args_section_with_default_values_passes(self):
        """Test that Args section with default values passes."""
        code = '''
def example_function(param1="default", param2=42):
    """Example function with default values.

    Args:
        param1: First parameter description.
        param2: Second parameter description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_args_section_with_args_kwargs_passes(self):
        """Test that Args section with *args and **kwargs passes."""
        code = '''
def example_function(param1, *args, **kwargs):
    """Example function with *args and **kwargs.

    Args:
        param1: First parameter description.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.
    """
    return f"{param1} {args} {kwargs}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_args_section_format_issues(self):
        """Test that multiple functions with Args section format issues are all detected."""
        code = '''
def function1(param1, param2):
    """Function with Args section format issues.

    Args:
        param1: first parameter description.
        param2:
    """
    return f"{param1} {param2}"

def function2(param1, param2):
    """Another function with Args section format issues.

    Args:
        param1: first parameter description.
        param2:
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 4
        assert all(f.rule_id == "DG206" for f in findings)
        assert any(
            "Parameter 'param1' description should start with capital letter"
            in f.message
            for f in findings
        )
        assert any(
            "Parameter 'param2' in Args section is missing description" in f.message
            for f in findings
        )

    def test_args_section_with_long_description_passes(self):
        """Test that Args section with long description passes."""
        code = '''
def example_function(param1, param2):
    """Example function with long parameter description.

    Args:
        param1: This is a very long description that explains what the parameter does in detail.
        param2: Another long description that provides comprehensive information about the parameter.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
