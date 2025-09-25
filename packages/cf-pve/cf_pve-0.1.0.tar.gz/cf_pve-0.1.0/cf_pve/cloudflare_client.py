"""Cloudflare API client for CF-PVE."""

import json
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Any
from cloudflare import Cloudflare
import typer


class CloudflareTunnel:
    """Represents a Cloudflare tunnel."""
    
    def __init__(self, tunnel_id: str, name: str, status: str = "inactive"):
        self.tunnel_id = tunnel_id
        self.name = name
        self.status = status
    
    def __repr__(self):
        return f"CloudflareTunnel(id={self.tunnel_id}, name={self.name}, status={self.status})"


class CloudflareClient:
    """Client for interacting with Cloudflare API."""
    
    def __init__(self, api_token: str, zone_id: str, account_id: Optional[str] = None):
        self.api_token = api_token
        self.zone_id = zone_id
        self.account_id = account_id
        self.cf = Cloudflare(api_token=api_token)
        
        # Validate connection on initialization
        self._validate_connection()
    
    def _validate_connection(self) -> None:
        """Validate API connection and permissions."""
        try:
            # Test API token by getting user info
            user = self.cf.user.get()
            typer.echo(f"Connected to Cloudflare as: {user.email}")
            
            # Validate zone access
            zone = self.cf.zones.get(zone_id=self.zone_id)
            typer.echo(f"Zone access confirmed: {zone.name}")
            
        except Exception as e:
            typer.echo(f"Cloudflare API Error: {e}", err=True)
            raise typer.Exit(1)
    
    def create_tunnel(self, name: str) -> CloudflareTunnel:
        """Create a new Cloudflare tunnel."""
        try:
            # Use cloudflared CLI to create tunnel
            result = subprocess.run([
                'cloudflared', 'tunnel', 'create', name
            ], capture_output=True, text=True, check=True)
            
            # Parse tunnel ID from output
            # Expected format: "Created tunnel <name> with id <tunnel_id>"
            output_lines = result.stderr.split('\n')
            tunnel_id = None
            
            for line in output_lines:
                if 'Created tunnel' in line and 'with id' in line:
                    tunnel_id = line.split('with id ')[-1].strip()
                    break
            
            if not tunnel_id:
                raise Exception("Could not parse tunnel ID from cloudflared output")
            
            typer.echo(f"✅ Created tunnel: {name} (ID: {tunnel_id})")
            return CloudflareTunnel(tunnel_id=tunnel_id, name=name, status="created")
            
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr or str(e)
            if "already exists" in error_msg.lower():
                typer.echo(f"⚠️  Tunnel '{name}' already exists")
                # Try to get existing tunnel info
                return self.get_tunnel(name)
            else:
                typer.echo(f"Failed to create tunnel: {error_msg}", err=True)
                raise typer.Exit(1)
        except Exception as e:
            typer.echo(f"Error creating tunnel: {e}", err=True)
            raise typer.Exit(1)
    
    def list_tunnels(self) -> List[CloudflareTunnel]:
        """List all tunnels."""
        try:
            result = subprocess.run([
                'cloudflared', 'tunnel', 'list'
            ], capture_output=True, text=True, check=True)
            
            tunnels = []
            lines = result.stdout.split('\n')[1:]  # Skip header
            
            for line in lines:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 3:
                        tunnel_id = parts[0]
                        name = parts[1]
                        status = parts[2] if len(parts) > 2 else "unknown"
                        tunnels.append(CloudflareTunnel(tunnel_id, name, status))
            
            return tunnels
            
        except subprocess.CalledProcessError as e:
            typer.echo(f"Failed to list tunnels: {e.stderr}", err=True)
            return []
        except Exception as e:
            typer.echo(f"Error listing tunnels: {e}", err=True)
            return []
    
    def get_tunnel(self, name: str) -> Optional[CloudflareTunnel]:
        """Get tunnel by name."""
        tunnels = self.list_tunnels()
        for tunnel in tunnels:
            if tunnel.name == name:
                return tunnel
        return None
    
    def delete_tunnel(self, name: str) -> bool:
        """Delete a tunnel."""
        try:
            # First, cleanup the tunnel (remove DNS records, etc.)
            subprocess.run([
                'cloudflared', 'tunnel', 'cleanup', name
            ], check=False)  # Don't fail if cleanup fails
            
            # Delete the tunnel
            result = subprocess.run([
                'cloudflared', 'tunnel', 'delete', name
            ], capture_output=True, text=True, check=True)
            
            typer.echo(f"✅ Deleted tunnel: {name}")
            return True
            
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr or str(e)
            if "not found" in error_msg.lower():
                typer.echo(f"⚠️  Tunnel '{name}' not found")
                return False
            else:
                typer.echo(f"Failed to delete tunnel: {error_msg}", err=True)
                return False
        except Exception as e:
            typer.echo(f"Error deleting tunnel: {e}", err=True)
            return False
    
    def create_tunnel_config(self, tunnel_id: str, services: List[Dict[str, Any]], 
                           config_path: Optional[Path] = None) -> Path:
        """Create tunnel configuration file."""
        if config_path is None:
            config_path = Path(f"/etc/cloudflared/{tunnel_id}.yml")
        
        config = {
            "tunnel": tunnel_id,
            "credentials-file": f"/etc/cloudflared/{tunnel_id}.json",
            "ingress": []
        }
        
        # Add service ingress rules
        for service in services:
            ingress_rule = {
                "hostname": service["hostname"],
                "service": f"{service['protocol']}://{service['target']}"
            }
            
            # Add path if specified
            if service.get("path") and service["path"] != "/":
                ingress_rule["path"] = service["path"]
            
            # Add origin request options if needed
            if service.get("no_tls_verify", False):
                ingress_rule["originRequest"] = {"noTLSVerify": True}
            
            config["ingress"].append(ingress_rule)
        
        # Add catch-all rule
        config["ingress"].append({"service": "http_status:404"})
        
        # Add additional settings
        config.update({
            "metrics": "0.0.0.0:8082",
            "loglevel": "info"
        })
        
        # Create config directory
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write configuration
        import yaml
        with open(config_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, indent=2)
        
        typer.echo(f"✅ Created tunnel configuration: {config_path}")
        return config_path
    
    def start_tunnel(self, tunnel_name: str) -> bool:
        """Start a tunnel."""
        try:
            # Start tunnel as daemon
            subprocess.run([
                'cloudflared', 'tunnel', '--config', 
                f'/etc/cloudflared/{tunnel_name}.yml', 'run'
            ], check=True)
            
            typer.echo(f"✅ Started tunnel: {tunnel_name}")
            return True
            
        except subprocess.CalledProcessError as e:
            typer.echo(f"Failed to start tunnel: {e}", err=True)
            return False
        except Exception as e:
            typer.echo(f"Error starting tunnel: {e}", err=True)
            return False
    
    def create_dns_record(self, name: str, content: str, record_type: str = "CNAME", 
                         proxied: bool = True, ttl: int = 300) -> Optional[str]:
        """Create a DNS record."""
        try:
            record_data = {
                "name": name,
                "type": record_type,
                "content": content,
                "ttl": ttl
            }
            
            # Only set proxied for supported record types
            if record_type in ["A", "AAAA", "CNAME"]:
                record_data["proxied"] = proxied
            
            result = self.cf.dns.records.create(zone_id=self.zone_id, **record_data)
            typer.echo(f"✅ Created DNS record: {name} → {content}")
            return result.id
            
        except Exception as e:
            if "already exists" in str(e).lower():
                typer.echo(f"⚠️  DNS record '{name}' already exists")
                return self.get_dns_record_id(name)
            else:
                typer.echo(f"Failed to create DNS record: {e}", err=True)
                return None
    
    def delete_dns_record(self, name: str) -> bool:
        """Delete a DNS record by name."""
        try:
            record_id = self.get_dns_record_id(name)
            if not record_id:
                typer.echo(f"⚠️  DNS record '{name}' not found")
                return False
            
            self.cf.dns.records.delete(zone_id=self.zone_id, dns_record_id=record_id)
            typer.echo(f"✅ Deleted DNS record: {name}")
            return True
            
        except Exception as e:
            typer.echo(f"Error deleting DNS record: {e}", err=True)
            return False
    
    def get_dns_record_id(self, name: str) -> Optional[str]:
        """Get DNS record ID by name."""
        try:
            records = self.cf.dns.records.list(zone_id=self.zone_id, name=name)
            if records.result:
                return records.result[0].id
            return None
            
        except Exception as e:
            typer.echo(f"Error getting DNS record: {e}", err=True)
            return None
    
    def list_dns_records(self) -> List[Dict[str, Any]]:
        """List all DNS records in the zone."""
        try:
            records = self.cf.dns.records.list(zone_id=self.zone_id)
            return [record.__dict__ for record in records.result] if records.result else []
            
        except Exception as e:
            typer.echo(f"Error listing DNS records: {e}", err=True)
            return []