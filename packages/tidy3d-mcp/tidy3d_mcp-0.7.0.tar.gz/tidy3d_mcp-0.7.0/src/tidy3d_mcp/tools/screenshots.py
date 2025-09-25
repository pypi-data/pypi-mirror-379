from __future__ import annotations

from base64 import b64decode
from typing import Any

from fastmcp.exceptions import ToolError
from fastmcp.tools.tool import ToolResult
from fastmcp.utilities.types import Image

from ._dispatcher import invoke_viewer_command


def _image_from_data_url(data_url: str) -> Image:
    if not isinstance(data_url, str) or not data_url.startswith('data:'):
        raise ValueError('invalid data URL')
    header, _, payload = data_url.partition(',')
    if not payload:
        raise ValueError('invalid data URL')
    meta = header[5:]
    if ';' in meta:
        mime, _ = meta.split(';', 1)
    else:
        mime = meta
    try:
        raw = b64decode(payload, validate=True)
    except ValueError as exc:
        raise ValueError('invalid data URL') from exc
    format_hint = None
    if '/' in mime:
        subtype = mime.split('/', 1)[1]
        if subtype:
            format_hint = subtype.split('+', 1)[0]
    return Image(data=raw, format=format_hint)


async def capture(
    viewer_id: str,
    window_id: str | None = None,
) -> ToolResult:
    """Capture a viewer frame and return it as image content.

    Args:
        viewer_id: Identifier reported by `start_viewer`.
        window_id: Optional editor window scope returned by previous calls.

    Returns:
        ToolResult containing an image content block and structured metadata with
        `viewer_id`, `data_url`, and (when known) `window_id` plus `mime_type`.

    Raises:
        ValueError: If `viewer_id` is empty.
        ToolError: If the viewer cannot produce a capture payload.
    """
    if not viewer_id:
        raise ValueError('viewer_id is required')
    params: dict[str, object | None] = {'viewer': viewer_id}
    if window_id:
        params['window'] = window_id
    try:
        result = invoke_viewer_command('capture', 'shot', params, timeout=180.0)
    except RuntimeError as exc:
        raise ToolError(f'viewer did not respond to capture request: {exc}') from exc
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        raise ToolError(f'viewer reported error: {error_msg}')
    data_url = result.get('data_url')
    if not isinstance(data_url, str) or not data_url:
        raise ToolError('viewer did not return capture data')
    try:
        image = _image_from_data_url(data_url)
    except ValueError as exc:
        raise ToolError('viewer returned invalid image data') from exc
    structured: dict[str, Any] = {'viewer_id': viewer_id, 'data_url': data_url}
    mime_type = data_url[5:data_url.find(';')] if ';' in data_url else data_url[5:]
    if mime_type:
        structured['mime_type'] = mime_type
    reported_window = result.get('window_id')
    if isinstance(reported_window, str) and reported_window:
        structured['window_id'] = reported_window
    return ToolResult(
        content=[image.to_image_content(mime_type=mime_type or None)],
        structured_content=structured,
    )
