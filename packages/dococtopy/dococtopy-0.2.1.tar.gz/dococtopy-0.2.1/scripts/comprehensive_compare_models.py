#!/usr/bin/env python3
"""Compare LLM models for docstring generation quality and cost."""

import os
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

console = Console()

# Test fixture content (missing docstrings with nested structures)
FIXTURE_CONTENT = '''"""Enhanced test fixture with nested functions and classes for model comparison."""


def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def process_user_data(user_id, include_metadata=False):
    # Process user data
    user_info = get_user_info(user_id)
    
    if include_metadata:
        metadata = fetch_metadata(user_id)
        return user_info, metadata
    
    return user_info


def get_user_info(user_id):
    # Get user information
    pass


def fetch_metadata(user_id):
    # Fetch user metadata
    pass


class DataProcessor:
    # Process various types of data
    
    def __init__(self, config):
        self.config = config
        self.cache = {}
    
    def process(self, data):
        # Process the data
        if data in self.cache:
            return self.cache[data]
        
        result = self._transform(data)
        self.cache[data] = result
        return result
    
    def _transform(self, data):
        # Transform the data
        pass
    
    def cleanup(self):
        # Clean up resources
        self.cache.clear()


class UserManager:
    # Manage user operations
    
    def __init__(self):
        self.users = {}
    
    def add_user(self, user_data):
        # Add a new user
        user_id = generate_user_id()
        self.users[user_id] = user_data
        return user_id
    
    def get_user(self, user_id):
        # Get user by ID
        return self.users.get(user_id)
    
    def update_user(self, user_id, updates):
        # Update user data
        if user_id in self.users:
            self.users[user_id].update(updates)
            return True
        return False
    
    def delete_user(self, user_id):
        # Delete user
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False


def generate_user_id():
    # Generate a unique user ID
    import uuid
    return str(uuid.uuid4())


def validate_input(data, schema):
    # Validate input data against schema
    for field, rules in schema.items():
        if field not in data:
            if rules.get('required', False):
                raise ValueError(f"Missing required field: {field}")
        else:
            value = data[field]
            if 'type' in rules and not isinstance(value, rules['type']):
                raise TypeError(f"Field {field} must be of type {rules['type']}")
            if 'min_length' in rules and len(str(value)) < rules['min_length']:
                raise ValueError(f"Field {field} too short")


def handle_error(error, context=None):
    # Handle errors gracefully
    error_info = {
        'error': str(error),
        'type': type(error).__name__,
        'context': context
    }
    
    # Log error
    print(f"Error occurred: {error_info}")
    
    # Return appropriate response
    return {'success': False, 'error': error_info}
'''

# Model configurations
MODELS = {
    "openai": {
        "gpt-5-nano": {"cost_per_1k": 0.00015, "description": "Default model"},
        "gpt-5-mini": {"cost_per_1k": 0.0006, "description": "Premium model"},
        "gpt-4.1-nano": {"cost_per_1k": 0.0003, "description": "Best value"},
        "gpt-4.1-mini": {"cost_per_1k": 0.0012, "description": "Alternative"},
    },
    "anthropic": {
        "claude-haiku-3.5": {"cost_per_1k": 0.0008, "description": "Highest quality"},
        "claude-haiku-3": {"cost_per_1k": 0.00025, "description": "Budget option"},
        "claude-sonnet-4": {"cost_per_1k": 0.003, "description": "High performance"},
        "claude-opus-4.1": {"cost_per_1k": 0.015, "description": "Premium"},
    },
}


def run_model_comparison():
    """Run comprehensive model comparison."""
    console.print(
        Panel.fit(
            "[bold blue]DocOctopy Model Comparison[/bold blue]\n"
            "Comparing LLM models for docstring generation quality and cost",
            title="🚀 Model Comparison,
        )
    )

    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        fixture_file = temp_path / "test_fixture.py"
        fixture_file.write_text(FIXTURE_CONTENT)

        console.print(f"\n📁 Test fixture created: {fixture_file}")
        console.print(
            f"📊 Testing {sum(len(models) for models in MODELS.values())} models across {len(MODELS)} providers\n
        ")

        results = []

        # Test each model
        for provider, models in MODELS.items():
            console.print(
                f"[bold green]Testing {provider.upper()} models...[/bold green]"
            )

            for model_name, config in models.items():
                console.print(f"  🤖 Testing {model_name}...")

                try:
                    # Set environment variables
                    env = os.environ.copy()
                    if provider == "openai":
                        env["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
                    elif provider == "anthropic":
                        env["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY", "")

                    # Run dococtopy fix
                    result = subprocess.run(
                        [
                            "dococtopy",
                            "fix",
                            str(fixture_file),
                            "--llm-provider",
                            provider,
                            "--llm-model",
                            model_name,
                            "--output",
                            str(temp_path / f"{model_name}_result.py"),
                        ],
                        capture_output=True,
                        text=True,
                        env=env,
                        cwd=Path.cwd(),
                    )

                    if result.returncode == 0:
                        # Read the result file
                        result_file = temp_path / f"{model_name}_result.py"
                        if result_file.exists():
                            result_content = result_file.read_text()

                            # Calculate quality score (simplified)
                            quality_score = calculate_quality_score(result_content)

                            results.append(
                                {
                                    "provider": provider,
                                    "model": model_name,
                                    "quality": quality_score,
                                    "cost_per_1k": config["cost_per_1k"],
                                    "description": config["description"],
                                    "success": True,
                                    "output": result_content,
                                }
                            )

                            console.print(
                                f"    ✅ Success (Quality: {quality_score}/50)"
                            )
                        else:
                            console.print(f"    ❌ No output file generated")
                    else:
                        console.print(f"    ❌ Failed: {result.stderr}")
                        results.append(
                            {
                                "provider": provider,
                                "model": model_name,
                                "quality": 0,
                                "cost_per_1k": config["cost_per_1k"],
                                "description": config["description"],
                                "success": False,
                                "error": result.stderr,
                            }
                        )

                except Exception as e:
                    console.print(f"    ❌ Error: {str(e)}")
                    results.append(
                        {
                            "provider": provider,
                            "model": model_name,
                            "quality": 0,
                            "cost_per_1k": config["cost_per_1k"],
                            "description": config["description"],
                            "success": False,
                            "error": str(e),
                        }
                    )

        # Display results
        display_results(results)

        # Save results to files
        save_results(results, temp_path)

        return results


def calculate_quality_score(content: str) -> int:
    """Calculate a simple quality score based on docstring completeness."""
    score = 0

    # Check for docstrings
    if '"""' in content:
        score += 10

    # Check for Args sections
    if "Args:" in content:
        score += 10

    # Check for Returns sections
    if "Returns:" in content:
        score += 10

    # Check for Raises sections
    if "Raises:" in content:
        score += 10

    # Check for proper formatting
    if '    """' in content:  # Proper indentation
        score += 5

    # Check for descriptive content
    lines = content.split("\n")
    docstring_lines = 0
    in_docstring = False

    for line in lines:
        if '"""' in line and not in_docstring:
            in_docstring = True
            continue
        elif '"""' in line and in_docstring:
            in_docstring = False
            continue
        elif in_docstring:
            docstring_lines += 1

    if docstring_lines > 5:
        score += 5

    return min(score, 50)  # Cap at 50


def display_results(results: List[Dict]):
    """Display comparison results in a table."""
    console.print("\n" + "=" * 80)
    console.print("[bold blue]COMPARISON RESULTS[/bold blue]")
    console.print("=" * 80)

    # Create results table
    table = Table(title="Model Comparison Results")
    table.add_column("Provider", style="cyan")
    table.add_column("Model", style="green")
    table.add_column("Quality", style="yellow", justify="center")
    table.add_column("Cost/1K", style="red", justify="right")
    table.add_column("Description", style="blue")
    table.add_column("Status", style="magenta")

    # Sort results by quality (descending)
    sorted_results = sorted(results, key=lambda x: x["quality"], reverse=True)

    for result in sorted_results:
        status = "✅ Success" if result["success"] else "❌ Failed"
        table.add_row(
            result["provider"].upper(),
            result["model"],
            f"{result['quality']}/50",
            f"${result['cost_per_1k']:.4f}",
            result["description"],
            status,
        )

    console.print(table)

    # Show top performers
    successful_results = [r for r in sorted_results if r["success"]]
    if successful_results:
        console.print(f"\n[bold green]🏆 Top Performers:[/bold green]")
        for i, result in enumerate(successful_results[:3], 1):
            console.print(
                f"  {i}. {result['model']} ({result['provider']}) - Quality: {result['quality']}/50"
            )


def save_results(results: List[Dict], temp_path: Path):
    """Save results to files."""
    # Save comprehensive results
    results_file = Path("docs/model-comparison/comprehensive-comparison-results.txt")
    results_file.parent.mkdir(parents=True, exist_ok=True)

    with open(results_file, "w") as f:
        f.write("DocOctopy Model Comparison Results\n")
        f.write("=" * 50 + "\n\n")

        for result in results:
            f.write(f"Provider: {result['provider']}\n")
            f.write(f"Model: {result['model']}\n")
            f.write(f"Quality: {result['quality']}/50\n")
            f.write(f"Cost per 1K tokens: ${result['cost_per_1k']:.4f}\n")
            f.write(f"Description: {result['description']}\n")
            f.write(f"Status: {'Success' if result['success'] else 'Failed'}\n")
            if not result["success"] and "error" in result:
                f.write(f"Error: {result['error']}\n")
            f.write("-" * 30 + "\n\n")

    console.print(f"\n💾 Results saved to: {results_file}")

    # Save individual result files
    for result in results:
        if result["success"]:
            result_file = Path(f"docs/model-comparison/{result['model']}_result.py")
            result_file.write_text(result["output"])
            console.print(f"💾 {result['model']} output saved to: {result_file}"
)

def main():
    """Main function."""
    # Check for API keys
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if not openai_key and not anthropic_key:
        console.print("[bold red]❌ No API keys found![/bold red]")
        console.print(
            "Please set OPENAI_API_KEY and/or ANTHROPIC_API_KEY environment variables"
        )
        return 1

    if not openai_key:
        console.print(
            "[yellow]⚠️  No OpenAI API key found, skipping OpenAI models[/yellow]"
        )
        MODELS.pop("openai", None)

    if not anthropic_key:
        console.print(
            "[yellow]⚠️  No Anthropic API key found, skipping Anthropic models[/yellow]"
        )
        MODELS.pop("anthropic", None)

    if not MODELS:
        console.print("[bold red]❌ No models to test![/bold red]")
        return 1

    try:
        results = run_model_comparison()
        console.print(f"\n[bold green]✅ Comparison complete![/bold green]")
        console.print(f"📊 Tested {len(results)} models")
        console.print(f"✅ {sum(1 for r in results if r['success'])} successful")
        console.print(f"❌ {sum(1 for r in results if not r['success'])} failed")
        return 0
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Comparison interrupted by user[/yellow]")
        return 1
    except Exception as e:
        console.print(f"\n[bold red]❌ Error during comparison: {str(e)}[/bold red]")
        return 1


if __name__ == "__main__":
    exit(main())
