from importlib import import_module

__all__ = [
    "temporal_split",
    "TemporalSplitter",
    "temporal_graph_split",
    "validate_graph_split",
    "train_link_prediction",
    "train_link_prediction_main",
    "TrainingConfig",
    "EarlyStoppingConfig",
    "TemporalSplitConfig",
    "OptimizerConfig",
    "ONNXConverter",
    "ONNXOptimizer",
    "QuantizationConfig",
    "ContinuousLearningPipeline",
    "ModelVersionManager",
]

_LAZY = {
    "temporal_split": ("mega-header-astroml.training.temporal_split", None),
    "TemporalSplitter": ("mega-header-astroml.training.temporal_split", "TemporalSplitter"),
    "temporal_graph_split": ("mega-header-astroml.training.temporal_split", "temporal_graph_split"),
    "validate_graph_split": ("mega-header-astroml.training.temporal_split", "validate_graph_split"),
    "train_link_prediction": ("mega-header-astroml.training.train_link_prediction", "train_link_prediction"),
    "train_link_prediction_main": ("mega-header-astroml.training.train_link_prediction", "main"),
    "ONNXConverter": ("mega-header-astroml.training.optimization.onnx_converter", "ONNXConverter"),
    "ONNXOptimizer": ("mega-header-astroml.training.optimization.onnx_optimizer", "ONNXOptimizer"),
    "QuantizationConfig": ("mega-header-astroml.training.optimization.quantization", "QuantizationConfig"),
    "TrainingConfig": ("mega-header-astroml.training.config", "TrainingConfig"),
    "EarlyStoppingConfig": ("mega-header-astroml.training.config", "EarlyStoppingConfig"),
    "TemporalSplitConfig": ("mega-header-astroml.training.config", "TemporalSplitConfig"),
    "OptimizerConfig": ("mega-header-astroml.training.config", "OptimizerConfig"),
    "ContinuousLearningPipeline": ("mega-header-astroml.training.continuous_learning", "ContinuousLearningPipeline"),
    "ModelVersionManager": ("mega-header-astroml.training.continuous_learning", "ModelVersionManager"),
}


def __getattr__(name: str):
    if name in _LAZY:
        module_path, attr = _LAZY[name]
        module = import_module(module_path)
        value = getattr(module, attr) if attr else module
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
