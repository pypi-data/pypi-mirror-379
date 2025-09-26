"""
Docker execution commands
"""

from typing import Optional
import typer
import json
from rich.console import Console

from ....shared.config import config
from ....shared.streaming import stream_execution_output

console = Console()


docker_app = typer.Typer(name="docker", help="Docker execution commands")


@docker_app.command("run")
def run_docker(
    image: str = typer.Argument(..., help="Docker image to run"),
    machine_type: str = typer.Option(
        "cpu", "--machine", "-m", help="Machine type (cpu, a100, h100, etc.)"
    ),
    timeout: int = typer.Option(
        300, "--timeout", "-t", help="Execution timeout in seconds"
    ),
    file_name: Optional[str] = typer.Option(
        None, "--file-name", "-f", help="Name for the execution"
    ),
    command: Optional[str] = typer.Option(
        None,
        "--command",
        "-c",
        help="Command to run in container (e.g., 'python app.py')",
    ),
    env: Optional[list[str]] = typer.Option(
        None, "--env", "-e", help="Environment variables (e.g., KEY=value)"
    ),
    callback_url: Optional[str] = typer.Option(
        None, "--callback", help="Webhook URL for completion notification"
    ),
    registry_creds: Optional[str] = typer.Option(
        None, "--registry-creds", help="Docker registry credentials as JSON string"
    ),
    registry_type: Optional[str] = typer.Option(
        None, "--registry-type", help="Registry credential type: basic, aws, etc."
    ),
):
    """Execute a Docker container on Lyceum Cloud"""
    client = config.get_client()

    try:
        # Parse environment variables
        docker_env = {}
        if env:
            for env_var in env:
                if "=" in env_var:
                    key, value = env_var.split("=", 1)
                    docker_env[key] = value
                else:
                    console.print(
                        f"[yellow]Warning: Ignoring invalid env var format: {env_var}[/yellow]")

        # Parse command - will be processed in the API request below

        # Parse registry credentials
        registry_credentials = None
        if registry_creds:
            try:
                registry_credentials = json.loads(registry_creds)
            except json.JSONDecodeError:
                console.print(
                    "[red]Error: Invalid JSON format for registry credentials[/red]"
                )
                raise typer.Exit(1)

        # Validate registry credentials and type
        if (registry_creds and not registry_type) or (
            registry_type and not registry_creds
        ):
            console.print(
                "[red]Error: Both --registry-creds and --registry-type must be provided together[/red]"
            )
            raise typer.Exit(1)

        # The v2 image API uses different endpoints and format
        import httpx

        # Build request for v2 image API
        image_request = {
            "docker_image_ref": image,
            "timeout": timeout,
            "execution_type": machine_type,
        }

        if command:
            image_request["docker_run_cmd"] = command.split()
        if file_name:
            image_request["file_name"] = file_name
        if env:
            image_request["docker_run_env"] = " ".join(env)

        # Handle registry credentials
        if registry_type and registry_credentials:
            image_request["docker_registry_credential_type"] = registry_type

            if registry_type == "aws":
                creds = json.loads(registry_credentials)
                image_request.update(
                    {
                        "aws_access_key_id": creds.get("aws_access_key_id"),
                        "aws_secret_access_key": creds.get("aws_secret_access_key"),
                        "aws_session_token": creds.get("aws_session_token"),
                        "aws_region": creds.get(
                            "region",
                            "us-east-1"),
                    })
            elif registry_type == "basic":
                creds = json.loads(registry_credentials)
                image_request.update(
                    {
                        "docker_username": creds.get("username"),
                        "docker_password": creds.get("password"),
                    }
                )

        # Call the v2 image endpoint directly
        with httpx.Client() as http_client:
            response = http_client.post(
                f"{config.base_url}/api/v2/external/execution/image/start",
                json=image_request,
                headers={"Authorization": f"Bearer {config.api_key}"},
                timeout=30.0,
            )

            if response.status_code != 200:
                console.print(f"[red]Error: HTTP {response.status_code}[/red]")
                if response.content:
                    console.print(f"[red]{response.content.decode()}[/red]")
                raise typer.Exit(1)

            result = response.json()
            execution_id = result.get("execution_id")
            streaming_url = result.get("streaming_url")

            console.print(
                f"[green]✅ Docker execution started: {execution_id}[/green]")
            console.print(f"[dim]Image: {image}[/dim]")
            console.print(f"[dim]Streaming URL: {streaming_url}[/dim]")
            console.print(
                f"[dim]Status: {
                    result.get(
                        'status',
                        'unknown')}[/dim]")

        # Stream the execution output using the streaming URL from the response
        success = stream_execution_output(execution_id, client, streaming_url)

        if not success:
            console.print(
                "[yellow]💡 You can check the execution later with: lyceum status[/yellow]"
            )
            raise typer.Exit(1)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@docker_app.command("registry-examples")
def show_registry_examples():
    """Show examples of Docker registry credential formats"""
    console.print(
        "[bold cyan]Docker Registry Credential Examples[/bold cyan]\n")

    console.print("[bold]1. Docker Hub (basic)[/bold]")
    console.print("Type: [green]basic[/green]")
    console.print(
        'Credentials: [yellow]\'{"username": "myuser", "password": "mypassword"}\'[/yellow]\n'
    )

    console.print("[bold]2. AWS ECR (aws)[/bold]")
    console.print("Type: [green]aws[/green]")
    console.print(
        'Credentials: [yellow]\'{"region": "us-west-2", "aws_access_key_id": "AKIAI...", "aws_secret_access_key": "wJalrX...", "session_token": "optional..."}\'[/yellow]\n'
    )

    console.print("[bold]3. Private Registry (basic)[/bold]")
    console.print("Type: [green]basic[/green]")
    console.print(
        'Credentials: [yellow]\'{"username": "admin", "password": "secret"}\'[/yellow]\n'
    )

    console.print("[bold]Example Commands:[/bold]")
    console.print("# Docker Hub:")
    console.print(
        '[dim]lyceum docker run myuser/myapp:latest --registry-type basic --registry-creds \'{"username": "myuser", "password": "mytoken"}\'[/dim]'
    )
    console.print("\n# AWS ECR:")
    console.print(
        '[dim]lyceum docker run 123456789012.dkr.ecr.us-west-2.amazonaws.com/myapp:latest --registry-type aws --registry-creds \'{"region": "us-west-2", "aws_access_key_id": "AKIAI...", "aws_secret_access_key": "wJalrX..."}\'[/dim]'
    )
    console.print("\n# Private Registry:")
    console.print(
        '[dim]lyceum docker run myregistry.com/myapp:latest --registry-type basic --registry-creds \'{"username": "admin", "password": "secret"}\'[/dim]'
    )
