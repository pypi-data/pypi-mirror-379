# src/tinyargs/core.py

from __future__ import annotations

import sys
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple, Type, Union

__all__ = ["get", "flag", "args", "TinyArgsError"]


# ==============================================================================
# Errors
# ==============================================================================

class TinyArgsError(Exception):
    """Custom error for missing or invalid arguments."""


# ==============================================================================
# Constants / literals
# ==============================================================================

_TRUE_LITERALS = {"1", "true", "yes", "on"}
_FALSE_LITERALS = {"0", "false", "no", "off"}


# ==============================================================================
# Low-level helpers
# ==============================================================================

def _is_long_flag(token: str) -> bool:
    """Return True for tokens like --name, --port=8080, --verbose."""
    return token.startswith("--")


def _has_equal(token: str) -> bool:
    """Return True if the token is of the form --key=value."""
    return "=" in token


def _split_kv(token: str) -> Tuple[str, str]:
    """Split a --key=value token into (key, value). Assumes '=' present."""
    key, val = token.split("=", 1)
    return key, val


def _next_is_value(argv: Sequence[str], i: int) -> bool:
    """True if argv[i+1] exists and does not look like a flag token."""
    return (i + 1) < len(argv) and not _is_long_flag(argv[i + 1])


def _has_real_value(val: Any) -> bool:
    """
    True only if a value was actually supplied (not a bare flag).
    Treat empty string as missing as well.
    """
    if val is True:
        return False
    if val is None:
        return False
    if isinstance(val, str) and val == "":
        return False
    return True


def _cast_bool(value: Any) -> bool:
    """
    Conservative bool casting:
    - bare presence (True) stays True
    - common string literals map to True/False
    """
    if value is True:
        return True
    if isinstance(value, str):
        v = value.strip().lower()
        if v in _TRUE_LITERALS:
            return True
        if v in _FALSE_LITERALS:
            return False
    raise TinyArgsError(f"Could not cast {value!r} to bool")


def _cast(value: Any, typ: Type) -> Any:
    """Cast value to typ with clear error messaging."""
    if typ is bool:
        return _cast_bool(value)
    try:
        return typ(value)
    except Exception as exc:
        raise TinyArgsError(f"Could not cast {value!r} to {getattr(typ, '__name__', typ)}") from exc


# ==============================================================================
# argv parsing
# ==============================================================================

def _parse_argv(argv: Optional[Sequence[str]] = None) -> Dict[str, Any]:
    """
    Parse argv into a dict of {flag: value}.

    Rules:
    - --key=value      -> { "--key": "value" }
    - --key value      -> { "--key": "value" }
    - --flag           -> { "--flag": True }
    """
    if argv is None:
        argv = sys.argv[1:]

    out: Dict[str, Any] = {}
    i = 0
    while i < len(argv):
        token = argv[i]
        if _is_long_flag(token):
            if _has_equal(token):
                key, val = _split_kv(token)
                out[key] = val
            elif _next_is_value(argv, i):
                out[token] = argv[i + 1]
                i += 1
            else:
                # bare presence → treated as boolean flag
                out[token] = True
        # else: ignore non-flag tokens (positional args are out of scope for TinyArgs)
        i += 1
    return out


# ==============================================================================
# Public API
# ==============================================================================

def get(key: str, type: Type = str, default: Any = None, required: bool = False) -> Any:
    """
    Fetch a single argument by key.

    - Casts to 'type' if provided (bool uses conservative casting via _cast_bool)
    - Returns 'default' if missing (unless required=True)
    - Errors if present but valueless (e.g., '--key' without value) and type is not bool
    """
    data = _parse_argv()

    if key not in data:
        if required:
            raise TinyArgsError(f"Missing required argument: {key}")
        return default

    value = data[key]

    # Present but no actual value (not a bool request)
    if not _has_real_value(value) and type is not bool:
        if required:
            raise TinyArgsError(f"Argument {key} requires a value")
        return default

    return _cast(value, type)


def flag(key: str) -> bool:
    """
    Return True if the flag is present (as a bare presence or with any value), else False.
    Intended for boolean presence checks like --verbose or --dry-run.
    """
    data = _parse_argv()
    return bool(data.get(key, False))


def args(
    *keys: str,
    types: Optional[Mapping[str, Type]] = None,
    defaults: Optional[Mapping[str, Any]] = None,
    required: Optional[Iterable[str]] = None,
) -> Tuple[Any, ...]:
    """
    Fetch multiple arguments at once. Returns a tuple in the same order as 'keys'.

    Behavior mirrors 'get' per-key:
    - Missing + required → TinyArgsError
    - Present but valueless and not bool → TinyArgsError (if required) or default
    - Casting via 'types' mapping (bool uses conservative casting)
    """
    data = _parse_argv()
    types = dict(types or {})
    defaults = dict(defaults or {})
    required_set = set(required or [])

    results: List[Any] = []
    for k in keys:
        if k not in data:
            if k in required_set:
                raise TinyArgsError(f"Missing required argument: {k}")
            results.append(defaults.get(k))
            continue

        value = data[k]
        typ = types.get(k, str)

        if not _has_real_value(value) and typ is not bool:
            if k in required_set:
                raise TinyArgsError(f"Argument {k} requires a value")
            results.append(defaults.get(k))
            continue

        results.append(_cast(value, typ))

    return tuple(results)
