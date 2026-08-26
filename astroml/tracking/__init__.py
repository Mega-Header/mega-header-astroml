"""Tracking utilities (metrics, usage, experiment tracking, data lineage, etc)."""

# ---------------------------------------------------------------------------
# Imports & Package Exports
# ---------------------------------------------------------------------------
from __future__ import annotations

from importlib import import_module

from .ab_testing import ABTestingFramework
from .experiment_dashboard import (
    Experiment,
    ExperimentDashboard,
    ExperimentReport,
)
from .llm_usage_tracker import (
    LLMPrices,
    LLMUsage,
    LLMUsageTracker,
    default_llm_usage_tracker,
)
from .mlflow_tracker import MLflowTracker
from .model_registry import ModelRegistry
from .run_comparator import RunComparator, RunMetrics
from .visualizations import ChartData, ExperimentVisualizer

__all__ = [
    "ABTestingFramework",
    "Experiment",
    "ExperimentDashboard",
    "ExperimentReport",
    "MLflowTracker",
    "ModelRegistry",
    "LLMUsage",
    "LLMPrices",
    "LLMUsageTracker",
    "default_llm_usage_tracker",
    "RunComparator",
    "RunMetrics",
    "ChartData",
    "ExperimentVisualizer",
    "DataLineageTracker",
    "ProvenanceTracker",
    "LineageVisualizer",
    "MetadataStore",
    "Budget",
    "BudgetManager",
    "BudgetPeriod",
    "CostRecord",
    "CostTracker",
    "ResourceOptimizer",
    "ResourceType",
    "ResourceUsageSample",
    "default_cost_tracker",
]

_LAZY: dict[str, tuple[str, str]] = {
    "DataLineageTracker": ("mega-header-astroml.tracking.lineage.data_lineage", "DataLineageTracker"),
    "ProvenanceTracker": ("mega-header-astroml.tracking.lineage.provenance", "ProvenanceTracker"),
    "LineageVisualizer": ("mega-header-astroml.tracking.lineage.visualizer", "LineageVisualizer"),
    "MetadataStore": ("mega-header-astroml.tracking.lineage.metadata_store", "MetadataStore"),
    "Budget": ("mega-header-astroml.tracking.budget_manager", "Budget"),
    "BudgetManager": ("mega-header-astroml.tracking.budget_manager", "BudgetManager"),
    "BudgetPeriod": ("mega-header-astroml.tracking.budget_manager", "BudgetPeriod"),
    "CostRecord": ("mega-header-astroml.tracking.cost_tracker", "CostRecord"),
    "CostTracker": ("mega-header-astroml.tracking.cost_tracker", "CostTracker"),
    "ResourceType": ("mega-header-astroml.tracking.cost_tracker", "ResourceType"),
    "default_cost_tracker": ("mega-header-astroml.tracking.cost_tracker", "default_cost_tracker"),
    "ResourceOptimizer": ("mega-header-astroml.tracking.resource_optimizer", "ResourceOptimizer"),
    "ResourceUsageSample": ("mega-header-astroml.tracking.resource_optimizer", "ResourceUsageSample"),
}


def __getattr__(name: str):
    if name in _LAZY:
        module_path, attr = _LAZY[name]
        module = import_module(module_path)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
