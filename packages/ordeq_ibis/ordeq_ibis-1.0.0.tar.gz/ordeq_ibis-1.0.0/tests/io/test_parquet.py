from pathlib import Path

import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisParquet


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_loads(tmp_path: Path, df: pl.DataFrame, resource: str):
    path = tmp_path / "test_it_loads.parquet"
    ibis.connect(resource).to_parquet(ibis.memtable(df), path)
    actual = IbisParquet(path=path, resource=resource).load()
    assert actual.to_polars().equals(df)


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_saves(tmp_path: Path, df: pl.DataFrame, resource: str):
    path = tmp_path / "test_it_saves.parquet"
    IbisParquet(path=path, resource=resource).save(ibis.memtable(df))
    assert pl.read_parquet(path).equals(df)
