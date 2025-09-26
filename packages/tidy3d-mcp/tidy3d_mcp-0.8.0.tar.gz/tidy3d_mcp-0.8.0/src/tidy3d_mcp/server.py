from __future__ import annotations

import argparse
import hashlib
import os
import re
from pathlib import Path
from urllib.parse import urlparse

from fastmcp import FastMCP, settings as fastmcp_settings
from fastmcp.client.auth.oauth import OAuth
from fastmcp.server.proxy import ProxyClient
from fastmcp.tools import Tool

from .tools import (
    configure_dispatcher,
    capture,
    check_simulation,
    rotate_viewer,
    show_structures,
    start_viewer,
)


def _sanitize_identifier(value: str | None) -> str:
    if not value:
        return ''
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', value).strip('_')
    return slug


def _proxy_name_for_host(host: str | None) -> str:
    if not host:
        return 'Tidy3D'
    formatted = host.replace('_', ' ').strip()
    return f'Tidy3D ({formatted.title()})'


def _cache_dir_for_mcp(
    url: str,
    *,
    workdir: Path | None = None,
    host: str | None = None,
    window_id: str | None = None,
) -> Path:
    """Return an OAuth cache directory keyed by endpoint, workspace, host, and window."""
    parsed = urlparse(url)
    slug_source = f'{parsed.scheme}://{parsed.netloc}{parsed.path}'
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', slug_source).strip('_') or 'default'
    digest = hashlib.sha256(url.encode('utf-8')).hexdigest()[:12]

    base = (workdir or Path.cwd()).resolve()
    workspace_key = str(base)
    workspace_digest = hashlib.sha256(workspace_key.encode('utf-8')).hexdigest()[:12]
    workspace_label_source = (
        base.name or re.sub(r'[^a-zA-Z0-9]+', '_', base.anchor).strip('_') or 'workspace'
    )
    workspace_slug = re.sub(r'[^a-zA-Z0-9]+', '_', workspace_label_source).strip('_') or 'workspace'
    host_slug = _sanitize_identifier(host)
    window_slug = _sanitize_identifier(window_id)
    extras = '_'.join(filter(None, (host_slug, window_slug)))
    workspace_label = f'{workspace_slug}_{extras}' if extras else workspace_slug

    return (
        fastmcp_settings.home
        / 'oauth-mcp-client-cache'
        / f'{slug}_{digest}'
        / f'{workspace_label}_{workspace_digest}'
    )


def main(argv: list[str] | None = None):
    """Launch the FastMCP proxy with host-aware bookkeeping."""
    parser = argparse.ArgumentParser(prog='tidy3d-mcp')
    parser.add_argument('--host', choices=('vscode', 'cursor'), default=None)
    parser.add_argument('--window-id', default=None)
    args = parser.parse_args(argv)

    configure_dispatcher(args.host, args.window_id)
    mcp_url = os.getenv('REMOTE_MCP_URL', 'https://flexagent.dev-simulation.cloud/')
    cache_dir = _cache_dir_for_mcp(
        mcp_url,
        workdir=Path.cwd(),
        host=args.host,
        window_id=args.window_id,
    )
    oauth = OAuth(mcp_url=mcp_url, token_storage_cache_dir=cache_dir)
    proxy_name = _proxy_name_for_host(args.host)
    proxy = FastMCP.as_proxy(ProxyClient(mcp_url, auth=oauth), name=proxy_name)

    proxy.add_tool(Tool.from_function(start_viewer))
    proxy.add_tool(Tool.from_function(capture))
    proxy.add_tool(Tool.from_function(rotate_viewer))
    proxy.add_tool(Tool.from_function(show_structures))
    proxy.add_tool(Tool.from_function(check_simulation))

    proxy.run()


if __name__ == '__main__':
    main()
