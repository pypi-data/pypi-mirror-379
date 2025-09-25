"""Comprehensive tests for docstring indentation normalization."""

import pytest

from dococtopy.remediation.indentation import (
    detect_docstring_indentation_issues,
    get_docstring_base_indent,
    is_docstring_indentation_consistent,
    normalize_docstring_indentation,
)


class TestNormalizeDocstringIndentation:
    """Test the normalize_docstring_indentation function."""

    def test_empty_docstring(self):
        """Test handling of empty docstrings."""
        assert normalize_docstring_indentation("") == ""
        assert normalize_docstring_indentation("   ") == "   "
        assert normalize_docstring_indentation("\n\n") == "\n\n"

    def test_single_line_docstring(self):
        """Test handling of single line docstrings."""
        assert normalize_docstring_indentation("Simple docstring") == "Simple docstring"
        assert (
            normalize_docstring_indentation("  Simple docstring  ")
            == "Simple docstring"
        )

    def test_basic_normalization(self):
        """Test basic indentation normalization."""
        input_doc = "Summary line.\n\nArgs:\n    param: Description"
        expected = "Summary line.\n\nArgs:\n    param: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_remove_extra_indentation(self):
        """Test removal of extra indentation."""
        input_doc = "  Summary line.\n  \n  Args:\n      param: Description"
        expected = "Summary line.\n\nArgs:\n    param: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_preserve_relative_indentation(self):
        """Test preservation of relative indentation."""
        input_doc = "Summary line.\n\n    Args:\n        param: Description"
        expected = "Summary line.\n\n    Args:\n        param: Description"
        assert (
            normalize_docstring_indentation(
                input_doc, preserve_relative_indentation=True
            )
            == expected
        )

    def test_no_preserve_relative_indentation(self):
        """Test without preserving relative indentation."""
        input_doc = "Summary line.\n\n    Args:\n        param: Description"
        expected = "Summary line.\n\nArgs:\nparam: Description"
        assert (
            normalize_docstring_indentation(
                input_doc, preserve_relative_indentation=False
            )
            == expected
        )

    def test_custom_base_indent(self):
        """Test with custom base indentation."""
        input_doc = "  Summary line.\n  \n  Args:\n      param: Description"
        expected = "  Summary line.\n\n  Args:\n      param: Description"
        assert normalize_docstring_indentation(input_doc, base_indent="  ") == expected

    def test_complex_docstring(self):
        """Test complex docstring with multiple sections."""
        input_doc = """    Calculate the Fibonacci number.
    
    This function calculates the nth Fibonacci number using recursion.
    
        Args:
            n: The position in the Fibonacci sequence.
        
        Returns:
            The nth Fibonacci number.
        
        Raises:
            ValueError: If n is negative."""

        expected = """Calculate the Fibonacci number.

This function calculates the nth Fibonacci number using recursion.

    Args:
        n: The position in the Fibonacci sequence.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative."""

        assert normalize_docstring_indentation(input_doc) == expected

    def test_mixed_indentation_levels(self):
        """Test docstring with mixed indentation levels."""
        input_doc = """  Summary line.
  
          Args:
              param1: First parameter.
                  param2: Second parameter with extra indent.
  
          Returns:
              Description of return value."""

        expected = """Summary line.

        Args:
            param1: First parameter.
                param2: Second parameter with extra indent.

        Returns:
            Description of return value."""

        assert normalize_docstring_indentation(input_doc) == expected

    def test_tabs_vs_spaces(self):
        """Test handling of tabs vs spaces."""
        input_doc = "\tSummary line.\n\t\n\tArgs:\n\t\tparam: Description"
        expected = "Summary line.\n\nArgs:\nparam: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_whitespace_only_lines(self):
        """Test handling of lines with only whitespace."""
        input_doc = "Summary line.\n   \n\nArgs:\n    param: Description"
        expected = "Summary line.\n\n\nArgs:\n    param: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_leading_trailing_whitespace(self):
        """Test handling of leading and trailing whitespace."""
        input_doc = "  \n  Summary line.\n  \n  Args:\n    param: Description\n  "
        expected = "\nSummary line.\n\nArgs:\nparam: Description\n"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_edge_case_single_space(self):
        """Test edge case with single space indentation."""
        input_doc = " Summary line.\n \n Args:\n  param: Description"
        expected = "Summary line.\n\nArgs:\nparam: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_edge_case_no_indentation(self):
        """Test edge case with no indentation."""
        input_doc = "Summary line.\n\nArgs:\nparam: Description"
        expected = "Summary line.\n\nArgs:\nparam: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_preserve_empty_lines(self):
        """Test that empty lines are preserved."""
        input_doc = "Summary line.\n\n\nArgs:\n    param: Description"
        expected = "Summary line.\n\n\nArgs:\n    param: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_very_deep_indentation(self):
        """Test handling of very deep indentation."""
        input_doc = "        Summary line.\n        \n        Args:\n            param: Description"
        expected = "Summary line.\n\nArgs:\n    param: Description"
        assert normalize_docstring_indentation(input_doc) == expected

    def test_unicode_characters(self):
        """Test handling of Unicode characters in content."""
        input_doc = "  Summary line with émojis 🚀.\n  \n  Args:\n      param: Description with ñ"
        expected = (
            "Summary line with émojis 🚀.\n\nArgs:\n    param: Description with ñ"
        )
        assert normalize_docstring_indentation(input_doc) == expected

    def test_special_characters(self):
        """Test handling of special characters."""
        input_doc = "  Summary line with @#$%^&*().\n  \n  Args:\n      param: Description with [brackets]"
        expected = "Summary line with @#$%^&*().\n\nArgs:\n    param: Description with [brackets]"
        assert normalize_docstring_indentation(input_doc) == expected


class TestDetectDocstringIndentationIssues:
    """Test the detect_docstring_indentation_issues function."""

    def test_empty_docstring(self):
        """Test empty docstring."""
        assert detect_docstring_indentation_issues("") == []
        assert detect_docstring_indentation_issues("   ") == []

    def test_single_line_docstring(self):
        """Test single line docstring."""
        assert detect_docstring_indentation_issues("Simple docstring") == []

    def test_consistent_indentation(self):
        """Test docstring with consistent indentation."""
        docstring = "Summary line.\n\nArgs:\n    param: Description"
        # This should be considered consistent since the difference is a multiple of 4
        assert detect_docstring_indentation_issues(docstring) == []

    def test_inconsistent_indentation(self):
        """Test docstring with inconsistent indentation."""
        docstring = "Summary line.\n\n  Args:\n    param: Description"
        issues = detect_docstring_indentation_issues(docstring)
        assert len(issues) > 0
        assert "inconsistent indentation" in issues[0]

    def test_mixed_tabs_and_spaces(self):
        """Test docstring with mixed tabs and spaces."""
        docstring = "Summary line.\n\n\tArgs:\n    param: Description"
        issues = detect_docstring_indentation_issues(docstring)
        assert "Mixed tabs and spaces in indentation" in issues

    def test_multiple_issues(self):
        """Test docstring with multiple indentation issues."""
        docstring = "Summary line.\n\n  Args:\n\t    param: Description"
        issues = detect_docstring_indentation_issues(docstring)
        assert len(issues) > 1


class TestGetDocstringBaseIndent:
    """Test the get_docstring_base_indent function."""

    def test_empty_docstring(self):
        """Test empty docstring."""
        assert get_docstring_base_indent("") == ""
        assert get_docstring_base_indent("   ") == ""

    def test_no_indentation(self):
        """Test docstring with no indentation."""
        assert get_docstring_base_indent("Summary line") == ""

    def test_single_space_indentation(self):
        """Test docstring with single space indentation."""
        assert get_docstring_base_indent(" Summary line") == " "

    def test_four_space_indentation(self):
        """Test docstring with four space indentation."""
        assert get_docstring_base_indent("    Summary line") == "    "

    def test_tab_indentation(self):
        """Test docstring with tab indentation."""
        assert get_docstring_base_indent("\tSummary line") == "\t"

    def test_mixed_indentation(self):
        """Test docstring with mixed indentation."""
        docstring = "    Summary line.\n    \n    Args:\n        param: Description"
        assert get_docstring_base_indent(docstring) == "    "


class TestIsDocstringIndentationConsistent:
    """Test the is_docstring_indentation_consistent function."""

    def test_empty_docstring(self):
        """Test empty docstring."""
        assert is_docstring_indentation_consistent("") is True
        assert is_docstring_indentation_consistent("   ") is True

    def test_single_line_docstring(self):
        """Test single line docstring."""
        assert is_docstring_indentation_consistent("Simple docstring") is True

    def test_consistent_indentation(self):
        """Test docstring with consistent indentation."""
        docstring = "Summary line.\n\nArgs:\n    param: Description"
        # This should be considered consistent since the difference is a multiple of 4
        assert is_docstring_indentation_consistent(docstring) is True

    def test_inconsistent_indentation(self):
        """Test docstring with inconsistent indentation."""
        docstring = "Summary line.\n\n  Args:\n    param: Description"
        assert is_docstring_indentation_consistent(docstring) is False

    def test_mixed_tabs_and_spaces(self):
        """Test docstring with mixed tabs and spaces."""
        docstring = "Summary line.\n\n\tArgs:\n    param: Description"
        assert is_docstring_indentation_consistent(docstring) is False


class TestIntegrationScenarios:
    """Test integration scenarios that might occur in real usage."""

    def test_llm_generated_docstring_with_extra_indentation(self):
        """Test LLM-generated docstring with extra indentation."""
        # This simulates what the LLM might generate
        llm_output = """    Calculate the Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence.
    
    Returns:
        The nth Fibonacci number."""

        normalized = normalize_docstring_indentation(llm_output)
        expected = """Calculate the Fibonacci number.

Args:
    n: The position in the Fibonacci sequence.

Returns:
    The nth Fibonacci number."""

        assert normalized == expected
        assert is_docstring_indentation_consistent(normalized) is True

    def test_llm_generated_docstring_with_inconsistent_indentation(self):
        """Test LLM-generated docstring with inconsistent indentation."""
        # This simulates what the LLM might generate with inconsistent indentation
        llm_output = """Calculate the Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence.

    Returns:
        The nth Fibonacci number."""

        normalized = normalize_docstring_indentation(llm_output)
        expected = """Calculate the Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence.

    Returns:
        The nth Fibonacci number."""

        assert normalized == expected
        assert is_docstring_indentation_consistent(normalized) is True

    def test_llm_generated_docstring_with_mixed_indentation(self):
        """Test LLM-generated docstring with mixed indentation levels."""
        # This simulates what the LLM might generate with mixed indentation
        llm_output = """    Calculate the Fibonacci number.
    
            Args:
                n: The position in the Fibonacci sequence.
    
            Returns:
                The nth Fibonacci number."""

        normalized = normalize_docstring_indentation(llm_output)
        expected = """Calculate the Fibonacci number.

        Args:
            n: The position in the Fibonacci sequence.

        Returns:
            The nth Fibonacci number."""

        assert normalized == expected
        assert is_docstring_indentation_consistent(normalized) is True

    def test_round_trip_consistency(self):
        """Test that normalization is idempotent."""
        original = "Summary line.\n\nArgs:\n    param: Description"
        normalized = normalize_docstring_indentation(original)
        normalized_again = normalize_docstring_indentation(normalized)

        assert normalized == normalized_again

    def test_preserve_content_while_fixing_indentation(self):
        """Test that content is preserved while fixing indentation."""
        original = "  Summary line with special chars @#$%.\n  \n  Args:\n      param: Description with [brackets]"
        normalized = normalize_docstring_indentation(original)

        # Content should be preserved
        assert "Summary line with special chars @#$%." in normalized
        assert "param: Description with [brackets]" in normalized

        # Indentation should be fixed
        assert is_docstring_indentation_consistent(normalized) is True


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_none_input(self):
        """Test handling of None input."""
        # The function should handle None gracefully
        result = normalize_docstring_indentation(None)
        assert result is None

    def test_very_long_lines(self):
        """Test handling of very long lines."""
        long_line = "A" * 1000
        input_doc = f"  {long_line}\n  \n  Args:\n      param: Description"
        normalized = normalize_docstring_indentation(input_doc)

        assert long_line in normalized
        assert is_docstring_indentation_consistent(normalized) is True

    def test_very_deep_nesting(self):
        """Test handling of very deep nesting."""
        input_doc = "Summary line.\n\n        Args:\n            param: Description"
        normalized = normalize_docstring_indentation(input_doc)

        assert is_docstring_indentation_consistent(normalized) is True

    def test_only_whitespace_lines(self):
        """Test handling of docstring with only whitespace lines."""
        input_doc = "   \n   \n   "
        normalized = normalize_docstring_indentation(input_doc)

        assert normalized == input_doc

    def test_carriage_returns(self):
        """Test handling of carriage returns."""
        input_doc = "Summary line.\r\n\r\nArgs:\r\n    param: Description"
        normalized = normalize_docstring_indentation(input_doc)

        # Should handle CRLF line endings
        assert "Summary line." in normalized
        assert "Args:" in normalized
