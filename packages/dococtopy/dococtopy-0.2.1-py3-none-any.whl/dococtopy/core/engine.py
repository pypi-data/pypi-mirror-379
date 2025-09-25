from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Optional

from dococtopy.adapters.python.adapter import load_symbols_from_file
from dococtopy.core.cache import (
    CacheEntry,
    CacheStore,
    compute_fingerprint,
    deserialize_file_result,
    load_cache,
    save_cache,
    serialize_file_result,
)
from dococtopy.core.config import Config
from dococtopy.core.discovery import discover_python_files
from dococtopy.core.findings import (
    FileScanResult,
    Finding,
    FindingLevel,
    ScanReport,
    ScanSummary,
)

# Ensure default rules are registered (module has registration side-effects)
from dococtopy.rules import python  # noqa: F401
from dococtopy.rules.registry import all_rules


def scan_paths(
    paths: Iterable[Path],
    config: Optional[Config] = None,
    *,
    use_cache: bool = True,
    changed_only: bool = False,
) -> tuple[ScanReport, dict[str, int]]:
    extra_excludes = config.exclude if config else None
    files = discover_python_files(paths, extra_excludes=extra_excludes)
    file_results: List[FileScanResult] = []
    compliant_count = 0
    sum_coverage = 0.0
    cache = load_cache(Path.cwd()) if use_cache else None
    stats = {"cache_hits": 0, "cache_misses": 0, "files_processed": 0}
    rule_ids = [r.id for r in all_rules()]

    for fp in files:
        fingerprint = compute_fingerprint(
            fp, config.rules if config else None, rule_ids
        )
        stats["files_processed"] += 1

        # Try to use cache first
        cached_result = _try_cache_lookup(fp, fingerprint, cache, changed_only, stats)
        if cached_result:
            file_results.append(cached_result)
            sum_coverage += cached_result.coverage
            if not any(f.level == FindingLevel.ERROR for f in cached_result.findings):
                compliant_count += 1
            continue

        # Process file if not cached
        stats["cache_misses"] += 1
        file_result = _process_file(fp, config, cache, fingerprint)
        file_results.append(file_result)
        sum_coverage += file_result.coverage
        if not any(f.level == FindingLevel.ERROR for f in file_result.findings):
            compliant_count += 1

    # Generate report
    report = _generate_scan_report(file_results, compliant_count, sum_coverage)

    if cache is not None:
        save_cache(cache)
    return report, stats


def _compute_coverage(symbols) -> float:
    count_total = sum(1 for s in symbols if s.kind in {"function", "class"})
    if count_total == 0:
        return 1.0
    count_with = sum(
        1 for s in symbols if s.kind in {"function", "class"} and s.docstring
    )
    return count_with / count_total


def _overall_coverage(files: List[FileScanResult]) -> float:
    if not files:
        return 1.0
    # Unused in current code path; kept for future callers.
    return 1.0 * sum(getattr(fr, "coverage", 1.0) for fr in files) / len(files)


def _try_cache_lookup(
    file_path: Path,
    fingerprint: str,
    cache: Optional[CacheStore],
    changed_only: bool,
    stats: dict[str, int],
) -> Optional[FileScanResult]:
    """Try to get file result from cache."""
    if cache is None:
        return None

    ce = cache.get(file_path)
    if ce and ce.fingerprint == fingerprint:
        if changed_only:
            return None
        stats["cache_hits"] += 1
        return deserialize_file_result(ce.file_result)

    return None


def _process_file(
    file_path: Path,
    config: Optional[Config],
    cache: Optional[CacheStore],
    fingerprint: str,
) -> FileScanResult:
    """Process a single file and return scan result."""
    symbols = load_symbols_from_file(file_path)
    findings: List[Finding] = []

    for rule in all_rules():
        if config and not config.is_rule_enabled(rule.id):
            continue
        findings.extend(rule.check(symbols=symbols))

    coverage = _compute_coverage(symbols)
    file_result = FileScanResult(path=file_path, findings=findings, coverage=coverage)  # type: ignore[call-arg]

    # Cache the result
    if cache is not None:
        cache.set(
            file_path,
            CacheEntry(
                fingerprint=fingerprint, file_result=serialize_file_result(file_result)
            ),
        )

    return file_result


def _generate_scan_report(
    file_results: List[FileScanResult], compliant_count: int, sum_coverage: float
) -> ScanReport:
    """Generate the final scan report."""
    summary = ScanSummary(
        files_total=len(file_results),
        files_compliant=compliant_count,
        coverage_overall=(sum_coverage / len(file_results) if file_results else 1.0),
    )
    return ScanReport(summary=summary, files=file_results)  # type: ignore[call-arg]
