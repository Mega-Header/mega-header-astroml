"""Federated learning framework for privacy-preserving distributed model training."""

from mega-header-astroml.training.federated.aggregator import (
    AggregationAlgorithm,
    AggregatorFactory,
    BaseAggregator,
    ClientUpdate,
    FedAvgAggregator,
    FedProxAggregator,
    KrumAggregator,
    MedianAggregator,
    TrimmedMeanAggregator,
)
from mega-header-astroml.training.federated.client import (
    DPConfig,
    FederatedClient,
)
from mega-header-astroml.training.federated.secure_aggregation import (
    MaskedUpdate,
    SecureAggregator,
)
from mega-header-astroml.training.federated.server import (
    ClientSelectionStrategy,
    DataVolumeWeightedSelector,
    FederatedServer,
    RandomClientSelector,
    RoundResult,
    RoundRobinSelector,
)

__all__ = [
    # Client
    "FederatedClient",
    "DPConfig",
    "ClientUpdate",
    # Server & selection
    "FederatedServer",
    "RoundResult",
    "ClientSelectionStrategy",
    "RandomClientSelector",
    "DataVolumeWeightedSelector",
    "RoundRobinSelector",
    # Aggregators
    "AggregationAlgorithm",
    "BaseAggregator",
    "FedAvgAggregator",
    "FedProxAggregator",
    "TrimmedMeanAggregator",
    "MedianAggregator",
    "KrumAggregator",
    "AggregatorFactory",
    # Secure Aggregation
    "SecureAggregator",
    "MaskedUpdate",
]
