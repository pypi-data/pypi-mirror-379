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
    if not hasattr(sym, "ast_node") or not isinstance(sym.ast_node, ast.FunctionDef):
        return set()

    params = set()
    for arg in sym.ast_node.args.args:
        if arg.arg != "self":  # Skip self parameter
            params.add(arg.arg)
    return params


def has_return_annotation(sym: PythonSymbol) -> bool:
    """Check if function has return type annotation.

    Args:
        sym: Python symbol representing a function

    Returns:
        True if function has return type annotation
    """
    if not hasattr(sym, "ast_node") or not isinstance(sym.ast_node, ast.FunctionDef):
        return False
    return sym.ast_node.returns is not None


def is_generator_function(sym: PythonSymbol) -> bool:
    """Check if function contains yield statements.

    Args:
        sym: Python symbol representing a function

    Returns:
        True if function contains yield statements
    """
    if not hasattr(sym, "ast_node") or not isinstance(sym.ast_node, ast.FunctionDef):
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
    if not hasattr(sym, "ast_node") or not isinstance(sym.ast_node, ast.FunctionDef):
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
    return attrs


def has_special_behavior(sym: PythonSymbol) -> bool:
    """Check if function has special behavior that should be noted.

    Args:
        sym: Python symbol representing a function

    Returns:
        True if function has special behavior patterns
    """
    if not hasattr(sym, "ast_node") or not isinstance(sym.ast_node, ast.FunctionDef):
        return False

    # Check for special patterns
    for node in ast.walk(sym.ast_node):
        # Check for *args or **kwargs
        if isinstance(node, ast.FunctionDef):
            if node.args.vararg or node.args.kwarg:
                return True
        # Check for decorators
        if isinstance(node, ast.FunctionDef) and node.decorator_list:
            return True
        # Check for complex control flow
        if isinstance(node, (ast.For, ast.While, ast.If)) and len(node.body) > 5:
            return True

    return False


def is_complex_function(sym: PythonSymbol) -> bool:
    """Check if function is complex enough to warrant Examples section.

    Args:
        sym: Python symbol representing a function

    Returns:
        True if function is considered complex
    """
    if not hasattr(sym, "ast_node") or not isinstance(sym.ast_node, ast.FunctionDef):
        return False

    # Consider complex if it has more than 3 parameters or more than 20 lines
    param_count = len(sym.ast_node.args.args)
    line_count = (
        sym.ast_node.end_lineno - sym.ast_node.lineno if sym.ast_node.end_lineno else 0
    )

    return param_count > 3 or line_count > 20
