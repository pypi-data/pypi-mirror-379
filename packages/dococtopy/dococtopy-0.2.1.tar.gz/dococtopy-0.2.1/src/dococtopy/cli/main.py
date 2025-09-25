"""
Main CLI entry point for DocOctopy.
"""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import typer
from rich.console import Console

from dococtopy import __version__
from dococtopy.core.config import ConfigManager
from dococtopy.remediation.llm import LLMConfig

# Create the main app
app = typer.Typer(
    name="dococtopy",
    help="A language-agnostic docstyle compliance & remediation tool.",
    no_args_is_help=True,
)

console = Console()


def version_callback(value: bool):
    """Print version and exit."""
    if value:
        console.print(f"dococtopy {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, help="Show version and exit."
    ),
):
    """DocOctopy - Docstring compliance and remediation tool."""
    pass


@app.command()
def scan(
    paths: List[Path] = typer.Argument(
        ...,
        help="Paths to scan for documentation issues.",
        exists=True,
    ),
    format: str = typer.Option(
        "pretty", "--format", "-f", help="Output format: pretty, json, sarif, both"
    ),
    config: Optional[Path] = typer.Option(
        None, "--config", help="Path to config file (default: pyproject.toml)"
    ),
    fail_level: str = typer.Option(
        "error",
        "--fail-level",
        help="Exit with error if findings at this level or above: error, warning, info",
    ),
    no_cache: bool = typer.Option(
        False, "--no-cache", help="Disable on-disk cache for scanning"
    ),
    changed_only: bool = typer.Option(
        False, "--changed-only", help="Only process files whose fingerprint changed"
    ),
    stats: bool = typer.Option(
        False, "--stats", help="Show cache performance statistics"
    ),
    output_file: Optional[Path] = typer.Option(
        None, "--output-file", "-o", help="Write JSON report to file"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
):
    """Scan paths for documentation compliance issues."""
    # Import heavy modules only when needed
    from dococtopy.core.config import load_config
    from dococtopy.core.engine import scan_paths
    from dococtopy.core.findings import FindingLevel
    from dococtopy.reporters.console import print_report
    from dococtopy.reporters.json_reporter import to_json
    from dococtopy.reporters.sarif import to_sarif

    if verbose:
        console.print(f"[dim]Loading config from: {config or 'pyproject.toml'}[/dim]")

    cfg = load_config(config)

    if verbose:
        console.print(f"[dim]Scanning paths: {', '.join(str(p) for p in paths)}[/dim]")
        console.print(f"[dim]Cache enabled: {not no_cache}[/dim]")
        console.print(f"[dim]Changed only: {changed_only}[/dim]")

    report, scan_stats = scan_paths(
        paths, config=cfg, use_cache=not no_cache, changed_only=changed_only
    )

    if verbose:
        console.print(
            f"[dim]Found {len(report.get_all_findings())} findings across {len(report.files)} files[/dim]"
        )
        console.print(
            f"[dim]Cache hits: {scan_stats['cache_hits']}, misses: {scan_stats['cache_misses']}[/dim]"
        )
        console.print(f"[dim]Files processed: {scan_stats['files_processed']}[/dim]")

    if format in ("pretty", "both"):
        import sys

        print_report(report, sys.stdout, stats=scan_stats if stats else None)
    if format in ("json", "both"):
        # Use plain stdout to ensure clean JSON without Rich formatting
        import sys

        json_output = to_json(report)
        if output_file:
            output_file.write_text(json_output, encoding="utf-8")
        else:
            sys.stdout.write(json_output + "\n")
    if format == "sarif":
        import json
        import sys

        sarif_output = json.dumps(to_sarif(report), indent=2)
        if output_file:
            output_file.write_text(sarif_output, encoding="utf-8")
        else:
            sys.stdout.write(sarif_output + "\n")

    target_level = fail_level.lower()
    level_order = {"info": 0, "warning": 1, "error": 2}
    threshold = level_order.get(target_level, 2)

    def level_to_ord(lv: FindingLevel) -> int:
        return level_order.get(str(lv.value if hasattr(lv, "value") else lv), 2)

    has_failure = any(
        level_to_ord(f.level) >= threshold for fr in report.files for f in fr.findings
    )
    raise typer.Exit(code=1 if has_failure else 0)


@app.command()
def fix(
    paths: List[Path] = typer.Argument(
        ..., help="Paths to fix documentation issues in.", exists=True
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be fixed without making changes."
    ),
    interactive: bool = typer.Option(
        False, "--interactive", help="Interactively accept/reject each fix."
    ),
    rule: Optional[str] = typer.Option(
        None,
        "--rule",
        help="Comma-separated list of rule IDs to fix (e.g., DG101,DG202).",
    ),
    max_changes: Optional[int] = typer.Option(
        None, "--max-changes", help="Maximum number of changes to make."
    ),
    llm_provider: str = typer.Option(
        "openai", "--llm-provider", help="LLM provider: openai, anthropic, ollama."
    ),
    llm_model: str = typer.Option(
        "gpt-4o-mini", "--llm-model", help="LLM model to use."
    ),
    llm_base_url: Optional[str] = typer.Option(
        None, "--llm-base-url", help="Base URL for LLM provider (for Ollama, etc.)."
    ),
    config: Optional[Path] = typer.Option(
        None, "--config", help="Path to config file (default: pyproject.toml)"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
):
    """Fix documentation issues using LLM assistance."""
    try:
        # Import heavy modules only when needed
        from dococtopy.core.config import load_config
        from dococtopy.core.engine import scan_paths
        from dococtopy.remediation.engine import RemediationEngine, RemediationOptions
        from dococtopy.remediation.interactive import (
            InteractiveReviewer,
            InteractiveReviewOptions,
        )
        from dococtopy.remediation.llm import LLMConfig

        # Parse rule IDs
        rule_ids = _parse_rule_ids(rule, verbose)

        # Create LLM config
        llm_config = _create_llm_config(llm_provider, llm_model, llm_base_url)

        # Check if provider is configured
        from dococtopy.core.config import ConfigManager

        config_manager = ConfigManager()
        if not config_manager.is_provider_configured(llm_provider):
            console.print(
                f"[red]Error: {llm_provider} provider is not configured.[/red]"
            )
            console.print(
                f"[yellow]Run 'dococtopy config setup' to configure your LLM provider.[/yellow]"
            )
            raise typer.Exit(1)

        # Print verbose configuration info
        if verbose:
            _print_verbose_config(
                llm_provider, llm_model, llm_base_url, dry_run, interactive, max_changes
            )

        # Create remediation options
        options = RemediationOptions(
            dry_run=dry_run,
            interactive=interactive,
            rule_ids=rule_ids,
            max_changes=max_changes,
            llm_config=llm_config,
            verbose=verbose,
        )

        # Load configuration
        if verbose:
            console.print(
                f"[dim]Loading config from: {config or 'pyproject.toml'}[/dim]"
            )
        cfg = load_config(config)

        # Create remediation engine with config
        engine = RemediationEngine(options, config=cfg)

        # Scan for issues
        console.print("[blue]Scanning for documentation issues...[/blue]")
        if verbose:
            console.print(
                f"[dim]Scanning paths: {', '.join(str(p) for p in paths)}[/dim]"
            )
        report, scan_stats = scan_paths(paths, config=cfg, use_cache=True)

        if verbose:
            console.print(
                f"[dim]Found {len(report.get_all_findings())} findings across {len(report.files)} files[/dim]"
            )
            console.print(
                f"[dim]Cache hits: {scan_stats['cache_hits']}, misses: {scan_stats['cache_misses']}[/dim]"
            )
        console.print(f"[dim]Files processed: {scan_stats['files_processed']}[/dim]")

        if not report.files:
            console.print("[green]No files found to process.[/green]")
            return

        # Process each file
        total_changes = _process_files(report, engine, dry_run, interactive)

        # Show summary
        if total_changes > 0:
            console.print(f"\n[green]Total changes: {total_changes}[/green]")
            if dry_run:
                console.print("[yellow]Run without --dry-run to apply changes[/yellow]")
        else:
            console.print("[green]No changes needed![/green]")

    except ImportError as e:
        if "DSPy is required" in str(e):
            console.print(f"[red]Error: {e}[/red]")
        else:
            console.print(f"[red]Error: {e}[/red]")
            console.print(
                "[yellow]Install LLM dependencies with: pip install dococtopy[llm][/yellow]"
            )
        raise typer.Exit(1)
    except Exception as e:
        if "DSPy is required" in str(e):
            console.print(f"[red]Error: {e}[/red]")
        else:
            console.print(f"[red]Error during remediation: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def config_init():
    """Initialize a default configuration file."""
    # Import only when needed
    from rich.panel import Panel

    config_content = """[tool.docguard]
exclude = ["**/.venv/**", "**/build/**", "**/node_modules/**"]

[tool.docguard.rules]
DG101 = "error"    # Missing docstrings
DG201 = "error"    # Google style parse errors
DG202 = "error"    # Missing parameters
DG203 = "error"    # Extra parameters
DG204 = "warning"  # Returns section issues
DG205 = "info"     # Raises validation
DG301 = "warning"  # Summary style
DG302 = "warning"  # Blank line after summary
DG211 = "info"     # Yields section validation
DG212 = "info"     # Attributes section validation
DG213 = "info"     # Examples section validation
DG214 = "info"     # Note section validation
"""

    config_path = Path("pyproject.toml")
    if config_path.exists():
        console.print(
            "[yellow]pyproject.toml already exists. Skipping creation.[/yellow]"
        )
        return

    config_path.write_text(config_content)
    console.print(f"[green]Created default configuration at {config_path}[/green]")

    # Show the configuration in a nice panel
    console.print(
        Panel(config_content, title="Default Configuration", border_style="blue")
    )


def _parse_rule_ids(rule: Optional[str], verbose: bool) -> Optional[set[str]]:
    """Parse comma-separated rule IDs into a set."""
    if not rule:
        return None

    rule_ids = set(rule.split(","))
    if verbose:
        console.print(f"[dim]Targeting rules: {', '.join(sorted(rule_ids))}[/dim]")
    return rule_ids


def _create_llm_config(provider: str, model: str, base_url: Optional[str]) -> LLMConfig:
    """Create and configure LLM config using the configuration system."""
    config_manager = ConfigManager()

    # Get provider configuration
    provider_config = config_manager.get_provider_config(provider)

    # Create LLMConfig with proper hierarchy
    llm_config = LLMConfig(
        provider=provider,
        model=model,
        base_url=base_url or provider_config.base_url,
        api_key=provider_config.api_key,
    )

    return llm_config


def _print_verbose_config(
    provider: str,
    model: str,
    base_url: Optional[str],
    dry_run: bool,
    interactive: bool,
    max_changes: Optional[int],
) -> None:
    """Print verbose configuration information."""
    console.print(f"[dim]LLM Provider: {provider}[/dim]")
    console.print(f"[dim]LLM Model: {model}[/dim]")
    if base_url:
        console.print(f"[dim]LLM Base URL: {base_url}[/dim]")
    console.print(f"[dim]Dry run: {dry_run}[/dim]")
    console.print(f"[dim]Interactive: {interactive}[/dim]")
    if max_changes:
        console.print(f"[dim]Max changes: {max_changes}[/dim]")


def _process_files(report, engine, dry_run: bool, interactive: bool) -> int:
    """Process all files in the report and return total changes made."""
    total_changes = 0

    for file_result in report.files:
        if not file_result.findings:
            continue

        console.print(f"\n[blue]Processing {file_result.path}...[/blue]")

        # Load symbols for this file
        from dococtopy.adapters.python.adapter import load_symbols_from_file

        symbols = load_symbols_from_file(file_result.path)

        # Remediate the file
        changes = engine.remediate_file(
            file_result.path,
            symbols,
            file_result.findings,
        )

        if changes:
            console.print(
                f"[green]Found {len(changes)} changes for {file_result.path}[/green]"
            )

            if interactive:
                total_changes += _handle_interactive_changes(
                    changes, file_result, engine, dry_run
                )
            else:
                total_changes += _handle_non_interactive_changes(
                    changes, file_result, engine, dry_run
                )

    return total_changes


def _handle_interactive_changes(changes, file_result, engine, dry_run: bool) -> int:
    """Handle changes in interactive mode."""
    from dococtopy.remediation.interactive import (
        InteractiveReviewer,
        InteractiveReviewOptions,
    )

    # Read original file content
    original_content = file_result.path.read_text(encoding="utf-8")

    # Create interactive reviewer
    review_options = InteractiveReviewOptions(
        show_full_context=True,
        auto_accept_safe_changes=False,
        batch_mode=False,
        preview_mode=True,
    )
    reviewer = InteractiveReviewer(console, review_options)

    # Review changes
    approved_changes = reviewer.review_changes(
        changes, file_result.path, original_content
    )

    # Apply approved changes
    if approved_changes and not dry_run:
        engine.apply_changes(file_result.path, approved_changes)
        console.print(f"[green]Applied {len(approved_changes)} changes[/green]")
    elif approved_changes and dry_run:
        console.print(
            f"[yellow]Would apply {len(approved_changes)} changes (dry run)[/yellow]"
        )

    # Show review summary
    reviewer.show_summary()

    return len(approved_changes) if approved_changes else 0


def _handle_non_interactive_changes(changes, file_result, engine, dry_run: bool) -> int:
    """Handle changes in non-interactive mode."""
    if changes and not dry_run:
        engine.apply_changes(file_result.path, changes)
        console.print(f"[green]Applied {len(changes)} changes[/green]")
    elif changes and dry_run:
        console.print(f"[yellow]Would apply {len(changes)} changes (dry run)[/yellow]")

    # Show changes
    for change in changes:
        console.print(
            f"\n[cyan]Change: {change.symbol_name} ({change.symbol_kind})[/cyan]"
        )
        console.print(f"[yellow]Issues: {', '.join(change.issues_addressed)}[/yellow]")

        if dry_run:
            console.print("[dim]Dry run - no changes applied[/dim]")
        else:
            console.print("[green]Applied fix[/green]")

    return len(changes) if changes else 0


@app.command()
def config(
    setup: bool = typer.Option(
        False, "--setup", help="Interactive configuration setup"
    ),
    show: bool = typer.Option(False, "--show", help="Show current configuration"),
    init: bool = typer.Option(False, "--init", help="Initialize project configuration"),
):
    """Manage DocOctopy configuration."""
    config_manager = ConfigManager()

    if setup:
        _interactive_config_setup(config_manager)
    elif show:
        _show_config(config_manager)
    elif init:
        _init_project_config(config_manager)
    else:
        console.print(
            "Use --setup, --show, or --init. Run 'dococtopy config --help' for details."
        )


def _interactive_config_setup(config_manager: ConfigManager) -> None:
    """Interactive configuration setup."""
    from rich.prompt import Confirm, Prompt

    console.print("[bold blue]DocOctopy Configuration Setup[/bold blue]")
    console.print("This will help you configure LLM providers for DocOctopy.\n")

    # Get current config
    current_config = config_manager.get_user_config()
    llm_config = current_config.get("llm", {})

    # Default provider
    default_provider = Prompt.ask(
        "Default LLM provider",
        choices=["openai", "anthropic", "ollama"],
        default=llm_config.get("default_provider", "openai"),
    )

    # Default model
    default_model = Prompt.ask(
        "Default model", default=llm_config.get("default_model", "gpt-5-nano")
    )

    # Provider-specific configuration
    providers_config = {}

    if default_provider == "openai" or Confirm.ask("Configure OpenAI?", default=False):
        api_key = Prompt.ask("OpenAI API Key", password=True)
        base_url = Prompt.ask("OpenAI Base URL", default="https://api.openai.com/v1")
        providers_config["openai"] = {
            "api_key": api_key,
            "base_url": base_url,
            "default_model": Prompt.ask("Default OpenAI model", default="gpt-5-nano"),
        }

    if default_provider == "anthropic" or Confirm.ask(
        "Configure Anthropic?", default=False
    ):
        api_key = Prompt.ask("Anthropic API Key", password=True)
        base_url = Prompt.ask("Anthropic Base URL", default="https://api.anthropic.com")
        providers_config["anthropic"] = {
            "api_key": api_key,
            "base_url": base_url,
            "default_model": Prompt.ask(
                "Default Anthropic model", default="claude-3-haiku-20240307"
            ),
        }

    if default_provider == "ollama" or Confirm.ask("Configure Ollama?", default=True):
        base_url = Prompt.ask("Ollama Base URL", default="http://localhost:11434")
        providers_config["ollama"] = {
            "base_url": base_url,
            "default_model": Prompt.ask(
                "Default Ollama model", default="codeqwen:latest"
            ),
        }

    # Build new config
    new_config = {
        "llm": {
            "default_provider": default_provider,
            "default_model": default_model,
            **providers_config,
        }
    }

    # Save configuration
    if Confirm.ask("\nSave configuration?", default=True):
        config_manager.save_user_config(new_config)
        console.print("[green]✅ Configuration saved![/green]")
        console.print(f"Configuration file: {config_manager.user_config_file}")
    else:
        console.print("[yellow]Configuration not saved.[/yellow]")


def _show_config(config_manager: ConfigManager) -> None:
    """Show current configuration."""
    console.print("[bold blue]Current DocOctopy Configuration[/bold blue]\n")

    llm_config = config_manager.get_llm_config()

    console.print(
        f"[bold]Default Provider:[/bold] {llm_config.default_provider or 'Not set'}"
    )
    console.print(
        f"[bold]Default Model:[/bold] {llm_config.default_model or 'Not set'}\n"
    )

    for provider_name, provider_config in llm_config.providers.items():
        console.print(f"[bold]{provider_name.title()}:[/bold]")

        if provider_config.api_key:
            masked_key = f"{'*' * 20}...{provider_config.api_key[-4:]}"
            console.print(f"  API Key: {masked_key}")
        else:
            console.print(f"  API Key: [red]Not configured[/red]")

        if provider_config.base_url:
            console.print(f"  Base URL: {provider_config.base_url}")

        if provider_config.default_model:
            console.print(f"  Default Model: {provider_config.default_model}")

        console.print()


def _init_project_config(config_manager: ConfigManager) -> None:
    """Initialize project configuration."""
    console.print("[bold blue]Initialize Project Configuration[/bold blue]")

    project_root = Path.cwd()
    pyproject_file = project_root / "pyproject.toml"

    if not pyproject_file.exists():
        console.print("[red]No pyproject.toml found in current directory.[/red]")
        return

    # Get current project config
    project_config = config_manager.get_project_config(project_root)

    # Get LLM preferences
    from rich.prompt import Prompt

    default_provider = Prompt.ask(
        "Default LLM provider for this project",
        choices=["openai", "anthropic", "ollama"],
        default="ollama",
    )

    default_model = Prompt.ask(
        "Default model for this project",
        default="codeqwen:latest" if default_provider == "ollama" else "gpt-5-nano",
    )

    # Build project LLM config
    llm_config: Dict[str, Any] = {
        "default_provider": default_provider,
        "default_model": default_model,
    }

    if default_provider == "ollama":
        base_url = Prompt.ask("Ollama Base URL", default="http://localhost:11434")
        llm_config["ollama"] = {"base_url": base_url, "default_model": default_model}

    # Update pyproject.toml
    try:
        import tomllib

        import tomli_w

        # Read current pyproject.toml
        with open(pyproject_file, "rb") as f:
            data = tomllib.load(f)

        # Ensure tool.docguard section exists
        if "tool" not in data:
            data["tool"] = {}
        if "docguard" not in data["tool"]:
            data["tool"]["docguard"] = {}

        # Add LLM config
        data["tool"]["docguard"]["llm"] = llm_config

        # Write back to file
        with open(pyproject_file, "wb") as f:
            tomli_w.dump(data, f)

        console.print("[green]✅ Project configuration updated![/green]")
        console.print(f"Updated: {pyproject_file}")

    except Exception as e:
        console.print(f"[red]Error updating pyproject.toml: {e}[/red]")


if __name__ == "__main__":
    app()
