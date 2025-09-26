# Tidy3D MCP

A local Model Context Protocol (MCP) server that lets clients drive the
Flexcompute Tidy3D viewer and consume viewer artifacts without needing a browser session.

## Capabilities

- Authenticates against the remote FlexAgent MCP endpoint using OAuth.
- Proxies viewer automation commands such as launching the viewer, rotating the camera,
  toggling structure visibility, running simulation health checks, and capturing screenshots.
- Returns viewer captures as MCP images so downstream tools can consume them immediately.

## Requirements

- Python 3.10 or newer
- [`uv`](https://github.com/astral-sh/uv) for dependency management
- Network access to the target FlexAgent MCP deployment (defaults to the hosted
  `https://flexagent.dev-simulation.cloud/` endpoint)

## Installation

```bash
uv sync
```

This resolves the project environment and installs the `tidy3d-mcp` console entry point.

## Usage

Start the server from the project root:

```bash
uv run tidy3d-mcp
```

The server listens on stdio for MCP requests and forwards them to the remote FlexAgent server. The
first invocation prompts OAuth consent in a browser, then stores the token under the cache location
shown in [Configuration](#configuration).

### Integrating with MCP Hosts

- **VS Code / Cursor**: Select the "Tidy3D MCP" binary (`uv run tidy3d-mcp`) when
  configuring an stdio MCP provider.
- **Custom hosts**: Launch the command above and connect using the Model Context Protocol over the
  process stdio pipes.

## Configuration

Environment variables control the server at startup:

| Variable | Purpose | Default |
| --- | --- | --- |
| `REMOTE_MCP_URL` | Target MCP endpoint to proxy. | `https://flexagent.dev-simulation.cloud/` |

OAuth tokens persist under `~/.fastmcp/oauth-mcp-client-cache/<endpoint>/<workspace>` to avoid
re-authentication per session. Delete the cache directory to force a new OAuth consent flow.

## Tools Exposed to Clients

| Tool | Description |
| --- | --- |
| `start_viewer` | Launches the viewer for a simulation file and returns the resolved `viewer_id`. |
| `rotate_viewer` | Rotates the active viewer toward the requested direction (e.g. `TOP`, `BOTTOM`). |
| `show_structures` | Applies a boolean visibility array to the current viewer structures. |
| `capture` | Captures the current frame of the viewer. |
| `check_simulation` | Returns validation warnings or errors reported by the viewer. |

## Development Tips

- Run `uv run ruff check` to lint the project and `uv run ruff format` to apply formatting.
- The server relies on `fastmcp.as_proxy`; consult the upstream FastMCP documentation for advanced
  configuration such as custom authentication flows or additional transports.
- When debugging viewer interactions, inspect the returned `data_url` to confirm that capture
  payloads reach the client.

## Troubleshooting

- **OAuth consent window never opens**: Ensure the machine can launch a browser and that pop-up
  blockers allow the OAuth window.
- **Viewer fails to start**: Verify the simulation file exists, the MCP host provides the correct
  working directory, and the remote FlexAgent endpoint is reachable.
