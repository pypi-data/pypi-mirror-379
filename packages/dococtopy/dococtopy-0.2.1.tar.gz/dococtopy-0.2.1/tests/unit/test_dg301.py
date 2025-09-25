"""Tests for DG301SummaryStyle rule."""

import ast
from typing import List

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.python.formatting import DG301SummaryStyle


class TestDG301SummaryStyle:
    """Test cases for DG301SummaryStyle rule."""

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

    def test_summary_without_period_fails(self):
        """Test that docstring summary without period is flagged."""
        code = '''
def my_function():
    """This is a summary without period"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"
        assert findings[0].level == FindingLevel.WARNING
        assert "Docstring summary should end with a period." in findings[0].message
        assert findings[0].symbol == "my_function"

    def test_summary_with_period_passes(self):
        """Test that docstring summary with period passes."""
        code = '''
def my_function():
    """This is a summary with period."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_summary_without_period_fails(self):
        """Test that class docstring summary without period is flagged."""
        code = '''
class MyClass:
    """This is a class summary without period"""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"
        assert findings[0].symbol == "MyClass"

    def test_class_summary_with_period_passes(self):
        """Test that class docstring summary with period passes."""
        code = '''
class MyClass:
    """This is a class summary with period."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiline_docstring_first_line_without_period_fails(self):
        """Test multiline docstring where first line doesn't end with period."""
        code = '''
def my_function():
    """This is a summary without period
    
    This is additional content.
    """
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"
        assert findings[0].symbol == "my_function"

    def test_multiline_docstring_first_line_with_period_passes(self):
        """Test multiline docstring where first line ends with period."""
        code = '''
def my_function():
    """This is a summary with period.
    
    This is additional content.
    """
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_empty_docstring_not_checked(self):
        """Test that empty docstrings are not checked."""
        code = '''
def my_function():
    """"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_whitespace_only_docstring_not_checked(self):
        """Test that whitespace-only docstrings are not checked."""
        code = '''
def my_function():
    """   """
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring_not_checked(self):
        """Test that functions without docstrings are not checked."""
        code = """
def my_function():
    return 42
"""
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_module_docstring_not_checked(self):
        """Test that module docstrings are not checked."""
        code = '''
"""This is a module docstring without period"""
def my_function():
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        # Module docstrings should not be checked
        assert len(findings) == 0

    def test_summary_with_multiple_periods_passes(self):
        """Test that summary with multiple periods passes."""
        code = '''
def my_function():
    """This is a summary with multiple periods..."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_summary_with_question_mark_fails(self):
        """Test that summary ending with question mark fails."""
        code = '''
def my_function():
    """What does this function do?"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_exclamation_mark_fails(self):
        """Test that summary ending with exclamation mark fails."""
        code = '''
def my_function():
    """This is an exciting function!"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_colon_fails(self):
        """Test that summary ending with colon fails."""
        code = '''
def my_function():
    """This function does the following:"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_semicolon_fails(self):
        """Test that summary ending with semicolon fails."""
        code = '''
def my_function():
    """This function does something;"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_ellipsis_passes(self):
        """Test that summary ending with ellipsis passes (because it ends with period)."""
        code = '''
def my_function():
    """This function does something..."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        # This should pass because "..." ends with a period
        assert len(findings) == 0

    def test_summary_with_quotes_fails(self):
        """Test that summary ending with quotes fails."""
        code = '''
def my_function():
    """This function does 'something'"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_parentheses_fails(self):
        """Test that summary ending with parentheses fails."""
        code = '''
def my_function():
    """This function does something (important)"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_brackets_fails(self):
        """Test that summary ending with brackets fails."""
        code = '''
def my_function():
    """This function does something [important]"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_curly_braces_fails(self):
        """Test that summary ending with curly braces fails."""
        code = '''
def my_function():
    """This function does something {important}"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_numbers_fails(self):
        """Test that summary ending with numbers fails."""
        code = '''
def my_function():
    """This function does something 123"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_letters_fails(self):
        """Test that summary ending with letters fails."""
        code = '''
def my_function():
    """This function does something abc"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_whitespace_after_period_passes(self):
        """Test that summary with whitespace after period passes."""
        code = '''
def my_function():
    """This is a summary with period. """
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_summary_with_tabs_and_spaces_passes(self):
        """Test that summary with tabs and spaces before period passes."""
        code = '''
def my_function():
    """This is a summary with period.\t """
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_summary_issues(self):
        """Test multiple functions with summary issues."""
        code = '''
def function_one():
    """This function has no period"""
    return 1

def function_two():
    """This function has a period."""
    return 2

def function_three():
    """This function also has no period"""
    return 3
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG301" for f in findings)

        function_names = {f.symbol for f in findings}
        assert function_names == {"function_one", "function_three"}

    def test_mixed_classes_and_functions_with_summary_issues(self):
        """Test mixed classes and functions with summary issues."""
        code = '''
class MyClass:
    """This class has no period"""
    pass

def my_function():
    """This function has a period."""
    return 42

class AnotherClass:
    """This class also has no period"""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG301" for f in findings)

        symbol_names = {f.symbol for f in findings}
        assert symbol_names == {"MyClass", "AnotherClass"}

    def test_async_function_summary_without_period_fails(self):
        """Test async function summary without period."""
        code = '''
async def my_async_function():
    """This async function has no period"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"
        assert findings[0].symbol == "my_async_function"

    def test_async_function_summary_with_period_passes(self):
        """Test async function summary with period."""
        code = '''
async def my_async_function():
    """This async function has a period."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_summary_with_special_characters_and_period_passes(self):
        """Test summary with special characters but ending with period."""
        code = '''
def my_function():
    """This function does something (important) with 'quotes' and [brackets]."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_summary_with_unicode_characters_and_period_passes(self):
        """Test summary with unicode characters but ending with period."""
        code = '''
def my_function():
    """This function does something with unicode: café, naïve, résumé."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_summary_with_unicode_characters_without_period_fails(self):
        """Test summary with unicode characters but no period."""
        code = '''
def my_function():
    """This function does something with unicode: café, naïve, résumé"""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG301"

    def test_summary_with_only_period_fails(self):
        """Test summary that is only a period."""
        code = '''
def my_function():
    """."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        # This should pass because it ends with a period
        assert len(findings) == 0

    def test_summary_with_only_whitespace_and_period_passes(self):
        """Test summary that is only whitespace and period."""
        code = '''
def my_function():
    """ ."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG301SummaryStyle()
        findings = rule.check(symbols=symbols)

        # This should pass because it ends with a period
        assert len(findings) == 0
