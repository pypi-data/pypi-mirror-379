import polars as pl
import pytest


@pytest.fixture
def df() -> pl.DataFrame:
    return pl.DataFrame(
        data=[(1, "Netherlands"), (2, "Belgium"), (3, "Germany")],
        schema=["key", "value"],
        orient="row",
    )
