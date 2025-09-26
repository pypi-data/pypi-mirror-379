"""
Workload management commands: list jobs, abort, history
"""

import typer
from rich.console import Console

from ....shared.config import config
from ....shared.display import create_table, format_timestamp, truncate_id
from lyceum_cloud_execution_api_client.api.billing_credits import (
    get_execution_history_api_v2_external_billing_history_get,
)

console = Console()

workloads_app = typer.Typer(
    name="workloads",
    help="Workload management commands")


@workloads_app.command("list")
def list_jobs(
    limit: int = typer.Argument(10, help="Number of executions to show"),
):
    """List currently running executions"""
    try:
        # Use v2 API endpoint directly
        import httpx

        # Call the v2 workloads list endpoint
        with httpx.Client() as http_client:
            response = http_client.get(
                f"{config.base_url}/api/v2/external/workloads/list",
                headers={"Authorization": f"Bearer {config.api_key}"},
                timeout=30.0,
            )

            if response.status_code != 200:
                console.print(f"[red]Error: HTTP {response.status_code}[/red]")
                if response.content:
                    console.print(f"[red]{response.content.decode()}[/red]")
                raise typer.Exit(1)

            executions = response.json()
            if not isinstance(executions, list):
                executions = []

            # Apply limit
            executions = executions[:limit]

            if not executions:
                console.print("[dim]No running executions found[/dim]")
                return

            columns = [
                {"header": "ID", "style": "cyan", "no_wrap": True, "max_width": 12},
                {"header": "Status", "style": "yellow"},
                {"header": "File", "style": "magenta"},
                {"header": "Hardware", "style": "dim"},
                {"header": "Started", "style": "dim"},
            ]

            table = create_table("Running Executions", columns)

            for execution in executions:
                # Handle both JSON dict and object formats
                if isinstance(execution, dict):
                    execution_id = execution.get("execution_id", "N/A")
                    status = execution.get("status", "N/A")
                    file_name = execution.get("file_name", "N/A")
                    hardware_profile = execution.get("hardware_profile", "N/A")
                    created_at = execution.get("created_at", None)
                else:
                    execution_id = getattr(execution, "execution_id", "N/A")
                    status = getattr(execution, "status", "N/A")
                    file_name = getattr(execution, "file_name", "N/A")
                    hardware_profile = getattr(
                        execution, "hardware_profile", "N/A")
                    created_at = getattr(execution, "created_at", None)

                table.add_row(
                    truncate_id(execution_id, 8),
                    status,
                    file_name,
                    hardware_profile,
                    format_timestamp(created_at),
                )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@workloads_app.command("abort")
def abort(
    execution_id: str = typer.Argument(..., help="Execution ID to abort"),
):
    """Abort a running execution"""
    try:
        # Use v2 API endpoint directly
        import httpx

        # Call the v2 workloads abort endpoint
        with httpx.Client() as http_client:
            response = http_client.post(
                f"{config.base_url}/api/v2/external/workloads/abort/{execution_id}",
                headers={"Authorization": f"Bearer {config.api_key}"},
                timeout=30.0,
            )

            if response.status_code != 200:
                console.print(f"[red]Error: HTTP {response.status_code}[/red]")
                if response.content:
                    console.print(f"[red]{response.content.decode()}[/red]")
                raise typer.Exit(1)

            result = response.json()
            message = (
                result.get("message", "Execution aborted")
                if isinstance(result, dict)
                else "Execution aborted"
            )
            console.print(f"[green]✅ {message}[/green]")
            return

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@workloads_app.command("history")
def history(
    limit: int = typer.Argument(10, help="Number of executions to show"),
):
    """Show your execution history"""
    client = config.get_client()

    try:
        response = (
            get_execution_history_api_v2_external_billing_history_get.sync_detailed(
                client=client))

        if response.status_code != 200:
            console.print(f"[red]Error: HTTP {response.status_code}[/red]")
            raise typer.Exit(1)

        # Parse the response correctly - the API returns {"executions": [...],
        # "total_executions": N}
        if hasattr(response, "content"):
            import json

            try:
                data = json.loads(response.content)
                executions = (
                    data.get("executions", [])[:limit]
                    if isinstance(data, dict) and "executions" in data
                    else []
                )
            except Exception:
                executions = response.parsed[:limit] if response.parsed else []
        else:
            executions = response.parsed[:limit] if response.parsed else []

        if not executions:
            console.print("[dim]No execution history found[/dim]")
            return

        columns = [
            {"header": "ID", "style": "cyan", "no_wrap": True, "max_width": 12},
            {"header": "Status", "style": "green"},
            {"header": "File", "style": "yellow"},
            {"header": "Machine", "style": "magenta"},
            {"header": "Created", "style": "dim"},
        ]

        table = create_table("Execution History", columns)

        for execution in executions:
            # Handle both parsed objects and raw JSON dicts
            if isinstance(execution, dict):
                execution_id = execution.get("execution_id", "N/A")
                status = execution.get("status", "N/A")
                file_name = execution.get("file_name", "N/A")
                hardware_profile = execution.get("hardware_profile", "N/A")
                created_at = execution.get("created_at", None)
            else:
                execution_id = getattr(execution, "execution_id", "N/A")
                status = getattr(execution, "status", "N/A")
                file_name = getattr(execution, "file_name", "N/A")
                hardware_profile = getattr(
                    execution, "hardware_profile", "N/A")
                created_at = getattr(execution, "created_at", None)

            table.add_row(
                truncate_id(execution_id, 8),
                status,
                file_name,
                hardware_profile,
                format_timestamp(created_at),
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)
