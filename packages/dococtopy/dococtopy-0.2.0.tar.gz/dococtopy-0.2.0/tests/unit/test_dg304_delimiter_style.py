"""Tests for DG304 docstring delimiter style detection."""

import ast
from pathlib import Path

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.formatting import DG304DocstringDelimiterStyle


class TestDG304DelimiterStyle:
    """Test DG304 docstring delimiter style detection."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
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

    def test_single_quotes_in_docstring_detected(self):
        """Test that docstrings with single quotes are detected."""
        code = '''
def test_function():
    """This docstring contains 'quoted text' which might indicate single quote delimiters."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG304"
        assert "single quote delimiters" in findings[0].message
        assert findings[0].level.value == "info"

    def test_double_quotes_in_docstring_not_detected(self):
        """Test that docstrings with double quotes are not flagged."""
        code = '''
def test_function():
    """This docstring contains "double quotes" which is fine."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_mixed_quotes_not_detected(self):
        """Test that docstrings with both single and double quotes are not flagged."""
        code = '''
def test_function():
    """This docstring has both word's and "double" quotes."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_comment_like_docstring_detected(self):
        """Test that docstrings that look like comments are detected."""
        code = '''
def test_function():
    """# Short comment"""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG304"
        assert "comment instead of proper docstring" in findings[0].message
        assert findings[0].level.value == "warning"

    def test_long_comment_not_detected(self):
        """Test that longer docstrings starting with # are not flagged."""
        code = '''
def test_function():
    """# This is a longer docstring that starts with # but is clearly a docstring because it's long enough"""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring_not_checked(self):
        """Test that functions without docstrings are not checked."""
        code = """
def test_function():
    pass
"""
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_docstring_checked(self):
        """Test that class docstrings are also checked."""
        code = '''
class TestClass:
    """This class docstring contains 'quoted text'."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG304"
        assert "single quote delimiters" in findings[0].message

    def test_multiple_issues_detected(self):
        """Test that multiple delimiter issues are detected."""
        code = '''
def test_function1():
    """This docstring contains 'quoted text'."""
    pass

def test_function2():
    """# Short comment"""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG304" for f in findings)

    def test_valid_docstring_not_flagged(self):
        """Test that valid docstrings are not flagged."""
        code = '''
def test_function():
    """This is a valid docstring with proper content."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_empty_docstring_not_checked(self):
        """Test that empty docstrings are not checked."""
        code = '''
def test_function():
    """ """
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_function_single_quotes_detected(self):
        """Test that async functions with single quote patterns are detected."""
        code = '''
async def async_function():
    """This function uses 'quoted text' which might indicate single quote delimiters."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG304"
        assert "single quote delimiters" in findings[0].message

    def test_async_function_comment_like_detected(self):
        """Test that async functions with comment-like docstrings are detected."""
        code = '''
async def async_function():
    """# Short comment"""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG304"
        assert "comment instead of proper docstring" in findings[0].message

    def test_async_function_valid_docstring_not_flagged(self):
        """Test that valid async function docstrings are not flagged."""
        code = '''
async def async_function():
    """Fetches data from a remote API.

    Args:
        url: The URL to fetch data from.

    Returns:
        A dictionary containing the fetched data.
    """
    pass
'''
        symbols = self._parse_code(code)
        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
