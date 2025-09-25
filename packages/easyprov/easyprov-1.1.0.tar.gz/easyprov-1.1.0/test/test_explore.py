from pathlib import Path

from easyprov.direnv import DirEnv
from easyprov.explore import produce

pth = Path("data_explore.py")
params = {"scale": "scale", "zone": "ZONE"}


def test_produce_parses_all_paths():
    with DirEnv(Path(__file__).parent):
        pths = [pth_res.name for pth_res in produce(pth, params)]
        assert "data_zone.csv" in pths
        assert "data_scale_zone.svg" in pths
        assert "data_scale.json" in pths
        assert "data_scale.rst" in pths
