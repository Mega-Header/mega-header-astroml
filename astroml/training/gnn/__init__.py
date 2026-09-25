"""Graph Neural Network (GNN) models and training infrastructure for AstroML."""

from mega-header-astroml.training.gnn.data_loader import (
    GraphDataPreprocessor,
    TransactionGraphDataLoader,
    TransactionGraphDataset,
    create_node_masks,
)
from mega-header-astroml.training.gnn.gat import (
    GATNodeClassifier,
    evaluate_gat,
    train_gat_classifier,
)
from mega-header-astroml.training.gnn.graph_sage import (
    GraphSAGENodeClassifier,
    evaluate_graphsage,
    train_graphsage_classifier,
)

__all__ = [
    "GraphSAGENodeClassifier",
    "train_graphsage_classifier",
    "evaluate_graphsage",
    "GATNodeClassifier",
    "train_gat_classifier",
    "evaluate_gat",
    "GraphDataPreprocessor",
    "create_node_masks",
    "TransactionGraphDataset",
    "TransactionGraphDataLoader",
]
