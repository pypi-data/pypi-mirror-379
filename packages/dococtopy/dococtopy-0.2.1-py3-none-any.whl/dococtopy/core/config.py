from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # Python < 3.11
    except ImportError:
        tomllib = None  # type: ignore


@dataclass
class LLMProviderConfig:
    """Configuration for a specific LLM provider."""

    api_key: Optional[str] = None
    base_url: Optional[str] = None
    default_model: Optional[str] = None
    models: Dict[str, str] = field(default_factory=dict)


@dataclass
class LLMConfig:
    """Configuration for LLM providers."""

    default_provider: Optional[str] = None
    default_model: Optional[str] = None
    providers: Dict[str, LLMProviderConfig] = field(default_factory=dict)


@dataclass
class Config:
    root: Path
    exclude: List[str] = field(default_factory=list)
    rules: Dict[str, str] = field(default_factory=dict)  # e.g., {"DG101": "off"}

    def is_rule_enabled(self, rule_id: str) -> bool:
        state = self.rules.get(rule_id)
        return state is None or state.lower() not in {"off", "disabled", "disable"}


class ConfigManager:
    """Manages configuration from multiple sources with proper hierarchy."""

    def __init__(self, user_config_dir: Optional[Path] = None):
        """Initialize ConfigManager.

        Args:
            user_config_dir: Override default user config directory for testing
        """
        if user_config_dir:
            self.user_config_dir = user_config_dir
        else:
            # Use XDG Base Directory standard
            self.user_config_dir = Path.home() / ".config" / "dococtopy"

        self.user_config_file = self.user_config_dir / "config.toml"

    def get_user_config(self) -> Dict[str, Any]:
        """Load user configuration from ~/.config/dococtopy/config.toml."""
        if not self.user_config_file.exists() or tomllib is None:
            return {}

        try:
            with open(self.user_config_file, "rb") as f:
                data = tomllib.load(f)
                return dict(data) if isinstance(data, dict) else {}
        except Exception:
            return {}

    def save_user_config(self, config: Dict[str, Any]) -> None:
        """Save user configuration to ~/.config/dococtopy/config.toml."""
        self.user_config_dir.mkdir(parents=True, exist_ok=True)

        # Ensure secure file permissions
        if tomllib is None:
            raise RuntimeError("TOML support not available")

        # Convert to TOML format
        import tomli_w

        toml_content = tomli_w.dumps(config)

        with open(self.user_config_file, "w") as f:
            f.write(toml_content)

        # Set secure permissions (600 = user read/write only)
        self.user_config_file.chmod(0o600)

    def get_project_config(self, project_root: Optional[Path] = None) -> Dict[str, Any]:
        """Load project configuration from pyproject.toml."""
        if project_root is None:
            project_root = Path.cwd()

        config_file = project_root / "pyproject.toml"
        if not config_file.exists() or tomllib is None:
            return {}

        try:
            with open(config_file, "rb") as f:
                data = tomllib.load(f)
                tool_config = data.get("tool", {})
                docguard_config = tool_config.get("docguard", {})
                return (
                    dict(docguard_config) if isinstance(docguard_config, dict) else {}
                )
        except Exception:
            return {}

    def get_llm_config(self, project_root: Optional[Path] = None) -> LLMConfig:
        """Get LLM configuration with proper hierarchy.

        Hierarchy (highest to lowest priority):
        1. Environment variables
        2. User config file
        3. Project config file
        4. Defaults
        """
        # Start with defaults
        config = LLMConfig()

        # Load project config
        project_config = self.get_project_config(project_root)
        llm_config = project_config.get("llm", {})

        # Load user config
        user_config = self.get_user_config()
        user_llm_config = user_config.get("llm", {})

        # Apply project config
        if "default_provider" in llm_config:
            config.default_provider = llm_config["default_provider"]
        if "default_model" in llm_config:
            config.default_model = llm_config["default_model"]

        # Apply user config (overrides project)
        if "default_provider" in user_llm_config:
            config.default_provider = user_llm_config["default_provider"]
        if "default_model" in user_llm_config:
            config.default_model = user_llm_config["default_model"]

        # Process providers
        for provider_name in ["openai", "anthropic", "ollama"]:
            provider_config = LLMProviderConfig()

            # Project config
            project_provider = llm_config.get(provider_name, {})
            if "base_url" in project_provider:
                provider_config.base_url = project_provider["base_url"]
            if "default_model" in project_provider:
                provider_config.default_model = project_provider["default_model"]
            if "models" in project_provider:
                provider_config.models = project_provider["models"]

            # User config (overrides project)
            user_provider = user_llm_config.get(provider_name, {})
            if "api_key" in user_provider:
                provider_config.api_key = user_provider["api_key"]
            if "base_url" in user_provider:
                provider_config.base_url = user_provider["base_url"]
            if "default_model" in user_provider:
                provider_config.default_model = user_provider["default_model"]
            if "models" in user_provider:
                provider_config.models.update(user_provider["models"])

            # Environment variables (highest priority)
            if provider_name == "openai":
                env_key = os.getenv("OPENAI_API_KEY")
                if env_key:
                    provider_config.api_key = env_key
                env_url = os.getenv("OPENAI_BASE_URL")
                if env_url:
                    provider_config.base_url = env_url
            elif provider_name == "anthropic":
                env_key = os.getenv("ANTHROPIC_API_KEY")
                if env_key:
                    provider_config.api_key = env_key
                env_url = os.getenv("ANTHROPIC_BASE_URL")
                if env_url:
                    provider_config.base_url = env_url
            elif provider_name == "ollama":
                env_url = os.getenv("OLLAMA_BASE_URL")
                if env_url:
                    provider_config.base_url = env_url
                env_model = os.getenv("OLLAMA_MODEL")
                if env_model:
                    provider_config.default_model = env_model

            config.providers[provider_name] = provider_config

        return config

    def get_provider_config(
        self, provider: str, project_root: Optional[Path] = None
    ) -> LLMProviderConfig:
        """Get configuration for a specific provider."""
        llm_config = self.get_llm_config(project_root)
        return llm_config.providers.get(provider, LLMProviderConfig())

    def is_provider_configured(
        self, provider: str, project_root: Optional[Path] = None
    ) -> bool:
        """Check if a provider is properly configured."""
        config = self.get_provider_config(provider, project_root)

        if provider == "ollama":
            return True  # Ollama doesn't require API key
        elif provider in ["openai", "anthropic"]:
            return bool(config.api_key)

        return False


def load_config(explicit_path: Optional[Path]) -> Optional[Config]:
    """Load configuration from pyproject.toml [tool.docguard].

    Returns None if no config found, tomllib unavailable, or parsing fails.
    """
    cfg_path: Optional[Path]
    if explicit_path:
        cfg_path = Path(explicit_path)
    else:
        cfg_path = Path.cwd() / "pyproject.toml"
    if not cfg_path.exists() or tomllib is None:
        return None
    try:
        data = tomllib.loads(cfg_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    tool = data.get("tool", {}) if isinstance(data, dict) else {}
    docguard = tool.get("docguard", {}) if isinstance(tool, dict) else {}
    exclude = list(docguard.get("exclude", [])) if isinstance(docguard, dict) else []
    rules = dict(docguard.get("rules", {})) if isinstance(docguard, dict) else {}
    return Config(root=cfg_path.parent, exclude=exclude, rules=rules)
