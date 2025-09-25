from pathlib import Path

import pandas as pd
from ordeq_pandas import PandasExcel


def test_it_loads(tmp_path: Path, pdf: pd.DataFrame):
    path = tmp_path / "test_it_loads.xlsx"
    pdf.to_excel(path)
    pd.testing.assert_frame_equal(
        PandasExcel(path=path).load(header=0, usecols="B,C"), pdf
    )


def test_it_saves(tmp_path: Path, pdf: pd.DataFrame):
    path = tmp_path / "test_it_saves.xlsx"
    PandasExcel(path=path).save(pdf, header=("key", "value"), index=False)
    pd.testing.assert_frame_equal(pd.read_excel(path), pdf)
