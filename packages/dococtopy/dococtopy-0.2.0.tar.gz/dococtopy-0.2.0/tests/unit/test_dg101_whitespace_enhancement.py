"""Tests for DG101 enhancement to detect whitespace-only docstrings."""

import ast

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.missing_docstrings import DG101MissingDocstring


class TestDG101WhitespaceEnhancement:
    """Test DG101 enhancement for whitespace-only docstrings."""

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

    def test_missing_docstring_detected(self):
        """Test that missing docstrings are still detected."""
        code = """
def test_function():
    pass
"""
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "missing a docstring" in findings[0].message

    def test_whitespace_only_docstring_detected(self):
        """Test that whitespace-only docstrings are detected."""
        code = '''
def test_function():
    """   """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "whitespace-only docstring" in findings[0].message

    def test_tabs_only_docstring_detected(self):
        """Test that tab-only docstrings are detected."""
        code = '''
def test_function():
    """\t\t\t"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "whitespace-only docstring" in findings[0].message

    def test_newlines_only_docstring_detected(self):
        """Test that newline-only docstrings are detected."""
        code = '''
def test_function():
    """
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "whitespace-only docstring" in findings[0].message

    def test_mixed_whitespace_docstring_detected(self):
        """Test that mixed whitespace docstrings are detected."""
        code = '''
def test_function():
    """ \t\n  \t """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "whitespace-only docstring" in findings[0].message

    def test_valid_docstring_not_detected(self):
        """Test that valid docstrings are not flagged."""
        code = '''
def test_function():
    """This is a valid docstring."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_whitespace_docstring_detected(self):
        """Test that class whitespace-only docstrings are detected."""
        code = '''
class TestClass:
    """   """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "TestClass" in findings[0].symbol
        assert "whitespace-only docstring" in findings[0].message

    def test_async_function_whitespace_docstring_detected(self):
        """Test that async function whitespace-only docstrings are detected."""
        code = '''
async def async_function():
    """   """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "async_function" in findings[0].symbol
        assert "whitespace-only docstring" in findings[0].message

    def test_async_function_missing_docstring_detected(self):
        """Test that async function missing docstrings are detected."""
        code = """
async def async_function():
    pass
"""
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "async_function" in findings[0].symbol
        assert "missing a docstring" in findings[0].message

    def test_async_function_valid_docstring_not_detected(self):
        """Test that async function valid docstrings are not flagged."""
        code = '''
async def async_function():
    """Fetches data from API."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
