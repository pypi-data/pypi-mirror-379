"""
Basic formatting rules for Python docstrings.

This module contains basic formatting rules that apply to all docstring styles:
- DG301: Summary first line should be a sentence with period
- DG302: Blank line required after summary
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.registry import register


@dataclass
class DG301SummaryStyle:
    id: str = "DG301"
    name: str = "Summary first line should be a sentence with period"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        for sym in symbols:
            if sym.kind == "module":
                continue
            if sym.docstring:
                first_line = sym.docstring.strip().splitlines()[0].strip()
                if first_line and not first_line.endswith("."):
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Docstring summary should end with a period.",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
        return findings


@dataclass
class DG302BlankLineAfterSummary:
    id: str = "DG302"
    name: str = "Blank line required after summary"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        for sym in symbols:
            if sym.kind == "module" or not sym.docstring:
                continue
            lines = sym.docstring.splitlines()
            if len(lines) >= 2:
                # Google style: summary line, then blank line, then details/sections
                if lines[1].strip() != "":
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Expected blank line after docstring summary.",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
        return findings


# Register all formatting rules
register(DG301SummaryStyle())
register(DG302BlankLineAfterSummary())
