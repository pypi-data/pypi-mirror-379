"""Tests for DG303 content quality detection."""

import ast

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.formatting import DG303ContentQuality


class TestDG303ContentQuality:
    """Test DG303 content quality detection."""

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                docstring = None
                if (
                    node.body
                    and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Constant)
                    and isinstance(node.body[0].value.value, str)
                ):
                    docstring = node.body[0].value.value

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

    def test_todo_detected(self):
        """Test that TODO content is detected."""
        code = '''
def test_function():
    """TODO: This function needs work."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "placeholder content" in findings[0].message
        assert "TODO" in findings[0].message

    def test_fixme_detected(self):
        """Test that FIXME content is detected."""
        code = '''
def test_function():
    """FIXME: This needs to be fixed."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "FIXME" in findings[0].message

    def test_xxx_detected(self):
        """Test that XXX content is detected."""
        code = '''
def test_function():
    """XXX: This is a hack."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "XXX" in findings[0].message

    def test_placeholder_detected(self):
        """Test that placeholder content is detected."""
        code = '''
def test_function():
    """This is a placeholder function."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "placeholder" in findings[0].message

    def test_conflict_markers_detected(self):
        """Test that conflict markers are detected."""
        code = '''
def test_function():
    """This function has conflict markers.
    
    <<<<<<< HEAD
    Original content
    =======
    New content
    >>>>>>> branch
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "conflict markers" in findings[0].message
        assert findings[0].level.value == "error"  # Higher severity

    def test_multiple_issues_detected(self):
        """Test that multiple issues are detected."""
        code = '''
def test_function():
    """TODO: This function needs work.
    
    FIXME: Also needs fixing.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG303" for f in findings)
        assert any("TODO" in f.message for f in findings)
        assert any("FIXME" in f.message for f in findings)

    def test_legitimate_todo_context_not_detected(self):
        """Test that legitimate TODO context is not flagged."""
        code = '''
def test_function():
    """Test function for TODO items in the test suite."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        # Should NOT flag "TODO items" - it's legitimate context
        assert len(findings) == 0

    def test_legitimate_underscores_not_detected(self):
        """Test that legitimate underscores are not flagged."""
        code = '''
def test_function():
    """Test function with snake_case parameters."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        # Should NOT flag "snake_case" - it's legitimate technical term
        assert len(findings) == 0

    def test_legitimate_equals_not_detected(self):
        """Test that legitimate equals signs are not flagged."""
        code = '''
def test_function():
    """Test function: x = y + z."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        # Should NOT flag "x = y + z" - it's legitimate code example
        assert len(findings) == 0

    def test_case_insensitive_detection(self):
        """Test that detection is case insensitive."""
        code = '''
def test_function():
    """todo: This function needs work."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert "todo" in findings[0].message.lower()

    def test_valid_docstring_not_detected(self):
        """Test that valid docstrings are not flagged."""
        code = '''
def test_function():
    """This is a valid docstring with proper content."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_docstring_detected(self):
        """Test that class docstrings are also checked."""
        code = '''
class TestClass:
    """TODO: This class needs documentation."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "TestClass" in findings[0].symbol

    def test_empty_docstring_not_detected(self):
        """Test that empty docstrings are not flagged."""
        code = '''
def test_function():
    """ """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        # Empty docstrings are handled by DG101, not DG303
        assert len(findings) == 0

    def test_no_docstring_not_detected(self):
        """Test that functions without docstrings are not flagged."""
        code = """
def test_function():
    pass
"""
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        # Missing docstrings are handled by DG101, not DG303
        assert len(findings) == 0

    def test_async_function_todo_detected(self):
        """Test that TODO content is detected in async functions."""
        code = '''
async def async_function():
    """TODO: This async function needs work."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "TODO" in findings[0].message

    def test_async_function_conflict_markers_detected(self):
        """Test that conflict markers are detected in async functions."""
        code = '''
async def async_function():
    """Fetches data from API.
    
    <<<<<<< HEAD
    Uses new API endpoint.
    =======
    Uses old API endpoint.
    >>>>>>> branch
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "conflict markers" in findings[0].message

    def test_async_function_valid_docstring_not_detected(self):
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
        symbols = self._parse_symbols(code)
        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
