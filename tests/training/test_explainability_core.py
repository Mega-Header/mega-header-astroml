from mega-header-astroml.preprocessing.feature_importance import FeatureImportance
from mega-header-astroml.training.explainability import Explainability


def test_explain() -> None:
    assert Explainability().explain() == "explanation"
    assert FeatureImportance().compute() == []
