"""Tests for DG204ReturnsSectionMissing rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG204ReturnsSectionMissing


class TestDG204ReturnsSectionMissing:
    """Test cases for DG204ReturnsSectionMissing rule."""

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

    def test_function_with_return_annotation_and_returns_section_passes(self):
        """Test that functions with both return annotation and Returns section pass."""
        code = '''
def example_function() -> str:
    """Example function with return annotation and Returns section.

    Returns:
        str: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_without_return_annotation_and_no_returns_section_passes(self):
        """Test that functions without return annotation and no Returns section pass."""
        code = '''
def example_function():
    """Example function without return annotation or Returns section."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_return_annotation_but_no_returns_section_fails(self):
        """Test that functions with return annotation but no Returns section fail."""
        code = '''
def example_function() -> str:
    """Example function with return annotation but no Returns section."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG204"
        assert (
            "Function has return annotation but missing Returns section in docstring"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_function_with_returns_section_but_no_return_annotation_fails(self):
        """Test that functions with Returns section but no return annotation fail."""
        code = '''
def example_function():
    """Example function with Returns section but no return annotation.

    Returns:
        str: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG204"
        assert (
            "Function has Returns section but no return annotation"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_function_with_complex_return_type_and_returns_section_passes(self):
        """Test that functions with complex return types and Returns section pass."""
        code = '''
from typing import List, Dict

def example_function() -> List[Dict[str, int]]:
    """Example function with complex return type and Returns section.

    Returns:
        List[Dict[str, int]]: Description of return value.
    """
    return [{"key": 1}]
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_complex_return_type_but_no_returns_section_fails(self):
        """Test that functions with complex return types but no Returns section fail."""
        code = '''
from typing import List, Dict

def example_function() -> List[Dict[str, int]]:
    """Example function with complex return type but no Returns section."""
    return [{"key": 1}]
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG204"
        assert (
            "Function has return annotation but missing Returns section in docstring"
            in findings[0].message
        )

    def test_function_with_optional_return_type_and_returns_section_passes(self):
        """Test that functions with Optional return types and Returns section pass."""
        code = '''
from typing import Optional

def example_function() -> Optional[str]:
    """Example function with Optional return type and Returns section.

    Returns:
        Optional[str]: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_union_return_type_and_returns_section_passes(self):
        """Test that functions with Union return types and Returns section pass."""
        code = '''
from typing import Union

def example_function() -> Union[str, int]:
    """Example function with Union return type and Returns section.

    Returns:
        Union[str, int]: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_function_with_return_annotation_and_returns_section_passes(self):
        """Test that async functions with return annotation and Returns section pass."""
        code = '''
async def async_function() -> str:
    """Async function with return annotation and Returns section.

    Returns:
        str: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_function_with_return_annotation_but_no_returns_section_fails(self):
        """Test that async functions with return annotation but no Returns section fail."""
        code = '''
async def async_function() -> str:
    """Async function with return annotation but no Returns section."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG204"
        assert (
            "Function has return annotation but missing Returns section in docstring"
            in findings[0].message
        )

    def test_function_with_none_return_type_and_returns_section_passes(self):
        """Test that functions with None return type and Returns section pass."""
        code = '''
def example_function() -> None:
    """Example function with None return type and Returns section.

    Returns:
        None: This function returns nothing.
    """
    pass
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_none_return_type_but_no_returns_section_fails(self):
        """Test that functions with None return type but no Returns section fail."""
        code = '''
def example_function() -> None:
    """Example function with None return type but no Returns section."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG204"
        assert (
            "Function has return annotation but missing Returns section in docstring"
            in findings[0].message
        )

    def test_function_with_generator_return_type_and_yields_section_passes(self):
        """Test that generator functions with Yields section pass."""
        code = '''
from typing import Generator

def example_generator() -> Generator[int, None, None]:
    """Example generator function with Yields section.

    Yields:
        int: Description of yielded value.
    """
    yield 1
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_generator_return_type_but_no_yields_section_fails(self):
        """Test that generator functions without Yields section fail."""
        code = '''
from typing import Generator

def example_generator() -> Generator[int, None, None]:
    """Example generator function without Yields section."""
    yield 1
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG204"
        assert (
            "Function has return annotation but missing Returns section in docstring"
            in findings[0].message
        )

    def test_function_with_iterator_return_type_and_yields_section_passes(self):
        """Test that functions with Iterator return type and Yields section pass."""
        code = '''
from typing import Iterator

def example_iterator() -> Iterator[int]:
    """Example function with Iterator return type and Yields section.

    Yields:
        int: Description of yielded value.
    """
    yield 1
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring_not_checked(self):
        """Test that functions without docstrings are not checked."""
        code = """
def example_function() -> str:
    return "example"
"""
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
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
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_mismatched_returns(self):
        """Test that multiple functions with mismatched returns are all detected."""
        code = '''
def function1() -> str:
    """Function with return annotation but no Returns section."""
    return "example"

def function2():
    """Function with Returns section but no return annotation.

    Returns:
        str: Description of return value.
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG204" for f in findings)
        assert any(
            "Function has return annotation but missing Returns section" in f.message
            for f in findings
        )
        assert any(
            "Function has Returns section but no return annotation" in f.message
            for f in findings
        )

    def test_function_with_return_annotation_and_returns_section_with_no_description_passes(
        self,
    ):
        """Test that functions with return annotation and Returns section (even without description) pass."""
        code = '''
def example_function() -> str:
    """Example function with return annotation and Returns section.

    Returns:
        str
    """
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG204ReturnsSectionMissing()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
