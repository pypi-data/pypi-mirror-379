"""Tests for DG216DunderMethodDocstringRecommendation rule."""

import ast
from typing import List

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.python.missing_docstrings import (
    DG216DunderMethodDocstringRecommendation,
)


class TestDG216DunderMethodDocstringRecommendation:
    """Test cases for DG216DunderMethodDocstringRecommendation rule."""

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

    def test_str_method_without_docstring_fails(self):
        """Test that __str__ method without docstring is flagged."""
        code = """
class MyClass:
    def __str__(self):
        return "MyClass"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert findings[0].level == FindingLevel.INFO
        assert (
            "Standard dunder method '__str__' should have a docstring"
            in findings[0].message
        )
        assert findings[0].symbol == "__str__"

    def test_str_method_with_docstring_passes(self):
        """Test that __str__ method with docstring passes."""
        code = """
class MyClass:
    def __str__(self):
        \"\"\"String representation of the object.\"\"\"
        return "MyClass"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_repr_method_without_docstring_fails(self):
        """Test that __repr__ method without docstring is flagged."""
        code = """
class MyClass:
    def __repr__(self):
        return f"MyClass({self.value})"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__repr__" in findings[0].message

    def test_eq_method_without_docstring_fails(self):
        """Test that __eq__ method without docstring is flagged."""
        code = """
class MyClass:
    def __eq__(self, other):
        return self.value == other.value
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__eq__" in findings[0].message

    def test_hash_method_without_docstring_fails(self):
        """Test that __hash__ method without docstring is flagged."""
        code = """
class MyClass:
    def __hash__(self):
        return hash(self.value)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__hash__" in findings[0].message

    def test_len_method_without_docstring_fails(self):
        """Test that __len__ method without docstring is flagged."""
        code = """
class MyClass:
    def __len__(self):
        return len(self.items)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__len__" in findings[0].message

    def test_bool_method_without_docstring_fails(self):
        """Test that __bool__ method without docstring is flagged."""
        code = """
class MyClass:
    def __bool__(self):
        return bool(self.value)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__bool__" in findings[0].message

    def test_getitem_method_without_docstring_fails(self):
        """Test that __getitem__ method without docstring is flagged."""
        code = """
class MyClass:
    def __getitem__(self, key):
        return self.items[key]
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__getitem__" in findings[0].message

    def test_setitem_method_without_docstring_fails(self):
        """Test that __setitem__ method without docstring is flagged."""
        code = """
class MyClass:
    def __setitem__(self, key, value):
        self.items[key] = value
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__setitem__" in findings[0].message

    def test_iter_method_without_docstring_fails(self):
        """Test that __iter__ method without docstring is flagged."""
        code = """
class MyClass:
    def __iter__(self):
        return iter(self.items)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__iter__" in findings[0].message

    def test_next_method_without_docstring_fails(self):
        """Test that __next__ method without docstring is flagged."""
        code = """
class MyClass:
    def __next__(self):
        return next(self.iterator)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__next__" in findings[0].message

    def test_dir_method_without_docstring_fails(self):
        """Test that __dir__ method without docstring is flagged."""
        code = """
class MyClass:
    def __dir__(self):
        return ['attr1', 'attr2']
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__dir__" in findings[0].message

    def test_sizeof_method_without_docstring_fails(self):
        """Test that __sizeof__ method without docstring is flagged."""
        code = """
class MyClass:
    def __sizeof__(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__sizeof__" in findings[0].message

    def test_format_method_without_docstring_fails(self):
        """Test that __format__ method without docstring is flagged."""
        code = """
class MyClass:
    def __format__(self, format_spec):
        return format(self.value, format_spec)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__format__" in findings[0].message

    def test_reduce_method_without_docstring_fails(self):
        """Test that __reduce__ method without docstring is flagged."""
        code = """
class MyClass:
    def __reduce__(self):
        return (self.__class__, (self.value,))
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__reduce__" in findings[0].message

    def test_copy_method_without_docstring_fails(self):
        """Test that __copy__ method without docstring is flagged."""
        code = """
class MyClass:
    def __copy__(self):
        return self.__class__(self.value)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__copy__" in findings[0].message

    def test_deepcopy_method_without_docstring_fails(self):
        """Test that __deepcopy__ method without docstring is flagged."""
        code = """
class MyClass:
    def __deepcopy__(self, memo):
        return self.__class__(copy.deepcopy(self.value, memo))
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__deepcopy__" in findings[0].message

    def test_multiple_standard_dunder_methods_without_docstrings(self):
        """Test multiple standard dunder methods without docstrings."""
        code = """
class MyClass:
    def __str__(self):
        return "MyClass"
    
    def __repr__(self):
        return f"MyClass({self.value})"
    
    def __eq__(self, other):
        return self.value == other.value
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 3
        assert all(f.rule_id == "DG216" for f in findings)
        assert all("should have a docstring" in f.message for f in findings)

        method_names = {f.symbol for f in findings}
        assert method_names == {"__str__", "__repr__", "__eq__"}

    def test_mixed_dunder_methods_only_standard_flagged(self):
        """Test that only standard dunder methods are flagged."""
        code = """
class MyClass:
    def __str__(self):
        return "MyClass"
    
    def __custom_dunder__(self):
        return 42
    
    def __repr__(self):
        return f"MyClass({self.value})"
    
    def __non_standard__(self):
        return "not flagged"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG216" for f in findings)

        method_names = {f.symbol for f in findings}
        assert method_names == {"__str__", "__repr__"}

    def test_standard_dunder_method_with_empty_docstring_fails(self):
        """Test that standard dunder methods with empty docstrings are flagged."""
        code = """
class MyClass:
    def __str__(self):
        \"\"\"\"\"\"
        return "MyClass"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__str__" in findings[0].message

    def test_standard_dunder_method_with_whitespace_only_docstring_fails(self):
        """Test that standard dunder methods with whitespace-only docstrings are flagged."""
        code = """
class MyClass:
    def __str__(self):
        \"\"\"   \"\"\"
        return "MyClass"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__str__" in findings[0].message

    def test_async_standard_dunder_method_without_docstring_fails(self):
        """Test that async standard dunder methods without docstrings are flagged."""
        code = """
class MyClass:
    async def __aiter__(self):
        return self
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        # __aiter__ is not in the standard dunder methods list, so should not be flagged
        assert len(findings) == 0

    def test_standard_dunder_method_with_parameters_and_docstring_passes(self):
        """Test standard dunder methods with parameters and docstrings."""
        code = """
class MyClass:
    def __getitem__(self, key):
        \"\"\"Get item by key.
        
        Args:
            key: The key to get the item for.
            
        Returns:
            The item at the given key.
        \"\"\"
        return self.items[key]
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_standard_dunder_method_with_parameters_without_docstring_fails(self):
        """Test standard dunder methods with parameters but no docstring."""
        code = """
class MyClass:
    def __getitem__(self, key):
        return self.items[key]
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__getitem__" in findings[0].message

    def test_standalone_standard_dunder_function_without_docstring_fails(self):
        """Test standalone standard dunder functions (not methods) without docstrings."""
        code = """
def __str__(self):
    return "standalone"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__str__" in findings[0].message

    def test_standalone_standard_dunder_function_with_docstring_passes(self):
        """Test standalone standard dunder functions with docstrings."""
        code = """
def __str__(self):
    \"\"\"Standalone dunder function with docstring.\"\"\"
    return "standalone"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_not_checked(self):
        """Test that classes are not checked by this rule."""
        code = """
class __MyClass__:
    pass
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_non_standard_dunder_method_not_flagged(self):
        """Test that non-standard dunder methods are not flagged."""
        code = """
class MyClass:
    def __custom_method__(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
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
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_private_method_not_flagged(self):
        """Test that private methods are not flagged by DG216."""
        code = """
class MyClass:
    def _private_method(self):
        return 42
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_classes_with_standard_dunder_methods(self):
        """Test multiple classes with standard dunder methods."""
        code = """
class ClassOne:
    def __str__(self):
        return "ClassOne"

class ClassTwo:
    def __repr__(self):
        return "ClassTwo"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG216" for f in findings)

        method_names = {f.symbol for f in findings}
        assert method_names == {"__str__", "__repr__"}

    def test_standard_dunder_method_with_decorator_without_docstring_fails(self):
        """Test standard dunder methods with decorators but no docstring."""
        code = """
class MyClass:
    @property
    def __str__(self):
        return "MyClass"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG216"
        assert "__str__" in findings[0].message

    def test_standard_dunder_method_with_decorator_with_docstring_passes(self):
        """Test standard dunder methods with decorators and docstrings."""
        code = """
class MyClass:
    @property
    def __str__(self):
        \"\"\"String representation property.\"\"\"
        return "MyClass"
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_all_standard_dunder_methods_coverage(self):
        """Test that all standard dunder methods in the rule are covered."""
        # This test ensures we're testing all the standard dunder methods
        # that are defined in the rule implementation
        standard_methods = {
            "__str__",
            "__repr__",
            "__eq__",
            "__hash__",
            "__len__",
            "__bool__",
            "__getitem__",
            "__setitem__",
            "__delitem__",
            "__iter__",
            "__next__",
            "__dir__",
            "__sizeof__",
            "__format__",
            "__reduce__",
            "__reduce_ex__",
            "__getstate__",
            "__setstate__",
            "__copy__",
            "__deepcopy__",
            "__mro_entries__",
            "__subclasshook__",
            "__instancecheck__",
            "__subclasscheck__",
            "__prepare__",
        }

        # Test a few more methods to ensure coverage
        code = """
class MyClass:
    def __delitem__(self, key):
        del self.items[key]
    
    def __reduce_ex__(self, protocol):
        return (self.__class__, (self.value,))
    
    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, state):
        self.__dict__.update(state)
"""
        symbols = self._parse_code(code)
        rule = DG216DunderMethodDocstringRecommendation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 4
        assert all(f.rule_id == "DG216" for f in findings)

        method_names = {f.symbol for f in findings}
        assert method_names == {
            "__delitem__",
            "__reduce_ex__",
            "__getstate__",
            "__setstate__",
        }
