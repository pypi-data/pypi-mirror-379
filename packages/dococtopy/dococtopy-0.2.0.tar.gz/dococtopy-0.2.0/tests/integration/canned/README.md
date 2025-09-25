# Canned Integration Tests

This directory contains canned integration tests for DocOctopy. These tests use predefined scenarios to verify that the LLM remediation functionality works correctly with different models and providers.

## Overview

The canned tests provide a structured way to:

- Test LLM providers (OpenAI, Anthropic, Ollama) with consistent scenarios
- Verify docstring generation and fixing capabilities
- Compare performance across different models
- Debug issues with specific test cases

## File Structure

### Fixture Files

The `fixtures/` directory contains two types of files:

#### `.fixture` Files (Test Inputs)

- **Purpose**: Contain the test input with missing, malformed, or improper docstrings
- **Usage**: Copied to the test directory during setup
- **Protection**: Read-only files to prevent accidental modification
- **Note**: Copied files are made writable (644) so they can be modified during testing
- **Examples**:
  - `missing_docstrings.py.fixture` - Functions and classes without docstrings
  - `malformed_docstrings.py.fixture` - Functions with malformed Google-style docstrings
  - `mixed_issues.py.fixture` - Various docstring issues (missing params, wrong sections, etc.)

#### `.py` Files (Expected Outputs)

- **Purpose**: Contain the expected output with proper docstrings
- **Usage**: Reference for what the LLM should generate
- **Examples**:
  - `missing_docstrings.py` - Functions and classes with proper docstrings
  - `malformed_docstrings.py` - Functions with corrected Google-style docstrings

### Test Runner

The `test_runner.py` script provides a modular interface for running tests:

```bash
# List available scenarios
uv run python -m tests.integration.canned.test_runner --list

# Set up test files (copy fixtures to test directory)
uv run python -m tests.integration.canned.test_runner --setup <scenario>

# Run the fix command on test files
uv run python -m tests.integration.canned.test_runner --run <scenario>

# Clean up test files
uv run python -m tests.integration.canned.test_runner --cleanup <scenario>

# Run everything in one command (setup + run + cleanup)
uv run python -m tests.integration.canned.test_runner --run-full <scenario>
```

## Available Scenarios

| Scenario | Description | Rules | Provider |
|----------|-------------|-------|----------|
| `missing_docstrings` | Add docstrings to functions and classes without them | DG101 | ollama:codeqwen:latest |
| `malformed_docstrings` | Fix malformed Google-style docstrings | DG201,DG202,DG203,DG204 | ollama:codeqwen:latest |
| `mixed_issues` | Handle mixed docstring issues | DG101,DG202,DG204,DG205 | ollama:codeqwen:latest |
| `real_world_patterns` | Real-world code patterns from actual projects | DG101,DG202,DG204 | ollama:codeqwen:latest |
| `openai_gpt5_nano` | Test with OpenAI GPT-5-nano | DG101 | openai:gpt-5-nano |
| `anthropic_haiku` | Test with Anthropic Claude Haiku | DG101 | anthropic:claude-3-haiku-20240307 |
| `google_style_patterns` | Comprehensive Google style docstring patterns | DG101,DG201,DG202,DG203,DG204,DG205,DG210 | ollama:codeqwen:latest |

## Configuration

### Setup Configuration

Before running tests, configure your LLM providers:

```bash
# Interactive configuration setup
uv run python -m tests.integration.canned.test_runner --setup-config

# Show current configuration
uv run python -m tests.integration.canned.test_runner --show-config
```

### Environment Variables

The test runner automatically sets environment variables for API keys:

- `OPENAI_API_KEY` - For OpenAI models
- `ANTHROPIC_API_KEY` - For Anthropic models
- `OLLAMA_BASE_URL` - For Ollama models (default: <http://localhost:11434>)

## Usage Examples

### Testing OpenAI GPT-5-nano

```bash
# Run the full test workflow
uv run python -m tests.integration.canned.test_runner --run-full openai_gpt5_nano

# Or run step by step for debugging
uv run python -m tests.integration.canned.test_runner --setup openai_gpt5_nano
uv run python -m tests.integration.canned.test_runner --run openai_gpt5_nano
uv run python -m tests.integration.canned.test_runner --cleanup openai_gpt5_nano
```

### Testing Ollama Models

```bash
# Run with Ollama (requires Ollama server running)
uv run python -m tests.integration.canned.test_runner --run-full missing_docstrings
```

### Inspecting Results

```bash
# Inspect a specific scenario
uv run python -m tests.integration.canned.test_runner --inspect openai_gpt5_nano
```

## Adding New Scenarios

To add a new test scenario:

1. **Create fixture files**:
   - `fixtures/your_scenario.py.fixture` - Test input with issues
   - `fixtures/your_scenario.py` - Expected output with proper docstrings

2. **Make fixture read-only**:

   ```bash
   chmod 444 fixtures/your_scenario.py.fixture
   ```

3. **Add scenario to test runner**:
   Edit `test_runner.py` and add your scenario to the `create_scenarios()` method.

## Troubleshooting

### Common Issues

1. **"DSPy is required" error**:

   ```bash
   uv add dspy-ai --group dev
   ```

2. **"OpenAI API key required" error**:
   - Set `OPENAI_API_KEY` environment variable
   - Or run `--setup-config` to configure interactively

3. **"Scenario files not found" error**:
   - Run `--setup <scenario>` first to copy fixture files

4. **"Could not fully fix docstring" warnings**:
   - These are common and indicate the LLM had trouble with indentation
   - The docstrings are still added, just with minor formatting issues

### Debugging

Use the modular commands to debug issues:

```bash
# Set up files and inspect them
uv run python -m tests.integration.canned.test_runner --setup openai_gpt5_nano
cat tests/integration/canned/scenarios/missing_docstrings.py

# Run fix and see detailed output
uv run python -m tests.integration.canned.test_runner --run openai_gpt5_nano

# Check results before cleanup
cat tests/integration/canned/scenarios/missing_docstrings.py
```

## Best Practices

1. **Always use `.fixture` files for test inputs** - they are read-only and protected
2. **Test with multiple providers** - compare results across OpenAI, Anthropic, and Ollama
3. **Use modular commands for debugging** - `--setup`, `--run`, `--cleanup` separately
4. **Check results before cleanup** - inspect the generated docstrings
5. **Document new scenarios** - update this README when adding new test cases

## Integration with CI/CD

These tests can be integrated into CI/CD pipelines:

```bash
# Run all scenarios
uv run python -m tests.integration.canned.test_runner --all

# Run specific provider tests
uv run python -m tests.integration.canned.test_runner --run-full openai_gpt5_nano
uv run python -m tests.integration.canned.test_runner --run-full anthropic_haiku
```
