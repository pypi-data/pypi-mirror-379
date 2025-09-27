# src/sundew/__init__.py
"""Sundew: bio-inspired, energy-aware selective activation."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from .config import SundewConfig
from .config_presets import get_preset, list_presets
from .core import ProcessingResult as CoreProcessingResult, SundewAlgorithm
from .demo import run_demo
from .runtime import PipelineRuntime, build_legacy_runtime, build_simple_runtime

# Expose a robust __version__ that works in editable installs too
try:
    __version__ = version("sundew-algorithms")
except PackageNotFoundError:
    __version__ = "0.7.1"

# Maintain backwards compatible names for core results
ProcessingResult = CoreProcessingResult

__all__ = [
    "SundewAlgorithm",
    "SundewConfig",
    "ProcessingResult",
    "PipelineRuntime",
    "build_legacy_runtime",
    "build_simple_runtime",
    "get_preset",
    "list_presets",
    "run_demo",
    "__version__",
]
