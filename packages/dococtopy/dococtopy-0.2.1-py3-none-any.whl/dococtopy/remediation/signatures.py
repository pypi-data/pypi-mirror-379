"""DSPy signatures for docstring generation and remediation.

This module defines the input/output contracts for LLM-based docstring generation
using DSPy's declarative approach.
"""

from __future__ import annotations

try:
    import dspy
except ImportError:
    dspy = None  # type: ignore


class DocstringGeneration(dspy.Signature if dspy else object):  # type: ignore
    """Generate a Google-style docstring for a Python function or class.

    This signature defines the contract for generating compliant docstrings
    based on function/class signatures and context.

    Examples:
    - Input: function_signature="def add(a, b):", function_purpose="Add two numbers"
    - Output: docstring="Add two numbers.\n\nArgs:\n    a: First number\n    b: Second number\n\nReturns:\n    Sum of a and b"
    """

    function_signature: str = dspy.InputField(  # type: ignore
        desc="The Python function or class signature including parameters and return type"
    )
    function_purpose: str = dspy.InputField(  # type: ignore
        desc="Brief description of what the function/class does"
    )
    existing_docstring: str = dspy.InputField(  # type: ignore
        desc="Current docstring (if any) to improve or replace"
    )
    context: str = dspy.InputField(  # type: ignore
        desc="Specific validation errors and compliance issues found by the scanner (e.g., 'DG101: Function is missing a docstring; DG204: Function has Returns section but no return annotation')"
    )

    docstring: str = dspy.OutputField(  # type: ignore
        desc="ONLY the docstring content without triple quotes or function signature. CRITICAL RULES: 1) Summary line ending with period, 2) Args section only if function has parameters, 3) Returns section only if function has return annotation, 4) Raises section only if function can raise exceptions, 5) Use 4-space indentation for sections, 6) Do NOT include function signature, 7) Do NOT include triple quotes, 8) Use ONLY ASCII characters (no Unicode), 9) INDENTATION: All lines must have consistent 4-space indentation, no extra spaces. CRITICAL: If function has no return annotation, do NOT include Returns section. If function raises no exceptions, do NOT include Raises section. Example: 'Add two numbers.\\n\\nArgs:\\n    a: First number\\n    b: Second number'"
    )


class DocstringFix(dspy.Signature if dspy else object):  # type: ignore
    """Fix a non-compliant docstring to meet Google style standards.

    This signature is used when we have an existing docstring that needs
    to be corrected rather than generated from scratch.
    """

    function_signature: str = dspy.InputField(  # type: ignore
        desc="The Python function or class signature"
    )
    current_docstring: str = dspy.InputField(  # type: ignore
        desc="The current non-compliant docstring"
    )
    issues: str = dspy.InputField(  # type: ignore
        desc="Specific validation errors and compliance issues found by the scanner (e.g., 'DG101: Function is missing a docstring; DG204: Function has Returns section but no return annotation')"
    )

    fixed_docstring: str = dspy.OutputField(  # type: ignore
        desc="Corrected Google-style docstring content ONLY (without triple quotes) that addresses all compliance issues. CRITICAL RULES: 1) Summary line ending with period, 2) Args section only if function has parameters, 3) Returns section only if function has return annotation, 4) Raises section only if function can raise exceptions, 5) Use 4-space indentation for sections, 6) Do NOT include function signature, 7) Do NOT include triple quotes, 8) Use ONLY ASCII characters (no Unicode), 9) INDENTATION: All lines must have consistent 4-space indentation, no extra spaces. CRITICAL: If function has no return annotation, do NOT include Returns section. If function raises no exceptions, do NOT include Raises section"
    )


class DocstringEnhancement(dspy.Signature if dspy else object):  # type: ignore
    """Enhance an existing docstring with missing information.

    This signature is used to add missing parameters, return descriptions,
    or other sections to an existing docstring.
    """

    function_signature: str = dspy.InputField(  # type: ignore
        desc="The Python function or class signature"
    )
    current_docstring: str = dspy.InputField(  # type: ignore
        desc="The current docstring that needs enhancement"
    )
    missing_elements: str = dspy.InputField(  # type: ignore
        desc="Description of what's missing (e.g., 'missing parameter xyz', 'missing Returns section')"
    )

    enhanced_docstring: str = dspy.OutputField(  # type: ignore
        desc="Enhanced docstring content ONLY (without triple quotes) with all missing elements added in Google style. Use ONLY ASCII characters (no Unicode). INDENTATION: All lines must have consistent 4-space indentation, no extra spaces."
    )


# Export signatures for use in other modules
__all__ = [
    "DocstringGeneration",
    "DocstringFix",
    "DocstringEnhancement",
]
