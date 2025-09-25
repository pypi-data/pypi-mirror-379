"""Tests for the specific DG210 warning scenario we fixed.

These tests verify that the specific issue we encountered - where valid Google-style
docstrings were incorrectly flagged as having inconsistent indentation - is now
properly handled.
"""

from __future__ import annotations

import ast
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.remediation.engine import RemediationEngine
from dococtopy.remediation.validation import (
    DocstringFixer,
    DocstringValidator,
    TrivialFixDetector,
)
from dococtopy.rules.python.google_style import DG210DocstringIndentation


class TestDG210WarningScenario:
    """Test the specific DG210 warning scenario we fixed."""

    def test_llm_generated_google_style_docstring_passes_validation(self):
        """Test that LLM-generated Google-style docstrings pass validation."""
        # This is the exact type of docstring the LLM was generating
        llm_generated_docstring = """Calculate the nth Fibonacci number.

Args:
    n: The index (n >= 0) of the Fibonacci sequence to compute.

Returns:
    The nth Fibonacci number.
"""

        # Create a proper AST node
        ast_node = ast.FunctionDef(
            name="calculate_fibonacci",
            args=ast.arguments(
                posonlyargs=[],
                args=[ast.arg(arg="n", annotation=None)],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=[],
            decorator_list=[],
            returns=ast.Constant(value=None),  # Add return annotation
            lineno=1,
            col_offset=0,
        )

        symbol = PythonSymbol(
            name="calculate_fibonacci",
            kind="function",
            lineno=1,
            col=0,
            docstring=llm_generated_docstring,
            ast_node=ast_node,
        )

        validator = DocstringValidator()
        result = validator.validate_docstring(symbol, llm_generated_docstring)

        # Should pass validation (no DG210 issues)
        assert result.is_valid
        assert len(result.findings) == 0

    def test_llm_generated_class_docstring_with_attributes_passes_validation(self):
        """Test that LLM-generated class docstrings with Attributes section pass validation."""
        # This is the exact type of docstring the LLM was generating for classes
        llm_generated_docstring = """UserManager handles operations related to managing user accounts.

This class provides interfaces to create, retrieve, update, and delete users.

Attributes:
    user_repository (object): Repository for persisting and retrieving user data.
    authentication_service (object): Service used to authenticate users.
    role_manager (object): Component that manages user roles and permissions.
"""

        # Create a proper AST node
        ast_node = ast.ClassDef(
            name="UserManager",
            bases=[],
            keywords=[],
            body=[],
            decorator_list=[],
            lineno=1,
            col_offset=0,
        )

        symbol = PythonSymbol(
            name="UserManager",
            kind="class",
            lineno=1,
            col=0,
            docstring=llm_generated_docstring,
            ast_node=ast_node,
        )

        validator = DocstringValidator()
        result = validator.validate_docstring(symbol, llm_generated_docstring)

        # Should pass validation (no DG210 issues)
        assert result.is_valid
        assert len(result.findings) == 0

    def test_llm_generated_method_docstring_passes_validation(self):
        """Test that LLM-generated method docstrings pass validation."""
        # This is the exact type of docstring the LLM was generating for methods
        llm_generated_docstring = """Initialize the instance with the given database URL.

Args:
    database_url: The database connection URL to be used by this instance.
"""

        # Create a proper AST node
        ast_node = ast.FunctionDef(
            name="__init__",
            args=ast.arguments(
                posonlyargs=[],
                args=[
                    ast.arg(arg="self", annotation=None),
                    ast.arg(arg="database_url", annotation=None),
                ],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=[],
            decorator_list=[],
            returns=None,
            lineno=1,
            col_offset=0,
        )

        symbol = PythonSymbol(
            name="__init__",
            kind="function",
            lineno=1,
            col=0,
            docstring=llm_generated_docstring,
            ast_node=ast_node,
        )

        validator = DocstringValidator()
        result = validator.validate_docstring(symbol, llm_generated_docstring)

        # Should pass validation (no DG210 issues)
        assert result.is_valid
        assert len(result.findings) == 0

    def test_docstring_fixer_with_google_style_output(self):
        """Test that DocstringFixer accepts Google-style LLM output."""
        # Create a symbol with missing docstring
        symbol = PythonSymbol(
            name="calculate_fibonacci",
            kind="function",
            lineno=1,
            col=0,
            docstring="",
            ast_node=ast.FunctionDef(
                name="calculate_fibonacci",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[ast.arg(arg="n", annotation=None)],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                ),
                body=[],
                decorator_list=[],
                returns=ast.Constant(value=None),
                lineno=1,
                col_offset=0,
            ),
        )

        # Create findings for missing docstring
        findings = [
            Finding(
                rule_id="DG101",
                level=FindingLevel.ERROR,
                message="Function 'calculate_fibonacci' is missing a docstring",
                symbol="calculate_fibonacci",
                location=Location(line=1, column=0),
            )
        ]

        # Mock LLM client that returns Google-style docstring
        mock_llm = Mock()
        mock_llm.generate_docstring.return_value = """Calculate the nth Fibonacci number.

Args:
    n: The index (n >= 0) of the Fibonacci sequence to compute.

Returns:
    The nth Fibonacci number.
"""

        # Create fixer
        validator = DocstringValidator()
        trivial_detector = TrivialFixDetector()
        fixer = DocstringFixer(validator, trivial_detector)

        # Mock options
        mock_options = Mock()
        mock_options.verbose = False

        with patch.object(fixer, "options", mock_options):
            # Test the fix
            new_docstring, applied_fixes, used_llm = fixer.fix_docstring(
                symbol=symbol,
                original_findings=findings,
                llm_client=mock_llm,
                file_path=Path("test.py"),
            )

        # Should succeed on first attempt (no retries needed)
        assert new_docstring
        assert "Calculate the nth Fibonacci number" in new_docstring
        assert "Args:" in new_docstring
        assert "Returns:" in new_docstring
        assert used_llm
        assert len(applied_fixes) == 1
        assert "LLM fix attempt 1" in applied_fixes[0]

        # Should only call LLM once (no retries)
        assert mock_llm.generate_docstring.call_count == 1

    def test_remediation_engine_with_google_style_output(self):
        """Test that RemediationEngine accepts Google-style LLM output."""
        # Create a symbol with missing docstring
        symbol = PythonSymbol(
            name="calculate_fibonacci",
            kind="function",
            lineno=1,
            col=0,
            docstring="",
            ast_node=ast.FunctionDef(
                name="calculate_fibonacci",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[ast.arg(arg="n", annotation=None)],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                ),
                body=[],
                decorator_list=[],
                returns=ast.Constant(value=None),
                lineno=1,
                col_offset=0,
            ),
        )

        # Create findings for missing docstring
        findings = [
            Finding(
                rule_id="DG101",
                level=FindingLevel.ERROR,
                message="Function 'calculate_fibonacci' is missing a docstring",
                symbol="calculate_fibonacci",
                location=Location(line=1, column=0),
            )
        ]

        # Mock LLM client that returns Google-style docstring
        mock_llm = Mock()
        mock_llm.generate_docstring.return_value = """Calculate the nth Fibonacci number.

Args:
    n: The index (n >= 0) of the Fibonacci sequence to compute.

Returns:
    The nth Fibonacci number.
"""

        # Create remediation engine with mocked LLM
        mock_config = Mock()
        mock_options = Mock()
        mock_options.verbose = False
        mock_options.rule_ids = None

        # Mock LLM config to prevent real LLM initialization
        mock_llm_config = Mock()
        mock_llm_config.provider = "openai"
        mock_llm_config.model = "gpt-4"
        mock_llm_config.api_key = "test-key"
        mock_options.llm_config = mock_llm_config

        engine = RemediationEngine(mock_options, mock_config)

        # Replace the LLM client with our mock
        engine.llm_client = mock_llm

        # Test remediation
        result = engine.remediate_symbol(symbol, findings, Path("test.py"))

        # Should succeed and create a change
        assert result is not None
        assert result.symbol_name == "calculate_fibonacci"
        assert result.change_type == "added"
        assert "Calculate the nth Fibonacci number" in result.new_docstring
        assert "Args:" in result.new_docstring
        assert "Returns:" in result.new_docstring

        # Should only call LLM once (no retries)
        assert mock_llm.generate_docstring.call_count == 1

    def test_multiple_llm_generated_docstrings_pass_validation(self):
        """Test that multiple LLM-generated docstrings all pass DG210 validation."""
        # Test cases based on the actual LLM output we encountered
        test_cases = [
            # Function docstring
            (
                "calculate_fibonacci",
                "function",
                """Calculate the nth Fibonacci number.
    
    Args:
        n: The index (n >= 0) of the Fibonacci sequence to compute.
    
    Returns:
        The nth Fibonacci number.
    """,
            ),
            # Class docstring
            (
                "UserManager",
                "class",
                """UserManager handles operations related to managing user accounts.
    
    This class provides interfaces to create, retrieve, update, and delete users.
    
    Attributes:
        user_repository (object): Repository for persisting and retrieving user data.
        authentication_service (object): Service used to authenticate users.
        role_manager (object): Component that manages user roles and permissions.
    """,
            ),
            # Method docstring
            (
                "__init__",
                "function",
                """Initialize the instance with the given database URL.
    
    Args:
        database_url: The database connection URL to be used by this instance.
    """,
            ),
        ]

        validator = DocstringValidator()

        for name, kind, docstring in test_cases:
            if kind == "function":
                ast_node = ast.FunctionDef(
                    name=name,
                    args=ast.arguments(
                        posonlyargs=[],
                        args=[ast.arg(arg="n", annotation=None)],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[],
                    decorator_list=[],
                    returns=ast.Constant(value=None),
                    lineno=1,
                    col_offset=0,
                )
            else:
                ast_node = ast.ClassDef(
                    name=name,
                    bases=[],
                    keywords=[],
                    body=[],
                    decorator_list=[],
                    lineno=1,
                    col_offset=0,
                )

            symbol = PythonSymbol(
                name=name,
                kind=kind,
                lineno=1,
                col=0,
                docstring=docstring,
                ast_node=ast_node,
            )

            # Test only DG210 rule (indentation)
            dg210_rule = DG210DocstringIndentation()
            findings = dg210_rule.check(symbols=[symbol])

            # All should pass DG210 validation (no indentation issues)
            assert (
                len(findings) == 0
            ), f"Docstring for {name} should pass DG210 validation:\n{docstring}\nFindings: {findings}"

    def test_old_dg210_rule_would_have_failed(self):
        """Test that the old DG210 rule would have incorrectly failed these docstrings."""
        # This test documents what the old behavior was
        # The old rule required ALL lines to have the same indentation
        # But Google-style docstrings have different indentation levels

        google_style_docstring = """Calculate the nth Fibonacci number.

Args:
    n: The index (n >= 0) of the Fibonacci sequence to compute.

Returns:
    The nth Fibonacci number.
"""

        # Parse the docstring lines to show the indentation levels
        lines = google_style_docstring.split("\n")

        # Find the base indentation (first content line)
        first_content_line = None
        for i, line in enumerate(lines):
            if line.strip() and not line.strip().startswith('"""'):
                first_content_line = i
                break

        assert first_content_line is not None

        base_indent = len(lines[first_content_line]) - len(
            lines[first_content_line].lstrip()
        )

        # Check indentation levels
        indent_levels = set()
        for line in lines[first_content_line:]:
            if line.strip() and not line.strip().startswith('"""'):
                indent = len(line) - len(line.lstrip())
                indent_levels.add(indent)

        # Google-style docstrings have multiple indentation levels
        # - Summary line: base_indent
        # - Section headers: base_indent
        # - Section content: base_indent + 4
        assert (
            len(indent_levels) > 1
        ), "Google-style docstrings should have multiple indentation levels"

        # The old rule would have failed because it expected all lines to have the same indentation
        # But our new rule correctly allows this structure
        symbol = PythonSymbol(
            name="calculate_fibonacci",
            kind="function",
            lineno=1,
            col=0,
            docstring=google_style_docstring,
            ast_node=ast.FunctionDef(
                name="calculate_fibonacci",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[ast.arg(arg="n", annotation=None)],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                ),
                body=[],
                decorator_list=[],
                returns=ast.Constant(value=None),
                lineno=1,
                col_offset=0,
            ),
        )

        validator = DocstringValidator()
        result = validator.validate_docstring(symbol, google_style_docstring)

        # New rule should pass
        assert result.is_valid
        assert len(result.findings) == 0
