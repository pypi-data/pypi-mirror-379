"""
Rules package for compliance checking.

This package contains all compliance rules for DocOctopy.
Rules are organized by type and severity level.

Available rule types:
- Python-specific rules (organized by functionality)
- Basic compliance rules
- Google style validation rules
- Advanced Google style rules

Planned rule types:
- Coverage threshold rules
- Custom rule framework
- Language-specific rules
"""

# Import Python rules to ensure they're registered
from . import python  # noqa: F401

# TODO: Add coverage threshold rules
# TODO: Add custom rule framework
# TODO: Add language-specific rules
# TODO: Add rule testing framework
