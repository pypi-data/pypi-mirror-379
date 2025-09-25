from pathlib import Path

import pandas as pd
from ordeq_pandas import PandasParquet


def test_it_loads(tmp_path: Path, pdf: pd.DataFrame):
    path = tmp_path / "test_it_loads.parquet"
    pdf.to_parquet(path)
    actual = PandasParquet(path=path).load()
    pd.testing.assert_frame_equal(actual, pdf)


def test_it_saves(tmp_path: Path, pdf):
    path = tmp_path / "test_it_saves.parquet"
    PandasParquet(path=path).save(pdf)
    pd.testing.assert_frame_equal(pd.read_parquet(path), pdf)
