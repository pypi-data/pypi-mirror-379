"""Integration test framework for DocOctopy canned scenarios."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

try:
    from .test_config import get_config
except ImportError:
    # Handle case when running as standalone script
    from test_config import get_config


@dataclass
class CannedTestScenario:
    """Configuration for a test scenario."""

    name: str
    description: str
    fixture_file: str
    rules: List[str]
    llm_provider: str
    llm_model: str
    llm_base_url: Optional[str] = None
    expected_changes: Optional[int] = None
    interactive: bool = False
    verbose: bool = False


@dataclass
class CannedTestResult:
    """Result of a test scenario."""

    scenario: CannedTestScenario
    success: bool
    changes_applied: int
    output: str
    error: Optional[str] = None


class CannedTestRunner:
    """Runner for canned integration tests."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.fixtures_dir = base_dir / "fixtures"
        self.results_dir = base_dir / "results"
        self.scenarios_dir = base_dir / "scenarios"
        self.console = Console()
        self.config = get_config()

        # Ensure directories exist
        self.results_dir.mkdir(exist_ok=True)
        self.scenarios_dir.mkdir(exist_ok=True)

    def create_scenarios(self) -> List[CannedTestScenario]:
        """Create predefined test scenarios."""
        scenarios = []

        # Ollama scenarios
        if self.config.is_provider_available("ollama"):
            ollama_config = self.config.get_ollama_config()
            scenarios.extend(
                [
                    CannedTestScenario(
                        name="missing_docstrings",
                        description="Add docstrings to functions and classes without them",
                        fixture_file="missing_docstrings.py",
                        rules=["DG101"],
                        llm_provider="ollama",
                        llm_model=ollama_config["default_model"],
                        llm_base_url=ollama_config["base_url"],
                        expected_changes=4,
                        interactive=False,
                    ),
                    CannedTestScenario(
                        name="malformed_docstrings",
                        description="Fix malformed Google-style docstrings",
                        fixture_file="malformed_docstrings.py",
                        rules=["DG201", "DG202", "DG203", "DG204"],
                        llm_provider="ollama",
                        llm_model=ollama_config["default_model"],
                        llm_base_url=ollama_config["base_url"],
                        expected_changes=5,
                        interactive=False,
                    ),
                    CannedTestScenario(
                        name="mixed_issues",
                        description="Handle mixed docstring issues",
                        fixture_file="mixed_issues.py",
                        rules=["DG101", "DG202", "DG204", "DG205"],
                        llm_provider="ollama",
                        llm_model=ollama_config["default_model"],
                        llm_base_url=ollama_config["base_url"],
                        expected_changes=8,
                        interactive=False,
                    ),
                    CannedTestScenario(
                        name="real_world_patterns",
                        description="Real-world code patterns from actual projects",
                        fixture_file="real_world_patterns.py",
                        rules=["DG101", "DG202", "DG204"],
                        llm_provider="ollama",
                        llm_model=ollama_config["default_model"],
                        llm_base_url=ollama_config["base_url"],
                        expected_changes=10,
                        interactive=False,
                    ),
                    CannedTestScenario(
                        name="interactive_missing_docstrings",
                        description="Interactive mode for missing docstrings",
                        fixture_file="missing_docstrings.py",
                        rules=["DG101"],
                        llm_provider="ollama",
                        llm_model=ollama_config["default_model"],
                        llm_base_url=ollama_config["base_url"],
                        expected_changes=6,
                        interactive=True,
                    ),
                ]
            )

        # OpenAI scenarios
        if self.config.is_provider_available("openai"):
            openai_config = self.config.get_openai_config()
            scenarios.append(
                CannedTestScenario(
                    name="openai_gpt5_nano",
                    description="Test with OpenAI GPT-5-nano",
                    fixture_file="missing_docstrings.py",
                    rules=["DG101"],
                    llm_provider="openai",
                    llm_model=openai_config["default_model"],
                    expected_changes=6,
                    interactive=False,
                )
            )

        # Anthropic scenarios
        if self.config.is_provider_available("anthropic"):
            anthropic_config = self.config.get_anthropic_config()
            scenarios.append(
                CannedTestScenario(
                    name="anthropic_haiku",
                    description="Test with Anthropic Claude Haiku",
                    fixture_file="missing_docstrings.py",
                    rules=["DG101"],
                    llm_provider="anthropic",
                    llm_model=anthropic_config["default_model"],
                    expected_changes=6,
                    interactive=False,
                )
            )

        # Google style patterns scenarios
        scenarios.append(
            CannedTestScenario(
                name="google_style_patterns",
                description="Comprehensive Google style docstring patterns",
                fixture_file="google_style_patterns.py",
                rules=[
                    "DG101",
                    "DG201",
                    "DG202",
                    "DG203",
                    "DG204",
                    "DG205",
                    "DG206",
                    "DG207",
                    "DG208",
                    "DG209",
                    "DG210",
                    "DG211",
                    "DG212",
                    "DG213",
                    "DG214",
                ],
                llm_provider="ollama",
                llm_model="codeqwen:latest",
                llm_base_url="http://192.168.0.132:11434",
                expected_changes=15,  # Many issues in the fixture
                interactive=False,
            )
        )

        return scenarios

    def setup_scenario(self, scenario: CannedTestScenario) -> Path:
        """Set up a test scenario by copying fixture files."""
        # Always use the .fixture file (contains the test input with missing/improper docstrings)
        # The .py file contains the expected output (with proper docstrings)
        fixture_path = self.fixtures_dir / f"{scenario.fixture_file}.fixture"
        if not fixture_path.exists():
            # Fall back to .py file if no .fixture file exists
            fixture_path = self.fixtures_dir / scenario.fixture_file

        # Create .py file in scenarios directory
        scenario_path = self.scenarios_dir / scenario.fixture_file

        if not fixture_path.exists():
            raise FileNotFoundError(f"Fixture file not found: {fixture_path}")

        # Copy fixture to scenarios directory
        shutil.copy2(fixture_path, scenario_path)

        # Make the copied file writable so it can be modified during testing
        scenario_path.chmod(0o644)

        self.console.print(f"[green]✓[/green] Set up scenario: {scenario.name}")
        return scenario_path

    def run_scenario(self, scenario: CannedTestScenario) -> CannedTestResult:
        """Run a test scenario."""
        self.console.print(
            f"\n[bold blue]Running scenario: {scenario.name}[/bold blue]"
        )
        self.console.print(f"[dim]{scenario.description}[/dim]")

        try:
            # Set up the scenario
            scenario_path = self.setup_scenario(scenario)

            # Build command
            cmd = [
                "uv",
                "run",
                "dococtopy",
                "fix",
                str(scenario_path),
                "--rule",
                ",".join(scenario.rules),
                "--llm-provider",
                scenario.llm_provider,
                "--llm-model",
                scenario.llm_model,
            ]

            if scenario.llm_base_url:
                cmd.extend(["--llm-base-url", scenario.llm_base_url])

            if scenario.interactive:
                cmd.append("--interactive")

            if scenario.verbose:
                cmd.append("--verbose")

            # Run the command
            self.console.print(f"[dim]Running: {' '.join(cmd)}[/dim]")

            # Set up environment variables for API keys
            env = os.environ.copy()
            if scenario.llm_provider == "openai":
                openai_config = self.config.get_openai_config()
                if openai_config["api_key"]:
                    env["OPENAI_API_KEY"] = openai_config["api_key"]
            elif scenario.llm_provider == "anthropic":
                anthropic_config = self.config.get_anthropic_config()
                if anthropic_config["api_key"]:
                    env["ANTHROPIC_API_KEY"] = anthropic_config["api_key"]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.base_dir.parent.parent.parent,  # Project root
                env=env,
            )

            # Count changes applied (improved heuristic)
            changes_applied = 0
            if "Total changes:" in result.stdout:
                # Extract from summary line
                for line in result.stdout.split("\n"):
                    if "Total changes:" in line:
                        try:
                            changes_applied = int(line.split(":")[1].strip())
                        except (ValueError, IndexError):
                            pass
                        break
            elif "Applied fix" in result.stdout:
                # Count "Applied fix" messages
                changes_applied = result.stdout.count("Applied fix")
            elif "Applied" in result.stdout:
                # Count "Applied" messages
                changes_applied = result.stdout.count("Applied")

            success = result.returncode == 0

            return CannedTestResult(
                scenario=scenario,
                success=success,
                changes_applied=changes_applied,
                output=result.stdout,
                error=result.stderr if result.returncode != 0 else None,
            )

        except Exception as e:
            return CannedTestResult(
                scenario=scenario,
                success=False,
                changes_applied=0,
                output="",
                error=str(e),
            )

    def setup_scenario_files(self, scenario: CannedTestScenario) -> Path:
        """Set up scenario files by copying fixture files to test directory."""
        self.console.print(
            f"[bold blue]Setting up scenario: {scenario.name}[/bold blue]"
        )
        self.console.print(f"[dim]{scenario.description}[/dim]")

        # Always use the .fixture file (contains the test input with missing/improper docstrings)
        # The .py file contains the expected output (with proper docstrings)
        fixture_path = self.fixtures_dir / f"{scenario.fixture_file}.fixture"
        if not fixture_path.exists():
            # Fall back to .py file if no .fixture file exists
            fixture_path = self.fixtures_dir / scenario.fixture_file

        # Create .py file in scenarios directory
        scenario_path = self.scenarios_dir / scenario.fixture_file

        if not fixture_path.exists():
            raise FileNotFoundError(f"Fixture file not found: {fixture_path}")

        # Copy fixture to scenarios directory
        shutil.copy2(fixture_path, scenario_path)

        # Make the copied file writable so it can be modified during testing
        scenario_path.chmod(0o644)

        self.console.print(f"[green]✓[/green] Set up scenario: {scenario.name}")
        self.console.print(f"[dim]Test file: {scenario_path}[/dim]")
        return scenario_path

    def run_scenario_fix(
        self, scenario: CannedTestScenario, scenario_path: Path
    ) -> CannedTestResult:
        """Run the dococtopy fix command on the scenario files."""
        self.console.print(f"[bold blue]Running fix on: {scenario.name}[/bold blue]")

        # Build command
        cmd = [
            "uv",
            "run",
            "dococtopy",
            "fix",
            str(scenario_path),
            "--rule",
            ",".join(scenario.rules),
            "--llm-provider",
            scenario.llm_provider,
            "--llm-model",
            scenario.llm_model,
        ]

        if scenario.llm_base_url:
            cmd.extend(["--llm-base-url", scenario.llm_base_url])

        if scenario.interactive:
            cmd.append("--interactive")

        if scenario.verbose:
            cmd.append("--verbose")

        # Run the command
        self.console.print(f"[dim]Running: {' '.join(cmd)}[/dim]")

        # Set up environment variables for API keys
        env = os.environ.copy()
        if scenario.llm_provider == "openai":
            openai_config = self.config.get_openai_config()
            if openai_config["api_key"]:
                env["OPENAI_API_KEY"] = openai_config["api_key"]
        elif scenario.llm_provider == "anthropic":
            anthropic_config = self.config.get_anthropic_config()
            if anthropic_config["api_key"]:
                env["ANTHROPIC_API_KEY"] = anthropic_config["api_key"]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=self.base_dir.parent.parent.parent,  # Project root
            env=env,
        )

        # Count changes applied (improved heuristic)
        changes_applied = 0
        if "Total changes:" in result.stdout:
            # Extract from summary line
            for line in result.stdout.split("\n"):
                if "Total changes:" in line:
                    try:
                        changes_applied = int(line.split(":")[1].strip())
                    except (ValueError, IndexError):
                        pass
                    break
        elif "Applied fix" in result.stdout:
            # Count "Applied fix" messages
            changes_applied = result.stdout.count("Applied fix")
        elif "Applied" in result.stdout:
            # Count "Applied" messages
            changes_applied = result.stdout.count("Applied")

        success = result.returncode == 0

        return CannedTestResult(
            scenario=scenario,
            success=success,
            changes_applied=changes_applied,
            output=result.stdout,
            error=result.stderr if result.returncode != 0 else None,
        )

    def cleanup_scenario_files(self, scenario: CannedTestScenario):
        """Clean up scenario files."""
        scenario_path = self.scenarios_dir / scenario.fixture_file
        if scenario_path.exists():
            scenario_path.unlink()
            self.console.print(f"[dim]Cleaned up: {scenario.name}[/dim]")

    def cleanup_scenario(self, scenario: CannedTestScenario):
        """Clean up scenario files (legacy method for backward compatibility)."""
        self.cleanup_scenario_files(scenario)

    def show_results(self, results: List[CannedTestResult]):
        """Display test results in a nice table."""
        table = Table(title="Canned Test Results")
        table.add_column("Scenario", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Changes", justify="right")
        table.add_column("Expected", justify="right")
        table.add_column("Provider", style="dim")

        for result in results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            status_style = "green" if result.success else "red"

            expected = (
                str(result.scenario.expected_changes)
                if result.scenario.expected_changes
                else "?"
            )
            changes = str(result.changes_applied)

            table.add_row(
                result.scenario.name,
                f"[{status_style}]{status}[/{status_style}]",
                changes,
                expected,
                f"{result.scenario.llm_provider}:{result.scenario.llm_model}",
            )

        self.console.print(table)

    def run_all_scenarios(
        self, scenario_names: Optional[List[str]] = None
    ) -> List[CannedTestResult]:
        """Run all or selected scenarios."""
        scenarios = self.create_scenarios()

        if scenario_names:
            scenarios = [s for s in scenarios if s.name in scenario_names]

        results = []

        for scenario in scenarios:
            try:
                result = self.run_scenario(scenario)
                results.append(result)

                # Show individual result
                if result.success:
                    self.console.print(
                        f"[green]✓[/green] {scenario.name}: {result.changes_applied} changes applied"
                    )
                else:
                    self.console.print(f"[red]✗[/red] {scenario.name}: {result.error}")

            finally:
                # Always cleanup
                self.cleanup_scenario(scenario)

        return results

    def inspect_scenario(self, scenario_name: str):
        """Inspect the results of a specific scenario."""
        scenarios = self.create_scenarios()
        scenario = next((s for s in scenarios if s.name == scenario_name), None)

        if not scenario:
            self.console.print(f"[red]Scenario not found: {scenario_name}[/red]")
            return

        # Set up scenario
        scenario_path = self.setup_scenario(scenario)

        # Show before/after
        self.console.print(f"\n[bold]Before fix:[/bold]")
        with open(scenario_path, "r") as f:
            content = f.read()

        panel = Panel(content, title=f"{scenario.name} - Before", border_style="blue")
        self.console.print(panel)

        # Run fix
        result = self.run_scenario(scenario)

        if result.success:
            self.console.print(f"\n[bold]After fix:[/bold]")
            with open(scenario_path, "r") as f:
                content = f.read()

            panel = Panel(
                content, title=f"{scenario.name} - After", border_style="green"
            )
            self.console.print(panel)

        # Cleanup
        self.cleanup_scenario(scenario)


def main():
    """Main entry point for canned tests."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Run DocOctopy canned integration tests"
    )
    parser.add_argument("--scenario", help="Run specific scenario")
    parser.add_argument("--inspect", help="Inspect specific scenario")
    parser.add_argument("--list", action="store_true", help="List available scenarios")
    parser.add_argument("--all", action="store_true", help="Run all scenarios")
    parser.add_argument(
        "--setup-config", action="store_true", help="Setup configuration"
    )
    parser.add_argument(
        "--show-config", action="store_true", help="Show current configuration"
    )

    # New modular commands
    parser.add_argument(
        "--setup", help="Set up scenario files (copy fixtures to test directory)"
    )
    parser.add_argument("--run", help="Run fix command on scenario files")
    parser.add_argument("--cleanup", help="Clean up scenario files")
    parser.add_argument("--run-full", help="Run full scenario (setup + run + cleanup)")

    args = parser.parse_args()

    # Find the canned test directory
    current_dir = Path(__file__).parent
    runner = CannedTestRunner(current_dir)

    if args.setup_config:
        from .test_config import setup_config

        setup_config()
        return

    if args.show_config:
        from .test_config import show_config

        show_config()
        return

    if args.list:
        scenarios = runner.create_scenarios()
        table = Table(title="Available Scenarios")
        table.add_column("Name", style="cyan")
        table.add_column("Description", style="dim")
        table.add_column("Rules", style="yellow")
        table.add_column("Provider", style="dim")

        for scenario in scenarios:
            table.add_row(
                scenario.name,
                scenario.description,
                ",".join(scenario.rules),
                f"{scenario.llm_provider}:{scenario.llm_model}",
            )

        runner.console.print(table)
        return

    if args.inspect:
        runner.inspect_scenario(args.inspect)
        return

    # New modular commands
    if args.setup:
        scenarios = runner.create_scenarios()
        scenario = next((s for s in scenarios if s.name == args.setup), None)
        if not scenario:
            runner.console.print(f"[red]Scenario not found: {args.setup}[/red]")
            return
        try:
            scenario_path = runner.setup_scenario_files(scenario)
            runner.console.print(f"[green]✓[/green] Scenario files set up successfully")
            runner.console.print(f"[dim]Test file: {scenario_path}[/dim]")
        except Exception as e:
            runner.console.print(f"[red]Error setting up scenario: {e}[/red]")
        return

    if args.run:
        scenarios = runner.create_scenarios()
        scenario = next((s for s in scenarios if s.name == args.run), None)
        if not scenario:
            runner.console.print(f"[red]Scenario not found: {args.run}[/red]")
            return
        scenario_path = runner.scenarios_dir / scenario.fixture_file
        if not scenario_path.exists():
            runner.console.print(
                f"[red]Scenario files not found. Run --setup {args.run} first.[/red]"
            )
            return
        try:
            result = runner.run_scenario_fix(scenario, scenario_path)
            runner.console.print(f"[green]✓[/green] Fix completed")
            runner.console.print(
                f"[dim]Changes applied: {result.changes_applied}[/dim]"
            )
            if result.error:
                runner.console.print(f"[red]Error: {result.error}[/red]")
            if result.output:
                runner.console.print(f"[dim]Output:[/dim]")
                runner.console.print(result.output)
        except Exception as e:
            runner.console.print(f"[red]Error running fix: {e}[/red]")
        return

    if args.cleanup:
        scenarios = runner.create_scenarios()
        scenario = next((s for s in scenarios if s.name == args.cleanup), None)
        if not scenario:
            runner.console.print(f"[red]Scenario not found: {args.cleanup}[/red]")
            return
        try:
            runner.cleanup_scenario_files(scenario)
            runner.console.print(f"[green]✓[/green] Scenario files cleaned up")
        except Exception as e:
            runner.console.print(f"[red]Error cleaning up scenario: {e}[/red]")
        return

    if args.run_full:
        scenarios = runner.create_scenarios()
        scenario = next((s for s in scenarios if s.name == args.run_full), None)
        if not scenario:
            runner.console.print(f"[red]Scenario not found: {args.run_full}[/red]")
            return
        try:
            # Setup
            scenario_path = runner.setup_scenario_files(scenario)
            # Run
            result = runner.run_scenario_fix(scenario, scenario_path)
            # Cleanup
            runner.cleanup_scenario_files(scenario)

            # Show results
            runner.console.print(f"\n[bold]Results:[/bold]")
            runner.console.print(f"Success: {'✓' if result.success else '✗'}")
            runner.console.print(f"Changes applied: {result.changes_applied}")
            if result.error:
                runner.console.print(f"Error: {result.error}")
        except Exception as e:
            runner.console.print(f"[red]Error running full scenario: {e}[/red]")
            # Try to cleanup on error
            try:
                runner.cleanup_scenario_files(scenario)
            except:
                pass
        return

    if args.scenario:
        results = runner.run_all_scenarios([args.scenario])
    elif args.all:
        results = runner.run_all_scenarios()
    else:
        runner.console.print("[yellow]Use --help to see available options[/yellow]")
        return

    # Show results
    runner.show_results(results)


if __name__ == "__main__":
    main()
