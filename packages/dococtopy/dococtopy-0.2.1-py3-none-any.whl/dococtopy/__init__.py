"""
DocOctopy - A language-agnostic docstyle compliance & remediation tool.

Version Management:
This package uses a centralized version management system. The version is defined
in _version.py and imported here dynamically. All components should import the
version using: from dococtopy import __version__

To manage versions, use the task commands:
- uv run task version:show           # Show current version
- uv run task version:bump:patch     # Bump patch version
- uv run task version:bump:minor     # Bump minor version
- uv run task version:bump:major     # Bump major version
- uv run task version:set X.Y.Z      # Set specific version
"""

from dococtopy._version import __version__

__author__ = "Your Name"
__email__ = "your.email@example.com"
__description__ = "A language-agnostic docstyle compliance & remediation tool"

# Core exports
from dococtopy.core.findings import Finding, FindingLevel

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__description__",
    "Finding",
    "FindingLevel",
]
