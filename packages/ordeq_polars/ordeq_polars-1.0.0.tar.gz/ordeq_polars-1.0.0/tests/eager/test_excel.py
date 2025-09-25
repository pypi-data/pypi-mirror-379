from pathlib import Path

import polars as pl
from ordeq_polars import PolarsEagerExcel


def test_it_loads(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads.xlsx"
    df.write_excel(path)
    assert PolarsEagerExcel(path=path).load().equals(df)


def test_it_saves(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves.xlsx"
    PolarsEagerExcel(path=path).save(df)
    assert pl.read_excel(path).equals(df)
