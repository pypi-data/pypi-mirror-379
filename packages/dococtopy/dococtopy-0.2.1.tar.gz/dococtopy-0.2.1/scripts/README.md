# Scripts Directory

This directory contains development and utility scripts for DocOctopy.

## Available Scripts

### `comprehensive_compare_models.py`

A comprehensive script to compare different LLM models for docstring generation quality and cost.

**Usage:**

```bash
# Set API keys
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"

# Run comparison
python3 scripts/comprehensive_compare_models.py
```

**What it does:**

- Tests multiple OpenAI and Anthropic models
- Generates docstrings for a test fixture
- Calculates quality scores based on docstring completeness
- Compares cost-effectiveness
- Saves results to `docs/model-comparison/`

**Requirements:**

- `rich` library for colored output
- Valid API keys for the providers you want to test
- DocOctopy installed and accessible via `dococtopy` command

**Output:**

- Console table with comparison results
- `docs/model-comparison/comprehensive-comparison-results.txt` - Detailed results
- Individual `*_result.py` files for each model tested

**Models Tested:**

- **OpenAI**: gpt-5-nano, gpt-5-mini, gpt-4.1-nano, gpt-4.1-mini
- **Anthropic**: claude-haiku-3.5, claude-haiku-3, claude-sonnet-4, claude-opus-4.1

### `pre-commit.sh`

Pre-commit hook script that runs formatting and linting checks.

**Usage:**

```bash
# Run manually
./scripts/pre-commit.sh

# Or as a git hook
ln -s ../../scripts/pre-commit.sh .git/hooks/pre-commit
```

**What it does:**

- Runs Black code formatting
- Runs isort import sorting
- Runs mypy type checking
- Runs pytest tests
- Ensures code quality before commits

### `publish.sh`

Publishing script for releasing DocOctopy to PyPI.

**Usage:**

```bash
# Publish to PyPI
./scripts/publish.sh

# Dry run (check only)
./scripts/publish.sh --dry-run
```

**What it does:**

- Validates project configuration
- Builds distribution packages
- Runs tests and checks
- Publishes to PyPI (if not dry run)
- Handles version management

## Adding New Scripts

When adding new scripts to this directory:

1. Make them executable (`chmod +x`)
2. Add documentation to this README
3. Include proper error handling and user feedback
4. Use `rich` for colored output when appropriate
