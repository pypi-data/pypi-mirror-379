"""Tests for special Python constructs that can have docstrings.

This module tests docstring validation for various special Python constructs
including dunder methods, private methods, generators, class methods, etc.
"""

import ast
from pathlib import Path

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.formatting import (
    DG303ContentQuality,
    DG304DocstringDelimiterStyle,
)
from dococtopy.rules.python.google_style import (
    DG202ParamMissingFromDocstring,
    DG209SummaryLength,
)
from dococtopy.rules.python.missing_docstrings import DG101MissingDocstring


class TestSpecialPythonConstructs:
    """Test docstring validation for special Python constructs."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        tree = ast.parse(code)
        symbols = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
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

    def test_dunder_init_method(self):
        """Test __init__ method docstring validation."""
        code = '''
class MyClass:
    """A test class for dunder method testing."""
    
    def __init__(self, value: int):
        """Initialize the class with a value.

        Args:
            value: The initial value.
        """
        self.value = value
'''
        symbols = self._parse_code(code)

        # Test DG101 - should require docstring for __init__
        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Has docstring

    def test_dunder_init_missing_docstring(self):
        """Test __init__ method missing docstring detection."""
        code = '''
class MyClass:
    """A test class for dunder method testing."""
    
    def __init__(self, value: int):
        self.value = value
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 1
        assert findings[0].rule_id == "DG101"
        assert "__init__" in findings[0].symbol

    def test_dunder_str_method(self):
        """Test __str__ method docstring validation."""
        code = '''
class MyClass:
    """A test class for dunder method testing."""
    
    def __str__(self) -> str:
        """Return string representation of the object."""
        return f"MyClass({self.value})"
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Has docstring

    def test_dunder_repr_method(self):
        """Test __repr__ method docstring validation."""
        code = '''
class MyClass:
    """A test class for dunder method testing."""
    
    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"MyClass(value={self.value})"
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Has docstring

    def test_private_method_optional_docstring(self):
        """Test that private methods don't require docstrings."""
        code = '''
class MyClass:
    """A test class for private method testing."""
    
    def _private_method(self):
        """This is optional but recommended."""
        pass
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Private methods are optional

    def test_private_method_missing_docstring_allowed(self):
        """Test that private methods can have missing docstrings."""
        code = '''
class MyClass:
    """A test class for private method testing."""
    
    def _private_method(self):
        pass
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Private methods don't require docstrings

    def test_generator_function(self):
        """Test generator function docstring validation."""
        code = '''
def fibonacci(n: int):
    """Generate Fibonacci numbers up to n.

    Args:
        n: Maximum number of Fibonacci numbers to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)

        # Test DG202 - parameter validation
        rule = DG202ParamMissingFromDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # All parameters documented

    def test_generator_function_missing_yields_section(self):
        """Test generator function missing Yields section."""
        code = '''
def fibonacci(n: int):
    """Generate Fibonacci numbers up to n.

    Args:
        n: Maximum number of Fibonacci numbers to generate.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)

        # This should be caught by DG211 (Yields section validation)
        # For now, just test that the function is parsed correctly
        assert len(symbols) == 1
        assert symbols[0].name == "fibonacci"

    def test_class_method(self):
        """Test class method docstring validation."""
        code = '''
class MyClass:
    """A test class for class method testing."""
    
    @classmethod
    def from_string(cls, s: str) -> 'MyClass':
        """Create instance from string representation.

        Args:
            s: String representation of the value.

        Returns:
            New instance of MyClass.
        """
        return cls(int(s))
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Has docstring

    def test_static_method(self):
        """Test static method docstring validation."""
        code = '''
class MyClass:
    """A test class for static method testing."""
    
    @staticmethod
    def helper_function(x: int, y: int) -> int:
        """Helper function to add two numbers.

        Args:
            x: First number.
            y: Second number.

        Returns:
            Sum of x and y.
        """
        return x + y
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Has docstring

    def test_property_method(self):
        """Test property method docstring validation."""
        code = '''
class MyClass:
    """A test class for property method testing."""
    
    @property
    def value(self) -> int:
        """Get the current value.

        Returns:
            The current value.
        """
        return self._value
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Has docstring

    def test_nested_function(self):
        """Test nested function docstring validation."""
        code = '''
def outer_function(x: int) -> int:
    """Outer function that contains a nested function.

    Args:
        x: Input value.

    Returns:
        Result from nested function.
    """
    def inner_function(y: int) -> int:
        """Inner function that doubles the input.

        Args:
            y: Input value.

        Returns:
            Doubled value.
        """
        return y * 2
    
    return inner_function(x)
'''
        symbols = self._parse_code(code)

        # Should detect both functions
        assert len(symbols) == 2
        function_names = {sym.name for sym in symbols}
        assert "outer_function" in function_names
        assert "inner_function" in function_names

    def test_async_generator_function(self):
        """Test async generator function docstring validation."""
        code = '''
async def async_fibonacci(n: int):
    """Generate Fibonacci numbers asynchronously.

    Args:
        n: Maximum number of Fibonacci numbers to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)

        rule = DG101MissingDocstring()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 0  # Has docstring

    def test_dunder_method_content_quality(self):
        """Test dunder method content quality validation."""
        code = '''
class MyClass:
    def __str__(self) -> str:
        """TODO: Implement proper string representation."""
        return "MyClass"
'''
        symbols = self._parse_code(code)

        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "TODO" in findings[0].message

    def test_private_method_content_quality(self):
        """Test private method content quality validation."""
        code = '''
class MyClass:
    def _helper_method(self):
        """FIXME: This method needs refactoring."""
        pass
'''
        symbols = self._parse_code(code)

        rule = DG303ContentQuality()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 1
        assert findings[0].rule_id == "DG303"
        assert "FIXME" in findings[0].message

    def test_generator_function_wall_of_text(self):
        """Test generator function wall of text detection."""
        code = '''
def fibonacci(n: int):
    """This is a very long docstring that goes on and on without any line breaks and contains way too much information in a single line which makes it hard to read and understand what the function actually does."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)

        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)
        assert len(findings) >= 1  # Should detect wall of text
        wall_of_text_findings = [f for f in findings if "wall of text" in f.message]
        assert len(wall_of_text_findings) >= 1

    def test_class_method_delimiter_style(self):
        """Test class method delimiter style validation."""
        code = '''
class MyClass:
    @classmethod
    def from_string(cls, s: str) -> 'MyClass':
        """This method uses 'single quotes' which might indicate delimiter issues."""
        return cls(int(s))
'''
        symbols = self._parse_code(code)

        rule = DG304DocstringDelimiterStyle()
        findings = rule.check(symbols=symbols)
        assert len(findings) == 1
        assert findings[0].rule_id == "DG304"
        assert "single quote delimiters" in findings[0].message
