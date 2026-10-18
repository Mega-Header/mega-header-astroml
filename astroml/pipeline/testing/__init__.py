"""Pipeline testing framework for data quality, schema validation, and integrity checks.

Issue #638: Comprehensive testing framework for data pipelines.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any, Callable, Dict, List, Optional, Union

__all__ = [
    "DataTestSuite",
    "DataTestResult",
    "DataAssertion",
    "SchemaValidator",
    "SchemaValidationResult",
    "IntegrityChecker",
    "IntegrityReport",
    "PipelineFixture",
    "PipelineTestRunner",
    "DataDiffReport",
    "RegressionTest",
]

_LAZY: dict[str, tuple[str, str]] = {
    "DataTestSuite": ("mega-header-astroml.pipeline.testing.data_tests", "DataTestSuite"),
    "DataTestResult": ("mega-header-astroml.pipeline.testing.data_tests", "DataTestResult"),
    "DataAssertion": ("mega-header-astroml.pipeline.testing.data_tests", "DataAssertion"),
    "SchemaValidator": ("mega-header-astroml.pipeline.testing.schema_validator", "SchemaValidator"),
    "SchemaValidationResult": (
        "mega-header-astroml.pipeline.testing.schema_validator",
        "SchemaValidationResult",
    ),
    "IntegrityChecker": ("mega-header-astroml.pipeline.testing.integrity", "IntegrityChecker"),
    "IntegrityReport": ("mega-header-astroml.pipeline.testing.integrity", "IntegrityReport"),
    "PipelineFixture": ("mega-header-astroml.pipeline.testing.fixtures", "PipelineFixture"),
    "PipelineTestRunner": ("mega-header-astroml.pipeline.testing.fixtures", "PipelineTestRunner"),
    "DataDiffReport": ("mega-header-astroml.pipeline.testing.data_tests", "DataDiffReport"),
    "RegressionTest": ("mega-header-astroml.pipeline.testing.data_tests", "RegressionTest"),
}


def __getattr__(name: str):
    if name in _LAZY:
        module_path, attr = _LAZY[name]
        module = import_module(module_path)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
