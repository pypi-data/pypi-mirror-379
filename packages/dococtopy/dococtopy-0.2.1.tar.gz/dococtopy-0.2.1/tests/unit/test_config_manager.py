"""Tests for the ConfigManager class."""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from dococtopy.core.config import ConfigManager, LLMConfig, LLMProviderConfig


@pytest.fixture
def clean_env():
    """Fixture to ensure clean environment for tests."""
    # Store original environment
    original_env = {}
    env_vars_to_clear = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "OLLAMA_BASE_URL",
        "OLLAMA_MODEL",
        "OPENAI_BASE_URL",
        "ANTHROPIC_BASE_URL",
    ]

    for var in env_vars_to_clear:
        original_env[var] = os.environ.get(var)
        if var in os.environ:
            del os.environ[var]

    yield

    # Restore original environment
    for var, value in original_env.items():
        if value is not None:
            os.environ[var] = value
        elif var in os.environ:
            del os.environ[var]


class TestConfigManager:
    """Test ConfigManager functionality."""

    def test_config_manager_initialization(self, clean_env):
        """Test ConfigManager initialization."""
        config_manager = ConfigManager()
        assert config_manager.user_config_dir == Path.home() / ".config" / "dococtopy"
        assert (
            config_manager.user_config_file
            == config_manager.user_config_dir / "config.toml"
        )

    def test_config_manager_with_custom_dir(self, clean_env):
        """Test ConfigManager with custom config directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))
            assert config_manager.user_config_dir == Path(temp_dir)
            assert config_manager.user_config_file == Path(temp_dir) / "config.toml"

    def test_get_user_config_empty(self, clean_env):
        """Test getting user config when file doesn't exist."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))
            config = config_manager.get_user_config()
            assert config == {}

    def test_save_and_load_user_config(self, clean_env):
        """Test saving and loading user configuration."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))

            test_config = {
                "llm": {
                    "default_provider": "openai",
                    "default_model": "gpt-5-nano",
                    "openai": {
                        "api_key": "sk-test123",
                        "base_url": "https://api.openai.com/v1",
                    },
                }
            }

            # Save config
            config_manager.save_user_config(test_config)

            # Load config
            loaded_config = config_manager.get_user_config()
            assert loaded_config == test_config

    def test_get_project_config_empty(self, clean_env):
        """Test getting project config when pyproject.toml doesn't exist."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager()
            config = config_manager.get_project_config(Path(temp_dir))
            assert config == {}

    def test_get_project_config_with_pyproject(self, clean_env):
        """Test getting project config from pyproject.toml."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager()

            # Create pyproject.toml
            pyproject_content = """
[tool.docguard]
exclude = ["**/.venv/**"]

[tool.docguard.llm]
default_provider = "ollama"
default_model = "codeqwen:latest"

[tool.docguard.llm.ollama]
base_url = "http://localhost:11434"
"""

            pyproject_file = Path(temp_dir) / "pyproject.toml"
            pyproject_file.write_text(pyproject_content)

            config = config_manager.get_project_config(Path(temp_dir))
            assert config["exclude"] == ["**/.venv/**"]
            assert config["llm"]["default_provider"] == "ollama"

    def test_get_llm_config_hierarchy(self, clean_env):
        """Test LLM config hierarchy (env > user > project > defaults)."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))

            # Create user config
            user_config = {
                "llm": {
                    "default_provider": "anthropic",
                    "anthropic": {
                        "api_key": "sk-ant-user123",
                        "base_url": "https://api.anthropic.com",
                    },
                }
            }
            config_manager.save_user_config(user_config)

            # Create project config
            pyproject_content = """
[tool.docguard.llm]
default_provider = "openai"
default_model = "gpt-4"

[tool.docguard.llm.openai]
base_url = "https://api.openai.com/v1"
"""
            pyproject_file = Path(temp_dir) / "pyproject.toml"
            pyproject_file.write_text(pyproject_content)

            # Test hierarchy: user config should override project config
            llm_config = config_manager.get_llm_config(Path(temp_dir))
            assert llm_config.default_provider == "anthropic"  # User overrides project

            # Test environment variable override
            with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-env456"}):
                llm_config = config_manager.get_llm_config(Path(temp_dir))
                anthropic_config = llm_config.providers["anthropic"]
                assert anthropic_config.api_key == "sk-ant-env456"  # Env overrides user

    def test_get_provider_config(self, clean_env):
        """Test getting configuration for a specific provider."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))

            # Create user config
            user_config = {
                "llm": {
                    "openai": {
                        "api_key": "sk-test123",
                        "base_url": "https://api.openai.com/v1",
                        "default_model": "gpt-5-nano",
                    }
                }
            }
            config_manager.save_user_config(user_config)

            provider_config = config_manager.get_provider_config(
                "openai", Path(temp_dir)
            )
            assert provider_config.api_key == "sk-test123"
            assert provider_config.base_url == "https://api.openai.com/v1"
            assert provider_config.default_model == "gpt-5-nano"

    def test_is_provider_configured(self, clean_env):
        """Test checking if a provider is configured."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))

            # Ollama should always be configured (no API key required)
            assert config_manager.is_provider_configured("ollama", Path(temp_dir))

            # OpenAI should not be configured without API key
            assert not config_manager.is_provider_configured("openai", Path(temp_dir))

            # Configure OpenAI
            user_config = {"llm": {"openai": {"api_key": "sk-test123"}}}
            config_manager.save_user_config(user_config)
            assert config_manager.is_provider_configured("openai", Path(temp_dir))

    def test_environment_variable_override(self, clean_env):
        """Test that environment variables override config files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))

            # Create user config with API key
            user_config = {
                "llm": {
                    "openai": {
                        "api_key": "sk-user123",
                        "base_url": "https://api.openai.com/v1",
                    }
                }
            }
            config_manager.save_user_config(user_config)

            # Environment variable should override user config
            with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-env456"}):
                llm_config = config_manager.get_llm_config(Path(temp_dir))
                openai_config = llm_config.providers["openai"]
                assert openai_config.api_key == "sk-env456"

    def test_file_permissions(self, clean_env):
        """Test that config file gets secure permissions."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_manager = ConfigManager(Path(temp_dir))

            test_config = {"llm": {"default_provider": "openai"}}
            config_manager.save_user_config(test_config)

            # Check file permissions (should be 600 = user read/write only)
            file_stat = config_manager.user_config_file.stat()
            assert oct(file_stat.st_mode)[-3:] == "600"

    def test_environment_isolation(self, clean_env):
        """Test that tests are properly isolated from environment variables."""
        # This test verifies that the clean_env fixture works
        # Even if environment variables are set externally, they should be cleared

        # Use patch.dict to ensure clean environment during test
        with patch.dict(os.environ, {}, clear=True):
            # Test that our config system works without these variables
            with tempfile.TemporaryDirectory() as temp_dir:
                config_manager = ConfigManager(Path(temp_dir))

                # Should not be configured without API key
                assert not config_manager.is_provider_configured(
                    "openai", Path(temp_dir)
                )
                assert not config_manager.is_provider_configured(
                    "anthropic", Path(temp_dir)
                )

                # Ollama should still work (no API key required)
                assert config_manager.is_provider_configured("ollama", Path(temp_dir))


class TestLLMConfig:
    """Test LLM configuration classes."""

    def test_llm_provider_config_defaults(self, clean_env):
        """Test LLMProviderConfig defaults."""
        config = LLMProviderConfig()
        assert config.api_key is None
        assert config.base_url is None
        assert config.default_model is None
        assert config.models == {}

    def test_llm_config_defaults(self, clean_env):
        """Test LLMConfig defaults."""
        config = LLMConfig()
        assert config.default_provider is None
        assert config.default_model is None
        assert config.providers == {}
