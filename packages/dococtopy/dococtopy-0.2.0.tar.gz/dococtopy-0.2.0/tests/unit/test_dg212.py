"""Tests for DG212AttributesSectionValidation rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG212AttributesSectionValidation


class TestDG212AttributesSectionValidation:
    """Test cases for DG212AttributesSectionValidation rule."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        import ast

        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind=(
                            "function"
                            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                            else "class"
                        ),
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=docstring,
                        ast_node=node,
                    )
                )

        return symbols

    def test_class_with_attributes_section_passes(self):
        """Test that classes with Attributes section pass."""
        code = '''
class ExampleClass:
    """Example class with Attributes section.

    Attributes:
        name: The name of the instance.
        value: The value of the instance.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_without_attributes_section_fails(self):
        """Test that classes without Attributes section fail."""
        code = '''
class ExampleClass:
    """Example class without Attributes section."""
    def __init__(self, name, value):
        self.name = name
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG212"
        assert (
            "Class with public attributes should have Attributes section"
            in findings[0].message
        )
        assert findings[0].level.value == "warning"

    def test_class_without_public_attributes_passes(self):
        """Test that classes without public attributes pass."""
        code = '''
class ExampleClass:
    """Example class without public attributes."""
    def __init__(self):
        self._private_attr = "private"
        self.__very_private = "very private"
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_no_docstring_passes(self):
        """Test that classes without docstrings pass."""
        code = """
class ExampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value
"""
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_attributes_section_dash_format_passes(self):
        """Test that classes with Attributes section using dash format pass."""
        code = '''
class ExampleClass:
    """Example class with Attributes section using dash format.

    Attributes - name: The name of the instance.
    Attributes - value: The value of the instance.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_attributes_section_space_format_passes(self):
        """Test that classes with Attributes section using space format pass."""
        code = '''
class ExampleClass:
    """Example class with Attributes section using space format.

    Attributes name: The name of the instance.
    Attributes value: The value of the instance.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_attributes_section_newline_format_passes(self):
        """Test that classes with Attributes section using newline format pass."""
        code = '''
class ExampleClass:
    """Example class with Attributes section using newline format.

    Attributes
        name: The name of the instance.
        value: The value of the instance.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_mixed_public_private_attributes_fails(self):
        """Test that classes with mixed public and private attributes fail if no Attributes section."""
        code = '''
class ExampleClass:
    """Example class with mixed attributes."""
    def __init__(self, name, value):
        self.name = name  # public
        self.value = value  # public
        self._private = "private"
        self.__very_private = "very private"
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG212"
        assert (
            "Class with public attributes should have Attributes section"
            in findings[0].message
        )

    def test_class_with_class_attributes_passes(self):
        """Test that classes with class attributes and Attributes section pass."""
        code = '''
class ExampleClass:
    """Example class with class attributes.

    Attributes:
        CLASS_CONSTANT: A class constant.
        class_var: A class variable.
    """
    CLASS_CONSTANT = "constant"
    class_var = "variable"
    
    def __init__(self, name):
        self.name = name
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_class_attributes_without_section_fails(self):
        """Test that classes with class attributes without Attributes section fail."""
        code = '''
class ExampleClass:
    """Example class with class attributes."""
    CLASS_CONSTANT = "constant"
    class_var = "variable"
    
    def __init__(self, name):
        self.name = name
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG212"
        assert (
            "Class with public attributes should have Attributes section"
            in findings[0].message
        )

    def test_class_with_property_attributes_passes(self):
        """Test that classes with property attributes and Attributes section pass."""
        code = '''
class ExampleClass:
    """Example class with property attributes.

    Attributes:
        name: The name property.
        value: The value property.
    """
    def __init__(self, name, value):
        self._name = name
        self._value = value
    
    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_property_attributes_without_section_fails(self):
        """Test that classes with property attributes without Attributes section fail."""
        code = '''
class ExampleClass:
    """Example class with property attributes."""
    def __init__(self, name, value):
        self._name = name
        self._value = value
    
    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG212"
        assert (
            "Class with public attributes should have Attributes section"
            in findings[0].message
        )

    def test_class_with_only_private_attributes_passes(self):
        """Test that classes with only private attributes pass."""
        code = '''
class ExampleClass:
    """Example class with only private attributes."""
    def __init__(self):
        self._private_attr = "private"
        self.__very_private = "very private"
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_only_methods_passes(self):
        """Test that classes with only methods pass."""
        code = '''
class ExampleClass:
    """Example class with only methods."""
    def method1(self):
        return "method1"
    
    def method2(self):
        return "method2"
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_classes_with_attributes_section_issues(self):
        """Test that multiple classes with attributes section issues are all detected."""
        code = '''
class Class1:
    """First class without Attributes section."""
    def __init__(self, name):
        self.name = name

class Class2:
    """Second class without Attributes section."""
    def __init__(self, value):
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG212" for f in findings)
        assert all(
            "Class with public attributes should have Attributes section" in f.message
            for f in findings
        )

    def test_class_with_attributes_section_and_other_sections_passes(self):
        """Test that classes with Attributes section and other sections pass."""
        code = '''
class ExampleClass:
    """Example class with Attributes section and other sections.

    Args:
        name: The name parameter.
        value: The value parameter.

    Attributes:
        name: The name of the instance.
        value: The value of the instance.

    Raises:
        ValueError: When invalid parameters are provided.
    """
    def __init__(self, name, value):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_class_with_attributes_section_case_insensitive_passes(self):
        """Test that classes with Attributes section (case insensitive) pass."""
        code = '''
class ExampleClass:
    """Example class with Attributes section (case insensitive).

    ATTRIBUTES:
        name: The name of the instance.
        value: The value of the instance.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value
'''
        symbols = self._parse_code(code)
        rule = DG212AttributesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
