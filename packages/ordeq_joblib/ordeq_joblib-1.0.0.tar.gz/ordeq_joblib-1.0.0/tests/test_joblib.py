from pathlib import Path

import joblib
from ordeq_joblib import Joblib


class TestJoblib:
    def test_it_loads(self, tmp_path: Path):
        value = 12345
        path = tmp_path / "test_it_loads"
        with path.open(mode="wb") as fh:
            joblib.dump(value, fh)
        job = Joblib(path=path)
        assert job.load() == value

    def test_it_saves(self, tmp_path: Path):
        value = 12345
        path = tmp_path / "test_it_saves"
        job = Joblib(path=path)
        job.save(value)
        with path.open(mode="rb") as fh:
            assert joblib.load(fh) == value
