from typing import Any, Callable, Dict, List, Optional, Union

"""API routers for AstroML services."""

from __future__ import annotations

from importlib import import_module

__all__ = [
    "accounts",
    "compression",
    "data_quality",
    "feature_selection",
    "features",
    "federated",
    "fraud",
    "model_registry",
    "validation",
]


def __getattr__(name: str) -> Any:
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
