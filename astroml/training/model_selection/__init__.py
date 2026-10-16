"""Automated model selection and architecture search toolkit.

Provides an AutoML pipeline, a neural architecture search framework,
meta-learning based recommendations and a model benchmarking suite.
"""

from mega-header-astroml.training.model_selection.automl import (
    AutoMLConfig,
    AutoMLPipeline,
    AutoMLResult,
)
from mega-header-astroml.training.model_selection.benchmark import (
    BenchmarkResult,
    ModelBenchmark,
)
from mega-header-astroml.training.model_selection.meta_learning import (
    ExperienceRecord,
    MetaLearningRecommender,
    TaskDescriptor,
)
from mega-header-astroml.training.model_selection.nas import (
    ArchitectureSpec,
    NASResult,
    NeuralArchitectureSearch,
)

__all__ = [
    "AutoMLConfig",
    "AutoMLPipeline",
    "AutoMLResult",
    "BenchmarkResult",
    "ModelBenchmark",
    "ExperienceRecord",
    "MetaLearningRecommender",
    "TaskDescriptor",
    "ArchitectureSpec",
    "NASResult",
    "NeuralArchitectureSearch",
]
