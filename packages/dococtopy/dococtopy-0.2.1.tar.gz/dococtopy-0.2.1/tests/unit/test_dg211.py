"""Tests for DG211YieldsSectionValidation rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG211YieldsSectionValidation


class TestDG211YieldsSectionValidation:
    """Test cases for DG211YieldsSectionValidation rule."""

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

    def test_generator_function_with_yields_section_passes(self):
        """Test that generator functions with Yields section pass."""
        code = '''
def fibonacci(n):
    """Generate Fibonacci sequence.

    Args:
        n: Number of Fibonacci numbers to generate.

    Yields:
        int: Next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_without_yields_section_fails(self):
        """Test that generator functions without Yields section fail."""
        code = '''
def fibonacci(n):
    """Generate Fibonacci sequence.

    Args:
        n: Number of Fibonacci numbers to generate.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG211"
        assert "Generator function should have Yields section" in findings[0].message
        assert findings[0].level.value == "warning"

    def test_non_generator_function_passes(self):
        """Test that non-generator functions pass."""
        code = '''
def add_numbers(a, b):
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
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_with_no_docstring_passes(self):
        """Test that generator functions without docstrings pass."""
        code = """
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
"""
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_generator_function_with_yields_section_passes(self):
        """Test that async generator functions with Yields section pass."""
        code = '''
async def async_fibonacci(n):
    """Generate Fibonacci sequence asynchronously.

    Args:
        n: Number of Fibonacci numbers to generate.

    Yields:
        int: Next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_generator_function_without_yields_section_fails(self):
        """Test that async generator functions without Yields section fail."""
        code = '''
async def async_fibonacci(n):
    """Generate Fibonacci sequence asynchronously.

    Args:
        n: Number of Fibonacci numbers to generate.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG211"
        assert "Generator function should have Yields section" in findings[0].message
        assert findings[0].level.value == "warning"

    def test_generator_function_with_complex_yields_section_passes(self):
        """Test that generator functions with complex Yields section pass."""
        code = '''
def process_items(items):
    """Process items and yield results.

    Args:
        items: List of items to process.

    Yields:
        Dict[str, Any]: Processed item with metadata.
    """
    for item in items:
        result = {"processed": True, "data": item}
        yield result
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_with_multiple_yield_statements_passes(self):
        """Test that generator functions with multiple yield statements pass."""
        code = '''
def alternating_values():
    """Generate alternating values.

    Yields:
        str: Alternating 'even' and 'odd' values.
    """
    while True:
        yield "even"
        yield "odd"
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_with_conditional_yield_passes(self):
        """Test that generator functions with conditional yield pass."""
        code = '''
def filtered_items(items, condition):
    """Filter items based on condition.

    Args:
        items: List of items to filter.
        condition: Function to test items.

    Yields:
        Any: Items that pass the condition.
    """
    for item in items:
        if condition(item):
            yield item
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_with_nested_yield_passes(self):
        """Test that generator functions with nested yield pass."""
        code = '''
def nested_generator():
    """Generate nested values.

    Yields:
        int: Nested integer values.
    """
    for i in range(3):
        for j in range(3):
            yield i * 3 + j
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_with_yield_from_passes(self):
        """Test that generator functions with yield from pass."""
        code = '''
def flatten_nested(nested_list):
    """Flatten a nested list.

    Args:
        nested_list: List that may contain nested lists.

    Yields:
        Any: Flattened items from the nested list.
    """
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_nested(item)
        else:
            yield item
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_with_yield_in_try_except_passes(self):
        """Test that generator functions with yield in try-except pass."""
        code = '''
def safe_generator(items):
    """Safely generate items with error handling.

    Args:
        items: List of items to process.

    Yields:
        Any: Successfully processed items.
    """
    for item in items:
        try:
            yield process_item(item)
        except Exception:
            continue
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_generator_function_with_yield_in_loop_passes(self):
        """Test that generator functions with yield in loop pass."""
        code = '''
def countdown(n):
    """Count down from n to 1.

    Args:
        n: Starting number for countdown.

    Yields:
        int: Countdown numbers from n to 1.
    """
    while n > 0:
        yield n
        n -= 1
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_generator_functions_without_yields_section(self):
        """Test that multiple generator functions without Yields section are all detected."""
        code = '''
def fibonacci(n):
    """Generate Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def primes(n):
    """Generate prime numbers."""
    for i in range(2, n):
        if is_prime(i):
            yield i
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG211" for f in findings)
        assert all(
            "Generator function should have Yields section" in f.message
            for f in findings
        )

    def test_mixed_functions_generator_without_yields_section(self):
        """Test mixed functions where only generator without Yields section is detected."""
        code = '''
def fibonacci(n):
    """Generate Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def add_numbers(a, b):
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
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG211"
        assert "Generator function should have Yields section" in findings[0].message
        assert findings[0].symbol == "fibonacci"

    def test_generator_function_with_yields_section_and_other_sections_passes(self):
        """Test that generator functions with Yields section and other sections pass."""
        code = '''
def complex_generator(data):
    """Complex generator with multiple sections.

    Args:
        data: Input data to process.

    Yields:
        Dict[str, Any]: Processed data with metadata.

    Raises:
        ValueError: When data is invalid.

    Note:
        This generator processes data in chunks.
    """
    if not data:
        raise ValueError("Data cannot be empty")
    
    for chunk in data:
        yield {"processed": chunk, "timestamp": time.time()}
'''
        symbols = self._parse_code(code)
        rule = DG211YieldsSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
