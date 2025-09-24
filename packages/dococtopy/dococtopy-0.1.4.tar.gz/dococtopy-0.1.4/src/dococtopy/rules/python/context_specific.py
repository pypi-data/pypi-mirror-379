"""
Context-specific docstring rules for Python.

This module contains rules that apply specialized docstring requirements
based on the context or purpose of the code:

- DG401: Test function docstring style
- DG402: Public API function documentation
- DG403: Exception documentation completeness
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.registry import register


@dataclass
class DG401TestFunctionDocstringStyle:
    """Check that test functions have descriptive docstrings.

    Test functions should have clear docstrings that explain what they're testing.
    This improves test readability and debugging.
    """

    id: str = "DG401"
    name: str = "Test function docstring style"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Check if this is a test function
            if not self._is_test_function(sym):
                continue

            # Check if the docstring is descriptive enough
            if not self._has_descriptive_docstring(sym):
                findings.append(
                    Finding(  # type: ignore[call-arg]
                        rule_id=self.id,
                        level=FindingLevel.WARNING,
                        message="Test function should have a descriptive docstring explaining what it tests",
                        symbol=sym.name,
                        location=Location(line=sym.lineno, column=sym.col),
                    )
                )

        return findings

    def _is_test_function(self, sym: PythonSymbol) -> bool:
        """Check if a function is a test function."""
        return sym.name.startswith("test_") or "test" in sym.name.lower()

    def _has_descriptive_docstring(self, sym: PythonSymbol) -> bool:
        """Check if the docstring is descriptive enough for a test function."""
        if not sym.docstring:
            return False

        # Get the first line of the docstring (summary)
        first_line = sym.docstring.strip().splitlines()[0].strip()

        # Check if it's descriptive (not just "Test something" or empty)
        if not first_line:
            return False

        # Check for common non-descriptive patterns (exact matches or very short)
        non_descriptive_patterns = [
            "test",
            "test function",
            "test method",
            "test case",
            "unit test",
            "integration test",
        ]

        first_line_lower = first_line.lower()

        # Check for exact matches with non-descriptive patterns
        for pattern in non_descriptive_patterns:
            if first_line_lower == pattern:
                return False

        # Check minimum length (should be more than just "Test X")
        if len(first_line) < 20:
            return False

        return True


@dataclass
class DG402PublicAPIFunctionDocumentation:
    """Check that public API functions have comprehensive documentation.

    Public API functions should have complete docstrings with Args, Returns,
    and Raises sections to provide clear usage guidance.
    """

    id: str = "DG402"
    name: str = "Public API function documentation"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Check if this is a public API function
            if not self._is_public_api_function(sym):
                continue

            # Check if the docstring has required sections
            missing_sections = self._get_missing_sections(sym)
            if missing_sections:
                findings.append(
                    Finding(  # type: ignore[call-arg]
                        rule_id=self.id,
                        level=FindingLevel.WARNING,
                        message=f"Public API function should have {', '.join(missing_sections)} section(s)",
                        symbol=sym.name,
                        location=Location(line=sym.lineno, column=sym.col),
                    )
                )

        return findings

    def _is_public_api_function(self, sym: PythonSymbol) -> bool:
        """Check if a function is part of the public API."""
        name = sym.name

        # Skip private functions
        if name.startswith("_"):
            return False

        # Skip test functions
        if name.startswith("test_") or "test" in name.lower():
            return False

        # Skip dunder methods
        if name.startswith("__") and name.endswith("__"):
            return False

        # Skip internal/helper functions (common patterns)
        internal_patterns = [
            "_internal",
            "_helper",
            "_util",
            "_private",
            "internal_",
            "helper_",
            "util_",
        ]

        for pattern in internal_patterns:
            if pattern in name.lower():
                return False

        return True

    def _get_missing_sections(self, sym: PythonSymbol) -> List[str]:
        """Get list of missing required sections for public API functions."""
        missing = []

        if not sym.docstring:
            return ["Args", "Returns", "Raises"]

        docstring_lower = sym.docstring.lower()

        # Check for Args section (if function has parameters)
        if hasattr(sym, "ast_node") and sym.ast_node and hasattr(sym.ast_node, "args"):
            if sym.ast_node.args.args and "args:" not in docstring_lower:
                missing.append("Args")

        # Check for Returns section
        if "returns:" not in docstring_lower:
            missing.append("Returns")

        # Check for Raises section (recommended for public APIs)
        if "raises:" not in docstring_lower:
            missing.append("Raises")

        return missing


@dataclass
class DG403ExceptionDocumentationCompleteness:
    """Check that functions document all exceptions they raise.

    Functions that raise exceptions should document them in the Raises section
    to help users handle errors appropriately.
    """

    id: str = "DG403"
    name: str = "Exception documentation completeness"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Extract exceptions raised in the function
            raised_exceptions = self._extract_raised_exceptions(sym)
            if not raised_exceptions:
                continue

            # Check if exceptions are documented
            documented_exceptions = self._extract_documented_exceptions(sym)
            missing_exceptions = raised_exceptions - documented_exceptions

            if missing_exceptions:
                findings.append(
                    Finding(  # type: ignore[call-arg]
                        rule_id=self.id,
                        level=FindingLevel.WARNING,
                        message=f"Function raises {', '.join(missing_exceptions)} but doesn't document them in Raises section",
                        symbol=sym.name,
                        location=Location(line=sym.lineno, column=sym.col),
                    )
                )

        return findings

    def _extract_raised_exceptions(self, sym: PythonSymbol) -> set[str]:
        """Extract exception types raised in function using AST analysis."""
        if not hasattr(sym, "ast_node") or not sym.ast_node:
            return set()

        exceptions = set()

        class RaiseVisitor:
            def visit_Raise(self, node):
                if node.exc and hasattr(node.exc, "id"):
                    exceptions.add(node.exc.id)
                elif (
                    node.exc
                    and hasattr(node.exc, "func")
                    and hasattr(node.exc.func, "id")
                ):
                    exceptions.add(node.exc.func.id)

        # Simple AST walking for raise statements
        import ast

        for node in ast.walk(sym.ast_node):
            if isinstance(node, ast.Raise):
                if node.exc and isinstance(node.exc, ast.Name):
                    exceptions.add(node.exc.id)
                elif (
                    node.exc
                    and isinstance(node.exc, ast.Call)
                    and isinstance(node.exc.func, ast.Name)
                ):
                    exceptions.add(node.exc.func.id)

        return exceptions

    def _extract_documented_exceptions(self, sym: PythonSymbol) -> set[str]:
        """Extract exception types documented in the docstring."""
        if not sym.docstring:
            return set()

        documented = set()

        # Simple parsing of Raises section
        lines = sym.docstring.splitlines()
        in_raises_section = False

        for line in lines:
            line = line.strip()

            if line.lower().startswith("raises:"):
                in_raises_section = True
                continue

            if in_raises_section:
                # Check if we've moved to a new section (non-indented line that's not empty)
                if line and not line.startswith(" ") and not line.startswith("\t"):
                    # Check if this looks like a new section header
                    if any(
                        line.lower().startswith(section)
                        for section in [
                            "args:",
                            "returns:",
                            "yields:",
                            "attributes:",
                            "note:",
                            "example:",
                        ]
                    ):
                        break

                # Extract exception name from line
                if ":" in line:
                    exception_name = line.split(":")[0].strip()
                    if exception_name and exception_name[0].isupper():
                        documented.add(exception_name)

        return documented


# Register all context-specific rules
register(DG401TestFunctionDocstringStyle())
register(DG402PublicAPIFunctionDocumentation())
register(DG403ExceptionDocumentationCompleteness())
