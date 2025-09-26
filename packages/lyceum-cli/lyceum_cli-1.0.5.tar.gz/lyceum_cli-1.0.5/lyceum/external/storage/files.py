"""
Storage file management commands
"""

import json
from pathlib import Path
from typing import Optional
import typer
from rich.console import Console

from ...shared.config import config
from ...shared.display import create_table, format_timestamp

console = Console()

storage_app = typer.Typer(name="storage", help="File storage management")


@storage_app.command("upload")
def upload_file(
    file_path: str = typer.Argument(..., help="Path to file to upload"),
    key: Optional[str] = typer.Option(
        None, "--key", "-k", help="Storage key (defaults to filename)"
    ),
    folder: Optional[str] = typer.Option(
        None, "--folder", "-f", help="Folder/prefix for the file"
    ),
):
    """Upload a file to storage"""
    if not Path(file_path).exists():
        console.print(f"[red]Error: File '{file_path}' not found[/red]")
        raise typer.Exit(1)

    try:
        import httpx

        # Use filename as key if not provided
        if not key:
            key = Path(file_path).name

        # Add folder prefix if specified
        if folder:
            key = f"{folder.rstrip('/')}/{key}"

        console.print(f"[dim]📤 Uploading {file_path} as {key}...[/dim]")

        # Upload file using multipart form data
        with open(file_path, "rb") as f:
            files = {
                "file": (
                    Path(file_path).name,
                    f,
                    "application/octet-stream")}
            data = {"key": key}

            response = httpx.post(
                f"{config.base_url}/api/v2/external/storage/upload",
                headers={"Authorization": f"Bearer {config.api_key}"},
                files=files,
                data=data,
                timeout=60.0,
            )

        if response.status_code != 200:
            console.print(f"[red]Error: HTTP {response.status_code}[/red]")
            if response.content:
                console.print(f"[red]{response.content.decode()}[/red]")
            raise typer.Exit(1)

        result = response.json()

        console.print("[green]✅ File uploaded successfully![/green]")
        console.print(f"[cyan]Storage Key: {result.get('key', key)}[/cyan]")
        console.print(
            f"[dim]Size: {
                result.get(
                    'size',
                    'Unknown')} bytes[/dim]")
        console.print(f"[dim]URL: {result.get('url', 'N/A')}[/dim]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@storage_app.command("download")
def download_file(
    key: str = typer.Argument(..., help="Storage key of file to download"),
    output_path: Optional[str] = typer.Option(
        None, "--output", "-o", help="Output file path"
    ),
):
    """Download a file from storage"""
    try:
        import httpx

        console.print(f"[dim]⬇️  Downloading {key}...[/dim]")

        response = httpx.get(
            f"{config.base_url}/api/v2/external/storage/download/{key}",
            headers={"Authorization": f"Bearer {config.api_key}"},
            timeout=60.0,
        )

        if response.status_code != 200:
            console.print(f"[red]Error: HTTP {response.status_code}[/red]")
            if response.content:
                console.print(f"[red]{response.content.decode()}[/red]")
            raise typer.Exit(1)

        # Use key as filename if output path not provided
        if not output_path:
            output_path = Path(key).name

        # Write file content
        with open(output_path, "wb") as f:
            f.write(response.content)

        console.print(f"[green]✅ File downloaded to {output_path}[/green]")
        console.print(f"[dim]Size: {len(response.content)} bytes[/dim]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@storage_app.command("list")
def list_files(
    limit: int = typer.Argument(20, help="Number of files to show"),
    prefix: Optional[str] = typer.Option(
        None, "--prefix", "-p", help="Filter by prefix/folder"
    ),
):
    """List files in storage"""
    try:
        import httpx

        console.print("[dim]📋 Listing storage files...[/dim]")

        params = {"limit": limit}
        if prefix:
            params["prefix"] = prefix

        response = httpx.get(
            f"{config.base_url}/api/v2/external/storage/list-files",
            headers={"Authorization": f"Bearer {config.api_key}"},
            params=params,
            timeout=30.0,
        )

        if response.status_code != 200:
            console.print(f"[red]Error: HTTP {response.status_code}[/red]")
            if response.content:
                console.print(f"[red]{response.content.decode()}[/red]")
            raise typer.Exit(1)

        result = response.json()
        files = result.get("files", []) if isinstance(result, dict) else result

        if not files:
            console.print("[dim]No files found[/dim]")
            return

        columns = [
            {"header": "Key", "style": "cyan", "no_wrap": True},
            {"header": "Size", "style": "yellow", "justify": "right"},
            {"header": "Modified", "style": "dim"},
            {"header": "Content Type", "style": "magenta"},
        ]

        table = create_table("Storage Files", columns)

        for file_info in files:
            if isinstance(file_info, dict):
                key = file_info.get("key", "N/A")
                size = file_info.get("size", 0)
                modified = file_info.get("last_modified", None)
                content_type = file_info.get("content_type", "Unknown")
            else:
                key = getattr(file_info, "key", "N/A")
                size = getattr(file_info, "size", 0)
                modified = getattr(file_info, "last_modified", None)
                content_type = getattr(file_info, "content_type", "Unknown")

            # Format size
            if size > 1024 * 1024:
                size_str = f"{size / (1024 * 1024):.1f}MB"
            elif size > 1024:
                size_str = f"{size / 1024:.1f}KB"
            else:
                size_str = f"{size}B"

            table.add_row(
                key,
                size_str,
                format_timestamp(modified),
                content_type)

        console.print(table)
        console.print(f"\n[dim]Found {len(files)} files[/dim]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@storage_app.command("delete")
def delete_file(
    key: str = typer.Argument(..., help="Storage key of file to delete"),
    confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompt"),
):
    """Delete a file from storage"""
    if not confirm:
        if not typer.confirm(f"Are you sure you want to delete '{key}'?"):
            console.print("[dim]Deletion cancelled[/dim]")
            return

    try:
        import httpx

        console.print(f"[dim]🗑️  Deleting {key}...[/dim]")

        response = httpx.delete(
            f"{config.base_url}/api/v2/external/storage/delete/{key}",
            headers={"Authorization": f"Bearer {config.api_key}"},
            timeout=30.0,
        )

        if response.status_code != 200:
            console.print(f"[red]Error: HTTP {response.status_code}[/red]")
            if response.content:
                console.print(f"[red]{response.content.decode()}[/red]")
            raise typer.Exit(1)

        console.print(f"[green]✅ File {key} deleted successfully[/green]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@storage_app.command("delete-folder")
def delete_folder(
    folder: str = typer.Argument(..., help="Folder/prefix to delete"),
    confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompt"),
):
    """Delete all files in a folder/prefix"""
    if not confirm:
        if not typer.confirm(
            f"Are you sure you want to delete all files in '{folder}'?"
        ):
            console.print("[dim]Deletion cancelled[/dim]")
            return

    try:
        import httpx

        console.print(f"[dim]🗑️  Deleting folder {folder}...[/dim]")

        response = httpx.delete(
            f"{config.base_url}/api/v2/external/storage/delete-folder/{folder}",
            headers={"Authorization": f"Bearer {config.api_key}"},
            timeout=30.0,
        )

        if response.status_code != 200:
            console.print(f"[red]Error: HTTP {response.status_code}[/red]")
            if response.content:
                console.print(f"[red]{response.content.decode()}[/red]")
            raise typer.Exit(1)

        result = response.json()
        deleted_count = result.get("deleted_count", 0)
        console.print(
            f"[green]✅ Deleted {deleted_count} files from folder {folder}[/green]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@storage_app.command("credentials")
def get_credentials(
    provider: str = typer.Option(
        "s3", "--provider", "-p", help="Storage provider (s3, gcs, azure)"
    ),
    duration: int = typer.Option(
        3600, "--duration", "-d", help="Credential duration in seconds"
    ),
):
    """Get temporary storage credentials for direct access"""
    try:
        import httpx

        console.print(f"[dim]🔑 Getting {provider} credentials...[/dim]")

        request_data = {"provider": provider, "duration_seconds": duration}

        response = httpx.post(
            f"{config.base_url}/api/v2/external/storage/credentials",
            headers={"Authorization": f"Bearer {config.api_key}"},
            json=request_data,
            timeout=30.0,
        )

        if response.status_code != 200:
            console.print(f"[red]Error: HTTP {response.status_code}[/red]")
            if response.content:
                console.print(f"[red]{response.content.decode()}[/red]")
            raise typer.Exit(1)

        credentials = response.json()

        console.print(
            f"[green]✅ {
                provider.upper()} credentials obtained[/green]")
        console.print(f"[cyan]Expires in: {duration} seconds[/cyan]")
        console.print("[dim]Credentials (JSON):[/dim]")
        console.print(json.dumps(credentials, indent=2))

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)
