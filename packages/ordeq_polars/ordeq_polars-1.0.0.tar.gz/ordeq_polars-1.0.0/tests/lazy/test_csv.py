from pathlib import Path

import polars as pl
from ordeq_polars import PolarsLazyCSV
from polars import LazyFrame


def test_it_loads(tmp_path: Path, lf: LazyFrame):
    path = tmp_path / "test_it_loads.csv"
    lf.sink_csv(path)
    assert PolarsLazyCSV(path=path).load().collect().equals(lf.collect())


def test_it_saves(tmp_path: Path, lf: LazyFrame):
    path = tmp_path / "test_it_saves.json"
    PolarsLazyCSV(path=path).save(lf)
    assert pl.read_csv(path).equals(lf.collect())
