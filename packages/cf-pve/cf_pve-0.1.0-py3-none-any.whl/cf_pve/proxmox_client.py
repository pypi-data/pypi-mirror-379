"""Proxmox VE API client for CF-PVE."""

from typing import Dict, List, Optional, Any
from proxmoxer import ProxmoxAPI
import typer


class ProxmoxVM:
    """Represents a Proxmox VE virtual machine."""
    
    def __init__(self, vmid: int, name: str, status: str, node: str, ip_addresses: List[str] = None):
        self.vmid = vmid
        self.name = name
        self.status = status
        self.node = node
        self.ip_addresses = ip_addresses or []
    
    @property
    def primary_ip(self) -> Optional[str]:
        """Get the primary IP address (first non-localhost IP)."""
        for ip in self.ip_addresses:
            if ip and ip != "127.0.0.1" and not ip.startswith("::"):
                return ip
        return None
    
    def __repr__(self):
        return f"ProxmoxVM(id={self.vmid}, name={self.name}, status={self.status}, ip={self.primary_ip})"


class ProxmoxClient:
    """Client for interacting with Proxmox VE API."""
    
    def __init__(self, host: str, username: str, password: Optional[str] = None,
                 token_name: Optional[str] = None, token_value: Optional[str] = None,
                 port: int = 8006, verify_ssl: bool = False, timeout: int = 30):
        
        self.host = host
        self.port = port
        self.verify_ssl = verify_ssl
        
        try:
            # Initialize API client
            if token_name and token_value:
                # Use API token authentication
                self.proxmox = ProxmoxAPI(
                    host, user=username, token_name=token_name, token_value=token_value,
                    port=port, verify_ssl=verify_ssl, timeout=timeout
                )
                auth_method = f"API token ({username}!{token_name})"
            elif password:
                # Use password authentication
                self.proxmox = ProxmoxAPI(
                    host, user=username, password=password,
                    port=port, verify_ssl=verify_ssl, timeout=timeout
                )
                auth_method = f"password ({username})"
            else:
                raise ValueError("Either password or token_name+token_value must be provided")
            
            # Test connection
            self._validate_connection()
            typer.echo(f"Connected to Proxmox VE at {host}:{port} using {auth_method}")
            
        except Exception as e:
            typer.echo(f"Failed to connect to Proxmox VE: {e}", err=True)
            raise typer.Exit(1)
    
    def _validate_connection(self) -> None:
        """Validate API connection and permissions."""
        try:
            # Test connection by getting cluster status
            version = self.proxmox.version.get()
            typer.echo(f"Proxmox VE version: {version.get('version', 'unknown')}")
            
        except Exception as e:
            typer.echo(f"Proxmox API validation failed: {e}", err=True)
            raise
    
    def get_nodes(self) -> List[Dict[str, Any]]:
        """Get list of cluster nodes."""
        try:
            nodes = self.proxmox.nodes.get()
            return nodes
        except Exception as e:
            typer.echo(f"Error getting nodes: {e}", err=True)
            return []
    
    def list_vms(self, node: Optional[str] = None) -> List[ProxmoxVM]:
        """List all VMs across all nodes or specific node."""
        vms = []
        
        try:
            if node:
                nodes = [{"node": node}]
            else:
                nodes = self.get_nodes()
            
            for node_info in nodes:
                node_name = node_info["node"]
                
                try:
                    # Get VMs on this node
                    vm_list = self.proxmox.nodes(node_name).qemu.get()
                    
                    for vm_data in vm_list:
                        vmid = vm_data["vmid"]
                        name = vm_data.get("name", f"vm-{vmid}")
                        status = vm_data.get("status", "unknown")
                        
                        # Get detailed VM info including network
                        vm = ProxmoxVM(
                            vmid=vmid,
                            name=name,
                            status=status,
                            node=node_name
                        )
                        
                        # Try to get IP addresses
                        if status == "running":
                            vm.ip_addresses = self._get_vm_ip_addresses(node_name, vmid)
                        
                        vms.append(vm)
                        
                except Exception as e:
                    typer.echo(f"Error getting VMs from node {node_name}: {e}", err=True)
                    continue
            
            return vms
            
        except Exception as e:
            typer.echo(f"Error listing VMs: {e}", err=True)
            return []
    
    def get_vm(self, vmid: int, node: Optional[str] = None) -> Optional[ProxmoxVM]:
        """Get specific VM by ID."""
        try:
            if node:
                # Check specific node
                try:
                    vm_data = self.proxmox.nodes(node).qemu(vmid).status.current.get()
                    return self._create_vm_from_data(vm_data, node, vmid)
                except:
                    return None
            else:
                # Search all nodes
                nodes = self.get_nodes()
                for node_info in nodes:
                    node_name = node_info["node"]
                    try:
                        vm_data = self.proxmox.nodes(node_name).qemu(vmid).status.current.get()
                        return self._create_vm_from_data(vm_data, node_name, vmid)
                    except:
                        continue
                return None
                
        except Exception as e:
            typer.echo(f"Error getting VM {vmid}: {e}", err=True)
            return None
    
    def _create_vm_from_data(self, vm_data: Dict[str, Any], node: str, vmid: int) -> ProxmoxVM:
        """Create ProxmoxVM object from API data."""
        name = vm_data.get("name", f"vm-{vmid}")
        status = vm_data.get("status", "unknown")
        
        vm = ProxmoxVM(
            vmid=vmid,
            name=name,
            status=status,
            node=node
        )
        
        # Get IP addresses if VM is running
        if status == "running":
            vm.ip_addresses = self._get_vm_ip_addresses(node, vmid)
        
        return vm
    
    def _get_vm_ip_addresses(self, node: str, vmid: int) -> List[str]:
        """Get IP addresses for a VM."""
        ip_addresses = []
        
        try:
            # Try to get network interfaces from agent
            try:
                agent_info = self.proxmox.nodes(node).qemu(vmid).agent('network-get-interfaces').get()
                
                if agent_info and 'result' in agent_info:
                    for interface in agent_info['result']:
                        if 'ip-addresses' in interface:
                            for ip_info in interface['ip-addresses']:
                                if ip_info.get('ip-address-type') == 'ipv4':
                                    ip = ip_info.get('ip-address')
                                    if ip and ip != '127.0.0.1':
                                        ip_addresses.append(ip)
                
                return ip_addresses
                
            except:
                # Fallback: try to get IPs from config/status
                pass
            
            # Alternative method: parse network configuration
            try:
                config = self.proxmox.nodes(node).qemu(vmid).config.get()
                
                # Look for network device configurations
                for key, value in config.items():
                    if key.startswith('net') and isinstance(value, str):
                        # This is a basic approach - in real scenarios, 
                        # you might need more sophisticated IP detection
                        pass
                        
            except:
                pass
            
            # If no IPs found, try to guess based on VM ID (development helper)
            if not ip_addresses:
                # This is just for development - remove in production
                # Common pattern: 192.168.1.{100+vmid}
                potential_ip = f"192.168.1.{100 + vmid}"
                typer.echo(f"⚠️  No IP detected for VM {vmid}, using assumed IP: {potential_ip}")
                ip_addresses.append(potential_ip)
            
        except Exception as e:
            typer.echo(f"Error getting IP addresses for VM {vmid}: {e}", err=True)
        
        return ip_addresses
    
    def get_vm_status(self, vmid: int, node: Optional[str] = None) -> Optional[str]:
        """Get VM status."""
        vm = self.get_vm(vmid, node)
        return vm.status if vm else None
    
    def is_vm_running(self, vmid: int, node: Optional[str] = None) -> bool:
        """Check if VM is running."""
        status = self.get_vm_status(vmid, node)
        return status == "running"
    
    def search_vms(self, name_pattern: str) -> List[ProxmoxVM]:
        """Search VMs by name pattern."""
        all_vms = self.list_vms()
        matching_vms = []
        
        name_pattern = name_pattern.lower()
        
        for vm in all_vms:
            if (name_pattern in vm.name.lower() or 
                name_pattern in str(vm.vmid)):
                matching_vms.append(vm)
        
        return matching_vms
    
    def get_vm_config(self, vmid: int, node: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Get VM configuration."""
        try:
            vm = self.get_vm(vmid, node)
            if not vm:
                return None
            
            config = self.proxmox.nodes(vm.node).qemu(vmid).config.get()
            return config
            
        except Exception as e:
            typer.echo(f"Error getting VM {vmid} config: {e}", err=True)
            return None