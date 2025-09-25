"""Tests for DG207ReturnsSectionFormat rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG207ReturnsSectionFormat


class TestDG207ReturnsSectionFormat:
    """Test cases for DG207ReturnsSectionFormat rule."""

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

    def test_returns_section_with_proper_format_passes(self):
        """Test that Returns section with proper format passes."""
        code = '''
def example_function():
    """Example function with proper Returns section format.

    Returns:
        str: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_returns_section_with_missing_description_fails(self):
        """Test that Returns section with missing description fails."""
        code = '''
def example_function():
    """Example function with missing Returns description.

    Returns:
        
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert "Returns section is missing description" in findings[0].message
        assert findings[0].level.value == "warning"

    def test_returns_section_with_lowercase_description_fails(self):
        """Test that Returns section with lowercase description fails."""
        code = '''
def example_function():
    """Example function with lowercase Returns description.

    Returns:
        str: description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert (
            "Returns section description should start with capital letter"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_returns_section_with_empty_description_fails(self):
        """Test that Returns section with empty description fails."""
        code = '''
def example_function():
    """Example function with empty Returns description.

    Returns:
        str:   
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert "Returns section is missing description" in findings[0].message

    def test_returns_section_with_whitespace_only_description_fails(self):
        """Test that Returns section with whitespace-only description fails."""
        code = '''
def example_function():
    """Example function with whitespace-only Returns description.

    Returns:
        str: \t\n   
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert "Returns section is missing description" in findings[0].message

    def test_returns_section_with_proper_capitalization_passes(self):
        """Test that Returns section with proper capitalization passes."""
        code = '''
def example_function():
    """Example function with proper capitalization.

    Returns:
        str: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_returns_section_with_numbers_at_start_passes(self):
        """Test that Returns section with numbers at start of description passes."""
        code = '''
def example_function():
    """Example function with numbers at start of description.

    Returns:
        str: 1st return value description.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_returns_section_with_special_characters_at_start_passes(self):
        """Test that Returns section with special characters at start passes."""
        code = '''
def example_function():
    """Example function with special characters at start.

    Returns:
        str: @return description.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_returns_section_passes(self):
        """Test that functions without Returns section pass."""
        code = '''
def example_function():
    """Example function without Returns section."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring_passes(self):
        """Test that functions without docstrings pass."""
        code = """
def example_function():
    return "example"
"""
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_returns_section_format_issues_fails(self):
        """Test that classes with Returns section format issues fail."""
        code = '''
class ExampleClass:
    """Example class with Returns section format issues.

    Returns:
        str: description of return value.
    """
    def __init__(self):
        pass
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert (
            "Returns section description should start with capital letter"
            in findings[0].message
        )

    def test_async_function_with_returns_section_format_issues_fails(self):
        """Test that async functions with Returns section format issues fail."""
        code = '''
async def async_function():
    """Async function with Returns section format issues.

    Returns:
        str: description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert (
            "Returns section description should start with capital letter"
            in findings[0].message
        )

    def test_returns_section_with_complex_type_annotation_passes(self):
        """Test that Returns section with complex type annotation passes."""
        code = '''
def example_function():
    """Example function with complex type annotation.

    Returns:
        Dict[str, List[int]]: Description of return value.
    """
    return {"key": [1, 2, 3]}
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_returns_section_with_optional_type_passes(self):
        """Test that Returns section with optional type passes."""
        code = '''
def example_function():
    """Example function with optional type.

    Returns:
        Optional[str]: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_returns_section_with_union_type_passes(self):
        """Test that Returns section with union type passes."""
        code = '''
def example_function():
    """Example function with union type.

    Returns:
        Union[str, int]: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_returns_section_with_generator_type_passes(self):
        """Test that Returns section with generator type passes."""
        code = '''
def example_function():
    """Example function with generator type.

    Returns:
        Generator[int, None, None]: Description of return value.
    """
    yield 1
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_returns_section_format_issues(self):
        """Test that multiple functions with Returns section format issues are all detected."""
        code = '''
def function1():
    """Function with Returns section format issues.

    Returns:
        str: description of return value.
    """
    return "example"

def function2():
    """Another function with Returns section format issues.

    Returns:
        str: description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG207" for f in findings)
        assert all(
            "Returns section description should start with capital letter" in f.message
            for f in findings
        )

    def test_returns_section_with_long_description_passes(self):
        """Test that Returns section with long description passes."""
        code = '''
def example_function():
    """Example function with long Returns description.

    Returns:
        str: This is a very long description that explains what the function returns in detail.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_returns_section_with_multiline_description_passes(self):
        """Test that Returns section with multiline description passes."""
        code = '''
def example_function():
    """Example function with multiline Returns description.

    Returns:
        str: This is a multiline description that explains
            what the function returns in detail.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
