"""Initialize command for creating Canvas workspace structure."""

import os
from pathlib import Path
from typing import Optional

import click
import yaml
from rich.console import Console
from rich.table import Table

from ..utils.config import ConfigManager, CanvasConfig
from ..utils.exceptions import FileSystemError

console = Console()


@click.command()
@click.option(
    "--force",
    is_flag=True,
    help="Force initialization even if files exist"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
@click.option(
    "--name",
    help="Home directory name under current working directory to create and put all project workspaces in"
)
@click.argument("directory", required=True)
def init(directory: Optional[str], force: bool, profile: Optional[str], name: Optional[str]) -> None:
    """Initialize Canvas workspaces for all projects in separate folders by shortName."""
    
    try:
        # Resolve profile and API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            return
        from ..services.api_client import APIClient
        api_client = APIClient(user_profile)

        # Fetch projects
        console.print("[blue]Fetching projects to initialize workspaces...[/blue]")
        projects = api_client.list_projects() or []
        if not projects:
            console.print("[yellow]No projects found. Nothing to initialize.[/yellow]")
            return
        
        # Show table of projects (similar to list.py)
        table = Table(title="Canvas Projects", expand=True)
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Short Name", style="magenta", overflow="fold")
        table.add_column("Name", style="bright_white")
        table.add_column("Description", style="dim")
        table.add_column("Created", style="blue")
        table.add_column("Members", style="green", justify="center")
        for project in projects:
            table.add_row(
                project.get("id", "N/A"),
                project.get("shortName", "N/A"),
                project.get("name", "N/A"),
                project.get("description", "N/A"),
                str(project.get("createdAt"))[:10] if project.get("createdAt") is not None else "N/A",
                str(len(project.get("collaborators", [])))
            )
        console.print(table)
        
        # Prompt for default project short name and validate
        valid_short_names = {p.get("shortName") for p in projects if p.get("shortName")}
        default_project = None
        while not default_project:
            candidate = click.prompt("Enter default project short name", type=str)
            candidate = candidate.strip()
            if candidate in valid_short_names:
                default_project = candidate
            else:
                console.print(f"[red]'" + candidate + "' is not a valid project short name from the list above. Please try again.[/red]")
        
        # Determine and create workspace directory from argument (supports '.' or a folder name)
        target_arg = directory or "."
        workspace_path = Path.cwd() if target_arg == "." else (Path.cwd() / target_arg)
        console.print(f"[blue]Preparing home directory:[/blue] {workspace_path}")
        if not workspace_path.exists():
            workspace_path.mkdir(parents=True, exist_ok=True)
            console.print("[green]✓[/green] Created home directory")
        else:
            console.print("[yellow]•[/yellow] Home directory already exists")
                
        # Create directory structure
        _create_directory_structure(workspace_path)

        # Create project config file
        _create_project_config_file(workspace_path, projects)

        # Create configuration files
        _create_config_files(workspace_path, default_project)

        _create_env_files(workspace_path / "environments", projects)
                        
        # Update .gitignore
        _update_gitignore(workspace_path)
        
        console.print(f"[green]✓[/green] Canvas workspace '{default_project}' initialized successfully!")
                
    except Exception as e:
        raise FileSystemError(f"Failed to initialize workspace: {e}")


def _create_directory_structure(base_path: Path) -> None:
    """Create the Canvas directory structure."""
    directories = [
        "agents",
        "tools",
        "datasources",
        "environments"
    ]
    
    for directory in directories:
        dir_path = base_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        console.print(f"[green]✓[/green] Created directory: {directory}")


def _create_config_files(base_path: Path, project_name: str) -> None:
    """Create configuration files."""
    
    # Create canvas.yaml
    canvas_config = CanvasConfig(
        name=project_name,
        version="1.0",
        default_environment="dev"
    )
    
    config_manager = ConfigManager()
    config_manager.workspace_config = base_path / "canvas.yaml"
    config_manager.save_workspace_config(canvas_config)
    console.print("[green]✓[/green] Created canvas.yaml")
    
def _create_project_config_file(base_path: Path, projects: list) -> None:
    """Create a per-project config file with id, name, and selected project.config fields."""
    try:
        data = {}
        for project in projects:
            project_config = project.get("config", {}) or {}
            config_data = {
                "id": project.get("id") or project.get("publicId"),
                "name": project.get("name"),
                "config": {
                    "deploymentUrl": project_config.get("deploymentUrl"),
                    "platform": project_config.get("platform")
                }
            }
            data[project.get("shortName")] = config_data
        out_path = base_path / "project_config.yaml"
        with open(out_path, 'w') as f:
            yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)
        console.print(f"[green]✓[/green] Created project_config.yaml")
    except Exception as e:
        console.print(f"[yellow]Warning:[/yellow] Failed to write project_config.yaml: {e}")

def _create_env_files(base_path: Path, projects: list) -> None:
    """Create .env files for each project."""
    base_path.mkdir(parents=True, exist_ok=True)
    for project in projects:
        short_name = project.get("shortName")
        if not short_name:
            continue
        env_file = base_path / f"{short_name}.env"
        env_file.touch(exist_ok=True)
        console.print(f"[green]✓[/green] Created .env file for {short_name}")

def _update_gitignore(base_path: Path) -> None:
    """Update .gitignore to ignore .canvasrc."""
    gitignore_path = base_path / ".gitignore"
    
    gitignore_entries = [
        "# Canvas CLI",
        ".canvasrc",
        "*.lock.json",
        "__pycache__/",
        "*.pyc",
        ".env",
        ".venv/",
        "node_modules/",
    ]
    
    existing_content = ""
    if gitignore_path.exists():
        with open(gitignore_path, 'r') as f:
            existing_content = f.read()
    
    # Only add entries that don't already exist
    new_entries = []
    for entry in gitignore_entries:
        if entry not in existing_content:
            new_entries.append(entry)
    
    if new_entries:
        with open(gitignore_path, 'a') as f:
            if existing_content and not existing_content.endswith('\n'):
                f.write('\n')
            f.write('\n'.join(new_entries) + '\n')
        console.print("[green]✓[/green] Updated .gitignore")
    else:
        console.print("[yellow]•[/yellow] .gitignore already up to date")
