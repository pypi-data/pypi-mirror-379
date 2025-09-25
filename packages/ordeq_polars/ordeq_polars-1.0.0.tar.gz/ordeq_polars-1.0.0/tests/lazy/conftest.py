import polars as pl
import pytest


@pytest.fixture
def lf() -> pl.LazyFrame:
    return pl.LazyFrame(
        data=[(1, "Netherlands"), (2, "Belgium"), (3, "Germany")],
        schema=["key", "value"],
        orient="row",
    )
