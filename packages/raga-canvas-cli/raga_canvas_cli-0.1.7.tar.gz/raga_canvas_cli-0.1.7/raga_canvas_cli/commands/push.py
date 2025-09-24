"""Push command for deploying agents to Canvas platform."""

import os
import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from ..commands.pull import _safe_get_agent, _safe_get_tool, _safe_get_datasource
from ..utils.config import ConfigManager
from ..utils.exceptions import ValidationError, APIError, FileSystemError
from ..services.api_client import APIClient
from ..utils.helpers import _resolve_project_id
from ..commands.pull import _extract_tool_ids
from ..utils.helpers import convert_tool_obj_to_tool_data, convert_datasource_obj_to_datasource_data
from ..commands.pull import pull_agents, pull_tools, pull_datasources
from dotenv import dotenv_values

console = Console()


@click.group(name="push")
def push() -> None:
    """Push Canvas resources (agents, tools, datasources, etc.)."""
    pass


@push.command(name="agents")
@click.option(
    "--target-project",
    required=False,
    help="Project ID to push the agent to"
)
@click.option(
    "--agent",
    required=True,
    help="Agent directory name or ID to push"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
@click.option(
    "--force",
    is_flag=True,
    help="Force deployment even if validation warnings exist"
)
def push_agent_command(target_project: str, agent: str, 
         profile: Optional[str], force: True) -> None:
    """Push a local agent to the Canvas platform.
    
    agent: short name of the agent to deploy (directory name in agents/)
    target_project: Target project short name on the Canvas platform
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

        # Load env vars from environments/*.env for this process
        if(target_project):
            _load_env_from_environments_dir(target_project)
        else:
            _load_env_from_environments_dir(project)

        source_project_id = _resolve_project_id(project)
        if not source_project_id:
            console.print("[red]No source project found. Run 'canvas init' first.[/red]")
            raise click.Abort()
        
        target_project_id = source_project_id

        if(target_project):
            target_project_id = _resolve_project_id(target_project)
            if not target_project_id:
                console.print(f"[red]Project config not found locally: {target_project}[/red]")
                print("Run 'canvas pull projects' first to initialize the project config")
                raise click.Abort()
        
        console.print(f"[blue]Preparing to push agent '{agent}' in project '{target_project}'[/blue]")
                
        # Pre-sync referenced resources (tools and datasources)
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            sync_task = progress.add_task("Syncing referenced resources...", total=None)
            push_agent(target_project_id, agent, api_client, force)
                
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


@push.command(name="tools")
@click.option(
    "--target-project",
    required=False,
    help="Project ID to push the tool to"
)
@click.option(
    "--tool",
    required=True,
    help="Tool directory name or ID to push"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
@click.option(
    "--force",
    is_flag=True,
    help="Force deployment even if validation warnings exist"
)
def push_tool_command(target_project: str, tool: str, 
         profile: Optional[str], force: True) -> None:
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        project = config_manager.get_default_project()

        # Load env vars from environments/*.env for this process
        if(target_project):
            _load_env_from_environments_dir(target_project)
        else:
            _load_env_from_environments_dir(project)

        source_project_id = _resolve_project_id(project)
        if not source_project_id:
            console.print("[red]No source project found. Run 'canvas init' first.[/red]")
            raise click.Abort()
        
        target_project_id = source_project_id

        if(target_project):
            target_project_id = _resolve_project_id(target_project)
            if not target_project_id:
                console.print(f"[red]Project config not found locally: {target_project}[/red]")
                print("Run 'canvas pull projects' first to initialize the project config")
                raise click.Abort()
            
        push_tool(api_client, target_project_id, tool)
        
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


@push.command(name="datasources")
@click.option(
    "--target-project",
    required=False,
    help="Project ID to push the datasource to"
)
@click.option(
    "--datasource",
    required=True,
    help="Datasource directory name or ID to push"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
@click.option(
    "--force",
    is_flag=True,
    help="Force deployment even if validation warnings exist"
)
def push_datasource_command(target_project: str, datasource: str, 
         profile: Optional[str], force: True) -> None:
    try:
        # Get profile and create API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()
        
        api_client = APIClient(user_profile)
        project = config_manager.get_default_project()

        # Load env vars from environments/*.env for this process
        if(target_project):
            _load_env_from_environments_dir(target_project)
        else:
            _load_env_from_environments_dir(project)

        source_project_id = _resolve_project_id(project)
        if not source_project_id:
            console.print("[red]No source project found. Run 'canvas init' first.[/red]")
            raise click.Abort()
        
        target_project_id = source_project_id

        if(target_project):
            target_project_id = _resolve_project_id(target_project)
            if not target_project_id:
                console.print(f"[red]Project config not found locally: {target_project}[/red]")
                print("Run 'canvas pull projects' first to initialize the project config")
                raise click.Abort()
            
        push_datasource(api_client, target_project_id, datasource)
        
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


def push_agent(target_project_id: str, agent: str, api_client: APIClient, force: True) -> None:
    """Push a local agent to the Canvas platform."""
    local_agent_config = _load_agent_config(Path("agents") / agent , agent)
    tool_names = local_agent_config.get("tools", [])
    print("tool_names:", tool_names)
    datasource_name = local_agent_config.get("tracingConfigId", "")
    print("datasource_name:", datasource_name)
    subagent_names = local_agent_config.get("subAgents", [])
    print("subagent_names:", subagent_names)
    # Validate agent configuration
    _validate_agent_config(local_agent_config, force)

    # Subagents
    for subagent_name in subagent_names:
        push_agent(target_project_id, subagent_name, api_client, force)
    # Tools
    for tool_name in tool_names:
        push_tool(api_client, target_project_id, tool_name)
    # Datasources
    if datasource_name:
        push_datasource(api_client, target_project_id, datasource_name)

    remote_agent_config = None
    try:
        remote_agent_config_id = api_client.get_agent_by_short_name(target_project_id, agent).get("id")
        remote_agent_config = pull_agents([remote_agent_config_id], target_project_id, api_client, write_to_file=False)[1][0]
        # print("remote_agent_config:", remote_agent_config)
    except APIError:
        print("remote agent not found in the target project")
        remote_agent_config = None
    except Exception as e:
        print(f"error getting remote agent: {e}")
        remote_agent_config = None

    if remote_agent_config is None:
        if local_agent_config is None:
            console.print(f"[yellow]•[/yellow] Skipping agent {agent}: no local config and not found remotely")
            return
        local_agent_config = _resolve_references(local_agent_config, api_client, target_project_id)
        # print("created local_agent_config:", local_agent_config)
        api_client.create_agent(target_project_id, local_agent_config, agent)
        console.print(f"[green]✓[/green] Created agent {agent} in project {target_project_id}")

    else:
        if _normalize_config(remote_agent_config) != _normalize_config(local_agent_config):
            local_agent_config = _resolve_references(local_agent_config, api_client, target_project_id)
            # print("updated local_agent_config:", local_agent_config)
            api_client.update_agent(target_project_id, remote_agent_config_id, local_agent_config)
            console.print(f"[green]✓[/green] Updated agent {agent} in project {target_project_id}")



def _resolve_references(local_agent_config: Dict[str, Any], api_client: APIClient, target_project_id: str) -> Dict[str, Any]:
    subagent_list = []
    for subagent_name in local_agent_config.get("subAgents", []):
        subagent_id = api_client.get_agent_by_short_name(target_project_id, subagent_name).get("id")
        subagent_list.append({"agentId": subagent_id})
    local_agent_config["subAgents"] = subagent_list

    tool_list = []
    for tool_name in local_agent_config.get("tools", []):
        tool_id = api_client.get_tool_by_short_name(target_project_id, tool_name).get("id")
        tool_list.append({"toolId": tool_id})
    local_agent_config["tools"] = tool_list    

    if local_agent_config.get("tracingConfigId"):
        datasource_id = api_client.get_datasource_by_short_name(target_project_id, local_agent_config.get("tracingConfigId")).get("id")
        local_agent_config["tracingConfigId"] = datasource_id
    return local_agent_config


def _load_agent_config(agent_dir: Path, agent_name: str) -> Dict[str, Any]:
    """Load and merge agent configuration from the per-project folder."""
    
    agent_yaml = agent_dir / "agent.yaml"
    if not agent_dir.exists() or not agent_yaml.exists():
        raise FileSystemError(f"Agent configuration '{agent_yaml}' not found")
    
    with open(agent_yaml, 'r') as f:
        agent_config = yaml.safe_load(f)
        
    return agent_config


def _merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge configuration dictionaries."""
    result = base.copy()
    
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _merge_configs(result[key], value)
        else:
            result[key] = value
    
    return result

def _validate_agent_config(agent_config: Dict[str, Any], force: bool) -> None:
    """Validate agent configuration."""
    
    errors = []
    warnings = []
    
    # Required fields
    required_fields = ["agentName", "description", "agentType", "modelConfig", "promptConfig"]
    for field in required_fields:
        if field not in agent_config:
            errors.append(f"Missing required field: {field}")
    
    # Validate config section
    config = agent_config.get("modelConfig", {})
    if not config.get("model"):
        errors.append("No model specified in modelConfig")
    
    prompt_config = agent_config.get("promptConfig", {})
    if not prompt_config.get("systemPrompt"):
        errors.append("No system prompt specified")
    
    # Validate tools
    tools = agent_config.get("tools", [])
    for tool in tools:
        if not isinstance(tool, str):
            errors.append(f"Tool {tool} is not a string")
    
    # Validate datasources
    tracing_config_id = agent_config.get("tracingConfigId", "")
    if tracing_config_id:
        if not isinstance(tracing_config_id, str):
            errors.append("tracing config ID must be a string")
    
    # Report errors
    if errors:
        console.print("[red]Validation Errors:[/red]")
        for error in errors:
            console.print(f"  • {error}")
        raise ValidationError("Agent configuration has validation errors")
    
    # Report warnings
    if warnings:
        console.print("[yellow]Validation Warnings:[/yellow]")
        for warning in warnings:
            console.print(f"  • {warning}")
        
        if not force and not click.confirm("Continue with warnings?", default=True):
            raise click.Abort()


def _show_deployment_summary(agent_config: Dict[str, Any], project_id: str, 
                           environment: Optional[str]) -> None:
    """Show deployment summary for dry run."""
    
    console.print("\n[bold]Deployment Summary[/bold]")
    console.print(f"[blue]Agent Name:[/blue] {agent_config.get('name', 'N/A')}")
    console.print(f"[blue]Description:[/blue] {agent_config.get('description', 'N/A')}")
    console.print(f"[blue]Type:[/blue] {agent_config.get('type', 'N/A')}")
    console.print(f"[blue]Version:[/blue] {agent_config.get('version', 'N/A')}")
    console.print(f"[blue]Target Project:[/blue] {project_id}")
    console.print(f"[blue]Environment:[/blue] {environment or 'default'}")
    
    config = agent_config.get("config", {})
    console.print(f"[blue]Model:[/blue] {config.get('model', 'N/A')}")
    console.print(f"[blue]Temperature:[/blue] {config.get('temperature', 'N/A')}")
    console.print(f"[blue]Max Tokens:[/blue] {config.get('max_tokens', 'N/A')}")
    
    tools = agent_config.get("tools", [])
    console.print(f"[blue]Tools:[/blue] {len(tools)}")
    for tool in tools:
        console.print(f"  • {tool.get('name') or tool.get('id') or tool.get('publicId') or 'Unnamed'}")
    
    datasources = agent_config.get("datasources", [])
    console.print(f"[blue]Datasources:[/blue] {len(datasources)}")
    for ds in datasources:
        console.print(f"  • {ds.get('name') or ds.get('id') or ds.get('publicId') or 'Unnamed'}")
    
    metadata = agent_config.get("metadata", {})
    if metadata.get("tags"):
        console.print(f"[blue]Tags:[/blue] {', '.join(metadata['tags'])}")
    if metadata.get("owners"):
        console.print(f"[blue]Owners:[/blue] {', '.join(metadata['owners'])}")


def _generate_lock_file(project_root: Path, agent_name: str, agent_config: Dict[str, Any], project_id: str) -> None:
    """Generate agent lock file with deployment information under the project folder."""
    
    lock_data = {
        "name": agent_config.get("name") or agent_config.get("agentName"),
        "version": agent_config.get("version"),
        "project_id": project_id,
        "deployed_at": "2024-01-01T00:00:00Z",
        "tools": [
            (tool.get("id") or tool.get("publicId") or tool.get("name") or tool.get("toolId"))
            for tool in agent_config.get("tools", [])
            if isinstance(tool, dict)
        ],
        "datasources": [agent_config.get("tracingConfigId")] if agent_config.get("tracingConfigId") else [],
        "config_hash": hash(str(agent_config))
    }
    
    lock_file = project_root / "agents" / agent_name / "agent.lock.json"
    lock_file.parent.mkdir(parents=True, exist_ok=True)
    with open(lock_file, 'w') as f:
        json.dump(lock_data, f, indent=2)
    
    console.print(f"[green]✓[/green] Generated lock file: {lock_file}")


# ---------- Pre-sync helpers ----------



def _normalize_config(obj: Any) -> Any:
    """Normalize config for comparison (sort keys, remove transient fields)."""
    if isinstance(obj, dict):
        # Remove known server-managed fields
        cleaned = {k: _normalize_config(v) for k, v in obj.items() if k not in {"createdAt", "modifiedAt", "version", "publicId", "id"}}
        # Return items sorted by key for stable comparison
        return {k: cleaned[k] for k in sorted(cleaned.keys())}
    if isinstance(obj, list):
        normalized_items = [_normalize_config(v) for v in obj]
        try:
            # Sort by canonical JSON so list order does not affect equality
            return sorted(normalized_items, key=lambda x: json.dumps(x, sort_keys=True))
        except Exception:
            return normalized_items
    return obj





def push_tool(api_client: APIClient, target_project_id: str, tool_name: str) -> None:
    """Push a tool to the Canvas platform."""
    # Resolve actual tool id from local config if the provided value is a short name

    # Load local tool config if present (new layout)
    local_path_yaml = Path("tools") / tool_name / "tool.yaml"
    local_tool = None
    if local_path_yaml.exists():
        with open(local_path_yaml, 'r') as f:
            local_tool = yaml.safe_load(f) or {}
            if(local_tool.get("config", {}).get("dataSourceId")):
                push_datasource(api_client, target_project_id, local_tool.get("config", {}).get("dataSourceId"))
            local_tool = _resolve_protected_references(local_tool, api_client, type="tool")
    else:
        console.print(f"[yellow]•[/yellow] Skipping tool {tool_name}: no local config")
        return
    remote_tool = None
    try:
        remote_tool_id = api_client.get_tool_by_short_name(target_project_id, tool_name).get("id")
        remote_tool = pull_tools([remote_tool_id], target_project_id, api_client, write_to_file=False)[1][0]
        # print("remote_tool:", remote_tool)
    except APIError:
        remote_tool = None

    if remote_tool is None:
        if local_tool is None:
            console.print(f"[yellow]•[/yellow] Skipping tool {tool_name}: no local config and not found remotely")
            return
        local_tool = _resolve_tool_references(local_tool, api_client, target_project_id)
        # print("created local_tool:", local_tool)
        api_client.create_tool(target_project_id, local_tool, tool_name)
        console.print(f"[green]✓[/green] Created tool {tool_name} in project {target_project_id}")
        return

    if local_tool is not None and _normalize_config(remote_tool) != _normalize_config(local_tool):
        local_tool = _resolve_tool_references(local_tool, api_client, target_project_id)
        # print("updated local_tool:", local_tool)
        # print("remote_tool:", remote_tool)
        api_client.update_tool(target_project_id, remote_tool_id, local_tool)
        console.print(f"[green]✓[/green] Updated tool {tool_name} in project {target_project_id}")


def _resolve_tool_references(local_tool: Dict[str, Any], api_client: APIClient, target_project_id: str) -> Dict[str, Any]:
    if(local_tool.get("config", {}).get("dataSourceId")):
        ds_id = api_client.get_datasource_by_short_name(target_project_id, local_tool.get("config", {}).get("dataSourceId")).get("id")
        local_tool["config"]["dataSourceId"] = ds_id
    return local_tool

def push_datasource(api_client: APIClient, target_project_id: str, datasource_name: str) -> None:
    """Push a datasource to the Canvas platform."""

    local_path_yaml = Path("datasources") / f"{datasource_name}" / "datasource.yaml"
    local_ds = None
    if local_path_yaml.exists():
        with open(local_path_yaml, 'r') as f:
            local_ds = _resolve_protected_references(yaml.safe_load(f) or {}, api_client, type="datasource")
    else:
        console.print(f"[yellow]•[/yellow] Skipping datasource {datasource_name}: no local config")
        return

    remote_ds = None
    try:
        remote_ds_id = api_client.get_datasource_by_short_name(target_project_id, datasource_name).get("id")
        remote_ds = pull_datasources([remote_ds_id], target_project_id, api_client, write_to_file=False)[1][0]
        # print("remote_ds:", remote_ds)
    except APIError:
        remote_ds = None

    if remote_ds is None:
        if local_ds is None:
            console.print(f"[yellow]•[/yellow] Skipping datasource {datasource_name}: no local config and not found remotely")
            return
        # print("created local_ds:", local_ds)
        api_client.create_datasource(target_project_id, local_ds, datasource_name)
        console.print(f"[green]✓[/green] Created datasource {datasource_name} in project {target_project_id}")
        return

    if local_ds is not None and _normalize_config(remote_ds) != _normalize_config(local_ds):
        # print("updated local_ds:", local_ds)
        # print("remote_ds:", remote_ds)
        api_client.update_datasource(target_project_id, remote_ds_id, local_ds)
        console.print(f"[green]✓[/green] Updated datasource {datasource_name} in project {target_project_id}")





def _resolve_protected_references(data: Dict[str, Any], api_client: APIClient, type: str) -> Dict[str, Any]:
    for key, value in data.get("config", {}).items():
        if(value.startswith("env.")):
            data["config"][key] = os.getenv(value.split(".")[1])
            print(f"{key}={data["config"][key]}")
    return data


def _load_env_from_environments_dir(target_project: str) -> None:
    env_dir_path = Path("environments") / f"{target_project}.env"
    if not env_dir_path.exists():
        return
    values = dotenv_values(env_dir_path)
    for key, value in values.items():
        if value is None:
            continue
        if key not in os.environ:
            os.environ[key] = value
