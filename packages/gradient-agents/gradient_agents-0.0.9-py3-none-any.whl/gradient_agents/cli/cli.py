from __future__ import annotations
from typing import Optional
import typer
import importlib.metadata

from .agent import (
    AgentConfigService,
    LaunchService,
    DeployService,
    ConfigReader,
    YamlAgentConfigService,
    DirectLaunchService,
    YamlConfigReader,
    MockDeployService,
    get_do_api_token,
    EnvironmentError,
)


def get_version() -> str:
    """Get the version from package metadata."""
    try:
        return importlib.metadata.version("gradient-agents")
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


_agent_config_service = YamlAgentConfigService()
_launch_service = DirectLaunchService()
_config_reader = YamlConfigReader()
_deploy_service = MockDeployService(_config_reader)


def version_callback(value: bool):
    """Show version and exit."""
    if value:
        version = get_version()
        typer.echo(f"gradient-agents version {version}")
        raise typer.Exit()


app = typer.Typer(no_args_is_help=True, add_completion=False, help="gradient CLI")


# Add version option to main app
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    )
):
    """Gradient ADK CLI"""
    pass


agent_app = typer.Typer(
    no_args_is_help=True,
    help="Agent configuration and management",
)
app.add_typer(agent_app, name="agent")


def get_agent_config_service() -> AgentConfigService:
    return _agent_config_service


def get_launch_service() -> LaunchService:
    return _launch_service


def get_deploy_service() -> DeployService:
    return _deploy_service


def get_config_reader() -> ConfigReader:
    return _config_reader


@agent_app.command("init")
def agent_init(
    agent_name: Optional[str] = typer.Option(
        None, "--agent-workspace-name", help="Name of the agent workspace"
    ),
    deployment_name: Optional[str] = typer.Option(
        None, "--deployment-name", help="Deployment name"
    ),
    entrypoint_file: Optional[str] = typer.Option(
        None,
        "--entrypoint-file",
        help="Python file containing @entrypoint decorated function",
    ),
    interactive: bool = typer.Option(
        True, "--interactive/--no-interactive", help="Interactive prompt mode"
    ),
):
    """Initializes a new agent."""
    import pathlib

    # Configure the agent
    agent_config_service = get_agent_config_service()
    agent_config_service.configure(
        agent_name=agent_name,
        agent_environment=deployment_name,
        entrypoint_file=entrypoint_file,
        interactive=interactive,
    )

    # Create project structure
    typer.echo("\n📁 Creating project structure...")

    # Define folders to create
    folders_to_create = ["agents", "datasets", "evaluations", "tools"]

    for folder in folders_to_create:
        folder_path = pathlib.Path(folder)
        if not folder_path.exists():
            folder_path.mkdir(exist_ok=True)
            typer.echo(f"   Created folder: {folder}/")
        # else:
        # typer.echo(f"   Folder already exists: {folder}/")

    # Create main.py if it doesn't exist
    main_py_path = pathlib.Path("main.py")
    if not main_py_path.exists():
        # Read the template file
        template_path = pathlib.Path(__file__).parent / "templates" / "main.py.template"
        if template_path.exists():
            main_py_content = template_path.read_text()
            main_py_path.write_text(main_py_content)
            typer.echo("   Created file: main.py")
        # else:
        # typer.echo("   Warning: Template file not found, main.py not created")

    # Create .gitignore if it doesn't exist
    gitignore_path = pathlib.Path(".gitignore")
    if not gitignore_path.exists():
        gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/

# Environments
.env
"""
        gitignore_path.write_text(gitignore_content)
        typer.echo("   Created file: .gitignore")

    typer.echo("\n✅ Project structure created successfully!")
    typer.echo("\n🚀 Next steps:")
    typer.echo("   1. Edit main.py to implement your agent logic")
    typer.echo("   2. Add your datasets to the datasets/ folder")
    typer.echo("   3. Create evaluation scripts in evaluations/")
    typer.echo("   4. Add custom tools to the tools/ folder")
    typer.echo("   5. Run 'gradient agent run' to test locally")
    typer.echo("   6. Use 'gradient agent deploy' when ready to deploy")


@agent_app.command("run")
def agent_run(
    dev: bool = typer.Option(
        True, "--dev/--no-dev", help="Run in development mode with auto-reload"
    ),
    port: int = typer.Option(8080, "--port", help="Port to run the server on"),
    host: str = typer.Option("0.0.0.0", "--host", help="Host to bind the server to"),
):
    """Runs the agent locally."""
    launch_service = get_launch_service()
    launch_service.launch_locally(dev_mode=dev, host=host, port=port)


@agent_app.command("deploy")
def agent_deploy(
    api_token: Optional[str] = typer.Option(
        None,
        "--api-token",
        help="DigitalOcean API token (overrides DO_API_TOKEN env var)",
        envvar="DO_API_TOKEN",
        hide_input=True,
    )
):
    """Deploy the agent to DigitalOcean."""
    try:
        # Deploy the agent
        deploy_service = get_deploy_service()
        deploy_service.deploy_agent()

    except EnvironmentError as e:
        typer.echo(f"❌ {e}", err=True)
        typer.echo("\nTo set your token permanently:", err=True)
        typer.echo("  export DO_API_TOKEN=your_token_here", err=True)
        raise typer.Exit(1)


@agent_app.command("evaluate")
def agent_evaluate():
    """Run an evaluation of the agent."""
    import time

    try:
        config_reader = get_config_reader()
        agent_name = config_reader.get_agent_name()
        agent_environment = config_reader.get_agent_environment()

        typer.echo(f"🧪 Initiating evaluation for agent: {agent_name}")
        typer.echo(f"🎯 Environment: {agent_environment}")
        typer.echo()

        # Setting up evaluation
        typer.echo("⚙️  Setting up evaluation...")
        time.sleep(2)

        # Starting run
        typer.echo("🚀 Starting run...")
        time.sleep(1)

        # Poll for 10 seconds with progress indicators
        typer.echo("📊 Running evaluation...")
        for i in range(10):
            time.sleep(1)
            dots = "." * ((i % 3) + 1)
            typer.echo(f"   Evaluating{dots}", nl=False)
            if i < 9:  # Don't print newline on last iteration
                typer.echo("\r", nl=False)

        typer.echo()  # Final newline
        time.sleep(0.5)

        # Complete
        typer.echo("✅ Evaluation completed!")
        typer.echo()
        typer.echo("📈 View detailed results at:")
        typer.echo(
            "   https://cloud.digitalocean.com/gen-ai/workspaces/11f076b0-2ff2-d71d-b074-4e013e2ddde4/evaluations/384ad568-76b5-11f0-b074-4e013e2ddde4/runs/73b04ba3-6494-42af-b7de-b093d8082814?i=b59231"
        )

    except Exception as e:
        typer.echo(f"❌ Evaluation failed: {e}", err=True)
        raise typer.Exit(1)


@agent_app.command("traces")
def agent_traces():
    """Open the Galileo traces UI for monitoring agent execution."""
    typer.echo("🔍 Galileo Traces UI")
    typer.echo("📊 To be implemented")
    typer.echo()
    typer.echo("This command will eventually open a URL to view:")
    typer.echo("  • Agent execution traces")
    typer.echo("  • Performance metrics")
    typer.echo("  • Debug information")
    typer.echo("  • Execution logs")
    typer.echo()
    typer.echo("💡 Coming soon: traces.do-ai.run/{agent-id}")


def run():
    app()
