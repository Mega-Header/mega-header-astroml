from mega-header-astroml.preprocessing.synthetic.generator import SyntheticGenerator
from mega-header-astroml.preprocessing.synthetic.gan import GAN
from mega-header-astroml.preprocessing.synthetic.statistical import StatisticalModel
def test_synthetic_all() -> None:
    s = SyntheticGenerator()
    assert s.generate() == []
    g = GAN()
    g.train()
    m = StatisticalModel()
    m.fit()
