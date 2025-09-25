from __future__ import annotations

from base64 import b64decode
from typing import Any

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
) -> dict[str, Any]:
    """Capture the current frame for `viewer_id` and return it as an MCP image."""
    params: dict[str, object | None] = {'viewer': viewer_id}
    if window_id:
        params['window'] = window_id
    result = invoke_viewer_command('capture', 'shot', params, timeout=180.0)
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        raise RuntimeError(f'Viewer reported error: {error_msg}')
    data_url = result.get('data_url')
    if not isinstance(data_url, str) or not data_url:
        raise RuntimeError('No screenshot was produced')
    try:
        image = _image_from_data_url(data_url)
    except ValueError as exc:
        raise RuntimeError('Viewer returned invalid image data') from exc
    response: dict[str, Any] = {'viewer_id': viewer_id, 'image': image, 'data_url': data_url}
    reported_window = result.get('window_id')
    if isinstance(reported_window, str) and reported_window:
        response['window_id'] = reported_window
    return response

