"""Tests for DG302BlankLineAfterSummary rule."""

import ast
from typing import List

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.python.formatting import DG302BlankLineAfterSummary


class TestDG302BlankLineAfterSummary:
    """Test cases for DG302BlankLineAfterSummary rule."""

    def _parse_code(self, code: str) -> List[PythonSymbol]:
        """Helper to parse code and extract symbols."""
        tree = ast.parse(code)
        symbols: List[PythonSymbol] = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=ast.get_docstring(node),
                        ast_node=node,
                    )
                )
            elif isinstance(node, ast.ClassDef):
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="class",
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=ast.get_docstring(node),
                        ast_node=node,
                    )
                )
            elif isinstance(node, ast.Module):
                symbols.append(
                    PythonSymbol(
                        name="<module>",
                        kind="module",
                        lineno=1,
                        col=0,
                        docstring=ast.get_docstring(node),
                        ast_node=node,
                    )
                )

        return symbols

    def test_multiline_docstring_without_blank_line_fails(self):
        """Test multiline docstring without blank line after summary."""
        code = '''
def my_function():
    """This is a summary.
    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG302"
        assert findings[0].level == FindingLevel.WARNING
        assert "Expected blank line after docstring summary." in findings[0].message
        assert findings[0].symbol == "my_function"

    def test_multiline_docstring_with_blank_line_passes(self):
        """Test multiline docstring with blank line after summary."""
        code = '''
def my_function():
    """This is a summary.

    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_single_line_docstring_passes(self):
        """Test single line docstring passes (no blank line needed)."""
        code = '''
def my_function():
    """This is a single line summary."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_empty_docstring_not_checked(self):
        """Test empty docstrings are not checked."""
        code = '''
def my_function():
    """"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring_not_checked(self):
        """Test functions without docstrings are not checked."""
        code = """
def my_function():
    return 42
"""
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_module_docstring_not_checked(self):
        """Test module docstrings are not checked."""
        code = '''
"""This is a module docstring.
This is additional content."""
def my_function():
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_docstring_without_blank_line_fails(self):
        """Test class docstring without blank line after summary."""
        code = '''
class MyClass:
    """This is a class summary.
    This is additional content."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG302"
        assert findings[0].symbol == "MyClass"

    def test_class_docstring_with_blank_line_passes(self):
        """Test class docstring with blank line after summary."""
        code = '''
class MyClass:
    """This is a class summary.

    This is additional content."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiline_with_whitespace_line_fails(self):
        """Test multiline docstring with whitespace-only line fails."""
        code = '''
def my_function():
    """This is a summary.
    
    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiline_with_tabs_line_fails(self):
        """Test multiline docstring with tabs-only line fails."""
        code = '''
def my_function():
    """This is a summary.
\t
    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiline_with_spaces_line_fails(self):
        """Test multiline docstring with spaces-only line fails."""
        code = '''
def my_function():
    """This is a summary.
    
    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_blank_line_issues(self):
        """Test multiple functions with blank line issues."""
        code = '''
def function_one():
    """This is a summary.
    This is additional content."""
    return 1

def function_two():
    """This is a summary.

    This is additional content."""
    return 2

def function_three():
    """This is a summary.
    This is also additional content."""
    return 3
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG302" for f in findings)

        function_names = {f.symbol for f in findings}
        assert function_names == {"function_one", "function_three"}

    def test_async_function_without_blank_line_fails(self):
        """Test async function without blank line after summary."""
        code = '''
async def my_async_function():
    """This is an async summary.
    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG302"
        assert findings[0].symbol == "my_async_function"

    def test_async_function_with_blank_line_passes(self):
        """Test async function with blank line after summary."""
        code = '''
async def my_async_function():
    """This is an async summary.

    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_docstring_with_sections_without_blank_line_fails(self):
        """Test docstring with sections without blank line after summary."""
        code = '''
def my_function():
    """This is a summary.
    Args:
        param: A parameter."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG302"

    def test_docstring_with_sections_with_blank_line_passes(self):
        """Test docstring with sections with blank line after summary."""
        code = '''
def my_function():
    """This is a summary.

    Args:
        param: A parameter."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_docstring_with_long_summary_without_blank_line_fails(self):
        """Test docstring with long summary without blank line."""
        code = '''
def my_function():
    """This is a very long summary that goes on and on and on.
    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG302"

    def test_docstring_with_long_summary_with_blank_line_passes(self):
        """Test docstring with long summary with blank line."""
        code = '''
def my_function():
    """This is a very long summary that goes on and on and on.

    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_mixed_classes_and_functions_with_blank_line_issues(self):
        """Test mixed classes and functions with blank line issues."""
        code = '''
class MyClass:
    """This is a class summary.
    This is additional content."""
    pass

def my_function():
    """This is a function summary.

    This is additional content."""
    return 42

class AnotherClass:
    """This is another class summary.
    This is also additional content."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG302" for f in findings)

        symbol_names = {f.symbol for f in findings}
        assert symbol_names == {"MyClass", "AnotherClass"}

    def test_docstring_with_only_whitespace_second_line_fails(self):
        """Test docstring with only whitespace on second line fails."""
        code = '''
def my_function():
    """This is a summary.
    
    This is additional content."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_docstring_with_three_lines_no_blank_line_fails(self):
        """Test docstring with three lines but no blank line after summary."""
        code = '''
def my_function():
    """This is a summary.
    This is line two.
    This is line three."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG302"

    def test_docstring_with_three_lines_with_blank_line_passes(self):
        """Test docstring with three lines and blank line after summary."""
        code = '''
def my_function():
    """This is a summary.

    This is line two.
    This is line three."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG302BlankLineAfterSummary()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
