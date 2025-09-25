"""Tests for cyclomatic complexity calculation in ast_utils."""

import ast

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.ast_utils import (
    _calculate_cyclomatic_complexity,
    is_complex_function,
)


class TestCyclomaticComplexity:
    """Test cases for cyclomatic complexity calculation."""

    def test_simple_function_complexity_1(self):
        """Test that simple functions have complexity 1."""
        code = """
def simple_function():
    return 42
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 1

    def test_function_with_if_statement_complexity_2(self):
        """Test that functions with if statements have complexity 2."""
        code = """
def function_with_if(value):
    if value > 0:
        return value
    return 0
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 2

    def test_function_with_multiple_if_statements(self):
        """Test that functions with multiple if statements have higher complexity."""
        code = """
def function_with_multiple_ifs(value):
    if value > 0:
        return value
    if value < 0:
        return -value
    return 0
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 3

    def test_function_with_for_loop_complexity_2(self):
        """Test that functions with for loops have complexity 2."""
        code = """
def function_with_for(items):
    for item in items:
        print(item)
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 2

    def test_function_with_while_loop_complexity_2(self):
        """Test that functions with while loops have complexity 2."""
        code = """
def function_with_while(n):
    while n > 0:
        n -= 1
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 2

    def test_function_with_try_except_complexity_2(self):
        """Test that functions with try-except have complexity 2."""
        code = """
def function_with_try_except():
    try:
        risky_operation()
    except Exception:
        handle_error()
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 2

    def test_function_with_multiple_except_handlers(self):
        """Test that functions with multiple except handlers have higher complexity."""
        code = """
def function_with_multiple_excepts():
    try:
        risky_operation()
    except ValueError:
        handle_value_error()
    except TypeError:
        handle_type_error()
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 3

    def test_function_with_boolean_operators(self):
        """Test that functions with boolean operators increase complexity."""
        code = """
def function_with_boolean_ops(a, b, c):
    if a and b and c:
        return True
    return False
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        # Base complexity (1) + if statement (1) + boolean operators (2) = 4
        assert complexity == 4

    def test_function_with_assert_statement(self):
        """Test that functions with assert statements increase complexity."""
        code = """
def function_with_assert(value):
    assert value > 0
    return value
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        assert complexity == 2

    def test_function_with_nested_conditionals(self):
        """Test that nested conditionals increase complexity."""
        code = """
def function_with_nested_conditionals(data):
    if data:
        if len(data) > 0:
            return data[0]
        else:
            return None
    return None
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        # Base (1) + outer if (1) + inner if (1) = 3 (else doesn't add complexity)
        assert complexity == 3

    def test_function_with_complex_logic(self):
        """Test a function with multiple types of complexity."""
        code = """
def complex_function(items, threshold):
    if not items:
        return []
    
    result = []
    for item in items:
        if item > threshold:
            try:
                processed = process_item(item)
                result.append(processed)
            except ValueError:
                continue
        else:
            result.append(item)
    
    return result
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        # Base (1) + if not items (1) + for loop (1) + if item > threshold (1) + except (1) = 5 (try doesn't add complexity)
        assert complexity == 5

    def test_async_function_complexity(self):
        """Test that async functions are handled correctly."""
        code = """
async def async_function(items):
    for item in items:
        if item > 0:
            yield item
"""
        tree = ast.parse(code)
        func_node = tree.body[0]
        complexity = _calculate_cyclomatic_complexity(func_node)
        # Base (1) + for loop (1) + if statement (1) = 3
        assert complexity == 3


class TestIsComplexFunction:
    """Test cases for is_complex_function using cyclomatic complexity."""

    def _create_symbol(self, code: str) -> PythonSymbol:
        """Helper to create a PythonSymbol from code."""
        tree = ast.parse(code)
        func_node = tree.body[0]
        return PythonSymbol(
            name=func_node.name,
            kind="function",
            lineno=func_node.lineno,
            col=func_node.col_offset,
            docstring=ast.get_docstring(func_node),
            ast_node=func_node,
        )

    def test_simple_function_not_complex(self):
        """Test that simple functions are not considered complex."""
        code = """
def add(a, b):
    return a + b
"""
        sym = self._create_symbol(code)
        assert not is_complex_function(sym)

    def test_function_with_many_parameters_complex(self):
        """Test that functions with many parameters are considered complex."""
        code = """
def many_params(a, b, c, d):
    return a + b + c + d
"""
        sym = self._create_symbol(code)
        assert is_complex_function(sym)  # 4 params > 3, should be complex

    def test_function_with_conditional_logic_complex(self):
        """Test that functions with conditional logic are considered complex."""
        code = """
def conditional_function(value):
    if value > 0:
        return value
    elif value < 0:
        return -value
    else:
        return 0
"""
        sym = self._create_symbol(code)
        assert is_complex_function(sym)  # complexity=3 > 2, should be complex

    def test_function_with_moderate_params_and_logic_complex(self):
        """Test that functions with moderate params and logic are complex."""
        code = """
def moderate_function(a, b, c):
    if a > b:
        return c
    return a + b
"""
        sym = self._create_symbol(code)
        assert is_complex_function(
            sym
        )  # 3 params, complexity=2, complex with new sophisticated logic

    def test_function_with_loops_not_complex(self):
        """Test that functions with simple loops are not considered complex."""
        code = """
def loop_function(items):
    result = []
    for item in items:
        result.append(item * 2)
    return result
"""
        sym = self._create_symbol(code)
        assert not is_complex_function(
            sym
        )  # complexity=2, not complex with new threshold

    def test_function_with_exception_handling_not_complex(self):
        """Test that functions with simple exception handling are not complex."""
        code = """
def exception_function(data):
    try:
        return process_data(data)
    except ValueError:
        return None
"""
        sym = self._create_symbol(code)
        assert not is_complex_function(
            sym
        )  # complexity=2, not complex with new threshold

    def test_async_function_with_complexity(self):
        """Test that async functions with complexity are detected."""
        code = """
async def async_complex_function(items):
    results = []
    for item in items:
        if item > 0:
            results.append(item)
    return results
"""
        sym = self._create_symbol(code)
        assert is_complex_function(sym)  # complexity=3 > 2, should be complex

    def test_function_with_kwargs_not_complex(self):
        """Test that functions with **kwargs are counted in parameter count."""
        code = """
def kwargs_function(a, b, **kwargs):
    return a + b
"""
        sym = self._create_symbol(code)
        assert not is_complex_function(sym)  # 3 params, not complex with new threshold

    def test_function_with_args_not_complex(self):
        """Test that functions with *args are counted in parameter count."""
        code = """
def args_function(*args):
    return sum(args)
"""
        sym = self._create_symbol(code)
        assert not is_complex_function(sym)  # 1 param, complexity=1, not complex

    def test_function_with_kwonlyargs_not_complex(self):
        """Test that functions with keyword-only args are counted."""
        code = """
def kwonly_function(a, *, b, c):
    return a + b + c
"""
        sym = self._create_symbol(code)
        assert not is_complex_function(sym)  # 3 params, not complex with new threshold

    def test_function_with_posonlyargs_not_complex(self):
        """Test that functions with positional-only args are counted."""
        code = """
def posonly_function(a, b, /, c):
    return a + b + c
"""
        sym = self._create_symbol(code)
        assert not is_complex_function(sym)  # 3 params, not complex with new threshold

    def test_function_with_mixed_parameter_types(self):
        """Test functions with mixed parameter types."""
        code = """
def mixed_params(a, b, /, c, d, *, e, f, **kwargs):
    return a + b + c + d + e + f
"""
        sym = self._create_symbol(code)
        assert is_complex_function(sym)  # 7 params > 3, should be complex

    def test_function_with_no_docstring_still_checked(self):
        """Test that functions without docstrings are still checked for complexity."""
        code = """
def no_docstring_function(a, b, c, d):
    return a + b + c + d
"""
        sym = self._create_symbol(code)
        assert is_complex_function(sym)  # 4 params > 3, should be complex

    def test_class_method_not_checked(self):
        """Test that non-function symbols are not checked."""
        code = """
class TestClass:
    def method(self):
        return 42
"""
        tree = ast.parse(code)
        class_node = tree.body[0]
        sym = PythonSymbol(
            name=class_node.name,
            kind="class",
            lineno=class_node.lineno,
            col=class_node.col_offset,
            docstring=ast.get_docstring(class_node),
            ast_node=class_node,
        )
        assert not is_complex_function(sym)
