from __future__ import annotations

from typing import Any

_STATE_BY_VIEWER: dict[str, dict[str, Any]] = {}


def remember(viewer_id: str | None, *, window_id: str | None = None, focusable: bool = False) -> None:
    if not viewer_id:
        return
    state = _STATE_BY_VIEWER.setdefault(viewer_id, {})
    if window_id:
        state['window_id'] = window_id
    if focusable:
        state['focusable'] = focusable


def resolve_window(viewer_id: str | None, explicit: str | None = None) -> str | None:
    if explicit:
        remember(viewer_id, window_id=explicit)
        return explicit
    if viewer_id:
        state = _STATE_BY_VIEWER.get(viewer_id)
        if state and isinstance(state.get('window_id'), str):
            return state['window_id']
    return None


def is_focus_only(viewer_id: str | None) -> bool:
    if not viewer_id:
        return False
    state = _STATE_BY_VIEWER.get(viewer_id)
    return bool(state and state.get('focusable'))


def forget(viewer_id: str | None) -> None:
    if viewer_id and viewer_id in _STATE_BY_VIEWER:
        del _STATE_BY_VIEWER[viewer_id]
