"""Tests for DG402PublicAPIFunctionDocumentation rule."""

import ast
from typing import List

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.python.context_specific import DG402PublicAPIFunctionDocumentation


class TestDG402PublicAPIFunctionDocumentation:
    """Test cases for DG402PublicAPIFunctionDocumentation rule."""

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

    def test_public_function_without_args_section_fails(self):
        """Test public function without Args section fails."""
        code = '''
def public_function(param1, param2):
    """This is a public function.
    
    Returns:
        str: A result.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG402"
        assert findings[0].level == FindingLevel.WARNING
        assert "Args" in findings[0].message
        assert findings[0].symbol == "public_function"

    def test_public_function_without_returns_section_fails(self):
        """Test public function without Returns section fails."""
        code = '''
def public_function(param1, param2) -> str:
    """This is a public function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG402"
        assert "Returns" in findings[0].message

    def test_public_function_with_complete_documentation_passes(self):
        """Test public function with complete documentation passes."""
        code = '''
def public_function(param1, param2) -> str:
    """This is a public function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    
    Returns:
        str: A result string.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_public_function_without_parameters_passes(self):
        """Test public function without parameters passes (no Args section needed)."""
        code = '''
def public_function() -> str:
    """This is a public function.
    
    Returns:
        str: A result string.
    """
    return "result"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_public_function_without_return_annotation_passes(self):
        """Test public function without return annotation passes (no Returns section needed)."""
        code = '''
def public_function(param1, param2):
    """This is a public function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_private_function_not_checked(self):
        """Test private functions are not checked."""
        code = '''
def _private_function(param1, param2):
    """This is a private function."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_test_function_not_checked(self):
        """Test test functions are not checked."""
        code = '''
def test_public_function():
    """This is a test function."""
    assert True
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_dunder_method_not_checked(self):
        """Test dunder methods are not checked."""
        code = '''
def __str__(self):
    """String representation."""
    return "object"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_internal_function_not_checked(self):
        """Test internal functions are not checked."""
        code = '''
def internal_function(param1, param2):
    """This is an internal function."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_helper_function_not_checked(self):
        """Test helper functions are not checked."""
        code = '''
def helper_function(param1, param2):
    """This is a helper function."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_util_function_not_checked(self):
        """Test util functions are not checked."""
        code = '''
def util_function(param1, param2):
    """This is a util function."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_without_docstring_not_checked(self):
        """Test functions without docstrings are not checked."""
        code = """
def public_function(param1, param2) -> str:
    return f"{param1} {param2}"
"""
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_public_function_without_args_section_fails(self):
        """Test async public function without Args section fails."""
        code = '''
async def public_function(param1, param2) -> str:
    """This is an async public function.
    
    Returns:
        str: A result.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG402"
        assert "Args" in findings[0].message

    def test_async_public_function_with_complete_documentation_passes(self):
        """Test async public function with complete documentation passes."""
        code = '''
async def public_function(param1, param2) -> str:
    """This is an async public function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    
    Returns:
        str: A result string.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_public_functions_with_mixed_documentation(self):
        """Test multiple public functions with mixed documentation."""
        code = '''
def good_function(param1, param2) -> str:
    """This is a good function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    
    Returns:
        str: A result string.
    """
    return f"{param1} {param2}"

def bad_function(param1, param2) -> str:
    """This is a bad function."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG402"
        assert findings[0].symbol == "bad_function"

    def test_public_function_with_args_and_returns_missing_both(self):
        """Test public function missing both Args and Returns sections."""
        code = '''
def public_function(param1, param2) -> str:
    """This is a public function."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG402"
        # Should mention both Args and Returns
        message = findings[0].message
        assert "Args" in message and "Returns" in message

    def test_public_function_with_kwargs_parameter(self):
        """Test public function with **kwargs parameter."""
        code = '''
def public_function(param1, **kwargs) -> str:
    """This is a public function.
    
    Args:
        param1: First parameter.
        **kwargs: Additional keyword arguments.
    
    Returns:
        str: A result string.
    """
    return f"{param1} {len(kwargs)}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_public_function_with_args_parameter(self):
        """Test public function with *args parameter."""
        code = '''
def public_function(*args) -> str:
    """This is a public function.
    
    Args:
        *args: Variable number of arguments.
    
    Returns:
        str: A result string.
    """
    return f"{len(args)}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_public_function_with_kwonlyargs(self):
        """Test public function with keyword-only arguments."""
        code = '''
def public_function(param1, *, kwarg1, kwarg2) -> str:
    """This is a public function.
    
    Args:
        param1: First parameter.
        kwarg1: First keyword argument.
        kwarg2: Second keyword argument.
    
    Returns:
        str: A result string.
    """
    return f"{param1} {kwarg1} {kwarg2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_public_function_with_posonlyargs(self):
        """Test public function with positional-only arguments."""
        code = '''
def public_function(param1, param2, /) -> str:
    """This is a public function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    
    Returns:
        str: A result string.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_not_checked(self):
        """Test that classes are not checked."""
        code = '''
class PublicClass:
    """This is a public class."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_test_in_name_not_checked(self):
        """Test function with 'test' in name is not checked."""
        code = '''
def get_test_data(param1, param2) -> str:
    """This function gets test data."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_internal_patterns_not_checked(self):
        """Test functions with internal patterns are not checked."""
        internal_patterns = [
            "_internal",
            "_helper",
            "_util",
            "_private",
            "internal_",
            "helper_",
            "util_",
        ]

        for pattern in internal_patterns:
            code = f'''
def {pattern}_function(param1, param2) -> str:
    """This is a {pattern} function."""
    return f"{{param1}} {{param2}}"
'''
            symbols = self._parse_code(code)
            rule = DG402PublicAPIFunctionDocumentation()
            findings = rule.check(symbols=symbols)

            assert len(findings) == 0, f"Pattern '{pattern}' should not be checked"

    def test_public_function_with_complex_return_type(self):
        """Test public function with complex return type."""
        code = '''
def public_function(param1, param2) -> List[Dict[str, Any]]:
    """This is a public function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries.
    """
    return [{"key": f"{param1} {param2}"}]
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_public_function_with_optional_return_type(self):
        """Test public function with optional return type."""
        code = '''
def public_function(param1, param2) -> Optional[str]:
    """This is a public function.
    
    Args:
        param1: First parameter.
        param2: Second parameter.
    
    Returns:
        Optional[str]: An optional result string.
    """
    return f"{param1} {param2}" if param1 else None
'''
        symbols = self._parse_code(code)
        rule = DG402PublicAPIFunctionDocumentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
