"""Pull command for downloading resources from Canvas platform."""
import os
import yaml
import requests
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from ..utils.config import ConfigManager
from ..utils.exceptions import APIError, FileSystemError
from ..services.api_client import APIClient
from ..utils.helpers import _resolve_project_id, _resolve_local_item_id
from ..commands.init import _create_project_config_file
from ..utils.helpers import convert_tool_obj_to_tool_data, convert_datasource_obj_to_datasource_data, convert_agent_obj_to_agent_data
from dotenv import dotenv_values

console = Console()



@click.group(name="pull")
def pull() -> None:
    """Pull Canvas resources (agents, tools, datasources, etc.)."""
    pass


@pull.command(name="projects")
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def pull_projects(profile: Optional[str]) -> None:
    """Pull projects into project_config.yaml."""
    try:
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()

        api_client = APIClient(user_profile)
        projects = api_client.list_projects()
        if not projects:
            console.print("[yellow]No projects found.[/yellow]")
            return  
        _create_project_config_file(Path.cwd(), projects)
        _create_env_files(Path("environments"), projects)
        console.print("[green]✓[/green] Pulled projects into project_config.yaml")
    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except FileSystemError as e:
        console.print(f"[red]File Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()



@pull.command(name="agents")
@click.option(
    "--agent",
    help="Agent short name or id to pull (pulls all agents if omitted)"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def pull_agents_command(agent: Optional[str], profile: Optional[str]) -> None:
    """Pull agent(s) along with required tools, datasources, and knowledge-bases.

    Examples:
      canvas pull agents --project=<shortName>
      canvas pull agents --project=<shortName> --agent=<agent-short-name-or-id>
    """
    try:
        # Get profile and API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()

        api_client = APIClient(user_profile)
        project = config_manager.get_default_project()
        existing_env_vars = load_env_from_environments_dir(project)
        project_id = _resolve_project_id(project)
        if not project_id:
            console.print("[red]No project found. Run 'canvas init' first.[/red]")
            raise click.Abort()
        # Validate workspace root (create dirs if needed)
        if not Path("agents").exists():
            print("agents directory not found. Run 'canvas init' first.")
        if not Path("tools").exists():
            print("tools directory not found. Run 'canvas init' first.")
        if not Path("datasources").exists():
            print("datasources directory not found. Run 'canvas init' first.")

        # Resolve which agents to pull
        agents_to_pull = []
        if agent:
            try:    
                agents_to_pull = [api_client.get_agent_by_short_name(project_id, agent).get("id")]
            except APIError:
                console.print(f"[yellow]•[/yellow] Agent not found or inaccessible: {agent}")
                return
        else:
            agents_to_pull = [agent_item.get("id") for agent_item in api_client.list_agents(project_id)]
        print("agents_to_pull:", agents_to_pull)
        if len(agents_to_pull) == 0:
            console.print("[yellow]No agents resolved to pull.[/yellow]")
            return
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            t = progress.add_task("Pulling agents...", total=None)
            pull_agents(agents_to_pull, project_id, api_client, write_to_file=True, existing_env_vars=existing_env_vars)
            _write_env_file(project, existing_env_vars)
            progress.update(t, description="Pull complete")

        console.print("\n[blue]Done.[/blue]")

    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except FileSystemError as e:
        console.print(f"[red]File Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()




@pull.command(name="tools")
@click.option(
    "--tool",
    help="Tool short name or id to pull (pulls all tools if omitted)"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def pull_tools_command(tool: Optional[str], profile: Optional[str]) -> None:
    """Pull tools into <project>/tools/<id> with tool.yaml and config.yaml."""
    try:
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()

        api_client = APIClient(user_profile)
        project = config_manager.get_default_project()
        project_id = _resolve_project_id(project)
        existing_env_vars = load_env_from_environments_dir(project)
        if not project_id:
            console.print("[red]No project found. Run 'canvas init' first.[/red]")
            raise click.Abort()
        Path("tools").mkdir(parents=True, exist_ok=True)
        tools_to_pull = []
        if tool:
            try:
                tools_to_pull = [api_client.get_tool_by_short_name(project_id, tool).get("id")]
            except APIError:
                console.print(f"[yellow]•[/yellow] Tool not found or inaccessible: {tool}")
                return
        else:
            tools_list = api_client.list_tools(project_id=project_id)
            tools_to_pull = [tool_item.get("id") for tool_item in tools_list]


        if len(tools_to_pull) == 0:
            console.print("[yellow]No tools found.[/yellow]")
            return

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            t = progress.add_task("Pulling tools...", total=None)
            pull_tools(tools_to_pull, project_id, api_client, write_to_file=True, existing_env_vars=existing_env_vars)
            _write_env_file(project, existing_env_vars)
            progress.update(t, description="Pull complete")

        console.print("\n[blue]Done.[/blue]")

    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except FileSystemError as e:
        console.print(f"[red]File Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()




@pull.command(name="datasources")
@click.option(
    "--datasource",
    help="Datasource short name or id to pull (pulls all datasources if omitted)"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def pull_datasources_command(datasource: Optional[str], profile: Optional[str]) -> None:
    """Pull datasources into <project>/datasources/<id> with datasource.yaml and config.yaml."""
    try:
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)
        if not user_profile:
            console.print("[red]No authentication profile found. Run 'canvas login' first.[/red]")
            raise click.Abort()

        api_client = APIClient(user_profile)
        project = config_manager.get_default_project()
        existing_env_vars = load_env_from_environments_dir(project)
        project_id = _resolve_project_id(project)
        if not project_id:
            console.print("[red]No project found. Run 'canvas init' first.[/red]")
            raise click.Abort()
        Path("datasources").mkdir(parents=True, exist_ok=True)


        datasources_to_pull = []
        if datasource:
            try:
                datasources_to_pull = [api_client.get_datasource_by_short_name(project_id, datasource).get("id")]
            except APIError:
                console.print(f"[yellow]•[/yellow] Datasource not found or inaccessible: {datasource}")
                return
        else:
            datasources_list = api_client.list_datasources(project_id=project_id)
            datasources_to_pull = [datasource_item.get("id") for datasource_item in datasources_list]

        if len(datasources_to_pull) == 0:
            console.print("[yellow]No datasources found.[/yellow]")
            return

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            t = progress.add_task("Pulling datasources...", total=None)
            pull_datasources(datasources_to_pull, project_id, api_client, write_to_file=True, existing_env_vars=existing_env_vars)
            _write_env_file(project, existing_env_vars)
            progress.update(t, description="Pull complete")

        console.print("\n[blue]Done.[/blue]")

    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except FileSystemError as e:
        console.print(f"[red]File Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()


def pull_agents(agent_ids: List[str], project_id: str, api_client: APIClient, write_to_file: bool = True, existing_env_vars: Optional[Dict[str, Any]] = None) -> Tuple[List[str], List[Dict[str, Any]]]:
    agent_names = []
    agent_datas = []
    for agent_id in agent_ids:
        # Save agent.yaml
        agent_obj = _safe_get_agent(api_client, project_id, agent_id)
        if not agent_obj:
            console.print(f"[yellow]•[/yellow] Agent not found or inaccessible: {agent_id}")
            continue
        agent_data = convert_agent_obj_to_agent_data(agent_obj)

        # Pull required subagents
        subagent_ids = _extract_subagent_ids(agent_data.get("subAgents", []))
        print("subagent_ids:", subagent_ids)
        subagent_names, subagent_datas = pull_agents(subagent_ids, project_id, api_client, write_to_file=write_to_file, existing_env_vars=existing_env_vars)
        agent_data["subAgents"] = subagent_names
        # Pull required tools
        tool_ids = _extract_tool_ids(agent_data.get("tools", []))
        tool_short_names, tool_datas = pull_tools(tool_ids, project_id, api_client, write_to_file=write_to_file, existing_env_vars=existing_env_vars)
        agent_data["tools"] = tool_short_names
        # Pull required datasources
        ds_id = agent_data.get("tracingConfigId", "")
        if ds_id:
            ds_names, ds_datas = pull_datasources([ds_id], project_id, api_client, write_to_file=write_to_file, existing_env_vars=existing_env_vars)
            agent_data["tracingConfigId"] = ds_names[0]

        agent_names.append(agent_obj.get("shortName"))
        agent_datas.append(agent_data)
        if(write_to_file):
            agent_dir = Path("agents") / agent_obj.get("shortName")
            agent_dir.mkdir(parents=True, exist_ok=True)
            _write_yaml(agent_dir / "agent.yaml", agent_data)
            _write_yaml(agent_dir / "config.yaml", {"id": agent_id, "name": agent_obj.get("name")})
            console.print(f"[green]✓[/green] Saved agent: {agent_dir / 'agent.yaml'}")

    return agent_names, agent_datas


    
def pull_tools(tool_ids: List[str], project_id: str, api_client: APIClient, write_to_file: bool = True, existing_env_vars: Optional[Dict[str, Any]] = None) -> Tuple[List[str], List[Dict[str, Any]]]:
    """Pull tools into <project>/tools/<id> with tool.yaml and config.yaml."""
    tool_names = []
    tool_datas = []
    for tool_id in tool_ids:
        tool_obj = _safe_get_tool(api_client, project_id, tool_id)
        if not tool_obj:
            console.print(f"[yellow]•[/yellow] Tool not found or inaccessible: {tool_id}")
            continue
        tool_data = convert_tool_obj_to_tool_data(tool_obj)
        tool_short_name = tool_obj.get("shortName")

        # Pull required datasources
        if(tool_data.get("config",{}).get("dataSourceId")):
            ds_names, ds_datas = pull_datasources([tool_data.get("config",{}).get("dataSourceId")], project_id, api_client, write_to_file=write_to_file, existing_env_vars=existing_env_vars)
            if(len(ds_names) > 0):
                tool_data["config"]["dataSourceId"] = ds_names[0]
            else:
                console.print(f"[yellow]•[/yellow] Datasource not found or inaccessible: {tool_data.get('config',{}).get('dataSourceId')}. Resolve the datasource to pull the tool {tool_short_name} successfully.")
                continue
        tool_datas.append(tool_data)
        tool_names.append(tool_short_name)
        if(write_to_file):
            tool_dir = Path("tools") / f"{tool_short_name}"
            tool_dir.mkdir(parents=True, exist_ok=True)
            _write_yaml(tool_dir / "tool.yaml", _resolve_protected_references(tool_data, api_client, type="tool", existing_env_vars=existing_env_vars))
            _write_yaml(tool_dir / "config.yaml", {"id": tool_id, "name": tool_obj.get("name")})
            console.print(f"[green]✓[/green] Saved tool: {tool_dir / 'tool.yaml'}")

    return tool_names, tool_datas



def pull_datasources(datasource_ids: List[str], project_id: str, api_client: APIClient, write_to_file: bool = True, existing_env_vars: Optional[Dict[str, Any]] = None) -> Tuple[List[str], List[Dict[str, Any]]]:
    """Pull datasources into <project>/datasources/<id> with datasource.yaml and config.yaml."""
    ds_names = []
    ds_datas = []
    for datasource_id in datasource_ids:
        ds_obj = _safe_get_datasource(api_client, project_id, datasource_id)
        if not ds_obj:
            console.print(f"[yellow]•[/yellow] Datasource not found or inaccessible: {datasource_id}.")
            continue
        ds_short_name = ds_obj.get("shortName")
        ds_data = convert_datasource_obj_to_datasource_data(ds_obj)
        ds_names.append(ds_short_name)
        ds_datas.append(ds_data)
        if(write_to_file):
            ds_dir = Path("datasources") / f"{ds_short_name}"
            ds_dir.mkdir(parents=True, exist_ok=True)
            _write_yaml(ds_dir / "datasource.yaml", _resolve_protected_references(ds_data, api_client, type="datasource", existing_env_vars=existing_env_vars))
            _write_yaml(ds_dir / "config.yaml", {"id": ds_obj.get("id"), "name": ds_obj.get("name")})
            console.print(f"[green]✓[/green] Saved datasource: {ds_dir / 'datasource.yaml'}")

    return ds_names, ds_datas


def _resolve_protected_references(
    data: Dict[str, Any],
    api_client: APIClient,
    type: str,
    existing_env_vars: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    if existing_env_vars is None:
        existing_env_vars = {}
    templates = []
    if(type == "tool"):
        templates = api_client.list_tool_templates()
    elif(type == "datasource"):
        templates = api_client.list_datasource_templates()
    for template in templates:
        if template.get("type") == data.get("type"):
            config_schemas = template.get("configSchema", {})
            for config_schema in config_schemas:
                if(config_schema.get("isEnvSpecific") == True):
                    raw_key = f"{data.get('name', '')}_{config_schema.get('fieldName')}"
                    env_key = raw_key.upper().replace(" ", "_")
                    existing_env_vars[env_key] = data["config"][config_schema.get("fieldName")]
                    print(f"{env_key}={data["config"][config_schema.get("fieldName")]}")
                    data["config"][config_schema.get("fieldName")] = "env." + env_key
    return data

def _safe_get_agent(api: APIClient, project_id: str, agent_id: str) -> Optional[Dict[str, Any]]:
    try:
        return api.get_agent(project_id, agent_id)
    except Exception:
        return None


def _safe_get_tool(api: APIClient, project_id: str, tool_id: str) -> Optional[Dict[str, Any]]:
    try:
        return api.get_tool(project_id, tool_id)
    except Exception:
        return None


def _safe_get_datasource(api: APIClient, project_id: str, ds_id: str) -> Optional[Dict[str, Any]]:
    try:
        return api.get_datasource(project_id, ds_id)
    except Exception:
        return None

def _extract_subagent_ids(subagents: List[Dict[str, Any]]) -> List[str]:
    """Extract a list of tool ids from a list of tools."""
    subagent_ids = []
    for subagent in subagents:
        subagent_ids.append(subagent.get("agentId"))
    return subagent_ids

def _extract_tool_ids(tools: List[Dict[str, Any]]) -> List[str]:
    """Extract a list of tool ids from a list of tools."""
    tool_ids = []
    for tool in tools:
        tool_ids.append(tool.get("toolId"))
    return tool_ids

def _write_yaml(path: Path, data: Dict[str, Any]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)
    except Exception as e:
        raise FileSystemError(f"Failed to write file {path}: {e}")
    

def load_env_from_environments_dir(project: str) -> Dict[str, Any]:
    env_file_path = Path("environments") / f"{project}.env"
    if not env_file_path.exists():
        return {}
    values = dotenv_values(env_file_path)
    return values


def _write_env_file(project: str, existing_env_vars: Dict[str, Any]) -> None:
    env_file_path = Path("environments") / f"{project}.env"
    env_file_path.parent.mkdir(parents=True, exist_ok=True)
    env_file_path.touch(exist_ok=True)
    with open(env_file_path, "w") as f:
        for key, value in existing_env_vars.items():
            f.write(f"{key}={value}\n")

def _create_env_files(base_path: Path, projects: list) -> None:
    """Create a per-project env file with id, name, and selected project.config fields."""
    try:
        for project in projects:
            env_file_path = base_path / f"{project.get('shortName')}.env"
            env_file_path.parent.mkdir(parents=True, exist_ok=True)
            env_file_path.touch(exist_ok=True)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()