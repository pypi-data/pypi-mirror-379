"""
CLI for pyweld - Multi-repository Python welding tool
"""

import typer
import os
import subprocess
from pathlib import Path
from typing import Optional, List  # Importing Optional and List
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm
from rich.panel import Panel
from rich import box

from pyweld import (
    init_project,
    weld,
    unweld,
    version as get_version,
    info as get_info,
    get_welded_repos,
    resolve_repo_path,
    is_valid_python_package,
    WeldConfig,
    ConfigError,
    RepoError,
)

app = typer.Typer(help="🔗 pyweld - Multi-repository Python welding CLI")
console = Console()

# ------------------------------
# Helper functions
# ------------------------------

def write_default_weldconfig(filepath: Path, project_name: Optional[str] = None) -> None:
    """
    Write a basic .weldconfig file to the given filepath.
    The config is a simple TOML-like format for demo purposes.
    """
    project_name = project_name or filepath.parent.name
    content = f"""# pyweld config file

[project]
name = "{project_name}"

[repos]
# Example:
# utils = "../shared-utils"
"""
    filepath.write_text(content)
    console.print(f"[green]✅ Created default .weldconfig at {filepath}[/green]")


# ------------------------------
# Commands
# ------------------------------

@app.command("init")
def cli_init(name: Optional[str] = typer.Option(None, help="Project name (optional)")):
    """
    Initialize a new pyweld project with a default .weldconfig
    Creates .weldconfig in the current working directory.
    """
    config_path = Path(os.getcwd()) / ".weldconfig"
    if config_path.exists():
        if not Confirm.ask(f".weldconfig already exists at {config_path}. Overwrite?"):
            console.print("[yellow]Init cancelled.[/yellow]")
            raise typer.Exit()
    write_default_weldconfig(config_path, name)


@app.command("add")
def cli_add(
    path: str = typer.Argument(..., help="Path to local repository"),
    as_name: Optional[str] = typer.Option(None, "--as", "-a", help="Name to assign in weld config")
):
    """
    Add a repository to .weldconfig
    """
    config_path = Path(os.getcwd()) / ".weldconfig"
    if not config_path.exists():
        console.print("[red]❌ .weldconfig not found. Run 'pyweld init' first.[/red]")
        raise typer.Exit(1)

    try:
        config = WeldConfig.load(str(config_path))
    except Exception as e:
        console.print(f"[red]❌ Failed to load .weldconfig: {e}[/red]")
        raise typer.Exit(1)

    repo_path = resolve_repo_path(path)

    if not is_valid_python_package(repo_path):
        if not Confirm.ask(f"[yellow]Path '{repo_path}' is not a valid Python package. Add anyway?[/yellow]"):
            raise typer.Exit(1)

    name = as_name or repo_path.name

    if name in config.repos:
        console.print(f"[red]❌ Repo '{name}' already exists in config.[/red]")
        raise typer.Exit(1)

    config.repos[name] = str(repo_path)
    try:
        config.save(str(config_path))
    except Exception as e:
        console.print(f"[red]❌ Failed to save .weldconfig: {e}[/red]")
        raise typer.Exit(1)

    console.print(f"[green]✅ Added repo '{name}' -> {repo_path}[/green]")


@app.command("remove")
def cli_remove(name: str = typer.Argument(..., help="Repository name to remove")):
    """
    Remove a repository from .weldconfig
    """
    config_path = Path(os.getcwd()) / ".weldconfig"
    if not config_path.exists():
        console.print("[yellow]No .weldconfig found.[/yellow]")
        raise typer.Exit(1)

    try:
        config = WeldConfig.load(str(config_path))
    except Exception as e:
        console.print(f"[red]❌ Failed to load .weldconfig: {e}[/red]")
        raise typer.Exit(1)

    if name not in config.repos:
        console.print(f"[red]❌ Repo '{name}' not found in config[/red]")
        raise typer.Exit(1)

    del config.repos[name]

    try:
        config.save(str(config_path))
    except Exception as e:
        console.print(f"[red]❌ Failed to save .weldconfig: {e}[/red]")
        raise typer.Exit(1)

    console.print(f"[green]✅ Removed repo '{name}'[/green]")


@app.command("list")
def cli_list():
    """
    List all repositories in .weldconfig
    """
    config_path = Path(os.getcwd()) / ".weldconfig"
    if not config_path.exists():
        console.print("[yellow]No .weldconfig found.[/yellow]")
        raise typer.Exit()

    try:
        config = WeldConfig.load(str(config_path))
    except Exception as e:
        console.print(f"[red]❌ Failed to load .weldconfig: {e}[/red]")
        raise typer.Exit(1)

    if not config.repos:
        console.print("[yellow]No repositories configured.[/yellow]")
        raise typer.Exit()

    table = Table(title=".weldconfig Repositories", box=box.SIMPLE)
    table.add_column("Name", style="bold cyan")
    table.add_column("Path", style="green")

    for name, path in config.repos.items():
        table.add_row(name, path)

    console.print(table)


@app.command("status")
def cli_status():
    """
    Show status of welded repositories
    """
    try:
        welded = get_welded_repos()
    except ConfigError:
        console.print("[red]❌ No .weldconfig found or invalid config[/red]")
        raise typer.Exit(1)

    if not welded:
        console.print("[yellow]No repositories currently welded.[/yellow]")
        raise typer.Exit()

    table = Table(title="Welded Repositories", box=box.SIMPLE)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Path", style="green")
    table.add_column("Status", style="bold")

    for name, info in welded.items():
        table.add_row(name, info.get("path", "?"), "✅")

    console.print(table)


@app.command("info")
def cli_info():
    """
    Show detailed info about pyweld environment
    """
    data = get_info()
    panel = Panel.fit(
        f"[bold]pyweld {data['version']}[/bold]\n"
        f"Description: {data['description']}\n"
        f"Author: {data['author']}\n"
        f"Welded repos: {data['welded_repos']}\n"
        f"Import hooks: {'✅' if data['import_hooks_installed'] else '❌'}",
        title="pyweld info",
        border_style="blue",
    )
    console.print(panel)


@app.command("doctor")
def cli_doctor():
    """
    Validate current weld configuration
    """
    config_path = Path(os.getcwd()) / ".weldconfig"
    if not config_path.exists():
        console.print("[red]❌ .weldconfig not found[/red]")
        raise typer.Exit(1)

    try:
        config = WeldConfig.load(str(config_path))
    except Exception as e:
        console.print(f"[red]❌ Failed to load .weldconfig: {e}[/red]")
        raise typer.Exit(1)

    all_valid = True

    for name, path in config.repos.items():
        resolved = Path(path).resolve()
        exists = resolved.exists()
        is_package = is_valid_python_package(resolved)

        if not exists:
            console.print(f"[red]❌ {name} → {resolved} does not exist[/red]")
            all_valid = False
        elif not is_package:
            console.print(f"[yellow]⚠️ {name} → {resolved} is not a valid Python package[/yellow]")
        else:
            console.print(f"[green]✅ {name} → {resolved} OK[/green]")

    if all_valid:
        console.print("[green]✔️ All repositories look good[/green]")


@app.command("run")
def cli_run(
    command: str = typer.Argument(..., help="Command to run"),
    args: List[str] = typer.Argument(None, help="Arguments for the command"),
):
    """
    Run a command in a context with welded repositories
    """
    try:
        welder = weld()
    except Exception as e:
        console.print(f"[red]❌ Failed to weld: {e}[/red]")
        raise typer.Exit(1)

    full_command = [command] + (args or [])
    console.print(f"[cyan]🔧 Running:[/cyan] {' '.join(full_command)}")

    try:
        subprocess.run(full_command, check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]❌ Command failed with code {e.returncode}[/red]")
        raise typer.Exit(e.returncode)
    finally:
        unweld()


@app.command("version")
def cli_version():
    """Show pyweld version"""
    console.print(f"[bold green]pyweld v{get_version()}[/bold green]")


# ------------------------------
# Entry point
# ------------------------------

def main():
    app()


if __name__ == "__main__":
    main()
