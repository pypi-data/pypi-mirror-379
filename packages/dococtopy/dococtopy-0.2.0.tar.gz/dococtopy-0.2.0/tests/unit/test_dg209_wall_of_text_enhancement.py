"""Tests for DG209 enhancement to detect wall of text and super-long lines."""

import ast

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG209SummaryLength


class TestDG209WallOfTextEnhancement:
    """Test DG209 enhancement for wall of text and super-long lines."""

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
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
                            "function" if isinstance(node, ast.FunctionDef) else "class"
                        ),
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=docstring,
                        ast_node=node,
                    )
                )

        return symbols

    def test_wall_of_text_detected(self):
        """Test that wall of text (single line > 120 chars) is detected."""
        code = '''
def test_function():
    """This is a very long docstring that exceeds 120 characters and should be flagged as a wall of text because it has no line breaks and is too long."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        # Should detect wall of text, long line, and long summary
        assert len(findings) >= 1
        wall_of_text_findings = [f for f in findings if "wall of text" in f.message]
        assert len(wall_of_text_findings) == 1
        assert wall_of_text_findings[0].rule_id == "DG209"

    def test_super_long_line_detected(self):
        """Test that super-long lines (> 120 chars) are detected."""
        code = '''
def test_function():
    """This is a normal summary.
    
    This is a very long line that exceeds 120 characters and should be flagged as too long because it's way too long for readability.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        # Should detect long line
        assert len(findings) >= 1
        long_line_findings = [f for f in findings if "too long" in f.message]
        assert len(long_line_findings) == 1
        assert long_line_findings[0].rule_id == "DG209"

    def test_multiple_long_lines_detected(self):
        """Test that multiple long lines are detected."""
        code = '''
def test_function():
    """This is a normal summary.
    
    This is a very long line that exceeds 120 characters and should be flagged as too long because it's way too long for readability.
    
    This is another very long line that also exceeds 120 characters and should also be flagged as too long for the same reason.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        # Should detect multiple long lines
        long_line_findings = [f for f in findings if "too long" in f.message]
        assert len(long_line_findings) >= 1

    def test_valid_docstring_not_detected(self):
        """Test that valid docstrings are not flagged."""
        code = '''
def test_function():
    """This is a normal summary.
    
    This is a normal line that is well within the 120 character limit.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        # Should not detect any issues
        assert len(findings) == 0

    def test_class_wall_of_text_detected(self):
        """Test that class wall of text is detected."""
        code = '''
class TestClass:
    """This is a very long class docstring that exceeds 120 characters and should be flagged as a wall of text because it has no line breaks and is too long."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        # Should detect wall of text
        assert len(findings) >= 1
        wall_of_text_findings = [f for f in findings if "wall of text" in f.message]
        assert len(wall_of_text_findings) == 1
        assert "TestClass" in wall_of_text_findings[0].symbol

    def test_existing_summary_length_validation_still_works(self):
        """Test that existing summary length validation still works."""
        code = '''
def test_function():
    """Short."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        # Should detect short summary
        assert len(findings) >= 1
        short_summary_findings = [f for f in findings if "too short" in f.message]
        assert len(short_summary_findings) == 1
