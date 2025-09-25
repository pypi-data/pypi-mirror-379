"""Tests for DG214NoteSectionValidation rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG214NoteSectionValidation


class TestDG214NoteSectionValidation:
    """Test cases for DG214NoteSectionValidation rule."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        import ast

        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                docstring = ast.get_docstring(node)
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

    def test_function_with_args_and_note_section_passes(self):
        """Test that functions with *args and Note section pass."""
        code = '''
def flexible_function(*args):
    """Process variable number of arguments.

    Args:
        *args: Variable number of arguments to process.

    Returns:
        List: Processed arguments.

    Note:
        This function can handle any number of arguments.
    """
    return list(args)
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_args_without_note_section_fails(self):
        """Test that functions with *args without Note section fail."""
        code = '''
def flexible_function(*args):
    """Process variable number of arguments.

    Args:
        *args: Variable number of arguments to process.

    Returns:
        List: Processed arguments.
    """
    return list(args)
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG214"
        assert (
            "Function with special behavior should have Note section"
            in findings[0].message
        )
        assert findings[0].level.value == "info"

    def test_function_with_kwargs_and_note_section_passes(self):
        """Test that functions with **kwargs and Note section pass."""
        code = '''
def configurable_function(**kwargs):
    """Process keyword arguments.

    Args:
        **kwargs: Keyword arguments to process.

    Returns:
        Dict: Processed keyword arguments.

    Note:
        This function accepts any keyword arguments.
    """
    return kwargs
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_kwargs_without_note_section_fails(self):
        """Test that functions with **kwargs without Note section fail."""
        code = '''
def configurable_function(**kwargs):
    """Process keyword arguments.

    Args:
        **kwargs: Keyword arguments to process.

    Returns:
        Dict: Processed keyword arguments.
    """
    return kwargs
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG214"
        assert (
            "Function with special behavior should have Note section"
            in findings[0].message
        )

    def test_function_with_decorator_and_note_section_passes(self):
        """Test that functions with decorators and Note section pass."""
        code = '''
def cached_function():
    """Expensive computation with caching.

    Returns:
        int: Computed result.

    Note:
        This function uses caching to improve performance.
    """
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_decorator_without_note_section_fails(self):
        """Test that functions with decorators without Note section fail."""
        code = '''
def cached_function():
    """Expensive computation with caching.

    Returns:
        int: Computed result.
    """
    return 42
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0  # No decorator in this function

    def test_function_with_complex_control_flow_and_note_section_passes(self):
        """Test that functions with complex control flow and Note section pass."""
        code = '''
def complex_processing(data):
    """Process data with complex logic.

    Args:
        data: Input data to process.

    Returns:
        List: Processed data.

    Note:
        This function uses complex control flow for data processing.
    """
    result = []
    for item in data:
        if item > 0:
            if item % 2 == 0:
                result.append(item * 2)
            else:
                result.append(item)
        else:
            result.append(0)
    return result
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_complex_control_flow_without_note_section_fails(self):
        """Test that functions with complex control flow without Note section fail."""
        code = '''
def complex_processing(data):
    """Process data with complex logic.

    Args:
        data: Input data to process.

    Returns:
        List: Processed data.
    """
    result = []
    for item in data:
        if item > 0:
            if item % 2 == 0:
                result.append(item * 2)
            else:
                result.append(item)
        else:
            result.append(0)
    return result
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0  # Control flow not complex enough

    def test_simple_function_passes(self):
        """Test that simple functions pass."""
        code = '''
def simple_function(a, b):
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        int: Sum of the two numbers.
    """
    return a + b
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_no_docstring_passes(self):
        """Test that functions without docstrings pass."""
        code = """
def flexible_function(*args):
    return list(args)
"""
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_function_with_special_behavior_and_note_section_passes(self):
        """Test that async functions with special behavior and Note section pass."""
        code = '''
async def async_flexible_function(*args, **kwargs):
    """Async function with variable arguments.

    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.

    Returns:
        Dict: Combined arguments.

    Note:
        This async function handles variable arguments.
    """
    return {"args": args, "kwargs": kwargs}
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_function_with_special_behavior_without_note_section_fails(self):
        """Test that async functions with special behavior without Note section fail."""
        code = '''
async def async_flexible_function(*args, **kwargs):
    """Async function with variable arguments.

    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.

    Returns:
        Dict: Combined arguments.
    """
    return {"args": args, "kwargs": kwargs}
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG214"
        assert (
            "Function with special behavior should have Note section"
            in findings[0].message
        )

    def test_function_with_note_section_dash_format_passes(self):
        """Test that functions with Note section using dash format pass."""
        code = '''
def flexible_function(*args):
    """Process variable number of arguments.

    Args:
        *args: Variable number of arguments to process.

    Returns:
        List: Processed arguments.

    Note - This function can handle any number of arguments.
    """
    return list(args)
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_note_section_space_format_passes(self):
        """Test that functions with Note section using space format pass."""
        code = '''
def flexible_function(*args):
    """Process variable number of arguments.

    Args:
        *args: Variable number of arguments to process.

    Returns:
        List: Processed arguments.

    Note This function can handle any number of arguments.
    """
    return list(args)
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_note_section_newline_format_passes(self):
        """Test that functions with Note section using newline format pass."""
        code = '''
def flexible_function(*args):
    """Process variable number of arguments.

    Args:
        *args: Variable number of arguments to process.

    Returns:
        List: Processed arguments.

    Note
        This function can handle any number of arguments.
    """
    return list(args)
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_multiple_special_behaviors_and_note_section_passes(self):
        """Test that functions with multiple special behaviors and Note section pass."""
        code = '''
def complex_flexible_function(*args, **kwargs):
    """Function with multiple special behaviors.

    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.

    Returns:
        Dict: Combined arguments.

    Note:
        This function combines multiple special behaviors.
    """
    result = {"args": args, "kwargs": kwargs}
    for item in args:
        if item > 0:
            result["positive"] = result.get("positive", 0) + 1
        else:
            result["negative"] = result.get("negative", 0) + 1
    return result
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_multiple_special_behaviors_without_note_section_fails(self):
        """Test that functions with multiple special behaviors without Note section fail."""
        code = '''
def complex_flexible_function(*args, **kwargs):
    """Function with multiple special behaviors.

    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.

    Returns:
        Dict: Combined arguments.
    """
    result = {"args": args, "kwargs": kwargs}
    for item in args:
        if item > 0:
            result["positive"] = result.get("positive", 0) + 1
        else:
            result["negative"] = result.get("negative", 0) + 1
    return result
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG214"
        assert (
            "Function with special behavior should have Note section"
            in findings[0].message
        )

    def test_multiple_functions_with_special_behavior_without_note_sections(self):
        """Test that multiple functions with special behavior without Note sections are all detected."""
        code = '''
def function1(*args):
    """First function with special behavior."""
    return list(args)

def function2(**kwargs):
    """Second function with special behavior."""
    return kwargs
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG214" for f in findings)
        assert all(
            "Function with special behavior should have Note section" in f.message
            for f in findings
        )

    def test_mixed_functions_special_behavior_without_note_section(self):
        """Test mixed functions where only those with special behavior without Note section are detected."""
        code = '''
def simple_function(a, b):
    """Simple function without special behavior."""
    return a + b

def flexible_function(*args):
    """Function with special behavior but no Note section."""
    return list(args)
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG214"
        assert (
            "Function with special behavior should have Note section"
            in findings[0].message
        )
        assert findings[0].symbol == "flexible_function"

    def test_function_with_note_section_and_other_sections_passes(self):
        """Test that functions with Note section and other sections pass."""
        code = '''
def comprehensive_function(*args, **kwargs):
    """Comprehensive function with all sections.

    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.

    Returns:
        Dict: Combined arguments.

    Raises:
        ValueError: When invalid arguments are provided.

    Note:
        This function demonstrates comprehensive documentation.

    Examples:
        >>> result = comprehensive_function(1, 2, key='value')
        >>> 'args' in result
        True
    """
    if not args and not kwargs:
        raise ValueError("At least one argument required")
    
    return {"args": args, "kwargs": kwargs}
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_note_section_case_insensitive_passes(self):
        """Test that functions with Note section (case insensitive) pass."""
        code = '''
def flexible_function(*args):
    """Process variable number of arguments.

    Args:
        *args: Variable number of arguments to process.

    Returns:
        List: Processed arguments.

    NOTE: This function can handle any number of arguments.
    """
    return list(args)
'''
        symbols = self._parse_code(code)
        rule = DG214NoteSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
