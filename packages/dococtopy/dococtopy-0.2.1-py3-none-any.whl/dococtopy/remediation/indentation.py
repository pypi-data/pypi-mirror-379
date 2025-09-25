"""Docstring indentation normalization utilities.

This module provides functions to normalize docstring indentation to ensure
consistent formatting regardless of how the LLM generates the content.
"""

from __future__ import annotations

from typing import List, Optional


def normalize_docstring_indentation(
    docstring: str, base_indent: str = "", preserve_relative_indentation: bool = True
) -> str:
    """
    Normalize docstring indentation to match the function/class indentation.

    Args:
        docstring: The docstring content to normalize
        base_indent: The base indentation to apply (default: no indentation)
        preserve_relative_indentation: Whether to preserve relative indentation between lines

    Returns:
        The docstring with normalized indentation

    Examples:
        >>> normalize_docstring_indentation("Summary line.\\n\\nArgs:\\n    param: Description")
        'Summary line.\\n\\nArgs:\\n    param: Description'

        >>> normalize_docstring_indentation("  Summary line.\\n  \\n  Args:\\n      param: Description")
        'Summary line.\\n\\nArgs:\\n    param: Description'

        >>> normalize_docstring_indentation("Summary line.\\n\\n    Args:\\n        param: Description")
        'Summary line.\\n\\nArgs:\\n    param: Description'
    """
    if docstring is None or not docstring.strip():
        return docstring

    lines = docstring.splitlines()
    if not lines:
        return docstring

    # Handle single line docstrings
    if len(lines) == 1:
        return lines[0].strip()

    # Find the minimum indentation (excluding empty lines and lines with only whitespace)
    min_indent = float("inf")
    for line in lines:
        if line.strip():  # Skip empty lines
            indent = len(line) - len(line.lstrip())
            min_indent = min(min_indent, indent)

    # If no content lines found, return original
    if min_indent == float("inf"):
        return docstring

    # Normalize indentation
    normalized_lines = []
    for line in lines:
        if line.strip():  # Non-empty line
            if preserve_relative_indentation:
                # Calculate relative indentation from the minimum
                current_indent = len(line) - len(line.lstrip())
                relative_indent = current_indent - min_indent
                content = line.lstrip()  # Remove all original indentation

                # Calculate how many 4-space levels of relative indentation
                relative_levels = max(0, relative_indent // 4)
                new_indent = base_indent + ("    " * relative_levels)
                normalized_lines.append(f"{new_indent}{content}")
            else:
                # Simple normalization - all lines get base_indent
                content = line.lstrip()  # Remove all original indentation
                normalized_lines.append(f"{base_indent}{content}")
        else:  # Empty line
            normalized_lines.append("")

    return "\n".join(normalized_lines)


def detect_docstring_indentation_issues(docstring: str) -> List[str]:
    """
    Detect indentation issues in a docstring.

    Args:
        docstring: The docstring to analyze

    Returns:
        List of indentation issue descriptions
    """
    if docstring is None or not docstring.strip():
        return []

    lines = docstring.splitlines()
    if len(lines) < 2:
        return []

    issues = []

    # Find the minimum indentation (excluding empty lines)
    min_indent = float("inf")
    for line in lines:
        if line.strip():
            indent = len(line) - len(line.lstrip())
            min_indent = min(min_indent, indent)

    if min_indent == float("inf"):
        return []

    # Check for inconsistent indentation - only flag if there are significant differences
    for i, line in enumerate(lines):
        if line.strip():
            current_indent = len(line) - len(line.lstrip())
            # Only flag if the difference is not a multiple of 4 (normal section indentation)
            if current_indent != min_indent and (current_indent - min_indent) % 4 != 0:
                issues.append(
                    f"Line {i + 1}: inconsistent indentation (expected {min_indent}, got {current_indent})"
                )

    # Check for mixed tabs and spaces
    has_tabs = any("\t" in line for line in lines)
    has_spaces = any(" " in line and line.strip() for line in lines)
    if has_tabs and has_spaces:
        issues.append("Mixed tabs and spaces in indentation")

    return issues


def get_docstring_base_indent(docstring: str) -> str:
    """
    Get the base indentation level of a docstring.

    Args:
        docstring: The docstring to analyze

    Returns:
        The base indentation string (spaces or tabs)
    """
    if docstring is None or not docstring.strip():
        return ""

    lines = docstring.splitlines()
    min_indent = float("inf")
    min_indent_line = None

    for line in lines:
        if line.strip():
            indent = len(line) - len(line.lstrip())
            if indent < min_indent:
                min_indent = indent
                min_indent_line = line

    if min_indent_line is None:
        return ""

    return min_indent_line[:min_indent]


def is_docstring_indentation_consistent(docstring: str) -> bool:
    """
    Check if docstring indentation is consistent.

    Args:
        docstring: The docstring to check

    Returns:
        True if indentation is consistent, False otherwise
    """
    return len(detect_docstring_indentation_issues(docstring)) == 0
