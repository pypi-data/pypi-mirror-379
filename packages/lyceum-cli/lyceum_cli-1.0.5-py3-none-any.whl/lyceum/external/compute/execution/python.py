"""
Python execution commands
"""

from pathlib import Path
from typing import Optional
import typer
from rich.console import Console

from ....shared.config import config
from ....shared.streaming import stream_execution_output

console = Console()


python_app = typer.Typer(name="python", help="Python execution commands")


@python_app.command("run")
def run_python(
    code_or_file: str = typer.Argument(
        ..., help="Python code to execute or path to Python file"
    ),
    machine_type: str = typer.Option(
        "cpu", "--machine", "-m", help="Machine type (cpu, gpu)"
    ),
    file_name: Optional[str] = typer.Option(
        None, "--file-name", "-f", help="Name for the execution"
    ),
    requirements: Optional[str] = typer.Option(
        None,
        "--requirements",
        "-r",
        help="Requirements file path or pip requirements string",
    ),
    imports: Optional[list[str]] = typer.Option(
        None, "--import", help="Pre-import modules (can be used multiple times)"
    ),
):
    """Execute Python code or file on Lyceum Cloud"""
    # Validate machine type
    if machine_type not in ["cpu", "gpu"]:
        console.print(
            f"[red]Error: machine type must be 'cpu' or 'gpu', got '{machine_type}'[/red]")
        raise typer.Exit(1)

    client = config.get_client()

    try:
        # Check if it's a file path
        code_to_execute = code_or_file
        if Path(code_or_file).exists():
            console.print(f"[dim]Reading code from file: {code_or_file}[/dim]")
            with open(code_or_file, "r") as f:
                code_to_execute = f.read()
            # Use filename as execution name if not provided
            if not file_name:
                file_name = Path(code_or_file).name

        # Handle requirements
        requirements_content = None
        if requirements:
            # Check if it's a file path
            if Path(requirements).exists():
                console.print(
                    f"[dim]Reading requirements from file: {requirements}[/dim]")
                with open(requirements, "r") as f:
                    requirements_content = f.read()
            else:
                # Treat as direct pip requirements string
                requirements_content = requirements

        # The v2 streaming API uses different endpoints and format
        import httpx

        # Build request for v2 streaming API
        streaming_request = {
            "code": code_to_execute,
            "nbcode": 0,  # 0 for regular Python code, 1 for notebook code
            "execution_type": machine_type,
        }

        if file_name:
            streaming_request["file_name"] = file_name
        if requirements_content:
            streaming_request["requirements_content"] = requirements_content
        if imports:
            streaming_request["prior_imports"] = imports

        # Call the v2 streaming endpoint directly
        with httpx.Client() as http_client:
            response = http_client.post(
                f"{config.base_url}/api/v2/external/execution/streaming/start",
                json=streaming_request,
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
                f"[green]✅ Execution started: {execution_id}[/green]")
            console.print(f"[dim]Streaming URL: {streaming_url}[/dim]")
            console.print(
                f"[dim]Status: {
                    result.get(
                        'status',
                        'unknown')}[/dim]")

            if result.get("pythia_decision"):
                console.print(
                    f"[dim]Pythia recommendation: {
                        result['pythia_decision']}[/dim]")

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
