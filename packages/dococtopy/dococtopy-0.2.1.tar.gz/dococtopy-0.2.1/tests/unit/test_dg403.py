"""Tests for DG403ExceptionDocumentationCompleteness rule."""

import ast
from typing import List

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.python.context_specific import (
    DG403ExceptionDocumentationCompleteness,
)


class TestDG403ExceptionDocumentationCompleteness:
    """Test cases for DG403ExceptionDocumentationCompleteness rule."""

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

    def test_function_with_undocumented_exception_fails(self):
        """Test function that raises exception but doesn't document it fails."""
        code = '''
def my_function():
    """This function does something."""
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        assert findings[0].level == FindingLevel.WARNING
        assert "ValueError" in findings[0].message
        assert findings[0].symbol == "my_function"

    def test_function_with_documented_exception_passes(self):
        """Test function that raises and documents exception passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises:
        ValueError: When input is invalid.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_without_exceptions_passes(self):
        """Test function that doesn't raise exceptions passes."""
        code = '''
def my_function():
    """This function does something."""
    return "result"
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_without_docstring_not_checked(self):
        """Test function without docstring is not checked."""
        code = """
def my_function():
    raise ValueError("Invalid input")
"""
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_multiple_undocumented_exceptions_fails(self):
        """Test function with multiple undocumented exceptions fails."""
        code = '''
def my_function():
    """This function does something."""
    if True:
        raise ValueError("Invalid input")
    else:
        raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        message = findings[0].message
        assert "ValueError" in message and "TypeError" in message

    def test_function_with_multiple_documented_exceptions_passes(self):
        """Test function with multiple documented exceptions passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises:
        ValueError: When input is invalid.
        TypeError: When type is wrong.
    """
    if True:
        raise ValueError("Invalid input")
    else:
        raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_partial_exception_documentation_fails(self):
        """Test function with partial exception documentation fails."""
        code = '''
def my_function():
    """This function does something.
    
    Raises:
        ValueError: When input is invalid.
    """
    if True:
        raise ValueError("Invalid input")
    else:
        raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        assert "TypeError" in findings[0].message

    def test_function_with_exception_call_fails(self):
        """Test function that raises exception via call fails."""
        code = '''
def my_function():
    """This function does something."""
    raise RuntimeError("Runtime error")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        assert "RuntimeError" in findings[0].message

    def test_function_with_exception_call_documented_passes(self):
        """Test function that raises exception via call and documents it passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises:
        RuntimeError: When runtime error occurs.
    """
    raise RuntimeError("Runtime error")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_function_with_undocumented_exception_fails(self):
        """Test async function with undocumented exception fails."""
        code = '''
async def my_function():
    """This async function does something."""
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        assert "ValueError" in findings[0].message

    def test_async_function_with_documented_exception_passes(self):
        """Test async function with documented exception passes."""
        code = '''
async def my_function():
    """This async function does something.
    
    Raises:
        ValueError: When input is invalid.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_nested_exceptions_fails(self):
        """Test function with exceptions in nested blocks fails."""
        code = '''
def my_function():
    """This function does something."""
    try:
        raise ValueError("Invalid input")
    except Exception:
        raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        message = findings[0].message
        assert "ValueError" in message and "TypeError" in message

    def test_function_with_nested_exceptions_documented_passes(self):
        """Test function with exceptions in nested blocks and documented passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises:
        ValueError: When input is invalid.
        TypeError: When type is wrong.
    """
    try:
        raise ValueError("Invalid input")
    except Exception:
        raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_raises_section_case_insensitive_passes(self):
        """Test function with Raises section case insensitive passes."""
        code = '''
def my_function():
    """This function does something.
    
    RAISES:
        ValueError: When input is invalid.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_multiline_raises_section_passes(self):
        """Test function with multiline Raises section passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises:
        ValueError: When input is invalid.
        This can happen when the input format is wrong.
        
        TypeError: When type is wrong.
        This occurs when the wrong data type is passed.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_raises_section_after_other_sections_passes(self):
        """Test function with Raises section after other sections passes."""
        code = '''
def my_function():
    """This function does something.
    
    Args:
        param: A parameter.
    
    Returns:
        str: A result.
    
    Raises:
        ValueError: When input is invalid.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_raises_section_before_other_sections_passes(self):
        """Test function with Raises section before other sections passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises:
        ValueError: When input is invalid.
    
    Args:
        param: A parameter.
    
    Returns:
        str: A result.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_custom_exception_fails(self):
        """Test function with custom exception fails."""
        code = '''
class CustomError(Exception):
    pass

def my_function():
    """This function does something."""
    raise CustomError("Custom error")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        assert "CustomError" in findings[0].message

    def test_function_with_custom_exception_documented_passes(self):
        """Test function with custom exception documented passes."""
        code = '''
class CustomError(Exception):
    pass

def my_function():
    """This function does something.
    
    Raises:
        CustomError: When custom error occurs.
    """
    raise CustomError("Custom error")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_conditional_exceptions_fails(self):
        """Test function with conditional exceptions fails."""
        code = '''
def my_function(flag):
    """This function does something."""
    if flag:
        raise ValueError("Invalid input")
    else:
        raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG403"
        message = findings[0].message
        assert "ValueError" in message and "TypeError" in message

    def test_function_with_conditional_exceptions_documented_passes(self):
        """Test function with conditional exceptions documented passes."""
        code = '''
def my_function(flag):
    """This function does something.
    
    Raises:
        ValueError: When flag is True.
        TypeError: When flag is False.
    """
    if flag:
        raise ValueError("Invalid input")
    else:
        raise TypeError("Wrong type")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_not_checked(self):
        """Test that classes are not checked."""
        code = '''
class MyClass:
    """This is a class."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_raises_section_no_colon_passes(self):
        """Test function with Raises section without colon passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises
        ValueError: When input is invalid.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_raises_section_dash_format_passes(self):
        """Test function with Raises section in dash format passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises -
        ValueError: When input is invalid.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_raises_section_space_format_passes(self):
        """Test function with Raises section in space format passes."""
        code = '''
def my_function():
    """This function does something.
    
    Raises 
        ValueError: When input is invalid.
    """
    raise ValueError("Invalid input")
'''
        symbols = self._parse_code(code)
        rule = DG403ExceptionDocumentationCompleteness()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
