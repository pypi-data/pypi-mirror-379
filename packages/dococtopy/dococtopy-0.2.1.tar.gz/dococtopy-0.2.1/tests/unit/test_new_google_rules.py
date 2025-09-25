"""
Unit tests for new Google-style docstring rules (DG206-DG210).
"""

import ast
from pathlib import Path

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import (
    DG206ArgsSectionFormat,
    DG207ReturnsSectionFormat,
    DG208RaisesSectionFormat,
    DG209SummaryLength,
    DG210DocstringIndentation,
)


class TestDG206ArgsSectionFormat:
    """Test DG206: Args section format validation."""

    def test_args_section_missing_description(self):
        """Test detection of missing parameter descriptions."""
        code = '''
def example_func(param1, param2):
    """Example function.
    
    Args:
        param1: 
        param2: Description for param2.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG206"
        assert "param1" in findings[0].message
        assert "missing description" in findings[0].message

    def test_args_section_lowercase_description(self):
        """Test detection of lowercase parameter descriptions."""
        code = '''
def example_func(param1):
    """Example function.
    
    Args:
        param1: this should be capitalized.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG206"
        assert "param1" in findings[0].message
        assert "capital letter" in findings[0].message

    def test_args_section_proper_format(self):
        """Test that properly formatted Args sections pass."""
        code = '''
def example_func(param1, param2):
    """Example function.
    
    Args:
        param1: Proper description for param1.
        param2: Another proper description.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_args_section(self):
        """Test that functions without Args sections pass."""
        code = '''
def example_func():
    """Example function without parameters."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG206ArgsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return PythonSymbol objects."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        docstring=docstring,
                        lineno=node.lineno,
                        col=node.col_offset,
                        ast_node=node,
                    )
                )

        return symbols


class TestDG207ReturnsSectionFormat:
    """Test DG207: Returns section format validation."""

    def test_returns_section_missing_description(self):
        """Test detection of missing Returns description."""
        code = '''
def example_func():
    """Example function.
    
    Returns:
        
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert "missing description" in findings[0].message

    def test_returns_section_lowercase_description(self):
        """Test detection of lowercase Returns description."""
        code = '''
def example_func():
    """Example function.
    
    Returns:
        some value.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG207"
        assert "capital letter" in findings[0].message

    def test_returns_section_proper_format(self):
        """Test that properly formatted Returns sections pass."""
        code = '''
def example_func():
    """Example function.
    
    Returns:
        Some value that is returned.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_returns_section(self):
        """Test that functions without Returns sections pass."""
        code = '''
def example_func():
    """Example function without return."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG207ReturnsSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return PythonSymbol objects."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        docstring=docstring,
                        lineno=node.lineno,
                        col=node.col_offset,
                        ast_node=node,
                    )
                )

        return symbols


class TestDG208RaisesSectionFormat:
    """Test DG208: Raises section format validation."""

    def test_raises_section_missing_description(self):
        """Test detection of missing Raises descriptions."""
        code = '''
def example_func():
    """Example function.
    
    Raises:
        ValueError: 
        TypeError: Some description.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert "ValueError" in findings[0].message
        assert "missing description" in findings[0].message

    def test_raises_section_lowercase_description(self):
        """Test detection of lowercase Raises descriptions."""
        code = '''
def example_func():
    """Example function.
    
    Raises:
        ValueError: this should be capitalized.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG208"
        assert "ValueError" in findings[0].message
        assert "capital letter" in findings[0].message

    def test_raises_section_proper_format(self):
        """Test that properly formatted Raises sections pass."""
        code = '''
def example_func():
    """Example function.
    
    Raises:
        ValueError: When invalid input is provided.
        TypeError: When wrong type is passed.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_raises_section(self):
        """Test that functions without Raises sections pass."""
        code = '''
def example_func():
    """Example function without exceptions."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG208RaisesSectionFormat()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return PythonSymbol objects."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        docstring=docstring,
                        lineno=node.lineno,
                        col=node.col_offset,
                        ast_node=node,
                    )
                )

        return symbols


class TestDG209SummaryLength:
    """Test DG209: Summary length validation."""

    def test_summary_too_short(self):
        """Test detection of too short summaries."""
        code = '''
def example_func():
    """Short."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG209"
        assert "too short" in findings[0].message

    def test_summary_too_long(self):
        """Test detection of too long summaries."""
        code = '''
def example_func():
    """This is a very long summary that exceeds the recommended length of eighty characters and should trigger the warning."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG209"
        assert "too long" in findings[0].message

    def test_summary_appropriate_length(self):
        """Test that appropriately sized summaries pass."""
        code = '''
def example_func():
    """This is a good summary of appropriate length."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_summary(self):
        """Test that functions without summaries pass."""
        code = '''
def example_func():
    """
    Args:
        param1: Description.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG209SummaryLength()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return PythonSymbol objects."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        docstring=docstring,
                        lineno=node.lineno,
                        col=node.col_offset,
                        ast_node=node,
                    )
                )

        return symbols


class TestDG210DocstringIndentation:
    """Test DG210: Docstring indentation validation."""

    def test_inconsistent_indentation(self):
        """Test detection of inconsistent indentation."""
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

        assert len(findings) == 1
        assert findings[0].rule_id == "DG210"
        assert "Inconsistent indentation" in findings[0].message

    def test_consistent_indentation(self):
        """Test that consistently indented docstrings pass."""
        code = '''
def example_func():
    """Example function.
    
    This line has proper indentation.
    This line also has proper indentation.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_google_style_indentation(self):
        """Test that Google style docstring indentation is accepted."""
        code = '''
def example_func():
    """Example function.
    
    Args:
        param1: Description of param1.
        param2: Description of param2.
    
    Returns:
        Description of return value.
    """
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_google_style_with_attributes_section(self):
        """Test that Google style docstring with Attributes section is accepted."""
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

        assert len(findings) == 0

    def test_google_style_with_raises_section(self):
        """Test that Google style docstring with Raises section is accepted."""
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

        assert len(findings) == 0

    def test_google_style_with_examples_section(self):
        """Test that Google style docstring with Examples section is accepted."""
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

        assert len(findings) == 0

    def test_google_style_with_note_section(self):
        """Test that Google style docstring with Note section is accepted."""
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

        assert len(findings) == 0

    def test_google_style_with_yields_section(self):
        """Test that Google style docstring with Yields section is accepted."""
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

        assert len(findings) == 0

    def test_google_style_with_warning_section(self):
        """Test that Google style docstring with Warning section is accepted."""
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

        assert len(findings) == 0

    def test_google_style_with_todo_section(self):
        """Test that Google style docstring with Todo section is accepted."""
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

        assert len(findings) == 0

    def test_google_style_mixed_sections(self):
        """Test that Google style docstring with multiple sections is accepted."""
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

        assert len(findings) == 0

    def test_google_style_section_content_indentation(self):
        """Test that section content with proper indentation is accepted."""
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

        assert len(findings) == 0

    def test_single_line_docstring(self):
        """Test that single-line docstrings pass."""
        code = '''
def example_func():
    """Single line docstring."""
    pass
'''
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_docstring(self):
        """Test that functions without docstrings pass."""
        code = """
def example_func():
    pass
"""
        symbols = self._parse_symbols(code)
        rule = DG210DocstringIndentation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def _parse_symbols(self, code: str) -> list[PythonSymbol]:
        """Parse code and return PythonSymbol objects."""
        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        docstring=docstring,
                        lineno=node.lineno,
                        col=node.col_offset,
                        ast_node=node,
                    )
                )

        return symbols
