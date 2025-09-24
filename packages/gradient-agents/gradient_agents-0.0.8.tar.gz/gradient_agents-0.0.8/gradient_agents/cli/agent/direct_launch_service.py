"""Direct FastAPI launch service implementation."""

from __future__ import annotations
import importlib
import sys
from pathlib import Path
import typer
import yaml

from .launch_service import LaunchService


class DirectLaunchService(LaunchService):
    """Direct FastAPI implementation of launch service."""

    def __init__(self):
        self.config_dir = Path.cwd() / ".gradient"
        self.config_file = self.config_dir / "agent.yml"

    def launch_locally(
        self, dev_mode: bool = False, host: str = "0.0.0.0", port: int = 8080
    ) -> None:
        """Launch the agent locally using FastAPI server."""
        config = self._load_config()
        entrypoint_file = config.get("entrypoint_file")
        agent_name = config.get("agent_name", "gradient-agent")

        if not entrypoint_file:
            typer.echo(
                "Error: No entrypoint file specified in configuration.", err=True
            )
            raise typer.Exit(1)

        self._validate_entrypoint_file(entrypoint_file)

        if dev_mode:
            typer.echo("🔧 Running in development mode with auto-reload...")
            self._start_dev_server(agent_name, entrypoint_file, host, port)
        else:
            typer.echo("🚀 Running in production mode...")
            self._import_entrypoint_module(entrypoint_file)
            self._start_server(agent_name, host, port)

    def _load_config(self) -> dict:
        """Load agent configuration from YAML file."""
        if not self.config_file.exists():
            typer.echo("Error: No agent configuration found.", err=True)
            typer.echo(
                "Please run 'gradient agent init' first to set up your agent.", err=True
            )
            raise typer.Exit(1)

        try:
            with open(self.config_file, "r") as f:
                return yaml.safe_load(f)
        except Exception as e:
            typer.echo(f"Error reading agent configuration: {e}", err=True)
            raise typer.Exit(1)

    def _validate_entrypoint_file(self, entrypoint_file: str) -> None:
        """Validate that the entrypoint file exists."""
        entrypoint_path = Path.cwd() / entrypoint_file
        if not entrypoint_path.exists():
            typer.echo(
                f"Error: Entrypoint file '{entrypoint_file}' does not exist.",
                err=True,
            )
            raise typer.Exit(1)

    def _import_entrypoint_module(self, entrypoint_file: str) -> None:
        """Import the entrypoint module to register the @entrypoint function."""
        try:
            current_dir = str(Path.cwd())
            if current_dir not in sys.path:
                sys.path.insert(0, current_dir)

            module_name = (
                entrypoint_file.replace(".py", "").replace("/", ".").replace("\\", ".")
            )
            typer.echo(f"Importing module: {module_name}")
            importlib.import_module(module_name)

        except ImportError as e:
            error_msg = str(e)
            typer.echo(
                f"Error: Error importing entrypoint module '{entrypoint_file}': {error_msg}",
                err=True,
            )
            self._show_import_help()
            raise typer.Exit(1)

    def _start_server(
        self, agent_name: str, host: str = "0.0.0.0", port: int = 8080
    ) -> None:
        """Start the FastAPI server."""
        typer.echo(f"Starting {agent_name} server...")
        typer.echo(f"Server will be accessible at http://{host}:{port}")
        typer.echo("Press Ctrl+C to stop the server")

        try:
            from gradient_agents import run_server

            run_server(host=host, port=port)
        except ImportError:
            typer.echo(
                "Error: gradient_agents package not found.",
                err=True,
            )
            typer.echo(
                "Please install it with: pip install gradient-agents",
                err=True,
            )
            raise typer.Exit(1)

    def _start_dev_server(
        self, agent_name: str, entrypoint_file: str, host: str, port: int
    ) -> None:
        """Start the server in development mode with auto-reload."""
        import subprocess
        import sys
        import os

        typer.echo(f"📂 Watching: {entrypoint_file}")
        typer.echo(f"🌐 Server: http://{host}:{port}")
        typer.echo(f"🏷️  Agent: {agent_name}")
        typer.echo(f"Entrypoint endpoint: http://{host}:{port}/completions")
        typer.echo("Auto-reload enabled - server will restart on file changes")
        typer.echo("Press Ctrl+C to stop the server\n")

        try:
            # Use uvicorn with reload for development
            cmd = [
                sys.executable,
                "-m",
                "uvicorn",
                "gradient_agents.server:create_app",
                "--factory",
                "--host",
                host,
                "--port",
                str(port),
                "--reload",
                "--reload-dir",
                str(Path.cwd()),
                "--reload-include",
                "*.py",
            ]

            # Set environment variable for the entrypoint file
            env = os.environ.copy()
            env["GRADIENT_ENTRYPOINT_FILE"] = entrypoint_file

            subprocess.run(cmd, env=env)

        except KeyboardInterrupt:
            typer.echo("\n🛑 Server stopped by user")
        except subprocess.CalledProcessError as e:
            typer.echo(f"❌ Server failed to start: {e}", err=True)
            typer.echo("💡 Falling back to production mode...")
            self._import_entrypoint_module(entrypoint_file)
            self._start_server(agent_name, host, port)
        except Exception as e:
            typer.echo(f"❌ Error starting development server: {e}", err=True)
            typer.echo("💡 Falling back to production mode...")
            self._import_entrypoint_module(entrypoint_file)
            self._start_server(agent_name, host, port)

    def _show_import_help(self) -> None:
        """Show help for import errors."""
        typer.echo(
            "Please install the gradient-agents package and ensure imports are correct:",
            err=True,
        )
        typer.echo("  pip install gradient-agents", err=True)
        typer.echo("  from gradient_agents import entrypoint", err=True)
