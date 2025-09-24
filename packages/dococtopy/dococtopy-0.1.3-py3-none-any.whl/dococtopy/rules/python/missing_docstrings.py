"""
Missing docstring rules for Python.

This module contains rules that detect missing docstrings:
- DG101: Missing docstrings (main rule)
- DG215: Private method docstring recommendations
- DG216: Dunder method docstring recommendations
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.core.findings import Finding, FindingLevel, Location
from dococtopy.rules.registry import register


@dataclass
class DG101MissingDocstring:
    """Enhanced missing docstring rule with proper handling of private and dunder methods."""

    id: str = "DG101"
    name: str = "Missing docstring"
    level_default: str = "error"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        for sym in symbols:
            if sym.kind in {"module", "function", "class"} and not sym.docstring:
                # Check if this symbol should require a docstring
                if self._should_require_docstring(sym):
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.ERROR,
                            message=f"{sym.kind.capitalize()} '{sym.name}' is missing a docstring",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
        return findings

    def _should_require_docstring(self, sym: PythonSymbol) -> bool:
        """
        Determine if a symbol should require a docstring based on Python conventions.

        Rules:
        - Modules: Always require docstrings
        - Classes: Always require docstrings (except private classes)
        - Functions: Require docstrings unless they're private or standard dunder methods
        - Private methods (starting with _): Optional but recommended
        - Standard dunder methods (__str__, __repr__, etc.): Optional but recommended
        - Important dunder methods (__init__, __new__, etc.): Always required
        """
        # Always require docstrings for modules and classes
        if sym.kind in {"module", "class"}:
            return True

        # For functions, check if they're private or dunder methods
        if sym.kind == "function":
            name = sym.name

            # Private methods (starting with _ but not __) - optional
            if name.startswith("_") and not name.startswith("__"):
                return False

            # Dunder methods - check if they're important ones
            if name.startswith("__") and name.endswith("__"):
                return self._should_dunder_method_have_docstring(name)

            # All other functions require docstrings
            return True

        # Handle other special cases
        return False

    def _should_dunder_method_have_docstring(self, name: str) -> bool:
        """Determine if a dunder method should require a docstring."""
        # Always require docstrings for these important dunder methods
        always_required = {
            "__init__",  # Constructor - always public
            "__new__",  # Object creation
            "__call__",  # Callable objects
            "__enter__",  # Context manager entry
            "__exit__",  # Context manager exit
            "__getattr__",  # Attribute access
            "__setattr__",  # Attribute setting
            "__delattr__",  # Attribute deletion
            "__getattribute__",  # Attribute access
            "__get__",  # Descriptor protocol
            "__set__",  # Descriptor protocol
            "__delete__",  # Descriptor protocol
            "__set_name__",  # Descriptor protocol
            "__init_subclass__",  # Class initialization
            "__class_getitem__",  # Generic type support
        }

        if name in always_required:
            return True

        # Optional but recommended for these dunder methods
        recommended = {
            "__str__",  # String representation
            "__repr__",  # Developer representation
            "__eq__",  # Equality comparison
            "__hash__",  # Hashing
            "__len__",  # Length
            "__bool__",  # Boolean conversion
            "__getitem__",  # Item access
            "__setitem__",  # Item setting
            "__delitem__",  # Item deletion
            "__iter__",  # Iteration
            "__next__",  # Iterator protocol
            "__dir__",  # Directory listing
            "__sizeof__",  # Size calculation
            "__format__",  # Formatting
            "__reduce__",  # Pickling
            "__reduce_ex__",  # Pickling
            "__getstate__",  # Pickling
            "__setstate__",  # Pickling
            "__copy__",  # Copying
            "__deepcopy__",  # Copying
            "__mro_entries__",  # MRO entries
            "__subclasshook__",  # Subclass checking
            "__instancecheck__",  # Instance checking
            "__subclasscheck__",  # Subclass checking
            "__prepare__",  # Class preparation
        }

        if name in recommended:
            # For now, make these optional (return False)
            # In the future, we could add a separate rule for these
            return False

        # For any other dunder methods, require docstrings
        # (they're likely custom implementations)
        return True


@dataclass
class DG215PrivateMethodDocstringRecommendation:
    """Recommend docstrings for private methods (optional but recommended)."""

    id: str = "DG215"
    name: str = "Private methods should have docstrings"
    level_default: str = "info"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        for sym in symbols:
            if sym.kind == "function" and not sym.docstring:
                name = sym.name
                # Check for private methods (starting with _ but not __)
                if name.startswith("_") and not name.startswith("__"):
                    findings.append(
                        Finding(  # type: ignore[call-arg]
                            rule_id=self.id,
                            level=FindingLevel.INFO,
                            message=f"Private method '{sym.name}' should have a docstring",
                            symbol=sym.name,
                            location=Location(line=sym.lineno, column=sym.col),
                        )
                    )
        return findings


@dataclass
class DG216DunderMethodDocstringRecommendation:
    """Recommend docstrings for standard dunder methods (optional but recommended)."""

    id: str = "DG216"
    name: str = "Standard dunder methods should have docstrings"
    level_default: str = "info"

    def check(self, *, symbols: List[PythonSymbol]) -> List[Finding]:
        findings: List[Finding] = []
        for sym in symbols:
            if sym.kind == "function" and not sym.docstring:
                name = sym.name
                # Check for standard dunder methods
                if name.startswith("__") and name.endswith("__"):
                    standard_dunder_methods = {
                        "__str__",
                        "__repr__",
                        "__eq__",
                        "__hash__",
                        "__len__",
                        "__bool__",
                        "__getitem__",
                        "__setitem__",
                        "__delitem__",
                        "__iter__",
                        "__next__",
                        "__dir__",
                        "__sizeof__",
                        "__format__",
                        "__reduce__",
                        "__reduce_ex__",
                        "__getstate__",
                        "__setstate__",
                        "__copy__",
                        "__deepcopy__",
                        "__mro_entries__",
                        "__subclasshook__",
                        "__instancecheck__",
                        "__subclasscheck__",
                        "__prepare__",
                    }

                    if name in standard_dunder_methods:
                        findings.append(
                            Finding(  # type: ignore[call-arg]
                                rule_id=self.id,
                                level=FindingLevel.INFO,
                                message=f"Standard dunder method '{sym.name}' should have a docstring",
                                symbol=sym.name,
                                location=Location(line=sym.lineno, column=sym.col),
                            )
                        )
        return findings


# Register all missing docstring rules
register(DG101MissingDocstring())
register(DG215PrivateMethodDocstringRecommendation())
register(DG216DunderMethodDocstringRecommendation())
