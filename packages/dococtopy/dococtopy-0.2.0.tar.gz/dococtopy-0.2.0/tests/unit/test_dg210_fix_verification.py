"""Simple tests to verify the DG210 fix works correctly.

These tests focus specifically on the DG210 indentation validation fix
without getting into complex integration scenarios.
"""

from __future__ import annotations

import ast
from unittest.mock import Mock

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG210DocstringIndentation


class TestDG210FixVerification:
    """Test that the DG210 fix works correctly."""

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                # Extract docstring
                docstring = None
                if (
                    node.body
                    and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Constant)
                    and isinstance(node.body[0].value.value, str)
                ):
                    docstring = node.body[0].value.value

                symbol = PythonSymbol(
                    name=node.name,
                    kind="function" if isinstance(node, ast.FunctionDef) else "class",
                    lineno=node.lineno,
                    col=node.col_offset,
                    docstring=docstring,
                    ast_node=node,
                )
                symbols.append(symbol)

        return symbols

    def test_google_style_docstring_passes_dg210(self):
        """Test that Google-style docstrings pass DG210 validation."""
        code = '''
def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number.

Args:
    n: The index (n >= 0) of the Fibonacci sequence to compute.

Returns:
    The nth Fibonacci number.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_class_docstring_passes_dg210(self):
        """Test that Google-style class docstrings pass DG210 validation."""
        code = '''
class UserManager:
    """UserManager handles operations related to managing user accounts.

This class provides interfaces to create, retrieve, update, and delete users.

Attributes:
    user_repository (object): Repository for persisting and retrieving user data.
    authentication_service (object): Service used to authenticate users.
    role_manager (object): Component that manages user roles and permissions.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_with_multiple_sections_passes_dg210(self):
        """Test that Google-style docstrings with multiple sections pass DG210 validation."""
        code = '''
def process_user_data(user_id, include_metadata=False):
    """Process user data.

Args:
    user_id: Identifier for the user.
    include_metadata: Flag indicating whether to include metadata.

Returns:
    Processed user data.

Raises:
    ValueError: If user_id is invalid.
    RuntimeError: If processing fails.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_with_examples_passes_dg210(self):
        """Test that Google-style docstrings with Examples section pass DG210 validation."""
        code = '''
def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number.

Args:
    n: The index (n >= 0) of the Fibonacci sequence to compute.

Returns:
    The nth Fibonacci number.

Examples:
    >>> calculate_fibonacci(0)
    0
    >>> calculate_fibonacci(5)
    5
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_with_note_passes_dg210(self):
        """Test that Google-style docstrings with Note section pass DG210 validation."""
        code = '''
def complex_function(*args, **kwargs):
    """Complex function with special behavior.

Args:
    *args: Variable length argument list.
    **kwargs: Arbitrary keyword arguments.

Note:
    This function has special behavior that requires careful handling.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_with_warning_passes_dg210(self):
        """Test that Google-style docstrings with Warning section pass DG210 validation."""
        code = '''
def dangerous_function():
    """Perform a dangerous operation.

Warning:
    This function may cause data loss. Use with caution.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_with_todo_passes_dg210(self):
        """Test that Google-style docstrings with Todo section pass DG210 validation."""
        code = '''
def incomplete_function():
    """Function that is not yet complete.

Todo:
    Add error handling.
    Implement logging.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_with_yields_passes_dg210(self):
        """Test that Google-style docstrings with Yields section pass DG210 validation."""
        code = '''
def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n.

Args:
    n: The maximum value to generate.

Yields:
    int: The next Fibonacci number in the sequence.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_mixed_sections_passes_dg210(self):
        """Test that Google-style docstrings with multiple sections pass DG210 validation."""
        code = '''
def comprehensive_function(param1, param2):
    """A comprehensive function with multiple sections.

This function demonstrates proper Google style docstring formatting
with multiple sections and proper indentation.

Args:
    param1: First parameter description.
    param2: Second parameter description.

Returns:
    str: Description of return value.

Raises:
    ValueError: If parameters are invalid.
    RuntimeError: If operation fails.

Examples:
    >>> comprehensive_function("test", 42)
    "test_42"

Note:
    This is a complex function with special behavior.

Warning:
    Use with caution in production environments.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_google_style_section_content_indentation_passes_dg210(self):
        """Test that section content with proper indentation passes DG210 validation."""
        code = '''
def function_with_long_descriptions():
    """Function with long parameter descriptions.

Args:
    param1: This is a very long parameter description that
    spans multiple lines and has proper indentation
    for continuation lines.
    param2: Another parameter with a long description
    that continues on the next line with proper
    indentation.

Returns:
    A complex return value that requires a long description
    to explain what it contains and how it should be
    used by the caller.
"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation
        assert len(findings) == 0

    def test_inconsistent_indentation_fails_dg210(self):
        """Test that docstrings with inconsistent indentation fail DG210 validation."""
        code = '''
def example_func():
    """Example function.
    
    This line has proper indentation.
      This line has inconsistent indentation (2 spaces instead of 4).
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should fail DG210 validation
        assert len(findings) == 1
        assert findings[0].rule_id == "DG210"
        assert "Inconsistent indentation" in findings[0].message

    def test_single_line_docstring_passes_dg210(self):
        """Test that single-line docstrings pass DG210 validation."""
        code = '''
def example_func():
    """Example function."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation (single line docstrings are skipped)
        assert len(findings) == 0

    def test_no_docstring_passes_dg210(self):
        """Test that functions without docstrings pass DG210 validation."""
        code = """
def example_func():
    pass
"""
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # Should pass DG210 validation (no docstring to validate)
        assert len(findings) == 0

    def test_old_dg210_rule_would_have_failed(self):
        """Test that documents what the old DG210 rule would have incorrectly failed."""
        # This test documents what the old behavior was
        # The old rule required ALL lines to have the same indentation
        # But Google-style docstrings have different indentation levels

        google_style_docstring = """Calculate the nth Fibonacci number.

Args:
    n: The index (n >= 0) of the Fibonacci sequence to compute.

Returns:
    The nth Fibonacci number.
"""

        # Parse the docstring lines to show the indentation levels
        lines = google_style_docstring.split("\n")

        # Find the base indentation (first content line)
        first_content_line = None
        for i, line in enumerate(lines):
            if line.strip() and not line.strip().startswith('"""'):
                first_content_line = i
                break

        assert first_content_line is not None

        base_indent = len(lines[first_content_line]) - len(
            lines[first_content_line].lstrip()
        )

        # Check indentation levels
        indent_levels = set()
        for line in lines[first_content_line:]:
            if line.strip() and not line.strip().startswith('"""'):
                indent = len(line) - len(line.lstrip())
                indent_levels.add(indent)

        # Google-style docstrings have multiple indentation levels
        # - Summary line: base_indent
        # - Section headers: base_indent
        # - Section content: base_indent + 4
        assert (
            len(indent_levels) > 1
        ), "Google-style docstrings should have multiple indentation levels"

        # The old rule would have failed because it expected all lines to have the same indentation
        # But our new rule correctly allows this structure
        code = f'''
def calculate_fibonacci(n):
    """{google_style_docstring}"""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        # New rule should pass
        assert len(findings) == 0
