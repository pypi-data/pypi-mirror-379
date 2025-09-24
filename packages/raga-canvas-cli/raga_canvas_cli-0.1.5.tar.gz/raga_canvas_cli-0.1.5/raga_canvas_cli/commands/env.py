import click
from pathlib import Path
import os
from typing import Dict
from dotenv import dotenv_values

@click.group(name="env")
def env_cmd() -> None:
    """Manage environment variables for Canvas projects."""
    pass


@env_cmd.command(name="set")
@click.option(
    "--override/--no-override",
    default=True,
    help="Override existing environment variables with values from .env files"
)
@click.option(
    "--environments-dir",
    default="environments",
    show_default=True,
    help="Directory containing .env files"
)
@click.option(
    "--profile",
    help="Profile to use for authentication"
)
def set_env(override: bool, environments_dir: str, profile: str = None) -> None:
    """Set environment variables from all .env files inside the environments folder."""
    env_dir_path = Path(environments_dir)
    if not env_dir_path.exists() or not env_dir_path.is_dir():
        print(f"{environments_dir} directory not found. Run 'canvas init' first.")
        raise click.Abort()
    
    # Collect all .env files (top-level) and sort for deterministic loading order
    dotenv_paths = sorted([p for p in env_dir_path.iterdir() if p.is_file() and p.suffix == ".env"], key=lambda p: p.name)
    if not dotenv_paths:
        print(f"No .env files found in {env_dir_path}")
        return
    
    added_count = 0
    updated_count = 0
    loaded_files: Dict[str, int] = {}
    
    for dotenv_path in dotenv_paths:
        values = dotenv_values(dotenv_path)
        loaded_files[dotenv_path.name] = 0
        for key, value in values.items():
            if value is None:
                continue
            if key in os.environ:
                if override:
                    os.environ[key] = value
                    updated_count += 1
                    loaded_files[dotenv_path.name] += 1
            else:
                os.environ[key] = value
                added_count += 1
                loaded_files[dotenv_path.name] += 1
    
    print("Loaded environment variables from the following files (in order):")
    for fname, count in loaded_files.items():
        print(f"- {fname}: {count} variables")
    print(f"Total variables added: {added_count}")
    print(f"Total variables updated: {updated_count}")
    
    # Note: variables are set for the current process and its children. To persist in your shell,
    # export them in your shell profile or use a tool like direnv.

# Provide 'set-env' as an alias for backward compatibility
env_cmd.add_command(set_env, name="set-env")