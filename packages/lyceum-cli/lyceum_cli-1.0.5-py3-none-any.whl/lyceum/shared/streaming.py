"""
Streaming utilities for execution output
"""

import json
import re
import httpx
from rich.console import Console

from .config import config

console = Console()


def strip_ansi_codes(text: str) -> str:
    """Remove ANSI escape codes from text"""
    ansi_escape = re.compile(r"\x1b\[[0-9;]*m")
    return ansi_escape.sub("", text)


def stream_execution_output(
    execution_id: str, client=None, streaming_url: str = None
) -> bool:
    """Stream execution output in real-time. Returns True if successful, False if failed."""
    # Use provided streaming URL if available (from v2 API response),
    # otherwise construct it
    if streaming_url:
        stream_url = streaming_url
    else:
        # Fallback for old format
        stream_url = (
            f"{config.base_url}/api/v2/external/compute/execution/stream/{execution_id}"
        )

    try:
        console.print("[dim]🔗 Connecting to execution stream...[/dim]")

        # For direct gRPC streaming, use POST with no auth headers (like the
        # extension)
        with httpx.stream(
            "POST", stream_url, headers={"Accept": "text/event-stream"}, timeout=600.0
        ) as response:
            if response.status_code != 200:
                console.print(
                    f"[red]❌ Stream failed: HTTP {response.status_code}[/red]"
                )
                return False

            console.print("[dim]📡 Streaming output...[/dim]")

            for line in response.iter_lines():
                if line.strip():
                    # Debug: show raw line
                    # console.print(f"[dim]DEBUG: {line}[/dim]")

                    # Parse Server-Sent Events format
                    if line.startswith("data: "):
                        data_json = line[6:]  # Remove "data: " prefix

                        # Handle plain text completion messages from gRPC
                        # service
                        if (
                            data_json == "Stream complete"
                            or "complete" in data_json.lower()
                        ):
                            console.print(f"[dim]{data_json}[/dim]")
                            continue

                        try:
                            data = json.loads(data_json)

                            # Handle new gRPC message format
                            if "Message" in data:
                                message = data["Message"]

                                # Handle output messages
                                if "Output" in message:
                                    output = message["Output"]
                                    content = output.get("content", "")
                                    if content:
                                        clean_output = strip_ansi_codes(
                                            content)
                                        console.print(clean_output, end="")

                                # Handle status updates
                                elif "StatusUpdate" in message:
                                    # Could show status updates if needed
                                    pass

                                # Handle job finished
                                elif "JobFinished" in message:
                                    job_finished = message["JobFinished"]
                                    result = job_finished.get("job", {}).get(
                                        "result", {}
                                    )
                                    return_code = result.get("return_code", 1)

                                    if return_code == 0:
                                        console.print(
                                            "\n[green]✅ Execution completed successfully[/green]"
                                        )
                                        return True
                                    else:
                                        console.print(
                                            f"\n[red]❌ Execution failed with code {return_code}[/red]")
                                        return False

                            # Handle old format (fallback)
                            event_type = data.get("type", "unknown")

                            if event_type == "output":
                                # Print output without extra formatting,
                                # stripping ANSI codes
                                output = data.get(
                                    "content", ""
                                )  # Fixed: server sends "content" not "output"
                                if output:
                                    clean_output = strip_ansi_codes(output)
                                    console.print(clean_output, end="")

                            elif event_type == "completed":
                                status = data.get("status", "unknown")
                                exec_time = data.get("execution_time", 0)

                                if status == "completed":
                                    console.print(
                                        f"\n[green]✅ Execution completed successfully in {
                                            exec_time:.1f}s[/green]")
                                elif status in ["failed_user", "failed_system"]:
                                    console.print(
                                        f"\n[red]❌ Execution failed: {status}[/red]")
                                    # Show errors if available
                                    errors = data.get("errors")
                                    if errors:
                                        console.print(
                                            f"[red]Error: {errors}[/red]")
                                elif status == "timeout":
                                    console.print(
                                        f"\n[yellow]⏰ Execution timed out after {
                                            exec_time:.1f}s[/yellow]")
                                elif status == "cancelled":
                                    console.print(
                                        "\n[yellow]🛑 Execution was cancelled[/yellow]"
                                    )

                                return status == "completed"

                            elif event_type == "error":
                                error_msg = data.get(
                                    "message", "Unknown error")
                                console.print(
                                    f"\n[red]❌ Error: {error_msg}[/red]")
                                return False

                        except json.JSONDecodeError:
                            # Skip malformed JSON
                            continue

            console.print(
                "\n[yellow]⚠️ Stream ended without completion signal[/yellow]"
            )
            return False

    except Exception as e:
        console.print(f"\n[red]❌ Streaming error: {e}[/red]")
        return False
