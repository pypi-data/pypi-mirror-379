"""
Google style docstring validation rules for Python.

This module contains rules that validate Google-style docstrings:
- DG201: Google style docstring parse error
- DG202: Parameter missing from docstring
- DG203: Extra parameter in docstring
- DG204: Returns section missing or mismatched
- DG205: Raises section validation
- DG206: Args section format validation
- DG207: Returns section format validation
- DG208: Raises section format validation
- DG209: Summary length validation
- DG210: Docstring indentation validation
- DG211: Yields section validation
- DG212: Attributes section validation
- DG213: Examples section validation
- DG214: Note section validation
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import List, Set

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.registry import register

from .ast_utils import (
    extract_function_params,
    extract_raised_exceptions,
    get_public_attributes,
    has_return_annotation,
    has_special_behavior,
    is_complex_function,
    is_generator_function,
)

try:
    from docstring_parser import parse
    from docstring_parser.common import DocstringStyle
except ImportError:
    parse = None  # type: ignore
    DocstringStyle = None  # type: ignore


@dataclass
class DG201GoogleStyleParseError:
    id: str = "DG201"
    name: str = "Google style docstring parse error"
    level_default: str = "error"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind == "module" or not sym.docstring:
                continue
            try:
                parse(sym.docstring, style=DocstringStyle.GOOGLE)
            except Exception as e:
                findings.append(
                    Finding(  # type: ignore[call-arg]
                        rule_id=self.id,
                        level=FindingLevel.ERROR,
                        message=f"Google style docstring parse error: {str(e)}",
                        symbol=sym.name,
                        location=Location(line=sym.lineno, column=sym.col),
                    )
                )
        return findings


@dataclass
class DG202ParamMissingFromDocstring:
    id: str = "DG202"
    name: str = "Parameter missing from docstring"
    level_default: str = "error"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Extract function parameters from AST
            func_params = extract_function_params(sym)
            if not func_params:
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                docstring_params = {param.arg_name for param in parsed.params}

                missing_params = func_params - docstring_params
                for param in missing_params:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.ERROR,
                            message=f"Parameter '{param}' missing from docstring",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


@dataclass
class DG203ExtraParamInDocstring:
    id: str = "DG203"
    name: str = "Extra parameter in docstring"
    level_default: str = "error"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Extract function parameters from AST
            func_params = extract_function_params(sym)

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                docstring_params = {param.arg_name for param in parsed.params}

                extra_params = docstring_params - func_params
                for param in extra_params:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.ERROR,
                            message=f"Extra parameter '{param}' in docstring",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


@dataclass
class DG204ReturnsSectionMissing:
    id: str = "DG204"
    name: str = "Returns section missing or mismatched"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Check if function has return annotation
            has_return = has_return_annotation(sym)

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                has_returns_section = parsed.returns is not None

                if has_return and not has_returns_section:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Function has return annotation but missing Returns section in docstring",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
                elif not has_return and has_returns_section:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Function has Returns section but no return annotation",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


@dataclass
class DG205RaisesSectionValidation:
    id: str = "DG205"
    name: str = "Raises section validation"
    level_default: str = "info"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Extract raised exceptions from AST
            raised_exceptions = extract_raised_exceptions(sym)

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                docstring_raises = {
                    raise_item.type_name for raise_item in parsed.raises
                }

                # Check for documented raises that aren't actually raised
                extra_raises = docstring_raises - raised_exceptions
                for exception in extra_raises:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.INFO,
                            message=f"Exception '{exception}' documented in Raises but not raised",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


@dataclass
class DG206ArgsSectionFormat:
    """Check that Args section follows Google style format."""

    id: str = "DG206"
    name: str = "Args section should use proper Google style format"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if not sym.docstring:
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                if not parsed.params:
                    continue

                for param in parsed.params:
                    # Check if param description is missing
                    if not param.description or param.description.strip() == "":
                        findings.append(
                            Finding(  # type: ignore[call-arg]
                                rule_id=self.id,
                                level=FindingLevel.WARNING,
                                message=f"Parameter '{param.arg_name}' in Args section is missing description",
                                symbol=sym.name,
                                location=Location(line=sym.lineno, column=sym.col),
                            )
                        )
                    # Check if description starts with lowercase (should be capitalized)
                    elif param.description and param.description[0].islower():
                        findings.append(
                            Finding(  # type: ignore[call-arg]
                                rule_id=self.id,
                                level=FindingLevel.WARNING,
                                message=f"Parameter '{param.arg_name}' description should start with capital letter",
                                symbol=sym.name,
                                location=Location(line=sym.lineno, column=sym.col),
                            )
                        )
            except Exception:
                # Skip if parsing fails (handled by DG201)
                continue

        return findings


@dataclass
class DG207ReturnsSectionFormat:
    """Check that Returns section follows Google style format."""

    id: str = "DG207"
    name: str = "Returns section should use proper Google style format"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if not sym.docstring:
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                if not parsed.returns:
                    continue

                # Check if returns description is missing
                if (
                    not parsed.returns.description
                    or parsed.returns.description.strip() == ""
                ):
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Returns section is missing description",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
                # Check if description starts with lowercase (should be capitalized)
                elif (
                    parsed.returns.description
                    and parsed.returns.description[0].islower()
                ):
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Returns section description should start with capital letter",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if parsing fails (handled by DG201)
                continue

        return findings


@dataclass
class DG208RaisesSectionFormat:
    """Check that Raises section follows Google style format."""

    id: str = "DG208"
    name: str = "Raises section should use proper Google style format"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if not sym.docstring:
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                if not parsed.raises:
                    continue

                for raise_item in parsed.raises:
                    # Check if raises description is missing
                    if (
                        not raise_item.description
                        or raise_item.description.strip() == ""
                    ):
                        findings.append(
                            Finding(  # type: ignore[call-arg]
                                rule_id=self.id,
                                level=FindingLevel.WARNING,
                                message=f"Exception '{raise_item.type_name}' in Raises section is missing description",
                                symbol=sym.name,
                                location=Location(line=sym.lineno, column=sym.col),
                            )
                        )
                    # Check if description starts with lowercase (should be capitalized)
                    elif raise_item.description and raise_item.description[0].islower():
                        findings.append(
                            Finding(  # type: ignore[call-arg]
                                rule_id=self.id,
                                level=FindingLevel.WARNING,
                                message=f"Exception '{raise_item.type_name}' description should start with capital letter",
                                symbol=sym.name,
                                location=Location(line=sym.lineno, column=sym.col),
                            )
                        )
            except Exception:
                # Skip if parsing fails (handled by DG201)
                continue

        return findings


@dataclass
class DG209SummaryLength:
    """Check that summary is not too long or too short."""

    id: str = "DG209"
    name: str = "Summary should be appropriate length"
    level_default: str = "info"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if not sym.docstring:
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)
                if not parsed.short_description:
                    continue

                summary = parsed.short_description.strip()
                # Check if summary is too short (less than 10 characters)
                if len(summary) < 10:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.INFO,
                            message="Summary is too short (less than 10 characters)",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
                # Check if summary is too long (more than 80 characters)
                elif len(summary) > 80:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.INFO,
                            message="Summary is too long (more than 80 characters)",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if parsing fails (handled by DG201)
                continue

        return findings


@dataclass
class DG210DocstringIndentation:
    """Check that docstring indentation is consistent."""

    id: str = "DG210"
    name: str = "Docstring should have consistent indentation"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []

        for sym in symbols:
            if not sym.docstring:
                continue

            # Get the raw docstring lines
            docstring_lines = sym.docstring.split("\n")
            if len(docstring_lines) < 2:
                continue

            # Check if first line after opening quotes is indented
            first_content_line = None
            for i, line in enumerate(docstring_lines):
                if line.strip() and not line.strip().startswith('"""'):
                    first_content_line = i
                    break

            if first_content_line is None:
                continue

            # Check indentation consistency
            expected_indent = len(docstring_lines[first_content_line]) - len(
                docstring_lines[first_content_line].lstrip()
            )

            for i, line in enumerate(
                docstring_lines[first_content_line + 1 :], first_content_line + 1
            ):
                if line.strip() and not line.strip().startswith('"""'):
                    actual_indent = len(line) - len(line.lstrip())
                    if actual_indent != expected_indent:
                        findings.append(
                            Finding(  # type: ignore[call-arg]
                                rule_id=self.id,
                                level=FindingLevel.WARNING,
                                message=f"Inconsistent indentation in docstring (line {i + 1})",
                                symbol=sym.name,
                                location=Location(line=sym.lineno + i, column=sym.col),
                            )
                        )
                        break  # Only report first inconsistency

        return findings


@dataclass
class DG211YieldsSectionValidation:
    """Check that generator functions have proper Yields section."""

    id: str = "DG211"
    name: str = "Generator functions should have Yields section"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Check if function is a generator (has yield statements)
            if not is_generator_function(sym):
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)

                # Check if Yields section exists
                has_yields = any(
                    meta.args[0] == "yields"
                    for meta in parsed.meta
                    if meta.args and len(meta.args) > 0
                )

                if not has_yields:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Generator function should have Yields section",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


@dataclass
class DG212AttributesSectionValidation:
    """Check that classes with attributes document them properly."""

    id: str = "DG212"
    name: str = "Classes should document public attributes"
    level_default: str = "warning"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "class" or not sym.docstring:
                continue

            # Get public attributes from the class
            public_attrs = get_public_attributes(sym)
            if not public_attrs:
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)

                # Check if Attributes section exists in the raw docstring
                has_attributes = False
                if sym.docstring:
                    # Look for Attributes: or Attributes - patterns in the raw docstring
                    docstring_lower = sym.docstring.lower()
                    has_attributes = any(
                        pattern in docstring_lower
                        for pattern in [
                            "attributes:",
                            "attributes -",
                            "attributes\n",
                            "attributes ",
                        ]
                    )

                if not has_attributes:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.WARNING,
                            message="Class with public attributes should have Attributes section",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


@dataclass
class DG213ExamplesSectionValidation:
    """Check that complex functions have Examples section."""

    id: str = "DG213"
    name: str = "Complex functions should have Examples section"
    level_default: str = "info"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Check if function is complex enough to warrant examples
            if not is_complex_function(sym):
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)

                # Check if Examples section exists
                if not parsed.examples:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.INFO,
                            message="Complex function should have Examples section",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


@dataclass
class DG214NoteSectionValidation:
    """Check that functions with special behavior have Note sections."""

    id: str = "DG214"
    name: str = "Functions with special behavior should have Note sections"
    level_default: str = "info"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        if parse is None or DocstringStyle is None:
            return findings

        for sym in symbols:
            if sym.kind != "function" or not sym.docstring:
                continue

            # Check if function has special behavior that should be noted
            if not has_special_behavior(sym):
                continue

            try:
                parsed = parse(sym.docstring, style=DocstringStyle.GOOGLE)

                # Check if Note section exists in the raw docstring
                has_note = False
                if sym.docstring:
                    # Look for Note: or Note - patterns in the raw docstring
                    docstring_lower = sym.docstring.lower()
                    has_note = any(
                        pattern in docstring_lower
                        for pattern in ["note:", "note -", "note\n", "note "]
                    )

                if not has_note:
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.INFO,
                            message="Function with special behavior should have Note section",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
            except Exception:
                # Skip if docstring parsing fails (handled by DG201)
                continue
        return findings


# Register all Google style rules
register(DG201GoogleStyleParseError())
register(DG202ParamMissingFromDocstring())
register(DG203ExtraParamInDocstring())
register(DG204ReturnsSectionMissing())
register(DG205RaisesSectionValidation())
register(DG206ArgsSectionFormat())
register(DG207ReturnsSectionFormat())
register(DG208RaisesSectionFormat())
register(DG209SummaryLength())
register(DG210DocstringIndentation())
register(DG211YieldsSectionValidation())
register(DG212AttributesSectionValidation())
register(DG213ExamplesSectionValidation())
register(DG214NoteSectionValidation())
