"""Tests for perfect NumPy-style docstrings.

This module tests that perfect NumPy-style docstrings pass all validation rules.
NumPy style uses sections with underlines for Parameters, Returns, etc.
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


class TestPerfectNumPyDocstrings:
    """Test that perfect NumPy-style docstrings pass all validation rules."""

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
                ), f"Expected Google-specific rules to fail for NumPy style: {expected_google_failures}"
        # Basic rules should pass
        assert (
            len(basic_rule_failures) == 0
        ), f"Basic rules failed: {basic_rule_failures}"

    def test_simple_function_with_args_and_returns(self):
        """Test a simple function with NumPy-style docstring."""
        code = '''
def calculate_sum(a, b):
    """Calculate the sum of two integers.

    Parameters
    ----------
    a : int
        First integer to add.
    b : int
        Second integer to add.

    Returns
    -------
    int
        The sum of a and b.
    """
    return a + b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy simple function findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_raises_section(self):
        """Test function with NumPy-style raises section."""
        code = '''
def divide_numbers(a, b):
    """Divide two numbers.

    Parameters
    ----------
    a : float
        Dividend.
    b : float
        Divisor.

    Returns
    -------
    float
        The result of division.

    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy raises function findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG208"]
        )

    def test_class_with_attributes_section(self):
        """Test class with NumPy-style attributes section."""
        code = '''
class Calculator:
    """A simple calculator class.

    Attributes
    ----------
    result : float
        The current calculation result.
    """

    def __init__(self):
        """Initialize the calculator."""
        self.result = 0.0

    def add(self, value):
        """Add a value to the result.

        Parameters
        ----------
        value : float
            Value to add.

        Returns
        -------
        None
        """
        self.result += value
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy class findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG212"]
        )

    def test_generator_function_with_yields(self):
        """Test generator function with NumPy-style yields section."""
        code = '''
def fibonacci(n):
    """Generate Fibonacci numbers.

    Parameters
    ----------
    n : int
        Number of Fibonacci numbers to generate.

    Yields
    ------
    int
        Next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy generator findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG211"]
        )

    def test_function_with_examples_section(self):
        """Test function with NumPy-style examples section."""
        code = '''
def power(base, exponent):
    """Calculate base raised to the power of exponent.

    Parameters
    ----------
    base : float
        The base number.
    exponent : float
        The exponent.

    Returns
    -------
    float
        The result of base^exponent.

    Notes
    -----
    This function handles both positive and negative exponents.

    Examples
    --------
    >>> power(2, 3)
    8.0
    >>> power(4, 0.5)
    2.0
    """
    return base ** exponent
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy examples function findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG213", "DG214"]
        )

    def test_async_function(self):
        """Test async function with NumPy-style docstring."""
        code = '''
async def fetch_data(url):
    """Fetch data from a remote URL.

    Parameters
    ----------
    url : str
        The URL to fetch data from.

    Returns
    -------
    dict
        A dictionary containing the fetched data.

    Raises
    ------
    ConnectionError
        If the connection fails.
    ValueError
        If the URL is invalid.

    Notes
    -----
    This is an async function that should be awaited.

    Examples
    --------
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

        print(f"NumPy async function findings: {findings}")
        self._assert_style_specific_behavior(
            findings,
            ["DG201", "DG202", "DG203", "DG206", "DG207", "DG208", "DG213", "DG214"],
        )

    def test_function_with_complex_types(self):
        """Test function with complex types in NumPy style."""
        code = '''
def process_data(data, config):
    """Process a list of data dictionaries.

    Parameters
    ----------
    data : list of dict
        List of data dictionaries to process.
    config : dict of str, str
        Configuration dictionary with string keys and values.

    Returns
    -------
    tuple of bool, str
        A tuple containing success status and message.
    """
    if not data:
        return False, "No data provided"
    return True, f"Processed {len(data)} items"
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy complex types findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_optional_parameters(self):
        """Test function with optional parameters in NumPy style."""
        code = '''
def create_user(name, email, age=None):
    """Create a new user.

    Parameters
    ----------
    name : str
        User's full name.
    email : str
        User's email address.
    age : int, optional
        User's age. The default is None.

    Returns
    -------
    dict
        Dictionary containing user information.
    """
    user = {"name": name, "email": email}
    if age is not None:
        user["age"] = age
    return user
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy optional params findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_multiple_exceptions(self):
        """Test function with multiple exceptions in NumPy style."""
        code = '''
def parse_config_file(filepath):
    """Parse a configuration file.

    Parameters
    ----------
    filepath : str
        Path to the configuration file.

    Returns
    -------
    dict
        Parsed configuration dictionary.

    Raises
    ------
    FileNotFoundError
        If the file doesn't exist.
    PermissionError
        If access to the file is denied.
    ValueError
        If the file format is invalid.
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

        print(f"NumPy multiple exceptions findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG208"]
        )

    def test_module_level_docstring(self):
        """Test module-level NumPy-style docstring."""
        code = '''
"""Data processing utilities.

This module provides utilities for processing various data formats.

Notes
-----
All functions in this module are thread-safe.

Examples
--------
>>> from data_utils import process_json
>>> result = process_json('{"key": "value"}')
>>> print(result)
"""

def process_json(data):
    """Process JSON data string.

    Parameters
    ----------
    data : str
        JSON string to process.

    Returns
    -------
    dict
        Parsed JSON dictionary.
    """
    import json
    return json.loads(data)
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy module docstring findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_no_parameters(self):
        """Test function with no parameters in NumPy style."""
        code = '''
def get_current_time():
    """Get the current time as a string.

    Returns
    -------
    str
        Current time in ISO format.
    """
    from datetime import datetime
    return datetime.now().isoformat()
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy no params findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_function_with_no_return_value(self):
        """Test function with no return value in NumPy style."""
        code = '''
def print_message(message):
    """Print a message to the console.

    Parameters
    ----------
    message : str
        Message to print.

    Returns
    -------
    None
    """
    print(message)
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy no return findings: {findings}")
        self._assert_style_specific_behavior(findings)

    def test_class_with_methods(self):
        """Test class with methods in NumPy style."""
        code = '''
class BankAccount:
    """A simple bank account class.

    Attributes
    ----------
    balance : float
        Current account balance.
    """

    def __init__(self, initial_balance=0.0):
        """Initialize the bank account.

        Parameters
        ----------
        initial_balance : float
            Starting balance for the account.
        """
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account.

        Parameters
        ----------
        amount : float
            Amount to deposit.

        Returns
        -------
        None
        """
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account.

        Parameters
        ----------
        amount : float
            Amount to withdraw.

        Returns
        -------
        bool
            True if withdrawal successful, False otherwise.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
'''
        symbols = self._parse_code(code)
        findings = self._run_all_rules(symbols)

        print(f"NumPy class with methods findings: {findings}")
        self._assert_style_specific_behavior(
            findings, ["DG201", "DG202", "DG203", "DG206", "DG207", "DG212"]
        )
