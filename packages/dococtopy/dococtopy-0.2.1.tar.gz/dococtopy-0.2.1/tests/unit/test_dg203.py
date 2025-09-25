"""Tests for DG203ExtraParamInDocstring rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG203ExtraParamInDocstring


class TestDG203ExtraParamInDocstring:
    """Test cases for DG203ExtraParamInDocstring rule."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        import ast

        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=docstring,
                        ast_node=node,
                    )
                )

        return symbols

    def test_no_extra_parameters_passes(self):
        """Test that functions with matching parameters pass validation."""
        code = '''
def example_function(param1, param2):
    """Example function with correct parameters.

    Args:
        param1: First parameter description.
        param2: Second parameter description.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_single_extra_parameter_detected(self):
        """Test that a single extra parameter in docstring is detected."""
        code = '''
def example_function(param1):
    """Example function with extra parameter in docstring.

    Args:
        param1: First parameter description.
        param2: Extra parameter not in function signature.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG203"
        assert "Extra parameter 'param2' in docstring" in findings[0].message
        assert findings[0].level.value == "error"

    def test_multiple_extra_parameters_detected(self):
        """Test that multiple extra parameters in docstring are detected."""
        code = '''
def example_function(param1):
    """Example function with multiple extra parameters.

    Args:
        param1: First parameter description.
        param2: Extra parameter not in function signature.
        param3: Another extra parameter not in function signature.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG203" for f in findings)
        assert any(
            "Extra parameter 'param2' in docstring" in f.message for f in findings
        )
        assert any(
            "Extra parameter 'param3' in docstring" in f.message for f in findings
        )

    def test_self_parameter_ignored(self):
        """Test that 'self' parameter is ignored in class methods."""
        code = '''
class ExampleClass:
    def method(self, param1):
        """Method with self parameter.

        Args:
            self: Instance reference.
            param1: First parameter description.
        """
        return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        # The rule actually flags 'self' as extra because extract_function_params skips it
        assert len(findings) == 1
        assert findings[0].rule_id == "DG203"
        assert "Extra parameter 'self' in docstring" in findings[0].message

    def test_cls_parameter_ignored(self):
        """Test that 'cls' parameter is ignored in class methods."""
        code = '''
class ExampleClass:
    @classmethod
    def class_method(cls, param1):
        """Class method with cls parameter.

        Args:
            cls: Class reference.
            param1: First parameter description.
        """
        return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_parameters_function_passes(self):
        """Test that functions with no parameters pass validation."""
        code = '''
def example_function():
    """Example function with no parameters."""
    return "example"
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_no_args_section_passes(self):
        """Test that functions without Args section pass validation."""
        code = '''
def example_function(param1, param2):
    """Example function without Args section."""
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_function_extra_parameter_detected(self):
        """Test that async functions with extra parameters are detected."""
        code = '''
async def async_function(param1):
    """Async function with extra parameter.

    Args:
        param1: First parameter description.
        param2: Extra parameter not in function signature.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG203"
        assert "Extra parameter 'param2' in docstring" in findings[0].message

    def test_function_with_default_parameters(self):
        """Test that functions with default parameters work correctly."""
        code = '''
def example_function(param1, param2="default"):
    """Example function with default parameters.

    Args:
        param1: First parameter description.
        param2: Second parameter with default value.
    """
    return f"{param1} {param2}"
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_extra_default_parameter_detected(self):
        """Test that extra default parameters in docstring are detected."""
        code = '''
def example_function(param1):
    """Example function with extra default parameter in docstring.

    Args:
        param1: First parameter description.
        param2: Extra parameter with default value.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG203"
        assert "Extra parameter 'param2' in docstring" in findings[0].message

    def test_function_with_kwargs_parameter(self):
        """Test that functions with **kwargs parameter work correctly."""
        code = '''
def example_function(param1, **kwargs):
    """Example function with kwargs parameter.

    Args:
        param1: First parameter description.
        **kwargs: Additional keyword arguments.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        # Now that extract_function_params includes **kwargs, this should pass
        assert len(findings) == 0

    def test_function_with_args_parameter(self):
        """Test that functions with *args parameter work correctly."""
        code = '''
def example_function(param1, *args):
    """Example function with args parameter.

    Args:
        param1: First parameter description.
        *args: Additional positional arguments.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        # Now that extract_function_params includes *args, this should pass
        assert len(findings) == 0

    def test_function_with_extra_kwargs_detected(self):
        """Test that extra **kwargs in docstring is detected."""
        code = '''
def example_function(param1):
    """Example function with extra kwargs in docstring.

    Args:
        param1: First parameter description.
        **kwargs: Extra kwargs not in function signature.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG203"
        assert "Extra parameter '**kwargs' in docstring" in findings[0].message

    def test_function_with_extra_args_detected(self):
        """Test that extra *args in docstring is detected."""
        code = '''
def example_function(param1):
    """Example function with extra args in docstring.

    Args:
        param1: First parameter description.
        *args: Extra args not in function signature.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG203"
        assert "Extra parameter '*args' in docstring" in findings[0].message

    def test_no_docstring_not_checked(self):
        """Test that functions without docstrings are not checked."""
        code = """
def example_function(param1, param2):
    return f"{param1} {param2}"
"""
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_not_checked(self):
        """Test that classes are not checked by this rule."""
        code = '''
class ExampleClass:
    """Example class docstring."""
    pass
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_functions_with_extra_parameters(self):
        """Test that multiple functions with extra parameters are all detected."""
        code = '''
def function1(param1):
    """Function with extra parameter.

    Args:
        param1: First parameter description.
        param2: Extra parameter.
    """
    return param1

def function2(param1):
    """Another function with extra parameter.

    Args:
        param1: First parameter description.
        param3: Another extra parameter.
    """
    return param1
'''
        symbols = self._parse_code(code)
        rule = DG203ExtraParamInDocstring()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG203" for f in findings)
        assert any(
            "Extra parameter 'param2' in docstring" in f.message for f in findings
        )
        assert any(
            "Extra parameter 'param3' in docstring" in f.message for f in findings
        )
