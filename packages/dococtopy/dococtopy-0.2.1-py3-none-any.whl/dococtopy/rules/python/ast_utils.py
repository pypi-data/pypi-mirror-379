"""
Shared AST analysis utilities for Python rules.

This module provides common AST analysis functions used across multiple rules
to eliminate code duplication and provide consistent behavior.
"""

from __future__ import annotations

import ast
from typing import Set

from dococtopy.adapters.python.adapter import PythonSymbol


def extract_function_params(sym: PythonSymbol) -> Set[str]:
    """Extract parameter names from function signature, excluding 'self'.

    Args:
        sym: Python symbol representing a function

    Returns:
        Set of parameter names (excluding 'self')
    """
    if not hasattr(sym, "ast_node") or not isinstance(
        sym.ast_node, (ast.FunctionDef, ast.AsyncFunctionDef)
    ):
        return set()

    params = set()

    # Regular positional arguments
    for arg in sym.ast_node.args.args:
        if arg.arg != "self":  # Skip self parameter
            params.add(arg.arg)

    # *args parameter
    if sym.ast_node.args.vararg:
        params.add(f"*{sym.ast_node.args.vararg.arg}")

    # **kwargs parameter
    if sym.ast_node.args.kwarg:
        params.add(f"**{sym.ast_node.args.kwarg.arg}")

    # Keyword-only arguments
    for arg in sym.ast_node.args.kwonlyargs:
        params.add(arg.arg)

    # Positional-only arguments
    for arg in sym.ast_node.args.posonlyargs:
        params.add(arg.arg)

    return params


def has_return_annotation(sym: PythonSymbol) -> bool:
    """Check if function has return type annotation.

    Args:
        sym: Python symbol representing a function

    Returns:
        True if function has return type annotation
    """
    if not hasattr(sym, "ast_node") or not isinstance(
        sym.ast_node, (ast.FunctionDef, ast.AsyncFunctionDef)
    ):
        return False
    return sym.ast_node.returns is not None


def is_generator_function(sym: PythonSymbol) -> bool:
    """Check if function contains yield statements.

    Args:
        sym: Python symbol representing a function

    Returns:
        True if function contains yield statements
    """
    if not hasattr(sym, "ast_node") or not isinstance(
        sym.ast_node, (ast.FunctionDef, ast.AsyncFunctionDef)
    ):
        return False

    # Walk the entire AST tree to find yield statements
    for node in ast.walk(sym.ast_node):
        if isinstance(node, ast.Yield):
            return True
    return False


def extract_raised_exceptions(sym: PythonSymbol) -> Set[str]:
    """Extract exception types raised in function using visitor pattern.

    Args:
        sym: Python symbol representing a function

    Returns:
        Set of exception type names raised in the function
    """
    if not hasattr(sym, "ast_node") or not isinstance(
        sym.ast_node, (ast.FunctionDef, ast.AsyncFunctionDef)
    ):
        return set()

    exceptions = set()

    class RaiseVisitor(ast.NodeVisitor):
        def visit_Raise(self, node: ast.Raise) -> None:
            if node.exc and isinstance(node.exc, ast.Name):
                exceptions.add(node.exc.id)
            elif (
                node.exc
                and isinstance(node.exc, ast.Call)
                and isinstance(node.exc.func, ast.Name)
            ):
                exceptions.add(node.exc.func.id)

    visitor = RaiseVisitor()
    visitor.visit(sym.ast_node)
    return exceptions


def get_public_attributes(sym: PythonSymbol) -> list[str]:
    """Get public attributes from class definition.

    Args:
        sym: Python symbol representing a class

    Returns:
        List of public attribute names found in the class
    """
    if not hasattr(sym, "ast_node") or not isinstance(sym.ast_node, ast.ClassDef):
        return []

    attrs = []
    # Look for assignments in the entire class AST tree
    for node in ast.walk(sym.ast_node):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Attribute):
                    # Check if it's a self.attr assignment (public attribute)
                    if isinstance(target.value, ast.Name) and target.value.id == "self":
                        if not target.attr.startswith("_"):
                            attrs.append(target.attr)

    # Also look for @property decorated methods
    for node in sym.ast_node.body:
        if isinstance(node, ast.FunctionDef):
            # Check if the function has @property decorator
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name) and decorator.id == "property":
                    if not node.name.startswith("_"):
                        attrs.append(node.name)

    return attrs


def has_special_behavior(sym: PythonSymbol) -> bool:
    """Check if function has special behavior that should be noted.

    Args:
        sym: Python symbol representing a function

    Returns:
        True if function has special behavior patterns
    """
    if not hasattr(sym, "ast_node") or not isinstance(
        sym.ast_node, (ast.FunctionDef, ast.AsyncFunctionDef)
    ):
        return False

    # Check for special patterns
    for node in ast.walk(sym.ast_node):
        # Check for *args or **kwargs
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.args.vararg or node.args.kwarg:
                return True
        # Check for decorators
        if (
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.decorator_list
        ):
            return True
        # Check for complex control flow
        if isinstance(node, (ast.For, ast.While, ast.If)) and len(node.body) > 5:
            return True

    return False


def is_complex_function(sym: PythonSymbol, config: dict | None = None) -> bool:
    """Check if function is complex enough to warrant Examples section.

    Uses cyclomatic complexity and parameter count to determine complexity.
    Supports configurable thresholds for different complexity criteria.

    Args:
        sym: Python symbol representing a function
        config: Optional configuration dict with thresholds:
            - max_params_simple: Max params for simple functions (default: 2)
            - max_params_moderate: Max params for moderate functions (default: 3)
            - max_complexity_simple: Max complexity for simple functions (default: 1)
            - max_complexity_moderate: Max complexity for moderate functions (default: 2)
            - high_complexity_threshold: High complexity threshold (default: 3)
            - many_params_threshold: Many parameters threshold (default: 4)

    Returns:
        True if function is considered complex
    """
    if not hasattr(sym, "ast_node") or not isinstance(
        sym.ast_node, (ast.FunctionDef, ast.AsyncFunctionDef)
    ):
        return False

    # Default configuration
    default_config = {
        "max_params_simple": 2,
        "max_params_moderate": 3,
        "max_complexity_simple": 1,
        "max_complexity_moderate": 2,
        "high_complexity_threshold": 3,
        "many_params_threshold": 4,
    }

    if config is None:
        config = default_config
    else:
        config = {**default_config, **config}

    # Count all types of parameters
    param_count = (
        len(sym.ast_node.args.args)
        + len(sym.ast_node.args.kwonlyargs)
        + len(sym.ast_node.args.posonlyargs)
        + (1 if sym.ast_node.args.vararg else 0)
        + (1 if sym.ast_node.args.kwarg else 0)
    )

    # Calculate cyclomatic complexity
    complexity = _calculate_cyclomatic_complexity(sym.ast_node)

    # Sophisticated complexity detection:
    # 1. Many parameters (regardless of complexity)
    if param_count >= config["many_params_threshold"]:
        return True

    # 2. High cyclomatic complexity (regardless of parameters)
    if complexity >= config["high_complexity_threshold"]:
        return True

    # 3. Moderate parameters + moderate complexity
    if (
        param_count > config["max_params_simple"]
        and complexity > config["max_complexity_simple"]
    ):
        return True

    # 4. Special case: __init__ methods are typically not complex
    if sym.name == "__init__":
        # Only consider __init__ complex if it has many params OR high complexity
        return bool(
            param_count >= config["many_params_threshold"]
            or complexity >= config["high_complexity_threshold"]
        )

    return False


def _calculate_cyclomatic_complexity(node: ast.AST) -> int:
    """Calculate cyclomatic complexity of a function.

    Args:
        node: AST node representing a function

    Returns:
        Cyclomatic complexity score
    """
    complexity = 1  # Base complexity

    for child in ast.walk(node):
        if isinstance(child, (ast.If, ast.While, ast.For, ast.AsyncFor)):
            complexity += 1
        elif isinstance(child, ast.ExceptHandler):
            complexity += 1
        elif isinstance(child, ast.BoolOp):
            # Count each operator in boolean expressions
            complexity += len(child.values) - 1
        elif isinstance(child, ast.Assert):
            complexity += 1

    return complexity
