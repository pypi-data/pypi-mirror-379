"""Canonical preprocessing toolkit for TimesTrader Story 1.7 pipelines."""

from __future__ import annotations

import sys

__version__ = "1.1.2"
__author__ = "TimeStrader Team"
__email__ = "team@timestrader.ai"


def is_colab_environment() -> bool:
    """Detect if running in a Google Colab notebook."""

    return "google.colab" in sys.modules


def is_jupyter_environment() -> bool:
    """Detect if running in a generic Jupyter notebook session."""

    try:
        from IPython import get_ipython

        return get_ipython() is not None
    except ImportError:
        return False


ENVIRONMENT_INFO = {
    "is_colab": is_colab_environment(),
    "is_jupyter": is_jupyter_environment(),
    "package_version": __version__,
    "python_version": sys.version,
    "canonical_indicators": (
        "vwap",
        "rsi",
        "atr",
        "ema9",
        "ema21",
        "stochastic",
    ),
}

from timestrader_preprocessing.common.models import (
    DataQualityMetrics,
    NormalizationParams,
    ProcessingConfig,
)
from timestrader_preprocessing.config.defaults import (
    ColabConfig,
    ParameterManager,
    ProductionConfig,
    get_default_config,
)
from timestrader_preprocessing.historical.processor import HistoricalProcessor
from timestrader_preprocessing.realtime.streaming import RealtimeNormalizer

from importlib import import_module as _import_module

# Expose subpackages so dotted patch paths resolve during testing.
historical = _import_module("timestrader_preprocessing.historical")
common = _import_module("timestrader_preprocessing.common")
config = _import_module("timestrader_preprocessing.config")
realtime = _import_module("timestrader_preprocessing.realtime")


__all__ = [
    "HistoricalProcessor",
    "RealtimeNormalizer",
    "ParameterManager",
    "ColabConfig",
    "ProductionConfig",
    "get_default_config",
    "NormalizationParams",
    "DataQualityMetrics",
    "ProcessingConfig",
    "is_colab_environment",
    "is_jupyter_environment",
    "ENVIRONMENT_INFO",
    "historical",
    "common",
    "config",
    "realtime",
]
