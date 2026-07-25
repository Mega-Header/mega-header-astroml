"""LLM Observability — distributed tracing, metrics, logging, and audit.

Resolves #456: Full observability stack for LLM services including
request tracing, performance metrics, structured logging, and audit trails.
"""
from mega-header-astroml.llm.observability.tracer import LLMTracer, TraceSpan
from mega-header-astroml.llm.observability.logger import LLMStructuredLogger
from mega-header-astroml.llm.observability.metrics import LLMMetrics
from mega-header-astroml.llm.observability.profiler import LLMProfiler, ProfileResult
from mega-header-astroml.llm.observability.audit import LLMAuditLog, LLMAuditEntry
from mega-header-astroml.llm.observability.debugger import LLMDebugger

__all__ = [
    "LLMTracer",
    "TraceSpan",
    "LLMStructuredLogger",
    "LLMMetrics",
    "LLMProfiler",
    "ProfileResult",
    "LLMAuditLog",
    "LLMAuditEntry",
    "LLMDebugger",
]
