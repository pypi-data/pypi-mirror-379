from pathlib import Path

import polars as pl
from ordeq_polars import PolarsEagerParquet


def test_it_loads(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads.parquet"
    df.write_parquet(path)
    actual = PolarsEagerParquet(path=path).load()
    assert actual.equals(df)


def test_it_saves(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves.parquet"
    PolarsEagerParquet(path=path).save(df)
    assert pl.read_parquet(path).equals(df)
