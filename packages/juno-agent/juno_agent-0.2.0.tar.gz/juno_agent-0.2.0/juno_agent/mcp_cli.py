"""MCP CLI Commands.

This module provides CLI commands for managing MCP servers, similar to Claude Code's
'claude mcp add' command structure.
"""

import json
import sys
from pathlib import Path
from typing import Optional, List

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

from .mcp_config import MCPServerConfig
from .mcp_config_manager import MCPConfigManager
import logging

mcp_logger = logging.getLogger("mcp_feature")
from .config import ConfigManager

# Create MCP CLI app
mcp_app = typer.Typer(
    name="mcp",
    help="MCP server management commands",
    add_completion=True
)

console = Console()


def get_mcp_config_manager(workdir: Optional[Path] = None) -> MCPConfigManager:
    """Get MCP configuration manager."""
    project_root = workdir or Path.cwd()
    return MCPConfigManager(project_root=project_root)


@mcp_app.command("add")
def add_server(
    name: str = typer.Argument(..., help="Server name"),
    command_and_args: Optional[List[str]] = typer.Argument(None, help="Command and arguments (e.g., python -m my_server)"),
    command: Optional[str] = typer.Option(None, "--command", help="Command to start the server (overrides positional)"),
    args: Optional[List[str]] = typer.Option(None, "--args", help="Command arguments (overrides positional)"),
    transport: str = typer.Option("stdio", "--transport", help="Transport type (stdio, sse, streamable-http)"),
    url: Optional[str] = typer.Option(None, "--url", help="Server URL (for sse/streamable-http)"),
    timeout: float = typer.Option(300.0, "--timeout", help="Connection timeout in seconds"),
    scope: str = typer.Option("local", "--scope", help="Configuration scope (local/global)"),
    enabled: bool = typer.Option(True, "--enabled/--disabled", help="Enable/disable server"),
    workdir: Optional[Path] = typer.Option(None, "--workdir", "-w", help="Working directory"),
) -> None:
    """Add a new MCP server configuration.

    Examples:
        # Minimal syntax (recommended) - use -- for commands with flags
        juno-agent mcp add my-server -- python -m my_mcp_server

        # Simple commands without flags
        juno-agent mcp add my-server python my_server.py

        # With options
        juno-agent mcp add my-server --timeout 60 --scope global -- python -m my_server

        # Explicit syntax (for complex commands)
        juno-agent mcp add my-server --command python --args "-m" --args "my_server"

        # SSE transport
        juno-agent mcp add sse-server --transport sse --url https://example.com/mcp
    """
    try:
        # Handle positional command and args if provided
        if command_and_args and len(command_and_args) > 0:
            # If explicit --command or --args are not provided, use positional
            if command is None:
                command = command_and_args[0]
            if args is None and len(command_and_args) > 1:
                args = command_and_args[1:]

        mcp_logger.info(f"Adding MCP server '{name}' with command '{command}'")

        config_manager = get_mcp_config_manager(workdir)

        # Validate scope
        if scope not in ["local", "global"]:
            console.print("[red]Error: Scope must be 'local' or 'global'[/red]")
            raise typer.Exit(1)

        # Validate transport requirements
        if transport in ["sse", "streamable-http"] and not url:
            console.print(f"[red]Error: {transport} transport requires --url parameter[/red]")
            raise typer.Exit(1)

        if transport == "stdio" and not command:
            console.print("[red]Error: stdio transport requires a command[/red]")
            raise typer.Exit(1)

        # Create server configuration
        server_config = MCPServerConfig(
            name=name,
            transport=transport,
            command=command,
            args=args or [],
            url=url,
            timeout=timeout,
            enabled=enabled
        )

        # Add server
        config_manager.add_server(server_config, scope=scope)

        # Display success
        console.print(Panel(
            f"✅ Successfully added MCP server '[bold]{name}[/bold]'\n\n"
            f"[dim]Transport:[/dim] {transport}\n"
            f"[dim]Command:[/dim] {command}\n"
            f"[dim]Scope:[/dim] {scope}\n"
            f"[dim]Enabled:[/dim] {'Yes' if enabled else 'No'}",
            title="MCP Server Added",
            border_style="green"
        ))

        mcp_logger.info(f"Successfully added MCP server '{name}' to {scope} configuration")

    except Exception as e:
        console.print(f"[red]Error adding MCP server: {e}[/red]")
        mcp_logger.error(f"Failed to add MCP server '{name}': {e}")
        raise typer.Exit(1)


@mcp_app.command("remove")
def remove_server(
    name: str = typer.Argument(..., help="Server name to remove"),
    scope: str = typer.Option("local", "--scope", help="Configuration scope (local/global)"),
    workdir: Optional[Path] = typer.Option(None, "--workdir", "-w", help="Working directory"),
    force: bool = typer.Option(False, "--force", help="Skip confirmation prompt"),
) -> None:
    """Remove an MCP server configuration."""
    try:
        config_manager = get_mcp_config_manager(workdir)

        # Validate scope
        if scope not in ["local", "global"]:
            console.print("[red]Error: Scope must be 'local' or 'global'[/red]")
            raise typer.Exit(1)

        # Check if server exists
        server = config_manager.get_server(name, scope=scope)
        if not server:
            console.print(f"[yellow]Server '[bold]{name}[/bold]' not found in {scope} configuration[/yellow]")
            raise typer.Exit(1)

        # Confirmation prompt
        if not force:
            confirmed = typer.confirm(f"Are you sure you want to remove server '{name}' from {scope} configuration?")
            if not confirmed:
                console.print("[yellow]Operation cancelled[/yellow]")
                return

        # Remove server
        removed = config_manager.remove_server(name, scope=scope)

        if removed:
            console.print(Panel(
                f"✅ Successfully removed MCP server '[bold]{name}[/bold]' from {scope} configuration",
                title="MCP Server Removed",
                border_style="green"
            ))
            mcp_logger.info(f"Successfully removed MCP server '{name}' from {scope} configuration")
        else:
            console.print(f"[yellow]Server '[bold]{name}[/bold]' was not found[/yellow]")

    except Exception as e:
        console.print(f"[red]Error removing MCP server: {e}[/red]")
        mcp_logger.error(f"Failed to remove MCP server '{name}': {e}")
        raise typer.Exit(1)


@mcp_app.command("list")
def list_servers(
    scope: str = typer.Option("merged", "--scope", help="Configuration scope (local/global/merged)"),
    workdir: Optional[Path] = typer.Option(None, "--workdir", "-w", help="Working directory"),
    detail: bool = typer.Option(False, "--detail", help="Show detailed information"),
) -> None:
    """List MCP server configurations."""
    try:
        config_manager = get_mcp_config_manager(workdir)

        # Validate scope
        if scope not in ["local", "global", "merged"]:
            console.print("[red]Error: Scope must be 'local', 'global', or 'merged'[/red]")
            raise typer.Exit(1)

        servers = config_manager.list_servers(scope=scope)

        if not servers:
            console.print(f"[yellow]No MCP servers found in {scope} configuration[/yellow]")
            return

        # Create table
        table = Table(
            title=f"MCP Servers ({scope} configuration)",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta"
        )

        if detail:
            table.add_column("Name", style="cyan", no_wrap=True)
            table.add_column("Transport", style="green")
            table.add_column("Command", style="blue")
            table.add_column("Args", style="yellow")
            table.add_column("Enabled", style="white")
            table.add_column("Timeout", style="white")

            for server in servers:
                table.add_row(
                    server.name,
                    server.transport,
                    server.command or "-",
                    " ".join(server.args) if server.args else "-",
                    "✅" if server.enabled else "❌",
                    f"{server.timeout}s"
                )
        else:
            table.add_column("Name", style="cyan", no_wrap=True)
            table.add_column("Transport", style="green")
            table.add_column("Status", style="white")
            table.add_column("Command", style="blue")

            for server in servers:
                status = "✅ Enabled" if server.enabled else "❌ Disabled"
                command_display = server.command or server.url or "-"
                if len(command_display) > 50:
                    command_display = command_display[:47] + "..."

                table.add_row(
                    server.name,
                    server.transport,
                    status,
                    command_display
                )

        console.print(table)

        # Show summary
        enabled_count = sum(1 for s in servers if s.enabled)
        console.print(f"\n[dim]Total: {len(servers)} servers, {enabled_count} enabled[/dim]")

    except Exception as e:
        console.print(f"[red]Error listing MCP servers: {e}[/red]")
        mcp_logger.error(f"Failed to list MCP servers: {e}")
        raise typer.Exit(1)


@mcp_app.command("show")
def show_server(
    name: str = typer.Argument(..., help="Server name"),
    scope: str = typer.Option("merged", "--scope", help="Configuration scope (local/global/merged)"),
    workdir: Optional[Path] = typer.Option(None, "--workdir", "-w", help="Working directory"),
) -> None:
    """Show detailed information about a specific MCP server."""
    try:
        config_manager = get_mcp_config_manager(workdir)

        # Validate scope
        if scope not in ["local", "global", "merged"]:
            console.print("[red]Error: Scope must be 'local', 'global', or 'merged'[/red]")
            raise typer.Exit(1)

        server = config_manager.get_server(name, scope=scope)

        if not server:
            console.print(f"[red]Server '[bold]{name}[/bold]' not found in {scope} configuration[/red]")
            raise typer.Exit(1)

        # Create detailed display
        details = f"""[bold]Name:[/bold] {server.name}
[bold]Transport:[/bold] {server.transport}
[bold]Enabled:[/bold] {'✅ Yes' if server.enabled else '❌ No'}
[bold]Timeout:[/bold] {server.timeout}s"""

        if server.command:
            details += f"\n[bold]Command:[/bold] {server.command}"

        if server.args:
            details += f"\n[bold]Arguments:[/bold] {' '.join(server.args)}"

        if server.url:
            details += f"\n[bold]URL:[/bold] {server.url}"

        if server.env:
            details += f"\n[bold]Environment:[/bold] {len(server.env)} variables"

        if server.include_tools:
            details += f"\n[bold]Include Tools:[/bold] {', '.join(server.include_tools)}"

        if server.exclude_tools:
            details += f"\n[bold]Exclude Tools:[/bold] {', '.join(server.exclude_tools)}"

        console.print(Panel(
            details,
            title=f"MCP Server: {name}",
            border_style="blue"
        ))

    except Exception as e:
        console.print(f"[red]Error showing MCP server: {e}[/red]")
        mcp_logger.error(f"Failed to show MCP server '{name}': {e}")
        raise typer.Exit(1)


@mcp_app.command("status")
def status(
    workdir: Optional[Path] = typer.Option(None, "--workdir", "-w", help="Working directory"),
) -> None:
    """Show MCP configuration status and information."""
    try:
        config_manager = get_mcp_config_manager(workdir)
        config_info = config_manager.get_config_info()

        # Create status display
        status_text = f"""[bold]Project Root:[/bold] {config_info['project_root']}

[bold]Configuration Files:[/bold]
• Local: {config_info['local']['file']} {'✅' if config_info['local']['exists'] else '❌'}
• Global: {config_info['global']['file']} {'✅' if config_info['global']['exists'] else '❌'}

[bold]Server Count:[/bold]
• Local: {config_info['local']['servers']} servers
• Global: {config_info['global']['servers']} servers
• Merged: {config_info['merged']['servers']} servers"""

        console.print(Panel(
            status_text,
            title="MCP Configuration Status",
            border_style="blue"
        ))

        # Show quick server list if any exist
        if config_info['merged']['servers'] > 0:
            servers = config_manager.list_servers(scope="merged")
            console.print("\n[bold]Quick Server List:[/bold]")
            for server in servers:
                status_icon = "✅" if server.enabled else "❌"
                console.print(f"  {status_icon} [cyan]{server.name}[/cyan] ({server.transport})")

    except Exception as e:
        console.print(f"[red]Error getting MCP status: {e}[/red]")
        mcp_logger.error(f"Failed to get MCP status: {e}")
        raise typer.Exit(1)


@mcp_app.command("test")
def test_server(
    name: str = typer.Argument(..., help="Server name to test"),
    scope: str = typer.Option("merged", "--scope", help="Configuration scope (local/global/merged)"),
    workdir: Optional[Path] = typer.Option(None, "--workdir", "-w", help="Working directory"),
) -> None:
    """Test connection to an MCP server."""
    try:
        console.print(f"[yellow]Testing MCP server '[bold]{name}[/bold]'...[/yellow]")

        config_manager = get_mcp_config_manager(workdir)
        server = config_manager.get_server(name, scope=scope)

        if not server:
            console.print(f"[red]Server '[bold]{name}[/bold]' not found in {scope} configuration[/red]")
            raise typer.Exit(1)

        if not server.enabled:
            console.print(f"[yellow]Server '[bold]{name}[/bold]' is disabled[/yellow]")

        # Test would require async context, so this is a basic validation
        console.print(f"[green]✅ Server '[bold]{name}[/bold]' configuration is valid[/green]")
        console.print(f"[dim]Transport: {server.transport}[/dim]")
        console.print(f"[dim]Command: {server.command or server.url or 'N/A'}[/dim]")
        console.print(f"[dim]Timeout: {server.timeout}s[/dim]")

        console.print("\n[yellow]Note: Full connection testing requires the application to be running[/yellow]")

    except Exception as e:
        console.print(f"[red]Error testing MCP server: {e}[/red]")
        mcp_logger.error(f"Failed to test MCP server '{name}': {e}")
        raise typer.Exit(1)


@mcp_app.command("export")
def export_config(
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file path"),
    scope: str = typer.Option("merged", "--scope", help="Configuration scope (local/global/merged)"),
    workdir: Optional[Path] = typer.Option(None, "--workdir", "-w", help="Working directory"),
) -> None:
    """Export MCP configuration to a file."""
    try:
        config_manager = get_mcp_config_manager(workdir)

        # Load configuration
        if scope == "local":
            config = config_manager.load_local_config()
        elif scope == "global":
            config = config_manager.load_global_config()
        else:
            config = config_manager.load_merged_config()

        # Convert to dict for JSON export
        config_dict = config.dict()

        # Output to file or console
        if output:
            with open(output, 'w') as f:
                json.dump(config_dict, f, indent=2)
            console.print(f"[green]✅ Configuration exported to {output}[/green]")
        else:
            console.print(json.dumps(config_dict, indent=2))

    except Exception as e:
        console.print(f"[red]Error exporting MCP configuration: {e}[/red]")
        mcp_logger.error(f"Failed to export MCP configuration: {e}")
        raise typer.Exit(1)


# Add the MCP app to the main app
def register_mcp_commands(main_app: typer.Typer) -> None:
    """Register MCP commands with the main application."""
    main_app.add_typer(mcp_app, name="mcp")
    mcp_logger.info("MCP CLI commands registered")