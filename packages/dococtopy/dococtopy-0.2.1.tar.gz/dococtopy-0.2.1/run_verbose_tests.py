#!/usr/bin/env python3
"""Run canned integration tests with verbose output for Ollama and OpenAI."""

import sys
from pathlib import Path

# Add the tests directory to the path
sys.path.insert(0, str(Path(__file__).parent / "tests" / "integration" / "canned"))

from test_runner import CannedTestRunner, CannedTestScenario
from test_config import get_config


def create_verbose_scenarios() -> list[CannedTestScenario]:
    """Create test scenarios with verbose output enabled."""
    config = get_config()
    scenarios = []
    
    # Ollama scenarios with verbose
    if config.is_provider_available("ollama"):
        ollama_config = config.get_ollama_config()
        scenarios.extend([
            CannedTestScenario(
                name="ollama_missing_docstrings_verbose",
                description="Add docstrings with Ollama (verbose)",
                fixture_file="missing_docstrings.py",
                rules=["DG101"],
                llm_provider="ollama",
                llm_model=ollama_config["default_model"],
                llm_base_url=ollama_config["base_url"],
                expected_changes=6,
                interactive=False,
                verbose=True,
            ),
            CannedTestScenario(
                name="ollama_google_style_verbose",
                description="Fix Google style patterns with Ollama (verbose)",
                fixture_file="google_style_patterns.py",
                rules=["DG101", "DG102", "DG103", "DG104", "DG105"],
                llm_provider="ollama",
                llm_model=ollama_config["default_model"],
                llm_base_url=ollama_config["base_url"],
                expected_changes=15,
                interactive=False,
                verbose=True,
            ),
        ])
    
    # OpenAI scenarios with verbose
    if config.is_provider_available("openai"):
        openai_config = config.get_openai_config()
        scenarios.extend([
            CannedTestScenario(
                name="openai_missing_docstrings_verbose",
                description="Add docstrings with OpenAI (verbose)",
                fixture_file="missing_docstrings.py",
                rules=["DG101"],
                llm_provider="openai",
                llm_model=openai_config["default_model"],
                expected_changes=6,
                interactive=False,
                verbose=True,
            ),
            CannedTestScenario(
                name="openai_google_style_verbose",
                description="Fix Google style patterns with OpenAI (verbose)",
                fixture_file="google_style_patterns.py",
                rules=["DG101", "DG102", "DG103", "DG104", "DG105"],
                llm_provider="openai",
                llm_model=openai_config["default_model"],
                expected_changes=15,
                interactive=False,
                verbose=True,
            ),
        ])
    
    return scenarios


def main():
    """Run verbose integration tests."""
    print("🚀 Running DocOctopy Integration Tests with Verbose Output")
    print("=" * 60)
    
    # Create test runner
    base_dir = Path(__file__).parent / "tests" / "integration" / "canned"
    runner = CannedTestRunner(base_dir)
    
    # Get verbose scenarios
    scenarios = create_verbose_scenarios()
    
    if not scenarios:
        print("❌ No scenarios available. Check your configuration.")
        return
    
    print(f"📋 Found {len(scenarios)} scenarios to run:")
    for scenario in scenarios:
        print(f"  • {scenario.name}: {scenario.description}")
    
    print("\n" + "=" * 60)
    
    # Run scenarios
    results = []
    for scenario in scenarios:
        try:
            result = runner.run_scenario(scenario)
            results.append(result)
            runner.cleanup_scenario(scenario)
        except Exception as e:
            print(f"❌ Error running {scenario.name}: {e}")
    
    # Show summary
    print("\n" + "=" * 60)
    print("📊 Test Results Summary")
    print("=" * 60)
    
    successful = sum(1 for r in results if r.success)
    total = len(results)
    
    print(f"✅ Successful: {successful}/{total}")
    print(f"❌ Failed: {total - successful}/{total}")
    
    if results:
        print("\n📋 Detailed Results:")
        for result in results:
            status = "✅" if result.success else "❌"
            print(f"  {status} {result.scenario.name}")
            if result.error:
                print(f"     Error: {result.error}")
            print(f"     Changes: {result.changes_applied}")
    
    return 0 if successful == total else 1


if __name__ == "__main__":
    sys.exit(main())
