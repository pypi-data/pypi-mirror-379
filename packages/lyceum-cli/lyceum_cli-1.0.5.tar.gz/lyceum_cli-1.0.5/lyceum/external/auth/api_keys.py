"""
API key management commands
"""

import typer
from rich.console import Console

from ...shared.config import config
from ...shared.display import create_table, format_timestamp, truncate_id

console = Console()


api_keys_app = typer.Typer(name="api-keys", help="API key management")


@api_keys_app.command("list")
def list_api_keys(
    limit: int = typer.Argument(10, help="Number of API keys to show"),
):
    """List your API keys"""
    try:
        # Use v2 API endpoint directly
        import httpx

        # Call the v2 API keys endpoint
        with httpx.Client() as http_client:
            response = http_client.get(
                f"{config.base_url}/api/v2/external/auth/api-keys/",
                headers={"Authorization": f"Bearer {config.api_key}"},
                timeout=30.0,
            )

            if response.status_code != 200:
                console.print(f"[red]Error: HTTP {response.status_code}[/red]")
                if response.content:
                    console.print(f"[red]{response.content.decode()}[/red]")
                raise typer.Exit(1)

            result = response.json()
            api_keys = result if isinstance(result, list) else []

            # Apply limit
            api_keys = api_keys[:limit]

        if not api_keys:
            console.print("[dim]No API keys found[/dim]")
            return

        columns = [
            {"header": "ID", "style": "cyan", "no_wrap": True, "max_width": 12},
            {"header": "Name", "style": "yellow"},
            {"header": "Active", "style": "green"},
            {"header": "Created", "style": "dim"},
        ]

        table = create_table("API Keys", columns)

        for key in api_keys:
            # Handle both JSON dict and object formats
            if isinstance(key, dict):
                key_id = key.get("id", "N/A")
                key_name = key.get("key_name", "N/A")
                is_active = key.get("is_active", False)
                created_at = key.get("created_at", None)
            else:
                key_id = getattr(key, "id", "N/A")
                key_name = getattr(key, "key_name", "N/A")
                is_active = getattr(key, "is_active", False)
                created_at = getattr(key, "created_at", None)

            table.add_row(
                truncate_id(key_id, 8),
                key_name,
                "✅" if is_active else "❌",
                format_timestamp(created_at),
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)
