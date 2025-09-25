"""Tests for CLI helper functions."""

import os
from unittest.mock import Mock, patch

import pytest
from rich.console import Console

from dococtopy.cli.main import (
    _create_llm_config,
    _handle_interactive_changes,
    _handle_non_interactive_changes,
    _parse_rule_ids,
    _print_verbose_config,
    _process_files,
)


class TestParseRuleIds:
    """Test the _parse_rule_ids helper function."""

    def test_parse_rule_ids_with_rule(self):
        """Test parsing comma-separated rule IDs."""
        with patch("dococtopy.cli.main.console") as mock_console:
            result = _parse_rule_ids("DG101,DG202,DG301", verbose=True)

            assert result == {"DG101", "DG202", "DG301"}
            mock_console.print.assert_called_once_with(
                "[dim]Targeting rules: DG101, DG202, DG301[/dim]"
            )

    def test_parse_rule_ids_with_rule_no_verbose(self):
        """Test parsing rule IDs without verbose output."""
        with patch("dococtopy.cli.main.console") as mock_console:
            result = _parse_rule_ids("DG101,DG202", verbose=False)

            assert result == {"DG101", "DG202"}
            mock_console.print.assert_not_called()

    def test_parse_rule_ids_with_single_rule(self):
        """Test parsing a single rule ID."""
        with patch("dococtopy.cli.main.console") as mock_console:
            result = _parse_rule_ids("DG101", verbose=True)

            assert result == {"DG101"}
            mock_console.print.assert_called_once_with(
                "[dim]Targeting rules: DG101[/dim]"
            )

    def test_parse_rule_ids_with_whitespace(self):
        """Test parsing rule IDs with whitespace."""
        with patch("dococtopy.cli.main.console") as mock_console:
            result = _parse_rule_ids(" DG101 , DG202 ", verbose=True)

            assert result == {" DG101 ", " DG202 "}
            mock_console.print.assert_called_once_with(
                "[dim]Targeting rules:  DG101 ,  DG202 [/dim]"
            )

    def test_parse_rule_ids_none(self):
        """Test parsing None rule input."""
        with patch("dococtopy.cli.main.console") as mock_console:
            result = _parse_rule_ids(None, verbose=True)

            assert result is None
            mock_console.print.assert_not_called()

    def test_parse_rule_ids_empty_string(self):
        """Test parsing empty string rule input."""
        with patch("dococtopy.cli.main.console") as mock_console:
            result = _parse_rule_ids("", verbose=True)

            assert result is None
            mock_console.print.assert_not_called()


class TestCreateLlmConfig:
    """Test the _create_llm_config helper function."""

    def test_create_llm_config_basic(self):
        """Test creating basic LLM config."""
        with patch("dococtopy.cli.main.LLMConfig") as mock_llm_config_class:
            mock_config = Mock()
            mock_config.api_key = None
            mock_llm_config_class.return_value = mock_config

            result = _create_llm_config("openai", "gpt-4", "https://api.openai.com")

            mock_llm_config_class.assert_called_once_with(
                provider="openai",
                model="gpt-4",
                base_url="https://api.openai.com",
            )
            assert result == mock_config

    def test_create_llm_config_with_openai_api_key(self):
        """Test creating LLM config with OpenAI API key from environment."""
        with (
            patch("dococtopy.cli.main.LLMConfig") as mock_llm_config_class,
            patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}),
        ):

            mock_config = Mock()
            mock_config.api_key = None
            mock_llm_config_class.return_value = mock_config

            result = _create_llm_config("openai", "gpt-4", None)

            assert result == mock_config
            assert mock_config.api_key == "test-key"

    def test_create_llm_config_with_anthropic_api_key(self):
        """Test creating LLM config with Anthropic API key from environment."""
        with (
            patch("dococtopy.cli.main.LLMConfig") as mock_llm_config_class,
            patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"}),
        ):

            mock_config = Mock()
            mock_config.api_key = None
            mock_llm_config_class.return_value = mock_config

            result = _create_llm_config("anthropic", "claude-3", None)

            assert result == mock_config
            assert mock_config.api_key == "test-key"

    def test_create_llm_config_with_existing_api_key(self):
        """Test creating LLM config when API key already exists."""
        with (
            patch("dococtopy.cli.main.LLMConfig") as mock_llm_config_class,
            patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}),
        ):

            mock_config = Mock()
            mock_config.api_key = "existing-key"
            mock_llm_config_class.return_value = mock_config

            result = _create_llm_config("openai", "gpt-4", None)

            assert result == mock_config
            assert mock_config.api_key == "existing-key"  # Should not be overwritten

    def test_create_llm_config_with_ollama_provider(self):
        """Test creating LLM config with Ollama provider (no API key needed)."""
        with patch("dococtopy.cli.main.LLMConfig") as mock_llm_config_class:
            mock_config = Mock()
            mock_config.api_key = None
            mock_llm_config_class.return_value = mock_config

            result = _create_llm_config("ollama", "llama2", "http://localhost:11434")

            assert result == mock_config
            assert mock_config.api_key is None  # Ollama doesn't need API key


class TestPrintVerboseConfig:
    """Test the _print_verbose_config helper function."""

    def test_print_verbose_config_basic(self):
        """Test printing basic verbose configuration."""
        with patch("dococtopy.cli.main.console") as mock_console:
            _print_verbose_config(
                "openai", "gpt-4", "https://api.openai.com", True, False, 10
            )

            expected_calls = [
                "[dim]LLM Provider: openai[/dim]",
                "[dim]LLM Model: gpt-4[/dim]",
                "[dim]LLM Base URL: https://api.openai.com[/dim]",
                "[dim]Dry run: True[/dim]",
                "[dim]Interactive: False[/dim]",
                "[dim]Max changes: 10[/dim]",
            ]

            assert mock_console.print.call_count == 6
            for i, expected_call in enumerate(expected_calls):
                assert mock_console.print.call_args_list[i][0][0] == expected_call

    def test_print_verbose_config_no_base_url(self):
        """Test printing verbose configuration without base URL."""
        with patch("dococtopy.cli.main.console") as mock_console:
            _print_verbose_config("anthropic", "claude-3", None, False, True, None)

            expected_calls = [
                "[dim]LLM Provider: anthropic[/dim]",
                "[dim]LLM Model: claude-3[/dim]",
                "[dim]Dry run: False[/dim]",
                "[dim]Interactive: True[/dim]",
            ]

            assert mock_console.print.call_count == 4
            for i, expected_call in enumerate(expected_calls):
                assert mock_console.print.call_args_list[i][0][0] == expected_call


class TestProcessFiles:
    """Test the _process_files helper function."""

    def test_process_files_no_files(self):
        """Test processing when no files are provided."""
        mock_report = Mock()
        mock_report.files = []
        mock_engine = Mock()

        result = _process_files(mock_report, mock_engine, False, False)

        assert result == 0
        mock_engine.remediate_file.assert_not_called()

    def test_process_files_with_files_no_findings(self):
        """Test processing files with no findings."""
        mock_file_result = Mock()
        mock_file_result.findings = []
        mock_report = Mock()
        mock_report.files = [mock_file_result]
        mock_engine = Mock()

        result = _process_files(mock_report, mock_engine, False, False)

        assert result == 0
        mock_engine.remediate_file.assert_not_called()

    def test_process_files_with_findings_non_interactive(self):
        """Test processing files with findings in non-interactive mode."""
        mock_file_result = Mock()
        mock_file_result.findings = [Mock()]
        mock_file_result.path = Mock()
        mock_report = Mock()
        mock_report.files = [mock_file_result]
        mock_engine = Mock()

        mock_changes = [Mock(), Mock()]
        mock_engine.remediate_file.return_value = mock_changes

        with (
            patch(
                "dococtopy.adapters.python.adapter.load_symbols_from_file"
            ) as mock_load_symbols,
            patch("dococtopy.cli.main._handle_non_interactive_changes") as mock_handle,
        ):

            mock_load_symbols.return_value = [Mock()]
            mock_handle.return_value = 2

            result = _process_files(mock_report, mock_engine, False, False)

            assert result == 2
            mock_engine.remediate_file.assert_called_once()
            mock_handle.assert_called_once_with(
                mock_changes, mock_file_result, mock_engine, False
            )

    def test_process_files_with_findings_interactive(self):
        """Test processing files with findings in interactive mode."""
        mock_file_result = Mock()
        mock_file_result.findings = [Mock()]
        mock_file_result.path = Mock()
        mock_report = Mock()
        mock_report.files = [mock_file_result]
        mock_engine = Mock()

        mock_changes = [Mock()]
        mock_engine.remediate_file.return_value = mock_changes

        with (
            patch(
                "dococtopy.adapters.python.adapter.load_symbols_from_file"
            ) as mock_load_symbols,
            patch("dococtopy.cli.main._handle_interactive_changes") as mock_handle,
        ):

            mock_load_symbols.return_value = [Mock()]
            mock_handle.return_value = 1

            result = _process_files(mock_report, mock_engine, True, True)

            assert result == 1
            mock_engine.remediate_file.assert_called_once()
            mock_handle.assert_called_once_with(
                mock_changes, mock_file_result, mock_engine, True
            )


class TestHandleInteractiveChanges:
    """Test the _handle_interactive_changes helper function."""

    def test_handle_interactive_changes_with_approved_changes(self):
        """Test handling interactive changes with approved changes."""
        mock_changes = [Mock(), Mock()]
        mock_file_result = Mock()
        mock_file_result.path = Mock()
        mock_file_result.path.read_text.return_value = "original content"
        mock_engine = Mock()

        with (
            patch(
                "dococtopy.remediation.interactive.InteractiveReviewer"
            ) as mock_reviewer_class,
            patch(
                "dococtopy.remediation.interactive.InteractiveReviewOptions"
            ) as mock_options_class,
            patch("dococtopy.cli.main.console") as mock_console,
        ):

            mock_reviewer = Mock()
            mock_reviewer.review_changes.return_value = mock_changes
            mock_reviewer_class.return_value = mock_reviewer

            result = _handle_interactive_changes(
                mock_changes, mock_file_result, mock_engine, False
            )

            assert result == 2
            mock_engine.apply_changes.assert_called_once_with(
                mock_file_result.path, mock_changes
            )
            mock_console.print.assert_called_with("[green]Applied 2 changes[/green]")
            mock_reviewer.show_summary.assert_called_once()

    def test_handle_interactive_changes_dry_run(self):
        """Test handling interactive changes in dry run mode."""
        mock_changes = [Mock()]
        mock_file_result = Mock()
        mock_file_result.path = Mock()
        mock_file_result.path.read_text.return_value = "original content"
        mock_engine = Mock()

        with (
            patch(
                "dococtopy.remediation.interactive.InteractiveReviewer"
            ) as mock_reviewer_class,
            patch(
                "dococtopy.remediation.interactive.InteractiveReviewOptions"
            ) as mock_options_class,
            patch("dococtopy.cli.main.console") as mock_console,
        ):

            mock_reviewer = Mock()
            mock_reviewer.review_changes.return_value = mock_changes
            mock_reviewer_class.return_value = mock_reviewer

            result = _handle_interactive_changes(
                mock_changes, mock_file_result, mock_engine, True
            )

            assert result == 1
            mock_engine.apply_changes.assert_not_called()
            mock_console.print.assert_called_with(
                "[yellow]Would apply 1 changes (dry run)[/yellow]"
            )

    def test_handle_interactive_changes_no_approved_changes(self):
        """Test handling interactive changes with no approved changes."""
        mock_changes = [Mock(), Mock()]
        mock_file_result = Mock()
        mock_file_result.path = Mock()
        mock_file_result.path.read_text.return_value = "original content"
        mock_engine = Mock()

        with (
            patch(
                "dococtopy.remediation.interactive.InteractiveReviewer"
            ) as mock_reviewer_class,
            patch(
                "dococtopy.remediation.interactive.InteractiveReviewOptions"
            ) as mock_options_class,
            patch("dococtopy.cli.main.console") as mock_console,
        ):

            mock_reviewer = Mock()
            mock_reviewer.review_changes.return_value = None
            mock_reviewer_class.return_value = mock_reviewer

            result = _handle_interactive_changes(
                mock_changes, mock_file_result, mock_engine, False
            )

            assert result == 0
            mock_engine.apply_changes.assert_not_called()
            mock_console.print.assert_not_called()


class TestHandleNonInteractiveChanges:
    """Test the _handle_non_interactive_changes helper function."""

    def test_handle_non_interactive_changes_with_changes(self):
        """Test handling non-interactive changes with changes."""
        mock_changes = [Mock(), Mock()]
        mock_changes[0].symbol_name = "test_function"
        mock_changes[0].symbol_kind = "function"
        mock_changes[0].issues_addressed = ["DG101", "DG202"]
        mock_changes[1].symbol_name = "test_class"
        mock_changes[1].symbol_kind = "class"
        mock_changes[1].issues_addressed = ["DG301"]

        mock_file_result = Mock()
        mock_engine = Mock()

        with patch("dococtopy.cli.main.console") as mock_console:
            result = _handle_non_interactive_changes(
                mock_changes, mock_file_result, mock_engine, False
            )

            assert result == 2
            mock_engine.apply_changes.assert_called_once_with(
                mock_file_result.path, mock_changes
            )
            mock_console.print.assert_any_call("[green]Applied 2 changes[/green]")
            mock_console.print.assert_any_call(
                "\n[cyan]Change: test_function (function)[/cyan]"
            )
            mock_console.print.assert_any_call("[yellow]Issues: DG101, DG202[/yellow]")
            mock_console.print.assert_any_call("[green]Applied fix[/green]")

    def test_handle_non_interactive_changes_dry_run(self):
        """Test handling non-interactive changes in dry run mode."""
        mock_changes = [Mock()]
        mock_changes[0].symbol_name = "test_function"
        mock_changes[0].symbol_kind = "function"
        mock_changes[0].issues_addressed = ["DG101"]

        mock_file_result = Mock()
        mock_engine = Mock()

        with patch("dococtopy.cli.main.console") as mock_console:
            result = _handle_non_interactive_changes(
                mock_changes, mock_file_result, mock_engine, True
            )

            assert result == 1
            mock_engine.apply_changes.assert_not_called()
            mock_console.print.assert_any_call(
                "[yellow]Would apply 1 changes (dry run)[/yellow]"
            )
            mock_console.print.assert_any_call(
                "\n[cyan]Change: test_function (function)[/cyan]"
            )
            mock_console.print.assert_any_call("[yellow]Issues: DG101[/yellow]")
            mock_console.print.assert_any_call(
                "[dim]Dry run - no changes applied[/dim]"
            )

    def test_handle_non_interactive_changes_no_changes(self):
        """Test handling non-interactive changes with no changes."""
        mock_changes = []
        mock_file_result = Mock()
        mock_engine = Mock()

        with patch("dococtopy.cli.main.console") as mock_console:
            result = _handle_non_interactive_changes(
                mock_changes, mock_file_result, mock_engine, False
            )

            assert result == 0
            mock_engine.apply_changes.assert_not_called()
            mock_console.print.assert_not_called()
