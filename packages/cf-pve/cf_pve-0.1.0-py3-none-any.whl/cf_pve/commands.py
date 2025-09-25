"""Core command logic for CF-PVE."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
import typer

from cf_pve.config import config_manager, Config
from cf_pve.cloudflare_client import CloudflareClient
from cf_pve.proxmox_client import ProxmoxClient


class ExposedService:
    """Represents an exposed service."""
    
    def __init__(self, vm_id: int, vm_name: str, port: int, subdomain: str, 
                 protocol: str = "http", tunnel_name: str = "main-tunnel"):
        self.vm_id = vm_id
        self.vm_name = vm_name
        self.port = port
        self.subdomain = subdomain
        self.protocol = protocol
        self.tunnel_name = tunnel_name
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vm_id": self.vm_id,
            "vm_name": self.vm_name,
            "port": self.port,
            "subdomain": self.subdomain,
            "protocol": self.protocol,
            "tunnel_name": self.tunnel_name
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ExposedService':
        return cls(**data)


class ServiceManager:
    """Manages exposed services state."""
    
    def __init__(self, state_file: Optional[Path] = None):
        self.state_file = state_file or self._get_default_state_file()
        self._services: List[ExposedService] = []
        self._load_state()
    
    @staticmethod
    def _get_default_state_file() -> Path:
        """Get default state file path."""
        config_dir = Path.home() / ".cf-pve"
        config_dir.mkdir(exist_ok=True)
        return config_dir / "services.json"
    
    def _load_state(self) -> None:
        """Load services state from file."""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    data = json.load(f)
                    self._services = [ExposedService.from_dict(s) for s in data.get('services', [])]
            except Exception as e:
                typer.echo(f"Warning: Could not load services state: {e}", err=True)
                self._services = []
    
    def _save_state(self) -> None:
        """Save services state to file."""
        try:
            self.state_file.parent.mkdir(parents=True, exist_ok=True)
            
            data = {
                'services': [s.to_dict() for s in self._services]
            }
            
            with open(self.state_file, 'w') as f:
                json.dump(data, f, indent=2)
            
        except Exception as e:
            typer.echo(f"Warning: Could not save services state: {e}", err=True)
    
    def add_service(self, service: ExposedService) -> None:
        """Add a service to the state."""
        # Remove existing service with same VM ID and port
        self._services = [s for s in self._services 
                         if not (s.vm_id == service.vm_id and s.port == service.port)]
        
        self._services.append(service)
        self._save_state()
    
    def remove_service(self, vm_id: int, port: int) -> Optional[ExposedService]:
        """Remove a service from the state."""
        for i, service in enumerate(self._services):
            if service.vm_id == vm_id and service.port == port:
                removed_service = self._services.pop(i)
                self._save_state()
                return removed_service
        return None
    
    def get_services(self) -> List[ExposedService]:
        """Get all exposed services."""
        return self._services.copy()
    
    def get_service(self, vm_id: int, port: int) -> Optional[ExposedService]:
        """Get specific service."""
        for service in self._services:
            if service.vm_id == vm_id and service.port == port:
                return service
        return None


class CFPVECommands:
    """Main command handler class."""
    
    def __init__(self):
        self.config: Optional[Config] = None
        self.cf_client: Optional[CloudflareClient] = None
        self.pve_client: Optional[ProxmoxClient] = None
        self.service_manager = ServiceManager()
    
    def _load_config(self) -> None:
        """Load configuration and initialize clients."""
        try:
            self.config = config_manager.get_config()
            
            # Initialize Cloudflare client
            self.cf_client = CloudflareClient(
                api_token=self.config.cloudflare.api_token,
                zone_id=self.config.cloudflare.zone_id,
                account_id=self.config.cloudflare.account_id
            )
            
            # Initialize Proxmox client
            self.pve_client = ProxmoxClient(
                host=self.config.proxmox.host,
                port=self.config.proxmox.port,
                username=self.config.proxmox.username,
                password=self.config.proxmox.password,
                token_name=self.config.proxmox.token_name,
                token_value=self.config.proxmox.token_value,
                verify_ssl=self.config.proxmox.verify_ssl,
                timeout=self.config.proxmox.timeout
            )
            
        except Exception as e:
            typer.echo(f"Error loading configuration: {e}", err=True)
            raise typer.Exit(1)
    
    def init_config(self) -> None:
        """Initialize configuration file."""
        if config_manager.config_exists():
            typer.echo("Configuration file already exists.")
            if not typer.confirm("Do you want to overwrite it?"):
                return
        
        config_manager.create_example_config()
        typer.echo("\n📝 Next steps:")
        typer.echo("1. Set environment variables:")
        typer.echo("   export CF_API_TOKEN='your_cloudflare_token'")
        typer.echo("   export CF_ZONE_ID='your_zone_id'")
        typer.echo("   export PVE_TOKEN='your_proxmox_token'")
        typer.echo("\n2. Edit configuration file if needed:")
        typer.echo(f"   nano {config_manager.config_path}")
        typer.echo("\n3. Test connection:")
        typer.echo("   cf-pve test")
    
    def test_connections(self) -> None:
        """Test API connections."""
        typer.echo("🔍 Testing connections...")
        
        try:
            self._load_config()
            typer.echo("✅ Configuration loaded successfully")
            typer.echo("✅ Cloudflare API connection working")
            typer.echo("✅ Proxmox VE API connection working")
            typer.echo("🎉 All connections are working!")
            
        except Exception as e:
            typer.echo(f"❌ Connection test failed: {e}", err=True)
            raise typer.Exit(1)
    
    def create_tunnel(self, name: str) -> None:
        """Create a new tunnel."""
        self._load_config()
        
        typer.echo(f"🚇 Creating tunnel: {name}")
        tunnel = self.cf_client.create_tunnel(name)
        typer.echo(f"✅ Tunnel created successfully: {tunnel}")
    
    def list_tunnels(self) -> None:
        """List all tunnels."""
        self._load_config()
        
        tunnels = self.cf_client.list_tunnels()
        
        if not tunnels:
            typer.echo("No tunnels found.")
            return
        
        typer.echo("🚇 Tunnels:")
        for tunnel in tunnels:
            status_emoji = "✅" if tunnel.status == "active" else "⏸️"
            typer.echo(f"  {status_emoji} {tunnel.name} (ID: {tunnel.tunnel_id}, Status: {tunnel.status})")
    
    def delete_tunnel(self, name: str) -> None:
        """Delete a tunnel."""
        self._load_config()
        
        if not typer.confirm(f"Are you sure you want to delete tunnel '{name}'?"):
            typer.echo("Cancelled.")
            return
        
        typer.echo(f"🗑️ Deleting tunnel: {name}")
        success = self.cf_client.delete_tunnel(name)
        
        if success:
            # Remove all services using this tunnel
            services_to_remove = [s for s in self.service_manager.get_services() 
                                if s.tunnel_name == name]
            
            for service in services_to_remove:
                self.service_manager.remove_service(service.vm_id, service.port)
                typer.echo(f"  Removed service: VM {service.vm_id}:{service.port}")
    
    def expose_service(self, vm_id: int, port: int, subdomain: str, 
                      protocol: str = "http", tunnel_name: str = "main-tunnel") -> None:
        """Expose a VM service through Cloudflare tunnel."""
        self._load_config()
        
        typer.echo(f"🌐 Exposing VM {vm_id}:{port} as {subdomain}")
        
        # Get VM info
        vm = self.pve_client.get_vm(vm_id)
        if not vm:
            typer.echo(f"❌ VM {vm_id} not found", err=True)
            raise typer.Exit(1)
        
        if not vm.is_running:
            typer.echo(f"⚠️  Warning: VM {vm_id} is not running (status: {vm.status})")
        
        vm_ip = vm.primary_ip
        if not vm_ip:
            typer.echo(f"❌ Could not determine IP address for VM {vm_id}", err=True)
            typer.echo("Make sure the VM has QEMU guest agent installed and running.")
            raise typer.Exit(1)
        
        # Ensure tunnel exists
        tunnel = self.cf_client.get_tunnel(tunnel_name)
        if not tunnel:
            typer.echo(f"Creating tunnel: {tunnel_name}")
            tunnel = self.cf_client.create_tunnel(tunnel_name)
        
        # Create DNS record
        target = f"{tunnel.tunnel_id}.cfargotunnel.com"
        dns_record_id = self.cf_client.create_dns_record(
            name=subdomain,
            content=target,
            record_type="CNAME",
            proxied=self.config.cloudflare.proxy_enabled,
            ttl=self.config.cloudflare.default_ttl
        )
        
        if not dns_record_id:
            typer.echo("❌ Failed to create DNS record", err=True)
            raise typer.Exit(1)
        
        # Create service configuration
        service = ExposedService(
            vm_id=vm_id,
            vm_name=vm.name,
            port=port,
            subdomain=subdomain,
            protocol=protocol,
            tunnel_name=tunnel_name
        )
        
        # Update tunnel configuration
        self._update_tunnel_config(tunnel_name, tunnel.tunnel_id)
        
        # Save service state
        self.service_manager.add_service(service)
        
        typer.echo(f"✅ Service exposed successfully!")
        typer.echo(f"   🖥️  VM: {vm.name} (ID: {vm_id}) at {vm_ip}")
        typer.echo(f"   🌐 URL: https://{subdomain}")
        typer.echo(f"   🚇 Tunnel: {tunnel_name}")
    
    def hide_service(self, vm_id: int, port: int) -> None:
        """Hide an exposed service."""
        self._load_config()
        
        service = self.service_manager.get_service(vm_id, port)
        if not service:
            typer.echo(f"❌ No exposed service found for VM {vm_id}:{port}")
            raise typer.Exit(1)
        
        typer.echo(f"🙈 Hiding service: VM {vm_id}:{port} ({service.subdomain})")
        
        # Remove DNS record
        self.cf_client.delete_dns_record(service.subdomain)
        
        # Remove from state
        self.service_manager.remove_service(vm_id, port)
        
        # Update tunnel configuration
        tunnel = self.cf_client.get_tunnel(service.tunnel_name)
        if tunnel:
            self._update_tunnel_config(service.tunnel_name, tunnel.tunnel_id)
        
        typer.echo(f"✅ Service hidden successfully!")
    
    def list_services(self) -> None:
        """List all exposed services."""
        self._load_config()
        
        services = self.service_manager.get_services()
        
        if not services:
            typer.echo("No exposed services.")
            return
        
        typer.echo("🌐 Exposed services:")
        
        for service in services:
            # Get VM status
            vm = self.pve_client.get_vm(service.vm_id)
            status_emoji = "✅" if vm and vm.status == "running" else "❌"
            vm_status = vm.status if vm else "unknown"
            
            typer.echo(f"  {status_emoji} VM {service.vm_id} ({service.vm_name}):{service.port}")
            typer.echo(f"      🌐 https://{service.subdomain}")
            typer.echo(f"      🚇 Tunnel: {service.tunnel_name}")
            typer.echo(f"      📊 Status: {vm_status}")
            typer.echo()
    
    def _update_tunnel_config(self, tunnel_name: str, tunnel_id: str) -> None:
        """Update tunnel configuration file."""
        services = [s for s in self.service_manager.get_services() 
                   if s.tunnel_name == tunnel_name]
        
        if not services:
            typer.echo(f"No services for tunnel {tunnel_name}, skipping config update")
            return
        
        # Build service configurations
        service_configs = []
        
        for service in services:
            vm = self.pve_client.get_vm(service.vm_id)
            if not vm or not vm.primary_ip:
                typer.echo(f"⚠️  Warning: Could not get IP for VM {service.vm_id}, skipping")
                continue
            
            service_config = {
                "hostname": service.subdomain,
                "protocol": service.protocol,
                "target": f"{vm.primary_ip}:{service.port}",
                "no_tls_verify": service.protocol == "https"  # Disable TLS verification for internal services
            }
            
            service_configs.append(service_config)
        
        if service_configs:
            config_path = self.cf_client.create_tunnel_config(tunnel_id, service_configs)
            typer.echo(f"📝 Updated tunnel configuration: {config_path}")


# Global command handler instance
commands = CFPVECommands()