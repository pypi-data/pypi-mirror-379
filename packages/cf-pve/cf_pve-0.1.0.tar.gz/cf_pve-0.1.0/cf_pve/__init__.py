"""
CF-PVE: Cloudflare + Proxmox VE Integration Tool

A simple CLI tool for automating Proxmox VE integration with Cloudflare ecosystem.
Allows easy management of tunnels, DNS records and automatic service exposure.
"""

__version__ = "0.1.0"
__author__ = "m3wory"
__email__ = "m3wory19@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/m3wory/cf-pve"

from .main import app

__all__ = ["app"]