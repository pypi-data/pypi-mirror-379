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
        """Derive the uvicorn module:app target with robust fallbacks.

        Strategy:
          1. If path doesn't exist, return naive file-based target.
          2. Build potential dotted module paths based on package ancestors (dirs with __init__.py).
          3. If directory name equals file stem (example_agent/example_agent.py) and directory is
             NOT a package yet (no __init__.py), prefer plain stem first.
          4. Probe candidates by attempting import (without executing user code deeply—normal import).
          5. Return first importable candidate; else fall back to plain stem.
        """
        path = Path(entrypoint_file).resolve()
        if not path.exists():
            return entrypoint_file.replace(".py", "") + ":app"

        file_stem = path.stem
        parent = path.parent

        # Discover package chain upwards
        package_chain = []
        cur = parent
        while cur != cur.parent and (cur / "__init__.py").exists():
            package_chain.append(cur.name)
            cur = cur.parent
        package_chain.reverse()

        candidates = []

        if package_chain:
            # Standard package path
            candidates.append(".".join(package_chain + [file_stem]))
        else:
            # Not inside a package chain
            candidates.append(file_stem)
            # If parent dir name differs and might be intended as a package (user forgot __init__.py)
            if parent.name != file_stem and parent != Path.cwd():
                candidates.append(f"{parent.name}.{file_stem}")
            # If names match (dir/file same) and user later adds __init__.py we still want single segment
            # but also consider doubled for completeness (will usually fail fast)
            if parent.name == file_stem:
                candidates.append(f"{file_stem}.{file_stem}")

        # Deduplicate preserving order
        seen = set()
        unique_candidates = []
        for c in candidates:
            if c not in seen:
                seen.add(c)
                unique_candidates.append(c)

        # Probe importability
        for mod in unique_candidates:
            try:
                importlib.import_module(mod)
                return f"{mod}:app"
            except Exception:
                continue

        # Fallback to simplest
        return f"{file_stem}:app"

    def _start_server(
        self,
        agent_name: str,
        entrypoint_file: str,
        host: str = "0.0.0.0",
        port: int = 8080,
    ) -> None:
        """Start the FastAPI server via a uvicorn subprocess to preserve import semantics."""
        typer.echo(f"Starting {agent_name} server...")
        typer.echo(f"Server will be accessible at http://{host}:{port}")
        typer.echo("Press Ctrl+C to stop the server")

        app_target = self._build_module_target(entrypoint_file)
        # typer.echo(f" Resolved app target: {app_target}")

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
        # typer.echo("🛠  Launching uvicorn subprocess...")
        # typer.echo(" ".join(shlex.quote(c) for c in cmd))

        # Environment: ensure correct root directory for package import is in PYTHONPATH
        env = dict(os.environ)  # type: ignore
        entry_path = Path(entrypoint_file).resolve()

        # Determine package root (first directory going up that is NOT a package)
        pkg_parent = entry_path.parent
        while (pkg_parent / "__init__.py").exists() and pkg_parent != pkg_parent.parent:
            pkg_parent = pkg_parent.parent

        # The directory to add is the last directory before we broke the loop *if* the entrypoint
        # resides within at least one package level; otherwise use current working directory.
        # Recompute by walking again to find topmost package dir.
        top_package_dir = entry_path.parent
        while (
            top_package_dir.parent / "__init__.py"
        ).exists() and top_package_dir.parent != top_package_dir.parent.parent:
            top_package_dir = top_package_dir.parent

        if (top_package_dir / "__init__.py").exists():
            # Add parent of the topmost package directory
            sys_path_root = top_package_dir.parent
        else:
            # Not inside a package chain; just use CWD
            sys_path_root = Path.cwd()

        existing = env.get("PYTHONPATH", "")
        existing_parts = [p for p in existing.split(":") if p]
        if str(sys_path_root) not in existing_parts:
            new_parts = [str(sys_path_root)] + existing_parts
            env["PYTHONPATH"] = ":".join(new_parts)

        # Also ensure CWD is present (for non-package local imports)
        if str(Path.cwd()) not in env.get("PYTHONPATH", "").split(":"):
            env["PYTHONPATH"] = (
                f"{env['PYTHONPATH']}:{Path.cwd()}"
                if env.get("PYTHONPATH")
                else str(Path.cwd())
            )

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
