"""List command for displaying Canvas resources."""

from typing import Optional, Dict, Any, List
import click
from rich.console import Console
from rich.table import Table
from rich.text import Text
from pathlib import Path
import yaml

from ..utils.config import ConfigManager
from ..utils.exceptions import ConfigurationError, APIError
from ..services.api_client import APIClient
from ..utils.helpers import _resolve_project_id

console = Console()


@click.group(name="list")
def list_cmd() -> None:
    """List Canvas resources (projects, agents, tools, etc.)."""
    pass


@list_cmd.command()
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def projects(profile: Optional[str]) -> None:
    """List all projects."""
    
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        
        console.print(f"[blue]Fetching projects from {user_profile.api_base}...[/blue]")
        
        # Fetch projects
        projects_data = api_client.list_projects()
        
        if not projects_data:
            console.print("[yellow]No projects found.[/yellow]")
            return
        
        # Create table
        table = Table(title="Canvas Projects", expand=True)
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Short Name", style="magenta", overflow="fold")
        table.add_column("Name", style="bright_white", overflow="fold")
        table.add_column("Description", style="dim", overflow="fold")
        table.add_column("Created", style="blue")
        table.add_column("Members", style="green", justify="center")
        
        for project in projects_data:
            table.add_row(
                project.get("id", "N/A"),
                project.get("shortName", "N/A"),
                project.get("name", "N/A"),
                project.get("description", "N/A"),
                str(project.get("createdAt"))[:10] if project.get("createdAt") is not None else "N/A",
                str(len(project.get("collaborators", [])))
            )
        
        console.print(table)
        console.print(f"\n[blue]Total projects:[/blue] {len(projects_data)}")
        
    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


@list_cmd.command()
@click.option(
    "--project",
    required=False,
    help="Project ID to list agents from"
)
@click.option(
    "--folder",
    help="Folder ID to filter agents"
)
@click.option(
    "--search",
    help="Search term to filter agents"
)
@click.option(
    "--active-only",
    is_flag=True,
    help="Show only active agents"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def agents(project: str, folder: Optional[str], search: Optional[str], 
          active_only: bool, profile: Optional[str]) -> None:
    """List agents in a project."""
    
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        
        # Resolve project id from local folder config
        if not project:
            project = config_manager.get_default_project()
        project_id = _resolve_project_id(project)
        if not project_id:
            raise click.Abort()
        
        console.print(f"[blue]Fetching agents from project {project}...[/blue]")
        
        # Fetch agents
        agents_data = api_client.list_agents(
            project_id=project_id,
            folder_id=folder,
            search=search,
            is_active=active_only if active_only else None
        )
        
        if not agents_data:
            console.print("[yellow]No agents found.[/yellow]")
            return
        
        # Create table
        table = Table(title=f"Agents in Project {project}", expand=True)
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Short Name", style="magenta", overflow="fold")
        table.add_column("Name", style="bright_white", overflow="fold")
        table.add_column("Type", style="magenta")
        table.add_column("Status", style="green")
        table.add_column("Version", style="blue")
        table.add_column("Deployed", style="yellow", justify="center")
        table.add_column("Created", style="dim")
        
        for agent in agents_data:
            status_color = "green" if agent.get("isActive") else "red"
            status_text = Text("Active" if agent.get("isActive") else "Inactive", style=status_color)
            
            deployed_text = Text("✓" if agent.get("isDeployed") else "✗", 
                                style="green" if agent.get("isDeployed") else "red")
            
            table.add_row(
                agent.get("id", "N/A"),
                agent.get("shortName", "N/A"),
                agent.get("name", "N/A"),
                agent.get("type", "N/A"),
                status_text,
                agent.get("version", "N/A"),
                deployed_text,
                str(agent.get("createdAt"))[:10] if agent.get("createdAt") is not None else "N/A"
            )
        
        console.print(table)
        console.print(f"\n[blue]Total agents:[/blue] {len(agents_data)}")
        
        # Show summary stats
        active_count = sum(1 for agent in agents_data if agent.get("isActive"))
        deployed_count = sum(1 for agent in agents_data if agent.get("isDeployed"))
        
        console.print(f"[green]Active:[/green] {active_count}")
        console.print(f"[yellow]Deployed:[/yellow] {deployed_count}")
        
    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


@list_cmd.command()
@click.option(
    "--project",
    required=True,
    help="Project ID to list tools from"
)
@click.option(
    "--search",
    help="Search term to filter tools"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def tools(project: str, search: Optional[str], profile: Optional[str]) -> None:
    """List tools in a project."""
    
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        
        # Resolve project id from local folder config
        project_id = _resolve_project_id(project)
        if not project_id:
            raise click.Abort()
        
        console.print(f"[blue]Fetching tools from project {project}...[/blue]")
        
        # Fetch tools
        tools_data = api_client.list_tools(project_id=project_id, search=search)
        
        # Handle paginated response
        if isinstance(tools_data, dict) and "content" in tools_data:
            tools_list = tools_data["content"]
            total_elements = tools_data.get("totalElements", 0)
        else:
            tools_list = tools_data if isinstance(tools_data, list) else []
            total_elements = len(tools_list)
        
        if not tools_list:
            console.print("[yellow]No tools found.[/yellow]")
            return
        
        # Create table
        table = Table(title=f"Tools in Project {project}", expand=True)
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Short Name", style="magenta", overflow="fold")
        table.add_column("Name", style="bright_white", overflow="fold")
        table.add_column("Type", style="magenta")
        table.add_column("Description", style="dim", overflow="fold")
        table.add_column("Version", style="blue")
        table.add_column("Created", style="dim")
        
        for tool in tools_list:
            table.add_row(
                tool.get("id", "N/A"),
                tool.get("shortName", "N/A"),
                tool.get("name", "N/A"),
                tool.get("type", "N/A"),
                str(tool.get("description", "")[:40] + "...") if len(tool.get("description", "")) > 40 else tool.get("description", ""),
                tool.get("version", "N/A"),
                str(tool.get("createdAt", "N/A"))[:10] if tool.get("createdAt") else "N/A"
            )
        
        console.print(table)
        console.print(f"\n[blue]Total tools:[/blue] {total_elements}")
        
    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


@list_cmd.command()
@click.option(
    "--project",
    required=True,
    help="Project ID to list datasources from"
)
@click.option(
    "--search",
    help="Search term to filter datasources"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def datasources(project: str, search: Optional[str], profile: Optional[str]) -> None:
    """List datasources in a project."""
    
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        
        # Resolve project id from local folder config
        project_id = _resolve_project_id(project)
        if not project_id:
            raise click.Abort()
        
        console.print(f"[blue]Fetching datasources from project {project}...[/blue]")
        
        # Fetch datasources
        datasources_data = api_client.list_datasources(project_id=project_id, search=search)
        
        # Handle paginated response
        if isinstance(datasources_data, dict) and "content" in datasources_data:
            datasources_list = datasources_data["content"]
            total_elements = datasources_data.get("totalElements", 0)
        else:
            datasources_list = datasources_data if isinstance(datasources_data, list) else []
            total_elements = len(datasources_list)
        
        if not datasources_list:
            console.print("[yellow]No datasources found.[/yellow]")
            return
        
        # Create table
        table = Table(title=f"Datasources in Project {project}", expand=True)
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Short Name", style="magenta", overflow="fold")
        table.add_column("Name", style="bright_white", overflow="fold")
        table.add_column("Type", style="magenta")
        table.add_column("Description", style="dim", overflow="fold")
        table.add_column("Status", style="green")
        table.add_column("Created", style="dim")
        for datasource in datasources_list:
            status_color = "green" if datasource.get("status") == "active" else "yellow"
            status_text = Text(datasource.get("status", "unknown"), style=status_color)
            desc_raw = datasource.get("description")
            desc = str(desc_raw) if desc_raw is not None else ""
            
            table.add_row(
                datasource.get("id", "N/A"),
                datasource.get("shortName", "N/A"),
                datasource.get("name", "N/A"),
                datasource.get("type", "N/A"),
                desc[:40] + "..." if len(desc) > 40 else desc,
                status_text,
                str(datasource.get("createdAt", "N/A"))[:10] if datasource.get("createdAt") else "N/A"
            )
        
        console.print(table)
        console.print(f"\n[blue]Total datasources:[/blue] {total_elements}")
        
    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


@list_cmd.command()
@click.option(
    "--project",
    required=True,
    help="Project ID to list workflows from"
)
@click.option(
    "--folder",
    help="Folder ID to filter workflows"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def workflows(project: str, folder: Optional[str], profile: Optional[str]) -> None:
    """List workflows in a project."""
    
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        
        # Resolve project id from local folder config
        project_id = _resolve_project_id(project)
        if not project_id:
            raise click.Abort()
        
        console.print(f"[blue]Fetching workflows from project {project}...[/blue]")
        
        # Fetch workflows
        workflows_data = api_client.list_workflows(project_id=project_id, folder_id=folder)
        
        if not workflows_data:
            console.print("[yellow]No workflows found.[/yellow]")
            return
        
        # Create table
        table = Table(title=f"Workflows in Project {project}", expand=True)
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Short Name", style="magenta", overflow="fold")
        table.add_column("Name", style="bright_white", overflow="fold")
        table.add_column("Description", style="dim", overflow="fold")
        table.add_column("Status", style="green")
        table.add_column("Deployed", style="yellow", justify="center")
        table.add_column("Created", style="dim")
        
        for workflow in workflows_data:
            status_color = "green" if workflow.get("status") == "active" else "yellow"
            status_text = Text(workflow.get("status", "unknown"), style=status_color)
            
            deployed_text = Text("✓" if workflow.get("isDeployed") else "✗", 
                                style="green" if workflow.get("isDeployed") else "red")
            
            table.add_row(
                workflow.get("publicId", "N/A"),
                workflow.get("shortName", "N/A"),
                workflow.get("name", "N/A"),
                (workflow.get("description", "")[:50] + "...") if len(workflow.get("description", "")) > 50 else workflow.get("description", ""),
                status_text,
                deployed_text,
                workflow.get("createdAt", "N/A")[:10] if workflow.get("createdAt") else "N/A"
            )
        
        console.print(table)
        console.print(f"\n[blue]Total workflows:[/blue] {len(workflows_data)}")
        
        # Show summary stats
        deployed_count = sum(1 for workflow in workflows_data if workflow.get("isDeployed"))
        console.print(f"[yellow]Deployed:[/yellow] {deployed_count}")
        
    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()
