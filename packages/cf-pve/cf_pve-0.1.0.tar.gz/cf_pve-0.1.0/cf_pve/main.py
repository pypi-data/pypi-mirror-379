"""
CF-PVE: Cloudflare + Proxmox VE Integration Tool

A simple CLI tool for automating Proxmox VE integration with Cloudflare ecosystem.
"""

import typer
from typing import Optional
from pathlib import Path

from cf_pve.commands import commands
from cf_pve import __version__


# Create main Typer app
app = typer.Typer(
    name="cf-pve",
    help="Cloudflare + Proxmox VE Integration Tool",
    epilog="Visit https://github.com/yourusername/cf-pve for documentation and examples.",
    no_args_is_help=True,
    rich_markup_mode="rich"
)

# Create subcommands
tunnel_app = typer.Typer(name="tunnel", help="Manage Cloudflare tunnels")
app.add_typer(tunnel_app)

config_app = typer.Typer(name="config", help="Manage configuration")
app.add_typer(config_app)


@app.command()
def version():
    """Show version information."""
    typer.echo(f"CF-PVE version {__version__}")


@app.command()
def init():
    """Initialize CF-PVE configuration."""
    commands.init_config()


@app.command()
def test():
    """Test API connections."""
    commands.test_connections()


@app.command()
def expose(
    vm_id: int = typer.Argument(..., help="Proxmox VM ID"),
    port: int = typer.Argument(..., help="Service port"),
    subdomain: str = typer.Argument(..., help="Subdomain (e.g., web.example.com)"),
    protocol: str = typer.Option("http", help="Protocol (http/https)"),
    tunnel: str = typer.Option("main-tunnel", "--tunnel", "-t", help="Tunnel name")
):
    """Expose a VM service through Cloudflare tunnel.
    
    Examples:
        cf-pve expose 101 80 web.example.com
        cf-pve expose 102 3000 api.example.com --protocol http
        cf-pve expose 103 443 secure.example.com --protocol https
    """
    commands.expose_service(vm_id, port, subdomain, protocol, tunnel)


@app.command()
def hide(
    vm_id: int = typer.Argument(..., help="Proxmox VM ID"),
    port: int = typer.Argument(..., help="Service port")
):
    """Hide an exposed service.
    
    Examples:
        cf-pve hide 101 80
        cf-pve hide 102 3000
    """
    commands.hide_service(vm_id, port)


@app.command(name="list")
def list_services():
    """List all exposed services.
    
    Shows all currently exposed services with their status.
    """
    commands.list_services()


# Alias commands for convenience
@app.command()
def up(
    vm_id: int = typer.Argument(..., help="Proxmox VM ID"),
    port: int = typer.Argument(..., help="Service port"),
    subdomain: str = typer.Argument(..., help="Subdomain"),
    protocol: str = typer.Option("http", help="Protocol"),
    tunnel: str = typer.Option("main-tunnel", "--tunnel", "-t", help="Tunnel name")
):
    """Alias for 'expose' command."""
    commands.expose_service(vm_id, port, subdomain, protocol, tunnel)


@app.command()
def down(
    vm_id: int = typer.Argument(..., help="Proxmox VM ID"),
    port: int = typer.Argument(..., help="Service port")
):
    """Alias for 'hide' command."""
    commands.hide_service(vm_id, port)


@app.command()
def ls():
    """Alias for 'list' command."""
    commands.list_services()


@app.command()
def ps():
    """Alias for 'tunnel list' command."""
    commands.list_tunnels()


# Config subcommands
@config_app.command("init")
def config_init():
    """Initialize configuration file."""
    commands.init_config()


@config_app.command("check")
def config_check():
    """Check configuration validity."""
    try:
        commands.test_connections()
        typer.echo("✅ Configuration is valid!")
    except typer.Exit:
        typer.echo("❌ Configuration has issues.")
        raise


@config_app.command("show")
def config_show():
    """Show current configuration (sensitive data hidden)."""
    from .config import config_manager
    
    try:
        config = config_manager.get_config()
        
        typer.echo("📋 Current Configuration:")
        typer.echo(f"  Cloudflare:")
        typer.echo(f"    Zone ID: {config.cloudflare.zone_id}")
        typer.echo(f"    API Token: {'*' * 20} (hidden)")
        typer.echo(f"    Proxy Enabled: {config.cloudflare.proxy_enabled}")
        typer.echo(f"    Default TTL: {config.cloudflare.default_ttl}")
        
        typer.echo(f"  Proxmox:")
        typer.echo(f"    Host: {config.proxmox.host}:{config.proxmox.port}")
        typer.echo(f"    Username: {config.proxmox.username}")
        typer.echo(f"    SSL Verification: {config.proxmox.verify_ssl}")
        
        typer.echo(f"  Tunnel:")
        typer.echo(f"    Default Name: {config.tunnel.default_name}")
        typer.echo(f"    Config Path: {config.tunnel.config_path}")
        
        typer.echo(f"  Logging:")
        typer.echo(f"    Level: {config.logging.level}")
        
        typer.echo(f"\n📁 Config file: {config_manager.config_path}")
        
    except Exception as e:
        typer.echo(f"❌ Error loading configuration: {e}", err=True)
        raise typer.Exit(1)


@config_app.command("edit")
def config_edit():
    """Edit configuration file in default editor."""
    from .config import config_manager
    import os
    import subprocess
    
    config_file = config_manager.config_path
    
    if not config_file.exists():
        typer.echo("Configuration file doesn't exist. Run 'cf-pve init' first.")
        raise typer.Exit(1)
    
    # Get editor from environment or use nano as default
    editor = os.getenv('EDITOR', 'nano')
    
    try:
        subprocess.run([editor, str(config_file)], check=True)
        typer.echo("Configuration file edited. Run 'cf-pve config check' to validate.")
    except subprocess.CalledProcessError:
        typer.echo(f"Error opening editor: {editor}", err=True)
        typer.echo(f"You can manually edit: {config_file}")
        raise typer.Exit(1)
    except FileNotFoundError:
        typer.echo(f"Editor '{editor}' not found. Set EDITOR environment variable or install nano.")
        typer.echo(f"You can manually edit: {config_file}")
        raise typer.Exit(1)


# Tunnel subcommands
@tunnel_app.command("create")
def tunnel_create(
    name: str = typer.Argument(..., help="Tunnel name")
):
    """Create a new Cloudflare tunnel.
    
    Example:
        cf-pve tunnel create my-tunnel
    """
    commands.create_tunnel(name)


@tunnel_app.command("list")
def tunnel_list():
    """List all Cloudflare tunnels."""
    commands.list_tunnels()


@tunnel_app.command("delete")
def tunnel_delete(
    name: str = typer.Argument(..., help="Tunnel name"),
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation")
):
    """Delete a Cloudflare tunnel.
    
    Example:
        cf-pve tunnel delete my-tunnel
        cf-pve tunnel delete my-tunnel --force
    """
    if not force and not typer.confirm(f"Delete tunnel '{name}' and all its services?"):
        typer.echo("Cancelled.")
        return
    
    commands.delete_tunnel(name)


@tunnel_app.command("status")
def tunnel_status(
    name: Optional[str] = typer.Argument(None, help="Tunnel name (optional)")
):
    """Show tunnel status."""
    if name:
        # Show specific tunnel status
        commands._load_config()
        tunnel = commands.cf_client.get_tunnel(name)
        if tunnel:
            typer.echo(f"Tunnel: {tunnel.name}")
            typer.echo(f"ID: {tunnel.tunnel_id}")
            typer.echo(f"Status: {tunnel.status}")
        else:
            typer.echo(f"Tunnel '{name}' not found.")
    else:
        # Show all tunnels
        commands.list_tunnels()


# Error handling
@app.callback()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
    config_file: Optional[Path] = typer.Option(None, "--config", "-c", help="Custom config file path")
):
    """CF-PVE: Cloudflare + Proxmox VE Integration Tool"""
    
    if verbose:
        typer.echo("🔧 Verbose mode enabled")
    
    if config_file:
        from cf_pve.config import config_manager
        config_manager.config_path = config_file
        if verbose:
            typer.echo(f"📁 Using config file: {config_file}")


def cli():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    cli()