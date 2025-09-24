"""Main CLI entry point for Raga Canvas CLI."""

import click
from rich.console import Console

from .commands.init import init
from .commands.login import login
from .commands.list import list_cmd
from .commands.push import push
from .commands.pull import pull
from .commands.deploy import deploy
from .commands.env import env_cmd
from .commands.set import set_group
from .utils.exceptions import CanvasError

console = Console()


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Raga Canvas CLI - Deploy and manage AI agents with ease."""
    ctx.ensure_object(dict)


# Register commands
cli.add_command(init)
cli.add_command(login)
cli.add_command(list_cmd, name="list")
cli.add_command(push)
cli.add_command(pull)
cli.add_command(deploy)
cli.add_command(env_cmd, name="env")
cli.add_command(set_group, name="set")

def main() -> None:
    """Main entry point."""
    try:
        cli()
    except CanvasError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")
        raise click.Abort()


if __name__ == "__main__":
    main()
