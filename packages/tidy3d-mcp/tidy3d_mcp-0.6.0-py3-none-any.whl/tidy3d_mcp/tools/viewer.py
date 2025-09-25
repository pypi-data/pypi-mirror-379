from __future__ import annotations

import json
from collections.abc import Iterable
from typing import Any

from fastmcp.exceptions import ToolError

from ..utils import ensure_file_uri
from ._dispatcher import invoke_viewer_command


def _normalize_warnings(raw: object) -> list[str] | None:
    if not raw:
        return None
    if isinstance(raw, str):
        return [raw]
    if isinstance(raw, Iterable):
        normalized = [str(item) for item in raw if item]
        return normalized or None
    return [str(raw)]


async def start_viewer(
    file: str,
    symbol: str | None = None,
    index: int | None = None,
    window_id: str | None = None,
) -> dict[str, Any]:
    """Launch the visual viewer for a simulation definition.

    Args:
        file: Absolute or workspace-relative path to the Python file or notebook cell URI.
        symbol: Optional variable name that holds the `tidy3d.Simulation` to display.
        index: Optional zero-based simulation index when multiple are discovered.
        window_id: Host window identifier returned by previous viewer calls.

    Returns:
        Mapping with the resolved `viewer_id` plus optional `status`, `window_id`, and `warnings`.

    Raises:
        ValueError: If `file` is empty or the viewer does not acknowledge the request.
        ToolError: If the host reports an error while opening the viewer.
    """
    if not file:
        raise ValueError('file is required')
    params: dict = {'file': ensure_file_uri(file)}
    if symbol:
        params['symbol'] = symbol
    if index is not None:
        params['index'] = index
    if window_id:
        params['window'] = window_id
    try:
        result = invoke_viewer_command('start', 'ready', params, timeout=300.0)
    except RuntimeError as exc:
        raise ToolError(f'viewer did not acknowledge start request: {exc}') from exc
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        raise ToolError(f'viewer reported error: {error_msg}')
    viewer_id = result.get('viewer_id')
    if not isinstance(viewer_id, str) or not viewer_id:
        raise ValueError('viewer did not confirm readiness')
    response: dict[str, Any] = {'viewer_id': viewer_id}
    status = result.get('status')
    if isinstance(status, str) and status:
        response['status'] = status
    reported_window = result.get('window_id')
    if isinstance(reported_window, str) and reported_window:
        response['window_id'] = reported_window
    warnings = _normalize_warnings(result.get('warnings') or result.get('warning'))
    if warnings:
        response['warnings'] = warnings
    return response


async def rotate_viewer(
    viewer_id: str,
    direction: str,
    window_id: str | None = None,
) -> dict[str, Any]:
    """Align the viewer camera with a principal axis.

    Args:
        viewer_id: Identifier obtained from `start_viewer`.
        direction: One of `TOP`, `BOTTOM`, `LEFT`, `RIGHT`, `FRONT`, `BACK` (case-insensitive).
        window_id: Optional window scope from previous responses.

    Returns:
        Mapping with `viewer_id`, normalized `direction`, and the reported `status` string.

    Raises:
        ValueError: If `viewer_id` or `direction` are missing or unsupported.
        ToolError: If the viewer fails to apply the rotation.
    """
    if not viewer_id:
        raise ValueError('viewer_id is required')
    if not direction:
        raise ValueError('direction is required')
    normalized = direction.upper()
    allowed = {'TOP', 'BOTTOM', 'LEFT', 'RIGHT', 'FRONT', 'BACK'}
    if normalized not in allowed:
        raise ValueError(f'direction must be one of {sorted(allowed)}')
    params: dict[str, object | None] = {'viewer': viewer_id, 'direction': normalized}
    if window_id:
        params['window'] = window_id
    try:
        result = invoke_viewer_command('rotate', 'rotate', params, timeout=60.0)
    except RuntimeError as exc:
        raise ToolError(f'viewer did not acknowledge rotation: {exc}') from exc
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        raise ToolError(f'rotation failed: {error_msg}')
    status = result.get('status', 'ok')
    return {'viewer_id': viewer_id, 'direction': normalized, 'status': status}


async def show_structures(
    viewer_id: str,
    visibility: list[bool],
    window_id: str | None = None,
) -> dict[str, Any]:
    """Toggle structure visibility using the simulation's declaration order.

    Args:
        viewer_id: Identifier returned by `start_viewer`.
        visibility: Booleans matching the order used in `tidy3d.Simulation(structures=[...])`.
        window_id: Optional window scope from prior responses.

    Returns:
        Mapping with the `viewer_id`, reported `status`, echoed `visibility` list, and optional `window_id`.

    Raises:
        ValueError: If `viewer_id` is missing or visibility cannot be serialized.
        ToolError: If the viewer rejects the visibility update.
    """
    if not viewer_id:
        raise ValueError('viewer_id is required')
    flags = [bool(entry) for entry in visibility]
    payload = json.dumps(flags)
    params: dict[str, object | None] = {'viewer': viewer_id, 'visibility': payload}
    if window_id:
        params['window'] = window_id
    try:
        result = invoke_viewer_command('visibility', 'visibility', params, timeout=60.0)
    except RuntimeError as exc:
        raise ToolError(f'viewer did not acknowledge visibility update: {exc}') from exc
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        raise ToolError(f'visibility update failed: {error_msg}')
    response: dict[str, Any] = {'viewer_id': viewer_id, 'status': result.get('status', 'ok')}
    reported_window = result.get('window_id')
    if isinstance(reported_window, str) and reported_window:
        response['window_id'] = reported_window
    returned_flags = result.get('visibility')
    if isinstance(returned_flags, list):
        response['visibility'] = [bool(entry) for entry in returned_flags]
    return response


async def check_simulation(viewer_id: str, window_id: str | None = None) -> dict[str, Any]:
    """Read the latest validation status from the viewer panel.

    Args:
        viewer_id: Identifier returned by `start_viewer`.
        window_id: Optional window scope from earlier responses.

    Returns:
        Mapping with `viewer_id`, plus any `warnings`, `error`, `status`, or resolved `window_id`.

    Raises:
        ValueError: If `viewer_id` is empty.
        ToolError: If the viewer fails to respond before the timeout.
    """
    if not viewer_id:
        raise ValueError('viewer_id is required')
    params: dict[str, object | None] = {'viewer': viewer_id}
    if window_id:
        params['window'] = window_id
    try:
        result = invoke_viewer_command('check', 'check', params, timeout=60.0)
    except RuntimeError as exc:
        raise ToolError(f'viewer status request timed out: {exc}') from exc
    response: dict[str, Any] = {'viewer_id': viewer_id}
    warnings = _normalize_warnings(result.get('warnings'))
    if warnings is not None:
        response['warnings'] = warnings
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        response['error'] = error_msg
    status = result.get('status')
    if isinstance(status, str) and status:
        response['status'] = status
    reported_window = result.get('window_id')
    if isinstance(reported_window, str) and reported_window:
        response['window_id'] = reported_window
    return response
