"""Configuration management for CF-PVE."""

import os
import yaml
from pathlib import Path
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, validator
import typer


class CloudflareConfig(BaseModel):
    """Cloudflare API configuration."""
    api_token: str = Field(..., description="Cloudflare API token")
    zone_id: str = Field(..., description="Cloudflare Zone ID")
    account_id: Optional[str] = Field(None, description="Cloudflare Account ID")
    default_ttl: int = Field(300, description="Default TTL for DNS records")
    proxy_enabled: bool = Field(True, description="Enable Cloudflare proxy")

    @validator('api_token')
    def api_token_not_empty(cls, v):
        if not v or v.startswith('${') and v.endswith('}'):
            # Allow environment variable placeholder
            return v
        if len(v) < 10:
            raise ValueError('API token seems too short')
        return v


class ProxmoxConfig(BaseModel):
    """Proxmox VE API configuration."""
    host: str = Field(..., description="Proxmox VE host")
    port: int = Field(8006, description="Proxmox VE port")
    username: str = Field(..., description="Proxmox VE username")
    password: Optional[str] = Field(None, description="Proxmox VE password")
    token_name: Optional[str] = Field(None, description="API token name")
    token_value: Optional[str] = Field(None, description="API token value")
    verify_ssl: bool = Field(False, description="Verify SSL certificate")
    timeout: int = Field(30, description="Request timeout in seconds")

    @validator('host')
    def host_not_empty(cls, v):
        if not v:
            raise ValueError('Host cannot be empty')
        return v


class TunnelConfig(BaseModel):
    """Tunnel configuration."""
    default_name: str = Field("main-tunnel", description="Default tunnel name")
    config_path: str = Field("/etc/cloudflared/", description="Cloudflared config path")
    auto_create: bool = Field(True, description="Auto-create tunnel if not exists")
    auto_start: bool = Field(True, description="Auto-start tunnel after creation")


class DNSConfig(BaseModel):
    """DNS configuration."""
    zone: Optional[str] = Field(None, description="Default DNS zone")
    auto_cleanup: bool = Field(True, description="Auto cleanup unused DNS records")
    backup_records: bool = Field(False, description="Backup DNS records before changes")


class LoggingConfig(BaseModel):
    """Logging configuration."""
    level: str = Field("INFO", description="Logging level")
    file: Optional[str] = Field(None, description="Log file path")
    max_size_mb: int = Field(10, description="Max log file size in MB")
    backup_count: int = Field(5, description="Number of backup log files")


class Config(BaseModel):
    """Main configuration model."""
    version: str = Field("1.0", description="Configuration version")
    cloudflare: CloudflareConfig
    proxmox: ProxmoxConfig
    tunnel: TunnelConfig = Field(default_factory=TunnelConfig)
    dns: DNSConfig = Field(default_factory=DNSConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)

    def resolve_env_vars(self) -> 'Config':
        """Resolve environment variables in configuration values."""
        config_dict = self.dict()
        
        def resolve_dict(d: Dict[str, Any]) -> Dict[str, Any]:
            for key, value in d.items():
                if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
                    env_var = value[2:-1]  # Remove ${ and }
                    env_value = os.getenv(env_var)
                    if env_value is None:
                        typer.echo(f"Warning: Environment variable {env_var} not set", err=True)
                    else:
                        d[key] = env_value
                elif isinstance(value, dict):
                    d[key] = resolve_dict(value)
            return d
        
        resolved_dict = resolve_dict(config_dict)
        return Config(**resolved_dict)


class ConfigManager:
    """Configuration file manager."""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or self._get_default_config_path()
        self._config: Optional[Config] = None
    
    @staticmethod
    def _get_default_config_path() -> Path:
        """Get default configuration file path."""
        config_dir = Path.home() / ".cf-pve"
        config_dir.mkdir(exist_ok=True)
        return config_dir / "config.yaml"
    
    def load_config(self) -> Config:
        """Load configuration from file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            config_data = yaml.safe_load(f)
        
        self._config = Config(**config_data).resolve_env_vars()
        return self._config
    
    def save_config(self, config: Config) -> None:
        """Save configuration to file."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_path, 'w') as f:
            yaml.dump(config.dict(exclude_none=True), f, default_flow_style=False, indent=2)
        
        # Set restrictive permissions for security
        self.config_path.chmod(0o600)
    
    def get_config(self) -> Config:
        """Get current configuration."""
        if self._config is None:
            self._config = self.load_config()
        return self._config
    
    def config_exists(self) -> bool:
        """Check if configuration file exists."""
        return self.config_path.exists()
    
    def create_example_config(self) -> None:
        """Create example configuration file."""
        example_config = Config(
            cloudflare=CloudflareConfig(
                api_token="${CF_API_TOKEN}",
                zone_id="${CF_ZONE_ID}",
                account_id="${CF_ACCOUNT_ID}"
            ),
            proxmox=ProxmoxConfig(
                host="pve.local.domain",
                username="cf-pve@pve",
                token_name="cf-pve-token",
                token_value="${PVE_TOKEN}"
            )
        )
        
        self.save_config(example_config)
        typer.echo(f"Example configuration created at: {self.config_path}")
        typer.echo("Please edit the configuration file and set your API tokens.")


# Global configuration manager instance
config_manager = ConfigManager()