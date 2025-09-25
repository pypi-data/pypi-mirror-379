from pathlib import Path

import pandas as pd
from ordeq_pandas import PandasCSV


def test_it_loads(tmp_path: Path, pdf: pd.DataFrame):
    path = tmp_path / "test_it_loads.csv"
    pdf.to_csv(path, index=False)
    actual = PandasCSV(path=path).load(header=0)
    pd.testing.assert_frame_equal(actual, pdf)


def test_it_saves(tmp_path: Path, pdf: pd.DataFrame):
    path = tmp_path / "test_it_saves.csv"
    PandasCSV(path=path).save(pdf, header=("key", "value"), index=False)
    pd.testing.assert_frame_equal(pd.read_csv(path), pdf)
