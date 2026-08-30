"""Inference pipelines for AstroML."""

from __future__ import annotations

from importlib import import_module

__all__ = [
    "InductiveGraphSAGE",
    "InductiveAnomalyScorer",
    "SchemaContract",
    "QualityContract",
    "SemanticContract",
    "ContractVerifier",
    "DataFlowDiagram",
    "ModelCard",
    "ModelCardBuilder",
    "PipelineDocGenerator",
    "PipelineMetadata",
]

_LAZY: dict[str, tuple[str, str]] = {
    "InductiveGraphSAGE": ("mega-header-astroml.pipeline.inductive", "InductiveGraphSAGE"),
    "InductiveAnomalyScorer": ("mega-header-astroml.pipeline.scoring", "InductiveAnomalyScorer"),
    "SchemaContract": ("mega-header-astroml.pipeline.contracts.schema_contract", "SchemaContract"),
    "QualityContract": ("mega-header-astroml.pipeline.contracts.quality_contract", "QualityContract"),
    "SemanticContract": ("mega-header-astroml.pipeline.contracts.semantic_contract", "SemanticContract"),
    "ContractVerifier": ("mega-header-astroml.pipeline.contracts.verifier", "ContractVerifier"),
    "DataFlowDiagram": ("mega-header-astroml.pipeline.documentation.data_flow", "DataFlowDiagram"),
    "ModelCard": ("mega-header-astroml.pipeline.documentation.model_card", "ModelCard"),
    "ModelCardBuilder": ("mega-header-astroml.pipeline.documentation.model_card", "ModelCardBuilder"),
    "PipelineDocGenerator": ("mega-header-astroml.pipeline.documentation.generator", "PipelineDocGenerator"),
    "PipelineMetadata": ("mega-header-astroml.pipeline.documentation.generator", "PipelineMetadata"),
}


def __getattr__(name: str):
    if name in _LAZY:
        module_path, attr = _LAZY[name]
        module = import_module(module_path)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
