"""Automated data profiling and exploratory analysis.

Generates comprehensive exploratory data analysis reports with statistics,
visualizations and insights for tabular datasets.
"""

from mega-header-astroml.preprocessing.profiling.data_profiler import (
    ColumnProfile,
    DataProfiler,
    DataProfileResult,
)
from mega-header-astroml.preprocessing.profiling.insights import (
    Insight,
    InsightGenerator,
)
from mega-header-astroml.preprocessing.profiling.report_generator import ReportGenerator
from mega-header-astroml.preprocessing.profiling.visualizations import ProfilingVisualizer

__all__ = [
    "ColumnProfile",
    "DataProfileResult",
    "DataProfiler",
    "Insight",
    "InsightGenerator",
    "ReportGenerator",
    "ProfilingVisualizer",
]
