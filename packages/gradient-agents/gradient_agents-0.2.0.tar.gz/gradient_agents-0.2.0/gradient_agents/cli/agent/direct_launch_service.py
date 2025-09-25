"""Direct FastAPI launch service implementation."""

from __future__ import annotations
import importlib
import sys
from pathlib import Path
import subprocess
import shlex
import os
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
            # typer.echo("🔧 Running in development mode with auto-reload...")
            self._start_dev_server(agent_name, entrypoint_file, host, port)
        else:
            typer.echo("🚀 Running in production mode...")
            self._import_entrypoint_module(entrypoint_file)
            self._start_server(agent_name, entrypoint_file, host, port)

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
        """(Retained for backwards compatibility) Validate the module can be imported.

        NOTE: We no longer rely on importing the module in-process before starting uvicorn,
        because that breaks relative imports for users whose agent code expects to be
        imported as part of a package. This method now performs a lightweight best-effort
        check but will not be fatal if validation cannot be completed; uvicorn subprocess
        will surface runtime errors with accurate import context.
        """
        try:
            current_dir = str(Path.cwd())
            if current_dir not in sys.path:
                sys.path.insert(0, current_dir)

            module_name = (
                entrypoint_file.replace(".py", "").replace("/", ".").replace("\\", ".")
            )
            module = importlib.import_module(module_name)
            if not hasattr(module, "app"):
                # Soft warning only; user will see clearer error from uvicorn
                typer.echo(
                    "⚠️  Warning: module has no 'app' attribute yet. Ensure @entrypoint is applied."
                )
        except Exception:
            # Suppress to allow uvicorn to attempt import in correct package context
            pass

    def _build_module_target(self, entrypoint_file: str) -> str:
        """Derive the uvicorn module:app target supporting package contexts.

        If the entrypoint file is inside a package (any parent with __init__.py), we build the
        dotted path relative to the nearest ancestor that is NOT a package root (i.e., stop when
        no __init__.py). Otherwise we fall back to simple filename without directories.
        """
        path = Path(entrypoint_file).resolve()
        if not path.exists():
            return entrypoint_file.replace(".py", "") + ":app"

        parts = []
        current = path.parent
        # Collect package parts while __init__.py exists
        while current != current.parent and (current / "__init__.py").exists():
            parts.append(current.name)
            current = current.parent

        parts.reverse()
        parts.append(path.stem)
        module_name = ".".join(parts) if parts else path.stem
        return f"{module_name}:app"

    def _start_server(
        self,
        agent_name: str,
        entrypoint_file: str,
        host: str = "0.0.0.0",
        port: int = 8080,
    ) -> None:
        """Start the FastAPI server via a uvicorn subprocess to preserve import semantics."""
        typer.echo(f"Starting {agent_name} server (subprocess)...")
        typer.echo(f"Server will be accessible at http://{host}:{port}")
        typer.echo("Press Ctrl+C to stop the server")

        app_target = self._build_module_target(entrypoint_file)
        typer.echo(f"🔍 Resolved app target: {app_target}")

        # Base command
        cmd = [
            sys.executable,
            "-m",
            "uvicorn",
            app_target,
            "--host",
            host,
            "--port",
            str(port),
            "--reload",
            "--reload-dir",
            str(Path.cwd()),
        ]

        # Exclusions not directly supported as flags; rely on uvicorn defaults.
        typer.echo("🛠  Launching uvicorn subprocess...")
        typer.echo(" ".join(shlex.quote(c) for c in cmd))

        # Environment: ensure current working dir is in PYTHONPATH
        env = dict(os.environ)  # type: ignore
        cwd = str(Path.cwd())
        existing = env.get("PYTHONPATH", "")
        if cwd not in existing.split(":"):
            env["PYTHONPATH"] = f"{cwd}:{existing}" if existing else cwd

        try:
            subprocess.run(cmd, env=env, check=True)
        except subprocess.CalledProcessError as e:
            typer.echo(f"❌ uvicorn exited with status {e.returncode}", err=True)
            raise typer.Exit(e.returncode)

    def _start_dev_server(
        self, agent_name: str, entrypoint_file: str, host: str, port: int
    ) -> None:
        """Start the server in development mode with auto-reload."""
        typer.echo(f"📂 Entrypoint: {entrypoint_file}")
        typer.echo(f"🌐 Server: http://{host}:{port}")
        typer.echo(f"🏷️  Agent: {agent_name}")
        typer.echo(f"🌐 Entrypoint endpoint: http://{host}:{port}/completions")
        typer.echo(
            "Auto-reload enabled - server will restart on any Python file changes"
        )
        typer.echo("Press Ctrl+C to stop the server\n")

        try:
            # Development mode still uses reload; same subprocess path
            self._start_server(agent_name, entrypoint_file, host, port)
        except KeyboardInterrupt:
            typer.echo("\n🛑 Server stopped by user")
        except subprocess.CalledProcessError as e:
            typer.echo(f"❌ Server failed to start: {e}", err=True)
            raise typer.Exit(e.returncode)
        except Exception as e:
            typer.echo(f"❌ Error starting development server: {e}", err=True)
            raise typer.Exit(1)

    def _show_import_help(self) -> None:
        """Show help for import errors."""
        typer.echo(
            "Please install the gradient-agents package and ensure imports are correct:",
            err=True,
        )
        typer.echo("  pip install gradient-agents", err=True)
        typer.echo("  from gradient_agents import entrypoint", err=True)

    def _show_entrypoint_example(self) -> None:
        """Show example of correct @entrypoint usage."""
        typer.echo("Please add the @entrypoint decorator to a function in this file:")
        typer.echo("Example:")
        typer.echo("  from gradient_agents import entrypoint")
        typer.echo("  ")
        typer.echo("  @entrypoint")
        typer.echo("  def main(query, context):")
        typer.echo("      return {'result': 'Hello World'}")
        typer.echo("  ")
        typer.echo(
            "  # The decorator automatically creates 'app' - no manual assignment needed!"
        )
        typer.echo("  # You can now run: uvicorn main:app")
        typer.echo("")
        typer.echo("Note: The entrypoint function must accept exactly 2 parameters")
