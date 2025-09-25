"""Tests for engine helper functions."""

from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from dococtopy.core.engine import (
    _generate_scan_report,
    _process_file,
    _try_cache_lookup,
)
from dococtopy.core.findings import (
    FileScanResult,
    Finding,
    FindingLevel,
    Location,
    ScanReport,
    ScanSummary,
)


class TestTryCacheLookup:
    """Test the _try_cache_lookup helper function."""

    def test_try_cache_lookup_no_cache(self):
        """Test cache lookup when cache is None."""
        file_path = Path("test.py")
        fingerprint = "test-fingerprint"
        cache = None
        changed_only = False
        stats = {"cache_hits": 0, "cache_misses": 0, "files_processed": 0}

        result = _try_cache_lookup(file_path, fingerprint, cache, changed_only, stats)

        assert result is None
        assert stats["cache_hits"] == 0

    def test_try_cache_lookup_cache_miss(self):
        """Test cache lookup when cache entry doesn't exist."""
        file_path = Path("test.py")
        fingerprint = "test-fingerprint"
        cache = Mock()
        cache.get.return_value = None
        changed_only = False
        stats = {"cache_hits": 0, "cache_misses": 0, "files_processed": 0}

        result = _try_cache_lookup(file_path, fingerprint, cache, changed_only, stats)

        assert result is None
        assert stats["cache_hits"] == 0
        cache.get.assert_called_once_with(file_path)

    def test_try_cache_lookup_fingerprint_mismatch(self):
        """Test cache lookup when fingerprint doesn't match."""
        file_path = Path("test.py")
        fingerprint = "test-fingerprint"
        cache = Mock()
        cache_entry = Mock()
        cache_entry.fingerprint = "different-fingerprint"
        cache.get.return_value = cache_entry
        changed_only = False
        stats = {"cache_hits": 0, "cache_misses": 0, "files_processed": 0}

        result = _try_cache_lookup(file_path, fingerprint, cache, changed_only, stats)

        assert result is None
        assert stats["cache_hits"] == 0

    def test_try_cache_lookup_success(self):
        """Test successful cache lookup."""
        file_path = Path("test.py")
        fingerprint = "test-fingerprint"
        cache = Mock()
        cache_entry = Mock()
        cache_entry.fingerprint = "test-fingerprint"
        cache_entry.file_result = "serialized-result"
        cache.get.return_value = cache_entry
        changed_only = False
        stats = {"cache_hits": 0, "cache_misses": 0, "files_processed": 0}

        mock_file_result = Mock()
        with patch("dococtopy.core.engine.deserialize_file_result") as mock_deserialize:
            mock_deserialize.return_value = mock_file_result

            result = _try_cache_lookup(
                file_path, fingerprint, cache, changed_only, stats
            )

            assert result == mock_file_result
            assert stats["cache_hits"] == 1
            mock_deserialize.assert_called_once_with("serialized-result")

    def test_try_cache_lookup_changed_only_skip(self):
        """Test cache lookup when changed_only is True."""
        file_path = Path("test.py")
        fingerprint = "test-fingerprint"
        cache = Mock()
        cache_entry = Mock()
        cache_entry.fingerprint = "test-fingerprint"
        cache.get.return_value = cache_entry
        changed_only = True
        stats = {"cache_hits": 0, "cache_misses": 0, "files_processed": 0}

        result = _try_cache_lookup(file_path, fingerprint, cache, changed_only, stats)

        assert result is None
        assert stats["cache_hits"] == 0


class TestProcessFile:
    """Test the _process_file helper function."""

    def test_process_file_basic(self):
        """Test basic file processing."""
        file_path = Path("test.py")
        config = None
        cache = None
        fingerprint = "test-fingerprint"

        mock_symbols = [Mock(), Mock()]
        mock_findings = [
            Finding(
                rule_id="DG101",
                level=FindingLevel.ERROR,
                message="Test finding 1",
                location=Location(line=1, column=0),
            ),
            Finding(
                rule_id="DG202",
                level=FindingLevel.WARNING,
                message="Test finding 2",
                location=Location(line=2, column=0),
            ),
        ]
        mock_rule = Mock()
        mock_rule.check.return_value = mock_findings

        with (
            patch("dococtopy.core.engine.load_symbols_from_file") as mock_load_symbols,
            patch("dococtopy.core.engine.all_rules") as mock_all_rules,
            patch("dococtopy.core.engine._compute_coverage") as mock_compute_coverage,
        ):

            mock_load_symbols.return_value = mock_symbols
            mock_all_rules.return_value = [mock_rule]
            mock_compute_coverage.return_value = 0.8

            result = _process_file(file_path, config, cache, fingerprint)

            assert isinstance(result, FileScanResult)
            assert result.path == file_path
            assert result.findings == mock_findings
            assert result.coverage == 0.8
            mock_load_symbols.assert_called_once_with(file_path)
            mock_rule.check.assert_called_once_with(symbols=mock_symbols)

    def test_process_file_with_config_rule_filtering(self):
        """Test file processing with config that disables some rules."""
        file_path = Path("test.py")
        config = Mock()
        config.is_rule_enabled.side_effect = lambda rule_id: rule_id != "disabled_rule"
        cache = None
        fingerprint = "test-fingerprint"

        mock_symbols = [Mock()]
        mock_rule1 = Mock()
        mock_rule1.id = "enabled_rule"
        mock_rule1.check.return_value = [
            Finding(
                rule_id="DG101",
                level=FindingLevel.ERROR,
                message="Test finding",
                location=Location(line=1, column=0),
            )
        ]
        mock_rule2 = Mock()
        mock_rule2.id = "disabled_rule"
        mock_rule2.check.return_value = [
            Finding(
                rule_id="DG202",
                level=FindingLevel.WARNING,
                message="Test finding",
                location=Location(line=1, column=0),
            )
        ]

        with (
            patch("dococtopy.core.engine.load_symbols_from_file") as mock_load_symbols,
            patch("dococtopy.core.engine.all_rules") as mock_all_rules,
            patch("dococtopy.core.engine._compute_coverage") as mock_compute_coverage,
        ):

            mock_load_symbols.return_value = mock_symbols
            mock_all_rules.return_value = [mock_rule1, mock_rule2]
            mock_compute_coverage.return_value = 0.9

            result = _process_file(file_path, config, cache, fingerprint)

            assert isinstance(result, FileScanResult)
            assert result.path == file_path
            assert result.coverage == 0.9
            mock_rule1.check.assert_called_once_with(symbols=mock_symbols)
            mock_rule2.check.assert_not_called()

    def test_process_file_with_cache(self):
        """Test file processing with caching enabled."""
        file_path = Path("test.py")
        config = None
        cache = Mock()
        fingerprint = "test-fingerprint"

        mock_symbols = [Mock()]
        mock_findings = [
            Finding(
                rule_id="DG101",
                level=FindingLevel.ERROR,
                message="Test finding",
                location=Location(line=1, column=0),
            )
        ]
        mock_rule = Mock()
        mock_rule.check.return_value = mock_findings

        with (
            patch("dococtopy.core.engine.load_symbols_from_file") as mock_load_symbols,
            patch("dococtopy.core.engine.all_rules") as mock_all_rules,
            patch("dococtopy.core.engine._compute_coverage") as mock_compute_coverage,
            patch("dococtopy.core.engine.serialize_file_result") as mock_serialize,
        ):

            mock_load_symbols.return_value = mock_symbols
            mock_all_rules.return_value = [mock_rule]
            mock_compute_coverage.return_value = 0.7
            mock_serialize.return_value = "serialized-result"

            result = _process_file(file_path, config, cache, fingerprint)

            assert isinstance(result, FileScanResult)
            assert result.path == file_path
            assert result.findings == mock_findings
            assert result.coverage == 0.7
            cache.set.assert_called_once()
            mock_serialize.assert_called_once_with(result)

    def test_process_file_multiple_rules(self):
        """Test file processing with multiple rules."""
        file_path = Path("test.py")
        config = None
        cache = None
        fingerprint = "test-fingerprint"

        mock_symbols = [Mock()]
        mock_findings1 = [
            Finding(
                rule_id="DG101",
                level=FindingLevel.ERROR,
                message="Test finding 1",
                location=Location(line=1, column=0),
            ),
            Finding(
                rule_id="DG202",
                level=FindingLevel.WARNING,
                message="Test finding 2",
                location=Location(line=2, column=0),
            ),
        ]
        mock_findings2 = [
            Finding(
                rule_id="DG301",
                level=FindingLevel.ERROR,
                message="Test finding 3",
                location=Location(line=3, column=0),
            )
        ]
        mock_rule1 = Mock()
        mock_rule1.check.return_value = mock_findings1
        mock_rule2 = Mock()
        mock_rule2.check.return_value = mock_findings2

        with (
            patch("dococtopy.core.engine.load_symbols_from_file") as mock_load_symbols,
            patch("dococtopy.core.engine.all_rules") as mock_all_rules,
            patch("dococtopy.core.engine._compute_coverage") as mock_compute_coverage,
        ):

            mock_load_symbols.return_value = mock_symbols
            mock_all_rules.return_value = [mock_rule1, mock_rule2]
            mock_compute_coverage.return_value = 0.6

            result = _process_file(file_path, config, cache, fingerprint)

            assert isinstance(result, FileScanResult)
            assert result.path == file_path
            assert result.findings == mock_findings1 + mock_findings2
            assert result.coverage == 0.6
            mock_rule1.check.assert_called_once_with(symbols=mock_symbols)
            mock_rule2.check.assert_called_once_with(symbols=mock_symbols)


class TestGenerateScanReport:
    """Test the _generate_scan_report helper function."""

    def test_generate_scan_report_basic(self):
        """Test basic scan report generation."""
        file_results = [
            FileScanResult(path=Path("test1.py"), findings=[], coverage=0.8),
            FileScanResult(path=Path("test2.py"), findings=[], coverage=0.9),
            FileScanResult(path=Path("test3.py"), findings=[], coverage=0.7),
        ]
        compliant_count = 2
        sum_coverage = 2.4

        result = _generate_scan_report(file_results, compliant_count, sum_coverage)

        assert isinstance(result, ScanReport)
        assert result.files == file_results
        assert result.summary.files_total == 3
        assert result.summary.files_compliant == 2
        assert abs(result.summary.coverage_overall - 0.8) < 0.001  # 2.4 / 3

    def test_generate_scan_report_empty_files(self):
        """Test scan report generation with no files."""
        file_results = []
        compliant_count = 0
        sum_coverage = 0.0

        result = _generate_scan_report(file_results, compliant_count, sum_coverage)

        assert isinstance(result, ScanReport)
        assert result.files == []
        assert result.summary.files_total == 0
        assert result.summary.files_compliant == 0
        assert result.summary.coverage_overall == 1.0  # Default when no files

    def test_generate_scan_report_single_file(self):
        """Test scan report generation with single file."""
        file_results = [FileScanResult(path=Path("test.py"), findings=[], coverage=0.9)]
        compliant_count = 1
        sum_coverage = 0.9

        result = _generate_scan_report(file_results, compliant_count, sum_coverage)

        assert isinstance(result, ScanReport)
        assert result.files == file_results
        assert result.summary.files_total == 1
        assert result.summary.files_compliant == 1
        assert result.summary.coverage_overall == 0.9

    def test_generate_scan_report_perfect_coverage(self):
        """Test scan report generation with perfect coverage."""
        file_results = [
            FileScanResult(path=Path("test1.py"), findings=[], coverage=1.0),
            FileScanResult(path=Path("test2.py"), findings=[], coverage=1.0),
        ]
        compliant_count = 2
        sum_coverage = 2.0

        result = _generate_scan_report(file_results, compliant_count, sum_coverage)

        assert isinstance(result, ScanReport)
        assert result.files == file_results
        assert result.summary.files_total == 2
        assert result.summary.files_compliant == 2
        assert result.summary.coverage_overall == 1.0

    def test_generate_scan_report_zero_coverage(self):
        """Test scan report generation with zero coverage."""
        file_results = [
            FileScanResult(path=Path("test1.py"), findings=[], coverage=0.0),
            FileScanResult(path=Path("test2.py"), findings=[], coverage=0.0),
        ]
        compliant_count = 0
        sum_coverage = 0.0

        result = _generate_scan_report(file_results, compliant_count, sum_coverage)

        assert isinstance(result, ScanReport)
        assert result.files == file_results
        assert result.summary.files_total == 2
        assert result.summary.files_compliant == 0
        assert result.summary.coverage_overall == 0.0

    def test_generate_scan_report_many_files(self):
        """Test scan report generation with many files."""
        file_results = [
            FileScanResult(path=Path(f"test{i}.py"), findings=[], coverage=0.85)
            for i in range(10)
        ]
        compliant_count = 7
        sum_coverage = 8.5

        result = _generate_scan_report(file_results, compliant_count, sum_coverage)

        assert isinstance(result, ScanReport)
        assert result.files == file_results
        assert result.summary.files_total == 10
        assert result.summary.files_compliant == 7
        assert result.summary.coverage_overall == 0.85  # 8.5 / 10
