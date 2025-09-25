#!/usr/bin/env python3
"""Quick setup script for Anthropic (Claude) configuration."""

import sys
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from tests.integration.canned.test_config import get_config


def setup_anthropic():
    """Set up Anthropic (Claude) configuration."""
    config = get_config()

    # Get API key from user
    api_key = input("Enter your Anthropic API key: ").strip()
    if not api_key:
        print("❌ No API key provided")
        return

    # Set Anthropic configuration
    config._config["anthropic"]["api_key"] = api_key
    config._config["anthropic"]["default_model"] = "claude-3-haiku-20240307"

    # Save configuration
    config.save_config()
    print("✅ Anthropic configuration saved!")
    print(f"   Model: {config._config['anthropic']['default_model']}")
    print(f"   API Key: {'*' * 20}...{api_key[-4:]}")


if __name__ == "__main__":
    setup_anthropic()
