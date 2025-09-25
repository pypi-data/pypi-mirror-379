"""Tests for DG401TestFunctionDocstringStyle rule."""

import ast
from typing import List

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.python.context_specific import DG401TestFunctionDocstringStyle


class TestDG401TestFunctionDocstringStyle:
    """Test cases for DG401TestFunctionDocstringStyle rule."""

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

        return symbols

    def test_test_function_with_non_descriptive_docstring_fails(self):
        """Test test function with non-descriptive docstring fails."""
        code = '''
def test_something():
    """test"""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"
        assert findings[0].level == FindingLevel.WARNING
        assert (
            "Test function should have a descriptive docstring" in findings[0].message
        )
        assert findings[0].symbol == "test_something"

    def test_test_function_with_descriptive_docstring_passes(self):
        """Test test function with descriptive docstring passes."""
        code = '''
def test_something():
    """Test that the function returns the expected value when given valid input."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_short_docstring_fails(self):
        """Test test function with short docstring fails."""
        code = '''
def test_something():
    """Test something."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_test_function_with_empty_docstring_fails(self):
        """Test test function with empty docstring fails."""
        code = '''
def test_something():
    """"""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        # Empty docstrings should be flagged as missing docstrings
        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_test_function_with_no_docstring_fails(self):
        """Test test function with no docstring fails."""
        code = """
def test_something():
    assert True
"""
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        # Functions without docstrings should be flagged
        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_non_test_function_not_checked(self):
        """Test that non-test functions are not checked."""
        code = '''
def regular_function():
    """This is a regular function."""
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_test_in_name_with_short_docstring_fails(self):
        """Test function with 'test' in name but short docstring fails."""
        code = '''
def get_test_data():
    """test data"""
    return []
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        # This should be flagged because it has 'test' in the name and short docstring
        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_function_with_test_in_name_with_descriptive_docstring_passes(self):
        """Test function with 'test' in name but descriptive docstring passes."""
        code = '''
def get_test_data():
    """Retrieve test data from the database for use in unit tests."""
    return []
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_non_descriptive_patterns_fails(self):
        """Test test function with various non-descriptive patterns fails."""
        non_descriptive_patterns = [
            "test function",
            "test method",
            "test case",
            "unit test",
            "integration test",
        ]

        for pattern in non_descriptive_patterns:
            code = f'''
def test_something():
    """{pattern}"""
    assert True
'''
            symbols = self._parse_code(code)
            rule = DG401TestFunctionDocstringStyle()
            findings = rule.check(symbols=symbols)

            assert len(findings) == 1, f"Pattern '{pattern}' should fail"
            assert findings[0].rule_id == "DG401"

    def test_test_function_with_non_descriptive_patterns_case_insensitive_fails(self):
        """Test test function with non-descriptive patterns case insensitive fails."""
        code = '''
def test_something():
    """TEST FUNCTION"""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_test_function_with_descriptive_content_passes(self):
        """Test test function with descriptive content passes."""
        code = '''
def test_user_authentication():
    """Verify that user authentication works correctly with valid credentials."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_multiline_descriptive_docstring_passes(self):
        """Test test function with multiline descriptive docstring passes."""
        code = '''
def test_user_authentication():
    """Verify that user authentication works correctly.
    
    This test checks that users can log in with valid credentials
    and are properly authenticated in the system."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_multiline_non_descriptive_first_line_fails(self):
        """Test test function with multiline docstring but non-descriptive first line fails."""
        code = '''
def test_user_authentication():
    """test function
    
    This test checks that users can log in with valid credentials."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_async_test_function_with_non_descriptive_docstring_fails(self):
        """Test async test function with non-descriptive docstring fails."""
        code = '''
async def test_async_something():
    """test"""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_async_test_function_with_descriptive_docstring_passes(self):
        """Test async test function with descriptive docstring passes."""
        code = '''
async def test_async_something():
    """Test that async operations complete successfully."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_test_functions_with_mixed_docstrings(self):
        """Test multiple test functions with mixed docstring quality."""
        code = '''
def test_good_function():
    """Test that the function works correctly with valid input."""
    assert True

def test_bad_function():
    """test"""
    assert True

def test_another_good_function():
    """Verify that error handling works as expected."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"
        assert findings[0].symbol == "test_bad_function"

    def test_test_function_with_whitespace_only_docstring_fails(self):
        """Test test function with whitespace-only docstring fails."""
        code = '''
def test_something():
    """   """
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        # Whitespace-only docstrings should be flagged as missing docstrings
        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_test_function_with_exactly_20_characters_passes(self):
        """Test test function with exactly 20 characters passes."""
        code = '''
def test_something():
    """Test something here."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_19_characters_fails(self):
        """Test test function with 19 characters fails."""
        code = '''
def test_something():
    """Test something."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG401"

    def test_test_function_with_whitespace_after_content_passes(self):
        """Test test function with whitespace after content passes."""
        code = '''
def test_something():
    """Test that something works correctly.   """
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_tabs_and_spaces_passes(self):
        """Test test function with tabs and spaces passes."""
        code = '''
def test_something():
    """Test that something works correctly.\t """
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_not_checked(self):
        """Test that classes are not checked."""
        code = '''
class TestClass:
    """This is a test class."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_special_characters_passes(self):
        """Test test function with special characters passes."""
        code = '''
def test_something():
    """Test that function handles special chars: @#$%^&*()!"""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_with_unicode_characters_passes(self):
        """Test test function with unicode characters passes."""
        code = '''
def test_something():
    """Test that function handles unicode: café, naïve, résumé."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG401TestFunctionDocstringStyle()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
