"""
Machine types and resources commands
"""

import typer
from rich.console import Console

from ...shared.config import config
from ...shared.display import create_table

console = Console()


resources_app = typer.Typer(
    name="resources",
    help="Machine types and resources")


@resources_app.command("machine-types")
def list_machine_types():
    """List available machine types and their pricing"""
    try:
        # Use v2 API endpoint directly
        import httpx

        # Call the v2 machine types endpoint
        with httpx.Client() as http_client:
            response = http_client.get(
                f"{config.base_url}/api/v2/external/execution/machine-types",
                headers={"Authorization": f"Bearer {config.api_key}"},
                timeout=30.0,
            )

            if response.status_code != 200:
                console.print(f"[red]Error: HTTP {response.status_code}[/red]")
                if response.content:
                    console.print(f"[red]{response.content.decode()}[/red]")
                raise typer.Exit(1)

            result = response.json()
            machine_types = (
                result.get(
                    "machine_types",
                    []) if isinstance(
                    result,
                    dict) else [])

            if not machine_types:
                console.print("[dim]No machine types found[/dim]")
                return

            columns = [
                {"header": "Name", "style": "cyan", "no_wrap": True},
                {"header": "Display Name", "style": "yellow"},
                {"header": "Category", "style": "blue"},
                {"header": "CPU", "style": "dim"},
                {"header": "Memory", "style": "dim"},
                {"header": "GPU", "style": "magenta"},
                {"header": "Price/hr", "style": "green"},
                {"header": "Available", "style": "dim"},
            ]

            table = create_table("Available Machine Types", columns)

            for machine_type in machine_types:
                # Handle both JSON dict and object formats
                if isinstance(machine_type, dict):
                    name = machine_type.get("name", "N/A")
                    display_name = machine_type.get("display_name", "N/A")
                    category = machine_type.get("category", "N/A")
                    cpu_cores = machine_type.get("cpu_cores", 0)
                    memory_gb = machine_type.get("memory_gb", 0)
                    gpu_model = machine_type.get("gpu_model", None)
                    gpu_count = machine_type.get("gpu_count", 0)
                    price = machine_type.get("price_per_hour", 0)
                    available = machine_type.get("available", True)
                else:
                    name = getattr(machine_type, "name", "N/A")
                    display_name = getattr(machine_type, "display_name", "N/A")
                    category = getattr(machine_type, "category", "N/A")
                    cpu_cores = getattr(machine_type, "cpu_cores", 0)
                    memory_gb = getattr(machine_type, "memory_gb", 0)
                    gpu_model = getattr(machine_type, "gpu_model", None)
                    gpu_count = getattr(machine_type, "gpu_count", 0)
                    price = getattr(machine_type, "price_per_hour", 0)
                    available = getattr(machine_type, "available", True)

                gpu_info = f"{gpu_model} x{gpu_count}" if gpu_model else "None"

                table.add_row(
                    name,
                    display_name,
                    category,
                    f"{cpu_cores} cores",
                    f"{memory_gb:.0f}GB",
                    gpu_info,
                    f"${price:.2f}",
                    "✅" if available else "❌",
                )

            console.print(table)
            console.print(
                f"\n[dim]Found {
                    len(machine_types)} machine types[/dim]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)
