"""Tests for DG215PrivateMethodDocstringRecommendation rule."""

import ast
from typing import List

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.python.missing_docstrings import (
    DG215PrivateMethodDocstringRecommendation,
)


class TestDG215PrivateMethodDocstringRecommendation:
    """Test cases for DG215PrivateMethodDocstringRecommendation rule."""

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

    def test_private_method_without_docstring_fails(self):
        """Test that private methods without docstrings are flagged."""
        code = """
class MyClass:
    def _private_method(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert findings[0].level == FindingLevel.INFO
        assert (
            "Private method '_private_method' should have a docstring"
            in findings[0].message
        )
        assert findings[0].symbol == "_private_method"

    def test_private_method_with_docstring_passes(self):
        """Test that private methods with docstrings pass."""
        code = """
class MyClass:
    def _private_method(self):
        \"\"\"Private method with docstring.\"\"\"
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_dunder_method_not_flagged(self):
        """Test that dunder methods (__method__) are not flagged by DG215."""
        code = """
class MyClass:
    def __str__(self):
        return "MyClass"
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_public_method_not_flagged(self):
        """Test that public methods are not flagged."""
        code = """
class MyClass:
    def public_method(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_private_methods_without_docstrings(self):
        """Test multiple private methods without docstrings."""
        code = """
class MyClass:
    def _method_one(self):
        return 1
    
    def _method_two(self):
        return 2
    
    def _method_three(self):
        return 3
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 3
        assert all(f.rule_id == "DG215" for f in findings)
        assert all("should have a docstring" in f.message for f in findings)

        method_names = {f.symbol for f in findings}
        assert method_names == {"_method_one", "_method_two", "_method_three"}

    def test_mixed_methods_only_private_flagged(self):
        """Test that only private methods are flagged in a mix of method types."""
        code = """
class MyClass:
    def public_method(self):
        return 1
    
    def _private_method(self):
        return 2
    
    def __dunder_method__(self):
        return 3
    
    def _another_private(self):
        return 4
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG215" for f in findings)

        method_names = {f.symbol for f in findings}
        assert method_names == {"_private_method", "_another_private"}

    def test_private_method_with_empty_docstring_fails(self):
        """Test that private methods with empty docstrings are flagged."""
        code = """
class MyClass:
    def _private_method(self):
        \"\"\"\"\"\"
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert "_private_method" in findings[0].message

    def test_private_method_with_whitespace_only_docstring_fails(self):
        """Test that private methods with whitespace-only docstrings are flagged."""
        code = """
class MyClass:
    def _private_method(self):
        \"\"\"   \"\"\"
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert "_private_method" in findings[0].message

    def test_async_private_method_without_docstring_fails(self):
        """Test that async private methods without docstrings are flagged."""
        code = """
class MyClass:
    async def _private_async_method(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert "_private_async_method" in findings[0].message

    def test_async_private_method_with_docstring_passes(self):
        """Test that async private methods with docstrings pass."""
        code = """
class MyClass:
    async def _private_async_method(self):
        \"\"\"Async private method with docstring.\"\"\"
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_private_method_with_parameters_and_docstring_passes(self):
        """Test private methods with parameters and docstrings."""
        code = """
class MyClass:
    def _private_method(self, param1, param2):
        \"\"\"Private method with parameters.
        
        Args:
            param1: First parameter.
            param2: Second parameter.
        \"\"\"
        return param1 + param2
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_private_method_with_parameters_without_docstring_fails(self):
        """Test private methods with parameters but no docstring."""
        code = """
class MyClass:
    def _private_method(self, param1, param2):
        return param1 + param2
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert "_private_method" in findings[0].message

    def test_standalone_private_function_without_docstring_fails(self):
        """Test standalone private functions (not methods) without docstrings."""
        code = """
def _private_function():
    return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert "_private_function" in findings[0].message

    def test_standalone_private_function_with_docstring_passes(self):
        """Test standalone private functions with docstrings."""
        code = """
def _private_function():
    \"\"\"Private function with docstring.\"\"\"
    return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_not_checked(self):
        """Test that classes are not checked by this rule."""
        code = """
class _PrivateClass:
    pass
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_edge_case_single_underscore_method(self):
        """Test edge case with method that starts with single underscore."""
        code = """
class MyClass:
    def _(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert "_" in findings[0].message

    def test_edge_case_double_underscore_not_dunder(self):
        """Test edge case with method starting with __ but not ending with __."""
        code = """
class MyClass:
    def __private_not_dunder(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        # This should NOT be flagged because it starts with __
        assert len(findings) == 0

    def test_multiple_classes_with_private_methods(self):
        """Test multiple classes with private methods."""
        code = """
class ClassOne:
    def _method_one(self):
        return 1

class ClassTwo:
    def _method_two(self):
        return 2
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG215" for f in findings)

        method_names = {f.symbol for f in findings}
        assert method_names == {"_method_one", "_method_two"}

    def test_private_method_with_decorator_without_docstring_fails(self):
        """Test private methods with decorators but no docstring."""
        code = """
class MyClass:
    @property
    def _private_property(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG215"
        assert "_private_property" in findings[0].message

    def test_private_method_with_decorator_with_docstring_passes(self):
        """Test private methods with decorators and docstrings."""
        code = """
class MyClass:
    @property
    def _private_property(self):
        \"\"\"Private property with docstring.\"\"\"
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG215PrivateMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
