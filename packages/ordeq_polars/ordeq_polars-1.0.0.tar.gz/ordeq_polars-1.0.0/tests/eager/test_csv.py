from pathlib import Path

import polars as pl
from ordeq_polars import PolarsEagerCSV


def test_it_loads(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads.csv"
    df.write_csv(path)
    actual = PolarsEagerCSV(path=path).load()
    assert actual.equals(df)


def test_it_saves(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves.csv"
    PolarsEagerCSV(path=path).save(df)
    assert pl.read_csv(path).equals(df)
