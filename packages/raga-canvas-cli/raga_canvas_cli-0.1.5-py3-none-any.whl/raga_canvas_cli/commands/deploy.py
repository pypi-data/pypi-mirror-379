"""Push command for deploying agents to Canvas platform."""

import os
import yaml
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from ..utils.config import ConfigManager
from ..utils.exceptions import ValidationError, APIError, FileSystemError
from ..services.api_client import APIClient
from ..utils.helpers import _resolve_project_id
from ..utils.helpers import _resolve_local_item_id

console = Console()


@click.group(name="deploy")
def deploy() -> None:
    """Deploy Canvas agents."""
    pass


@deploy.command(name="agents")
@click.option(
    "--target-project",
    required=False,
    help="Project ID to deploy the agent to"
)
@click.option(
    "--agent",
    required=True,
    help="Agent directory short name or ID to deploy"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def deploy_agent(target_project: str, agent: str, profile: Optional[str]) -> None:
    """Push an agent to the Canvas platform.
    
    AGENT_NAME: Name (short name) or ID of the agent to deploy
    PROJECT_ID: Target project ID on the Canvas platform
    """
    
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        project = config_manager.get_default_project()
        if not target_project:
            target_project = project
        target_project_id = _resolve_project_id(target_project)
        if not target_project_id:
            console.print(f"[red]Project config not found locally: {target_project}[/red]")
            print("Run 'canvas pull projects' first to initialize the project config")
            raise click.Abort()
        
        console.print(f"[blue]Preparing to deploy agent '{agent}' in project '{target_project}'[/blue]")

        remote_agent = api_client.get_agent_by_short_name(target_project_id, agent)
        if not remote_agent:
            console.print(f"[red]Agent '{agent}' not found in project '{target_project}'[/red]. Run 'canvas push' first.")
            raise click.Abort()
        
        resolved_agent_id = remote_agent.get("id")
                
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Deploying agent...", total=None)
            deployed_agent = api_client.deploy_agent(target_project_id, resolved_agent_id)
            progress.update(task, description="Agent deployed successfully")
            console.print(f"[green]✓[/green] Agent '{resolved_agent_id}' deployed successfully")
        
    except ValidationError as e:
        console.print(f"[red]Validation Error:[/red] {e}")
        raise click.Abort()
    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except FileSystemError as e:
        console.print(f"[red]File Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


def _generate_lock_file(project_root: Path, agent_name: str, agent_config: Dict[str, Any], project_id: str) -> None:
    """Generate agent lock file with deployment information."""
    
    lock_data = {
        "name": agent_config.get("name"),
        "version": agent_config.get("version"),
        "project_id": project_id,
        "deployed_at": datetime.now().isoformat(),
        "tools": [tool.get("name") for tool in agent_config.get("tools", [])],
        "datasources": [ds.get("name") for ds in agent_config.get("datasources", [])],
        "config_hash": hash(str(agent_config))  # Simple hash for change detection
    }
    
    lock_file = project_root / "agents" / agent_name / "agent.lock.json"
    with open(lock_file, 'w') as f:
        json.dump(lock_data, f, indent=2)
    
    console.print(f"[green]✓[/green] Generated lock file: {lock_file}")

def _load_agent_config(agent_name: str, project_root: Path) -> Dict[str, Any]:
    """Load and merge agent configuration."""
    
    agent_dir = project_root / "agents" / agent_name
    agent_yaml = agent_dir / "agent.yaml"
    
    if not agent_dir.exists():
        raise FileSystemError(f"Agent directory 'projects/{project_root.name}/agents/{agent_name}' not found. Pull the agent of create it first.")
    
    if not agent_yaml.exists():
        raise FileSystemError(f"Agent configuration 'projects/{project_root.name}/agents/{agent_name}/agent.yaml' not found")
    
    # Load base agent config
    with open(agent_yaml, 'r') as f:
        agent_config = yaml.safe_load(f)
    
    return agent_config
