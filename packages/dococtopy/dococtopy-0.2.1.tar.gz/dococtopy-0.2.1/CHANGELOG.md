# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2024-12-19

### Fixed
- **DSPy Installation Issue**: Fixed critical issue where users couldn't use LLM functionality after installing `dococtopy[llm]`
- **Package Building**: Fixed `.gitignore` exclusion that prevented CLI `main.py` from being included in the package
- **Error Messages**: Improved error messages to show correct installation command (`pip install dococtopy[llm]`)
- **Dependency Management**: Moved DSPy from main dependencies to optional `llm` extras to prevent conflicts

### Changed
- **Dependency Structure**: DSPy is now only included in the `llm` extras, not in core dependencies
- **Error Handling**: Enhanced error handling to avoid duplicate messages and provide clearer guidance

### Technical Improvements
- **Package Integrity**: Ensured all CLI files are properly included in the built package
- **Installation Experience**: Users can now install basic functionality without LLM dependencies, and add LLM support with `[llm]` extras

## [0.1.3] - 2024-12-19

### Added
- **Advanced Google Style Rules (DG211-DG214)**:
  - DG211: Generator functions should have Yields section validation
  - DG212: Classes with public attributes should have Attributes section validation
  - DG213: Complex functions should have Examples section validation
  - DG214: Functions with special behavior should have Note section validation

- **Context-Specific Rules (DG401-DG403)**:
  - DG401: Test function docstring style validation
  - DG402: Public API function documentation completeness
  - DG403: Exception documentation completeness with AST analysis

- **LLM Model Comparison Framework**:
  - Comprehensive model comparison tool (`scripts/comprehensive_compare_models.py`)
  - Detailed model performance analysis and cost comparison
  - Model recommendation system based on quality scores and cost efficiency
  - Support for OpenAI, Anthropic, and Ollama models

- **Enhanced Development Workflow**:
  - Pre-commit hooks for code quality
  - Development scripts in `scripts/` directory
  - Improved task management with taskipy
  - Better CI/CD integration

- **Trivial Fix Detection**:
  - Automatic detection and fixing of simple docstring issues
  - Smart fallback to LLM for complex fixes
  - Improved fix validation and error handling

### Changed
- **Improved Rule Architecture**:
  - Refactored rules into modular Python-specific modules
  - Better separation of concerns between rule types
  - Enhanced AST utilities for better symbol detection

- **Enhanced Documentation**:
  - Comprehensive README with model recommendations
  - Detailed rule reference with examples
  - Interactive fix mode documentation
  - Development setup and contribution guidelines

- **Better Error Handling**:
  - Improved validation for docstring fixes
  - Better error messages and debugging information
  - Enhanced edge case handling

### Fixed
- Fixed CLI startup time optimization
- Resolved virtual environment warnings
- Fixed dependency conflicts with DSPy
- Improved cache file handling
- Fixed formatting issues across the codebase

### Technical Improvements
- **Test Coverage**: 141 tests with 73% coverage
- **Code Quality**: All linting checks pass
- **Build System**: Improved package building and distribution
- **Performance**: Optimized CLI startup and scanning performance

## [0.1.2] - 2024-12-18

### Added
- Initial release with core docstring compliance checking
- Google-style docstring validation rules (DG201-DG210)
- Basic missing docstring detection (DG101)
- LLM-powered remediation with DSPy integration
- Multiple output formats (JSON, SARIF, console)
- Interactive fix workflows
- Configuration system with pyproject.toml support
- Caching and incremental scanning

### Features
- Python docstring compliance checking
- Google-style validation rules
- LLM-powered remediation
- Multiple output formats
- Configuration system
- Caching and incremental scanning
- Interactive fix workflows
- File writing capabilities
