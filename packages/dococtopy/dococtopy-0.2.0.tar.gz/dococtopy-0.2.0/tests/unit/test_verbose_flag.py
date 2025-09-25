"""Tests for the verbose flag functionality."""

import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest


class TestVerboseFlag:
    """Test verbose flag functionality."""

    def test_scan_verbose_flag_help(self):
        """Test that verbose flag appears in scan help."""
        result = subprocess.run(
            [sys.executable, "-m", "dococtopy", "scan", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Check for verbose flag (handle ANSI escape codes)
        assert "verbose" in result.stdout
        assert "-v" in result.stdout
        assert "Enable verbose output" in result.stdout

    def test_fix_verbose_flag_help(self):
        """Test that verbose flag appears in fix help."""
        result = subprocess.run(
            [sys.executable, "-m", "dococtopy", "fix", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Check for verbose flag (handle ANSI escape codes)
        assert "verbose" in result.stdout
        assert "-v" in result.stdout
        assert "Enable verbose output" in result.stdout

    def test_scan_verbose_output(self, tmp_path):
        """Test that scan command produces verbose output."""
        # Create a test file with missing docstring
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [sys.executable, "-m", "dococtopy", "scan", str(tmp_path), "--verbose"],
            capture_output=True,
            text=True,
        )

        # Should show verbose output
        assert "Loading config from: pyproject.toml" in result.stdout
        assert "Scanning paths:" in result.stdout
        assert "Cache enabled:" in result.stdout
        assert "Changed only:" in result.stdout
        assert "Found" in result.stdout and "findings across" in result.stdout
        assert "Cache hits:" in result.stdout
        assert "Files processed:" in result.stdout

    def test_scan_verbose_short_flag(self, tmp_path):
        """Test that scan command works with short verbose flag."""
        # Create a test file with missing docstring
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [sys.executable, "-m", "dococtopy", "scan", str(tmp_path), "-v"],
            capture_output=True,
            text=True,
        )

        # Should show verbose output
        assert "Loading config from: pyproject.toml" in result.stdout
        assert "Scanning paths:" in result.stdout

    def test_fix_verbose_output(self, tmp_path):
        """Test that fix command produces verbose output."""
        # Create a test file with missing docstring
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "dococtopy",
                "fix",
                str(tmp_path),
                "--dry-run",
                "--verbose",
            ],
            capture_output=True,
            text=True,
        )

        # Should show verbose output
        assert "LLM Provider:" in result.stdout
        assert "LLM Model:" in result.stdout
        assert "Dry run: True" in result.stdout
        assert "Interactive: False" in result.stdout
        assert "Loading config from: pyproject.toml" in result.stdout

    def test_fix_verbose_short_flag(self, tmp_path):
        """Test that fix command works with short verbose flag."""
        # Create a test file with missing docstring
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "dococtopy",
                "fix",
                str(tmp_path),
                "--dry-run",
                "-v",
            ],
            capture_output=True,
            text=True,
        )

        # Should show verbose output
        assert "LLM Provider:" in result.stdout
        assert "LLM Model:" in result.stdout

    def test_scan_no_verbose_output(self, tmp_path):
        """Test that scan command doesn't show verbose output without flag."""
        # Create a test file with missing docstring
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [sys.executable, "-m", "dococtopy", "scan", str(tmp_path)],
            capture_output=True,
            text=True,
        )

        # Should NOT show verbose output
        assert "Loading config from: pyproject.toml" not in result.stdout
        assert "Scanning paths:" not in result.stdout
        assert "Cache enabled:" not in result.stdout

    def test_fix_no_verbose_output(self, tmp_path):
        """Test that fix command doesn't show verbose output without flag."""
        # Create a test file with missing docstring
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [sys.executable, "-m", "dococtopy", "fix", str(tmp_path), "--dry-run"],
            capture_output=True,
            text=True,
        )

        # Should NOT show verbose output
        assert "LLM Provider:" not in result.stdout
        assert "LLM Model:" not in result.stdout
        assert "Dry run: True" not in result.stdout

    def test_verbose_with_custom_config(self, tmp_path):
        """Test verbose output with custom config file."""
        # Create a test file
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        # Create a custom config
        config_file = tmp_path / "custom.toml"
        config_file.write_text(
            """
[tool.docguard]
exclude = ["**/.venv/**"]
"""
        )

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "dococtopy",
                "scan",
                str(tmp_path),
                "--verbose",
                "--config",
                str(config_file),
            ],
            capture_output=True,
            text=True,
        )

        # Should show custom config path
        assert "Loading config from:" in result.stdout
        assert str(config_file) in result.stdout

    def test_verbose_with_rule_filtering(self, tmp_path):
        """Test verbose output with rule filtering."""
        # Create a test file
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "dococtopy",
                "fix",
                str(tmp_path),
                "--dry-run",
                "--verbose",
                "--rule",
                "DG101",
            ],
            capture_output=True,
            text=True,
        )

        # Should show rule filtering
        assert "Targeting rules: DG101" in result.stdout

    def test_verbose_with_max_changes(self, tmp_path):
        """Test verbose output with max changes limit."""
        # Create a test file
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "dococtopy",
                "fix",
                str(tmp_path),
                "--dry-run",
                "--verbose",
                "--max-changes",
                "5",
            ],
            capture_output=True,
            text=True,
        )

        # Should show max changes
        assert "Max changes: 5" in result.stdout

    def test_verbose_with_llm_base_url(self, tmp_path):
        """Test verbose output with custom LLM base URL."""
        # Create a test file
        test_file = tmp_path / "test.py"
        test_file.write_text("def hello(): pass")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "dococtopy",
                "fix",
                str(tmp_path),
                "--dry-run",
                "--verbose",
                "--llm-base-url",
                "http://localhost:11434",
            ],
            capture_output=True,
            text=True,
        )

        # Should show custom base URL
        assert "LLM Base URL: http://localhost:11434" in result.stdout
