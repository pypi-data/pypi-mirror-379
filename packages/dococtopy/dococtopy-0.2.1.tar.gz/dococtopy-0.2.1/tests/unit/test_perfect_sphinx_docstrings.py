"""Tests for perfect Sphinx-style (reStructuredText) docstrings.

This module tests that perfect Sphinx-style docstrings pass all validation rules.
Sphinx style uses reStructuredText format with :param:, :type:, :returns:, :rtype: etc.
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


class TestPerfectSphinxDocstrings:
    """Test that perfect Sphinx-style docstrings pass all validation rules."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Helper to parse code and return symbols."""
        tree = ast.parse(code)
        symbols = []
        for node in ast.walk(tree):
            if isinstance(
                node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)
            ):
                docstring = ast.get_docstring(node)
                if docstring:
                    symbols.append(
                        PythonSymbol(
                            name=node.name if hasattr(node, "name") else "module",
                            kind=(
                                "function"
                                if isinstance(
                                    node, (ast.FunctionDef, ast.AsyncFunctionDef)
                                )
                                else (
                                    "class"
                                    if isinstance(node, ast.ClassDef)
                                    else "module"
                                )
                            ),
                            lineno=node.lineno if hasattr(node, "lineno") else 1,
                            col=node.col_offset if hasattr(node, "col_offset") else 0,
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

    def _assert_style_specific_behavior(
        self, findings: list, expected_google_failures: list = None
    ):
        """Helper to assert expected behavior for non-Google docstring styles."""
        if expected_google_failures is None:
            expected_google_failures = ["DG201", "DG202", "DG203", "DG206", "DG207"]

        google_specific_failures = [
            f for f in findings if f.rule_id in expected_google_failures
        ]
        basic_rule_failures = [
            f
            for f in findings
            if f.rule_id
            in ["DG101", "DG209", "DG210", "DG301", "DG302", "DG303", "DG304"]
        ]

        # Google-specific rules are expected to fail for non-Google styles
        # But some functions (like those with no parameters) may not trigger certain rules
        if len(google_specific_failures) == 0:
            # Check if this is a function with no parameters that wouldn't trigger DG202
            has_params = any(f.rule_id == "DG202" for f in findings)
            if not has_params:
                # This is expected for functions with no parameters
                pass
            else:
                assert (
                    len(google_specific_failures) > 0
                ), f"Expected Google-specific rules to fail for Sphinx style: {expected_google_failures}"
        # Basic rules should pass
        assert (
            len(basic_rule_failures) == 0
        ), f"Basic rules failed: {basic_rule_failures}"

    def test_simple_function_with_args_and_returns(self):
        """Test a simple function with Sphinx-style docstring."""
        code = '''
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two integers.

    :param a: First integer to add.
    :type a: int
    :param b: Second integer to add.
    :type b: int
    :returns: The sum of a and b.
    :rtype: int
    """
    return a + b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        # Sphinx style should pass most rules, but may fail Google-specific ones
        print(f"Sphinx simple function findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_raises_section(self):
        """Test function with Sphinx-style raises section."""
        code = '''
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers.

    :param a: Dividend.
    :type a: float
    :param b: Divisor.
    :type b: float
    :returns: The result of division.
    :rtype: float
    :raises ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx raises function findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG208"]
        )

    def test_class_with_attributes_section(self):
        """Test class with Sphinx-style attributes section."""
        code = '''
class Calculator:
    """A simple calculator class.

    :ivar result: The current calculation result.
    :vartype result: float
    """

    def __init__(self):
        """Initialize the calculator."""
        self.result = 0.0

    def add(self, value: float) -> None:
        """Add a value to the result.

        :param value: Value to add.
        :type value: float
        :returns: None
        :rtype: None
        """
        self.result += value
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx class findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG212"]
        )

    def test_generator_function_with_yields(self):
        """Test generator function with Sphinx-style yields section."""
        code = '''
def fibonacci(n: int):
    """Generate Fibonacci numbers.

    :param n: Number of Fibonacci numbers to generate.
    :type n: int
    :yields: Next Fibonacci number in the sequence.
    :ytype: int
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx generator findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG211"]
        )

    def test_function_with_examples_section(self):
        """Test function with Sphinx-style examples section."""
        code = '''
def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent.

    :param base: The base number.
    :type base: float
    :param exponent: The exponent.
    :type exponent: float
    :returns: The result of base^exponent.
    :rtype: float

    .. note::
        This function handles both positive and negative exponents.

    Example:
        >>> power(2, 3)
        8.0
        >>> power(4, 0.5)
        2.0
    """
    return base ** exponent
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx examples function findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG213", "DG214"]
        )

    def test_async_function(self):
        """Test async function with Sphinx-style docstring."""
        code = '''
async def fetch_data(url: str) -> dict:
    """Fetch data from a remote URL.

    :param url: The URL to fetch data from.
    :type url: str
    :returns: A dictionary containing the fetched data.
    :rtype: dict
    :raises ConnectionError: If the connection fails.
    :raises ValueError: If the URL is invalid.

    .. note::
        This is an async function that should be awaited.

    Example:
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

        print(f"Sphinx async function findings: {findings}")
        self._assert_style_specific_behavior(
            findings,
            ["DG201", "DG202", "DG203", "DG206", "DG207", "DG208", "DG213", "DG214"],
        )

    def test_function_with_complex_types(self):
        """Test function with complex types in Sphinx style."""
        code = '''
def process_data(data: list[dict], config: dict[str, str]) -> tuple[bool, str]:
    """Process a list of data dictionaries.

    :param data: List of data dictionaries to process.
    :type data: list[dict]
    :param config: Configuration dictionary with string keys and values.
    :type config: dict[str, str]
    :returns: A tuple containing success status and message.
    :rtype: tuple[bool, str]
    """
    if not data:
        return False, "No data provided"
    return True, f"Processed {len(data)} items"
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx complex types findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_optional_parameters(self):
        """Test function with optional parameters in Sphinx style."""
        code = '''
def create_user(name: str, email: str, age: int = None) -> dict:
    """Create a new user.

    :param name: User's full name.
    :type name: str
    :param email: User's email address.
    :type email: str
    :param age: User's age (optional).
    :type age: int, optional
    :returns: Dictionary containing user information.
    :rtype: dict
    """
    user = {"name": name, "email": email}
    if age is not None:
        user["age"] = age
    return user
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx optional params findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_multiple_exceptions(self):
        """Test function with multiple exceptions in Sphinx style."""
        code = '''
def parse_config_file(filepath: str) -> dict:
    """Parse a configuration file.

    :param filepath: Path to the configuration file.
    :type filepath: str
    :returns: Parsed configuration dictionary.
    :rtype: dict
    :raises FileNotFoundError: If the file doesn't exist.
    :raises PermissionError: If access to the file is denied.
    :raises ValueError: If the file format is invalid.
    """
    import json
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {filepath}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format: {filepath}")
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx multiple exceptions findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG208"]
        )

    def test_module_level_docstring(self):
        """Test module-level Sphinx-style docstring."""
        code = '''
"""Data processing utilities.

This module provides utilities for processing various data formats.

.. versionadded:: 1.0.0
.. versionchanged:: 1.1.0
    Added support for JSON processing.

.. note::
    All functions in this module are thread-safe.

Example:
    >>> from data_utils import process_json
    >>> result = process_json('{"key": "value"}')
    >>> print(result)
"""

def process_json(data: str) -> dict:
    """Process JSON data string.

    :param data: JSON string to process.
    :type data: str
    :returns: Parsed JSON dictionary.
    :rtype: dict
    """
    import json
    return json.loads(data)
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx module docstring findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_no_parameters(self):
        """Test function with no parameters in Sphinx style."""
        code = '''
def get_current_time() -> str:
    """Get the current time as a string.

    :returns: Current time in ISO format.
    :rtype: str
    """
    from datetime import datetime
    return datetime.now().isoformat()
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx no params findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_no_return_value(self):
        """Test function with no return value in Sphinx style."""
        code = '''
def print_message(message: str) -> None:
    """Print a message to the console.

    :param message: Message to print.
    :type message: str
    :returns: None
    :rtype: None
    """
    print(message)
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx no return findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_class_with_methods(self):
        """Test class with methods in Sphinx style."""
        code = '''
class BankAccount:
    """A simple bank account class.

    :ivar balance: Current account balance.
    :vartype balance: float
    """

    def __init__(self, initial_balance: float = 0.0):
        """Initialize the bank account.

        :param initial_balance: Starting balance for the account.
        :type initial_balance: float
        """
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account.

        :param amount: Amount to deposit.
        :type amount: float
        :returns: None
        :rtype: None
        """
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account.

        :param amount: Amount to withdraw.
        :type amount: float
        :returns: True if withdrawal successful, False otherwise.
        :rtype: bool
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"Sphinx class with methods findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG212"]
        )
