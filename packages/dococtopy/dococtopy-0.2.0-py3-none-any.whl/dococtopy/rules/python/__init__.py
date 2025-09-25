"""
Python-specific rules for DocOctopy.

This package contains Python-specific compliance rules organized by functionality:

- missing_docstrings: Rules for missing docstring detection (DG101, DG215, DG216)
- google_style: Google-style docstring validation rules (DG201-DG214)
- formatting: Basic formatting rules (DG301, DG302)
- context_specific: Context-specific docstring rules (DG401-DG403)

Each module contains related rules with shared utilities and common patterns.
"""

# Import AST utilities for use by rules
from .ast_utils import *  # noqa: F401, F403
from .context_specific import *  # noqa: F401, F403
from .formatting import *  # noqa: F401, F403
from .google_style import *  # noqa: F401, F403

# Import all rules to ensure they're registered
from .missing_docstrings import *  # noqa: F401, F403
