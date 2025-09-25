"""Tests for perfect Google-style docstrings that should always pass inspection.

This module contains examples of immaculate Google-style docstrings that should
never trigger any of our validation rules. These serve as regression tests to
ensure our rules don't have false positives.
"""

import ast
from pathlib import Path

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.formatting import (
    DG301SummaryStyle,
    DG302BlankLineAfterSummary,
    DG303ContentQuality,
    DG304DocstringDelimiterStyle,
)
from dococtopy.rules.python.google_style import (
    DG201GoogleStyleParseError,
    DG202ParamMissingFromDocstring,
    DG203ExtraParamInDocstring,
    DG204ReturnsSectionMissing,
    DG205RaisesSectionValidation,
    DG206ArgsSectionFormat,
    DG207ReturnsSectionFormat,
    DG208RaisesSectionFormat,
    DG209SummaryLength,
    DG210DocstringIndentation,
    DG211YieldsSectionValidation,
    DG212AttributesSectionValidation,
    DG213ExamplesSectionValidation,
    DG214NoteSectionValidation,
)
from dococtopy.rules.python.missing_docstrings import DG101MissingDocstring


class TestPerfectGoogleDocstrings:
    """Test that perfect Google-style docstrings pass all validation rules."""

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

    def _run_all_rules(self, symbols: list[PythonSymbol]) -> list:
        """Run all validation rules on the symbols."""
        all_rules = [
            DG101MissingDocstring(),
            DG201GoogleStyleParseError(),
            DG202ParamMissingFromDocstring(),
            DG203ExtraParamInDocstring(),
            DG204ReturnsSectionMissing(),
            DG205RaisesSectionValidation(),
            DG206ArgsSectionFormat(),
            DG207ReturnsSectionFormat(),
            DG208RaisesSectionFormat(),
            DG209SummaryLength(),
            DG210DocstringIndentation(),
            DG211YieldsSectionValidation(),
            DG212AttributesSectionValidation(),
            DG213ExamplesSectionValidation(),
            DG214NoteSectionValidation(),
            DG301SummaryStyle(),
            DG302BlankLineAfterSummary(),
            DG303ContentQuality(),
            DG304DocstringDelimiterStyle(),
        ]

        all_findings = []
        for rule in all_rules:
            findings = rule.check(symbols=symbols)
            all_findings.extend(findings)

        return all_findings

    def test_simple_function_with_args_and_returns(self):
        """Test a simple function with Args and Returns sections."""
        code = '''
def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    """
    return length * width
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_raises_section(self):
        """Test a function with Args, Returns, and Raises sections."""
        code = '''
def divide_numbers(a: float, b: float) -> float:
    """Divides two numbers.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The result of the division.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_class_with_attributes_section(self):
        """Test a class with Attributes section."""
        code = '''
class Rectangle:
    """A rectangle with length and width.

    Attributes:
        length: The length of the rectangle.
        width: The width of the rectangle.
    """

    def __init__(self, length: float, width: float):
        """Initialize the rectangle.

        Args:
            length: The length of the rectangle.
            width: The width of the rectangle.
        """
        self.length = length
        self.width = width
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_generator_function_with_yields(self):
        """Test a generator function with Yields section."""
        code = '''
def fibonacci(n: int) -> Iterator[int]:
    """Generates Fibonacci numbers up to n.

    Args:
        n: The maximum number of Fibonacci numbers to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    from typing import Iterator
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_examples_section(self):
        """Test a function with Examples section."""
        code = '''
def find_max(numbers: list[int]) -> int:
    """Finds the maximum value in a list of numbers.

    Args:
        numbers: A list of integers.

    Returns:
        The maximum value in the list.

    Examples:
        >>> find_max([1, 5, 3, 9, 2])
        9
        >>> find_max([-1, -5, -3])
        -1
    """
    return max(numbers)
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_note_section(self):
        """Test a function with Note section."""
        code = '''
def process_data(data: str) -> str:
    """Processes input data and returns cleaned output.

    Args:
        data: Raw input data to process.

    Returns:
        Cleaned and processed data.

    Note:
        This function performs extensive validation and may take
        several seconds to complete for large datasets.
    """
    return data.strip().lower()
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_async_function(self):
        """Test an async function with proper docstring."""
        code = '''
async def fetch_data(url: str) -> dict:
    """Fetches data from a remote URL.

    Args:
        url: The URL to fetch data from.

    Returns:
        A dictionary containing the fetched data.

    Raises:
        ConnectionError: If the connection fails.
        ValueError: If the URL is invalid.

    Examples:
        >>> import asyncio
        >>> data = asyncio.run(fetch_data("https://api.example.com/data"))
        >>> print(data["status"])
    """
    import aiohttp
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    except aiohttp.ClientError as e:
        raise ConnectionError(f"Connection failed: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid URL: {e}")
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_complex_types(self):
        """Test a function with complex type annotations."""
        code = '''
def merge_dicts(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    """Merges two dictionaries with string keys and integer values.

    Args:
        dict1: First dictionary to merge.
        dict2: Second dictionary to merge.

    Returns:
        A new dictionary containing all key-value pairs from both inputs.
    """
    result = dict1.copy()
    result.update(dict2)
    return result
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_optional_parameters(self):
        """Test a function with optional parameters."""
        code = '''
def greet_user(name: str, greeting: str = "Hello") -> str:
    """Greets a user with a customizable message.

    Args:
        name: The name of the user to greet.
        greeting: The greeting message to use. Defaults to "Hello".

    Returns:
        A formatted greeting message.
    """
    return f"{greeting}, {name}!"
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_multiple_exceptions(self):
        """Test a function that raises multiple types of exceptions."""
        code = '''
def parse_config_file(filepath: str) -> dict:
    """Parses a configuration file and returns its contents.

    Args:
        filepath: Path to the configuration file.

    Returns:
        A dictionary containing the parsed configuration.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        PermissionError: If the file cannot be read due to permissions.
        ValueError: If the file contains invalid configuration data.

    Examples:
        >>> config = parse_config_file("config.json")
        >>> print(config["database_url"])
    """
    import json
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {filepath}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {filepath}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file: {e}")
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_module_level_docstring(self):
        """Test a module with a proper module-level docstring."""
        code = '''
"""A module for mathematical calculations.

This module provides various mathematical functions for common
calculations including area, volume, and statistical operations.
"""

def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    return a + b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_no_parameters(self):
        """Test a function with no parameters."""
        code = '''
def get_current_timestamp() -> float:
    """Returns the current Unix timestamp.

    Returns:
        The current timestamp as a floating point number.
    """
    import time
    return time.time()
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_function_with_no_return_value(self):
        """Test a function with no return value."""
        code = '''
def print_message(message: str) -> None:
    """Prints a message to the console.

    Args:
        message: The message to print.

    Returns:
        None.
    """
    print(message)
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"

    def test_class_with_methods(self):
        """Test a class with multiple methods."""
        code = '''
class Calculator:
    """A simple calculator for basic arithmetic operations.

    Attributes:
        result: The current result of calculations.
    """

    def __init__(self):
        """Initialize the calculator with zero result."""
        self.result = 0

    def add(self, value: float) -> None:
        """Adds a value to the current result.

        Args:
            value: The value to add to the result.

        Returns:
            None.
        """
        self.result += value

    def get_result(self) -> float:
        """Returns the current result.

        Returns:
            The current calculation result.
        """
        return self.result
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        assert len(findings) == 0, f"Perfect docstring failed validation: {findings}"
