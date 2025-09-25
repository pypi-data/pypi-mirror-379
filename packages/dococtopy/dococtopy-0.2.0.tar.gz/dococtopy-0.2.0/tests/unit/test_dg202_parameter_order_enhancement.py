"""Tests for DG202 enhancement to detect parameter order and duplicates."""

import ast

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import (
    DG202ParamMissingFromDocstring,
    DG203ExtraParamInDocstring,
)


class TestDG202ParameterOrderEnhancement:
    """Test DG202 enhancement for parameter order and duplicates."""

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
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
                        kind="function",
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=docstring,
                        ast_node=node,
                    )
                )

        return symbols

    def test_parameter_order_detected(self):
        """Test that wrong parameter order is detected."""
        code = '''
def test_function(a, b, c):
    """Test function.
    
    Args:
        c: Third parameter
        a: First parameter
        b: Second parameter
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG202ParamMissingFromDocstring()
        findings = rule.check(symbols=symbols)

        # Should detect parameter order issue
        assert len(findings) >= 1
        order_findings = [f for f in findings if "Parameter order" in f.message]
        assert len(order_findings) == 1
        assert order_findings[0].rule_id == "DG202"

    def test_duplicate_parameters_detected(self):
        """Test that duplicate parameters are detected."""
        code = '''
def test_function(a, b):
    """Test function.
    
    Args:
        a: First parameter
        a: Duplicate parameter
        b: Second parameter
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG202ParamMissingFromDocstring()
        findings = rule.check(symbols=symbols)

        # Should detect duplicate parameter
        assert len(findings) >= 1
        duplicate_findings = [f for f in findings if "Duplicate parameter" in f.message]
        assert len(duplicate_findings) == 1
        assert duplicate_findings[0].rule_id == "DG202"

    def test_correct_parameter_order_not_detected(self):
        """Test that correct parameter order is not flagged."""
        code = '''
def test_function(a, b, c):
    """Test function.
    
    Args:
        a: First parameter
        b: Second parameter
        c: Third parameter
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG202ParamMissingFromDocstring()
        findings = rule.check(symbols=symbols)

        # Should not detect any order issues
        order_findings = [f for f in findings if "Parameter order" in f.message]
        assert len(order_findings) == 0

    def test_existing_missing_parameter_detection_still_works(self):
        """Test that existing missing parameter detection still works."""
        code = '''
def test_function(a, b, c):
    """Test function.
    
    Args:
        a: First parameter
        b: Second parameter
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG202ParamMissingFromDocstring()
        findings = rule.check(symbols=symbols)

        # Should detect missing parameter
        assert len(findings) >= 1
        missing_findings = [
            f for f in findings if "missing from docstring" in f.message
        ]
        assert len(missing_findings) == 1
        assert "c" in missing_findings[0].message

    def test_existing_extra_parameter_detection_still_works(self):
        """Test that existing extra parameter detection still works."""
        code = '''
def test_function(a, b):
    """Test function.
    
    Args:
        a: First parameter
        b: Second parameter
        c: Extra parameter
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        # Should detect extra parameter
        assert len(findings) >= 1
        extra_findings = [f for f in findings if "Extra parameter" in f.message]
        assert len(extra_findings) == 1
        assert "c" in extra_findings[0].message

    def test_no_parameters_not_detected(self):
        """Test that functions without parameters are not flagged."""
        code = '''
def test_function():
    """Test function without parameters."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG202ParamMissingFromDocstring()
        findings = rule.check(symbols=symbols)

        # Should not detect any issues
        assert len(findings) == 0

    def test_self_parameter_ignored(self):
        """Test that self parameter is ignored in order checking."""
        code = '''
def test_function(self, a, b):
    """Test function.
    
    Args:
        b: Second parameter
        a: First parameter
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG202ParamMissingFromDocstring()
        findings = rule.check(symbols=symbols)

        # Should detect parameter order issue (ignoring self)
        assert len(findings) >= 1
        order_findings = [f for f in findings if "Parameter order" in f.message]
        assert len(order_findings) == 1
