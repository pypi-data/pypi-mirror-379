from pathlib import Path

import polars as pl
from ordeq_polars import PolarsLazyParquet


def test_it_loads(tmp_path: Path, lf: pl.LazyFrame):
    path = tmp_path / "test_it_loads.parquet"
    lf.sink_parquet(path)
    assert PolarsLazyParquet(path=path).load().collect().equals(lf.collect())


def test_it_saves(tmp_path: Path, lf: pl.LazyFrame):
    path = tmp_path / "test_it_saves.parquet"
    PolarsLazyParquet(path=path).save(lf)
    assert pl.read_parquet(path).equals(lf.collect())
