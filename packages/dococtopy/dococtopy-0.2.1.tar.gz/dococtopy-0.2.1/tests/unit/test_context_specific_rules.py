"""Tests for context-specific docstring rules."""

from pathlib import Path

from dococtopy.adapters.python.adapter import load_symbols_from_file
from dococtopy.rules.python.context_specific import (
    DG401TestFunctionDocstringStyle,
    DG402PublicAPIFunctionDocumentation,
    DG403ExceptionDocumentationCompleteness,
)


class TestDG401TestFunctionDocstringStyle:
    """Test DG401: Test function docstring style."""

    def test_test_function_with_good_docstring(self, tmp_path: Path) -> None:
        """Test that test functions with descriptive docstrings pass."""
        code = '''def test_user_authentication_works_correctly():
    """Test that user authentication validates credentials properly."""
    pass
'''
        p = tmp_path / "test.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG401TestFunctionDocstringStyle().check(symbols=syms)
        assert not any(f.rule_id == "DG401" for f in findings)

    def test_test_function_without_docstring(self, tmp_path: Path) -> None:
        """Test that test functions without docstrings are flagged."""
        code = """def test_user_login():
    pass
"""
        p = tmp_path / "test.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG401TestFunctionDocstringStyle().check(symbols=syms)
        assert any(
            f.rule_id == "DG401" for f in findings
        )  # No docstring = should be flagged

    def test_test_function_with_poor_docstring(self, tmp_path: Path) -> None:
        """Test that test functions with non-descriptive docstrings are flagged."""
        code = '''def test_user_login():
    """Test."""
    pass
'''
        p = tmp_path / "test.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG401TestFunctionDocstringStyle().check(symbols=syms)
        assert any(f.rule_id == "DG401" for f in findings)
        assert "descriptive docstring" in findings[0].message

    def test_test_function_with_generic_docstring(self, tmp_path: Path) -> None:
        """Test that test functions with generic docstrings are flagged."""
        code = '''def test_user_login():
    """Test function."""
    pass
'''
        p = tmp_path / "test.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG401TestFunctionDocstringStyle().check(symbols=syms)
        assert any(f.rule_id == "DG401" for f in findings)

    def test_non_test_function_ignored(self, tmp_path: Path) -> None:
        """Test that non-test functions are ignored."""
        code = '''def regular_function():
    """Just a regular function."""
    pass
'''
        p = tmp_path / "test.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG401TestFunctionDocstringStyle().check(symbols=syms)
        assert not any(f.rule_id == "DG401" for f in findings)


class TestDG402PublicAPIFunctionDocumentation:
    """Test DG402: Public API function documentation."""

    def test_public_api_function_with_complete_docstring(self, tmp_path: Path) -> None:
        """Test that public API functions with complete docstrings pass."""
        code = '''def process_data(data, options=None):
    """Process the input data according to the given options.
    
    Args:
        data: The input data to process
        options: Optional configuration options
        
    Returns:
        Processed data result
        
    Raises:
        ValueError: If data format is invalid
    """
    pass
'''
        p = tmp_path / "api.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG402PublicAPIFunctionDocumentation().check(symbols=syms)
        assert not any(f.rule_id == "DG402" for f in findings)

    def test_public_api_function_missing_sections(self, tmp_path: Path) -> None:
        """Test that public API functions missing sections are flagged."""
        code = '''def process_data(data, options=None):
    """Process the input data."""
    pass
'''
        p = tmp_path / "api.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG402PublicAPIFunctionDocumentation().check(symbols=syms)
        assert any(f.rule_id == "DG402" for f in findings)
        assert "should have" in findings[0].message

    def test_private_function_ignored(self, tmp_path: Path) -> None:
        """Test that private functions are ignored."""
        code = '''def _internal_helper():
    """Internal helper function."""
    pass
'''
        p = tmp_path / "api.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG402PublicAPIFunctionDocumentation().check(symbols=syms)
        assert not any(f.rule_id == "DG402" for f in findings)

    def test_test_function_ignored(self, tmp_path: Path) -> None:
        """Test that test functions are ignored."""
        code = '''def test_something():
    """Test something."""
    pass
'''
        p = tmp_path / "test.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG402PublicAPIFunctionDocumentation().check(symbols=syms)
        assert not any(f.rule_id == "DG402" for f in findings)


class TestDG403ExceptionDocumentationCompleteness:
    """Test DG403: Exception documentation completeness."""

    def test_function_with_documented_exceptions(self, tmp_path: Path) -> None:
        """Test that functions with documented exceptions pass."""
        code = '''def risky_function():
    """Do something risky.
    
    Raises:
        ValueError: If input is invalid
    """
    raise ValueError("test")
'''
        p = tmp_path / "risky.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG403ExceptionDocumentationCompleteness().check(symbols=syms)
        assert not any(f.rule_id == "DG403" for f in findings)

    def test_function_with_undocumented_exceptions(self, tmp_path: Path) -> None:
        """Test that functions with undocumented exceptions are flagged."""
        code = '''def risky_function():
    """Do something risky."""
    raise ValueError("test")
'''
        p = tmp_path / "risky.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG403ExceptionDocumentationCompleteness().check(symbols=syms)
        assert any(f.rule_id == "DG403" for f in findings)
        assert "raises" in findings[0].message.lower()

    def test_function_without_exceptions(self, tmp_path: Path) -> None:
        """Test that functions without exceptions are ignored."""
        code = '''def safe_function():
    """Do something safe."""
    return "safe"
'''
        p = tmp_path / "safe.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG403ExceptionDocumentationCompleteness().check(symbols=syms)
        assert not any(f.rule_id == "DG403" for f in findings)

    def test_function_with_partial_exception_documentation(
        self, tmp_path: Path
    ) -> None:
        """Test that functions with partial exception documentation are flagged."""
        code = '''def risky_function():
    """Do something risky.
    
    Raises:
        ValueError: If input is invalid
    """
    raise ValueError("test")
    raise RuntimeError("test")
'''
        p = tmp_path / "risky.py"
        p.write_text(code)
        syms = load_symbols_from_file(p)
        findings = DG403ExceptionDocumentationCompleteness().check(symbols=syms)
        assert any(f.rule_id == "DG403" for f in findings)
        assert "RuntimeError" in findings[0].message
