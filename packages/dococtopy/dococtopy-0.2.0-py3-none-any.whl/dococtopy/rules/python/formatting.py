"""
Basic formatting rules for Python docstrings.

This module contains basic formatting rules that apply to all docstring styles:
- DG301: Summary first line should be a sentence with period
- DG302: Blank line required after summary
- DG303: Content quality issues (TODO/placeholders, conflict markers)
- DG304: Docstring delimiter style (single quotes vs double quotes)
"""

from __future__ import annotations

import re
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


@dataclass
class DG303ContentQuality:
    """Detect content quality issues in docstrings."""

    id: str = "DG303"
    name: str = "Content quality issues detected"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []

        for sym in symbols:
            if not sym.docstring:
                continue

            # Check for high-confidence content quality issues
            findings.extend(self._check_todo_placeholders(sym))
            findings.extend(self._check_conflict_markers(sym))

        return findings

    def _check_todo_placeholders(self, sym: PythonSymbol) -> List[Finding]:
        """Check for TODO/placeholder content - HIGH CONFIDENCE."""
        findings = []

        # Check for specific TODO keywords individually
        todo_keywords = ["TODO", "FIXME", "XXX", "HACK", "BUG", "TEMP", "TBD", "LATER"]
        for keyword in todo_keywords:
            # Require colon or period to avoid false positives like "TODO items"
            pattern = rf"\b{keyword}\s*[:.]\s"
            if sym.docstring and re.search(pattern, sym.docstring, re.IGNORECASE):
                findings.append(
                    Finding(  # type: ignore[call-arg]
                        rule_id=self.id,
                        level=FindingLevel.WARNING,
                        message=f"Docstring contains placeholder content: {keyword}",
                        symbol=sym.name,
                        location=Location(line=sym.lineno, column=sym.col),
                    )
                )

        # Check for other placeholder patterns
        other_patterns = [
            r"\b(___|\.\.\.)\b",  # Obvious placeholders
            r"\b(placeholder|temp|dummy|example)\s+(function|method|class)\b",  # Generic placeholders
        ]

        for pattern in other_patterns:
            if sym.docstring and re.search(pattern, sym.docstring, re.IGNORECASE):
                findings.append(
                    Finding(  # type: ignore[call-arg]
                        rule_id=self.id,
                        level=FindingLevel.WARNING,
                        message=f"Docstring contains placeholder content: {pattern}",
                        symbol=sym.name,
                        location=Location(line=sym.lineno, column=sym.col),
                    )
                )

        return findings

    def _check_conflict_markers(self, sym: PythonSymbol) -> List[Finding]:
        """Check for version control conflict markers - MAXIMUM CONFIDENCE."""
        findings = []

        # These are NEVER legitimate in final code
        conflict_patterns = [
            r"<<<<<<<",
            r"=======",
            r">>>>>>>",
            r"<<<<<<< HEAD",
            r">>>>>>> [a-f0-9]+",
        ]

        # Check each pattern and only report the first match to avoid duplicates
        for pattern in conflict_patterns:
            if sym.docstring and re.search(pattern, sym.docstring):
                findings.append(
                    Finding(  # type: ignore[call-arg]
                        rule_id=self.id,
                        level=FindingLevel.ERROR,  # Higher severity - this is a bug
                        message="Docstring contains version control conflict markers",
                        symbol=sym.name,
                        location=Location(line=sym.lineno, column=sym.col),
                    )
                )
                break  # Only report the first match to avoid duplicates

        return findings


@dataclass
class DG304DocstringDelimiterStyle:
    """Detect incorrect docstring delimiter styles."""

    id: str = "DG304"
    name: str = "Docstring delimiter style should use double quotes"
    level_default: str = "info"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []

        for sym in symbols:
            if not sym.docstring or not sym.ast_node:
                continue

            # Check for delimiter style issues
            findings.extend(self._check_delimiter_style(sym))

        return findings

    def _check_delimiter_style(self, sym: PythonSymbol) -> List[Finding]:
        """Check for delimiter style issues by analyzing AST node."""
        findings: List[Finding] = []

        if not sym.ast_node:
            return findings

        try:
            import ast

            # For now, we'll implement a basic heuristic check
            # The challenge is that ast.get_docstring() normalizes quotes
            # So we need to infer delimiter style from context

            if sym.docstring:
                # Check for patterns that might indicate single quote delimiters
                # This is a limited approach due to AST normalization

                # Look for docstrings that contain unescaped single quotes
                # which might suggest the use of single quote delimiters
                # Only flag if the docstring contains single quotes but no double quotes
                # AND the single quotes appear to be part of the content (not delimiters)
                # AND the docstring is short enough to be suspicious (likely delimiter issue)
                if (
                    "'" in sym.docstring
                    and '"' not in sym.docstring
                    and len(sym.docstring.strip()) < 100
                ):
                    # Check if the single quotes are likely legitimate content using regex patterns
                    # Pattern 1: Possessive forms (word's, name's, etc.)
                    possessive_pattern = r"\w+'s\b"
                    # Pattern 2: Contractions (don't, won't, can't, etc.)
                    contraction_pattern = r"\w+n't\b"
                    # Pattern 3: Other contractions (it's, that's, etc.)
                    other_contraction_pattern = r"\w+'[a-z]+\b"
                    # Pattern 4: Common contractions and possessives (more comprehensive)
                    common_patterns = [
                        r"\bdon't\b",
                        r"\bwon't\b",
                        r"\bcan't\b",
                        r"\bisn't\b",
                        r"\baren't\b",
                        r"\bwasn't\b",
                        r"\bweren't\b",
                        r"\bhasn't\b",
                        r"\bhaven't\b",
                        r"\bhadn't\b",
                        r"\bwouldn't\b",
                        r"\bshouldn't\b",
                        r"\bcouldn't\b",
                        r"\bit's\b",
                        r"\bthat's\b",
                        r"\bthere's\b",
                        r"\bhere's\b",
                        r"\bwhat's\b",
                        r"\bwho's\b",
                        r"\buser's\b",
                        r"\bname's\b",
                        r"\bfile's\b",
                        r"\bdata's\b",
                        r"\bvalue's\b",
                        r"\bitem's\b",
                        r"\bobject's\b",
                        r"\bclass's\b",
                        r"\bmethod's\b",
                        r"\bfunction's\b",
                    ]

                    has_legitimate_single_quotes = any(
                        [
                            re.search(possessive_pattern, sym.docstring),
                            re.search(contraction_pattern, sym.docstring),
                            re.search(other_contraction_pattern, sym.docstring),
                        ]
                    ) or any(
                        re.search(pattern, sym.docstring) for pattern in common_patterns
                    )

                    # Only flag if single quotes are present but don't appear to be
                    # legitimate content (possessives, contractions, etc.)
                    if not has_legitimate_single_quotes:
                        findings.append(
                            Finding(  # type: ignore[call-arg]
                                rule_id=self.id,
                                level=FindingLevel.INFO,
                                message="Docstring may use single quote delimiters (''' instead of \"\"\")",
                                symbol=sym.name,
                                location=Location(line=sym.lineno, column=sym.col),
                            )
                        )

                # Check for docstrings that look like they might be comments
                # This is a heuristic - if docstring is very short and looks like a comment
                docstring_stripped = sym.docstring.strip()
                if len(docstring_stripped) < 20 and docstring_stripped.startswith("#"):
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Docstring appears to be a comment instead of proper docstring",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )

        except Exception:
            # If we can't analyze the AST node, skip this symbol
            pass

        return findings


# Register all formatting rules
register(DG301SummaryStyle())
register(DG302BlankLineAfterSummary())
register(DG303ContentQuality())
register(DG304DocstringDelimiterStyle())
