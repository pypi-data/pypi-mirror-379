import zoneinfo
from datetime import datetime, date
from uuid import UUID

import polars
import pytest


def test_to_polars(transaction, temperature):
    if transaction.flavor != "postgresql":
        pytest.skip("Sqlite not supported with polars")

    # Upsert
    temperature.upsert("timestamp", "city", "value").executemany(
        [
            ("1970-01-02", "Berlin", 10),
            ("1970-01-02", "London", 12),
        ]
    )
    # Read data
    df = temperature.select().to_polars()
    columns = df.collect_schema().names()
    assert columns == ["timestamp", "city", "value"]
    # to_polars return a LazyFrame, we matertialize it
    df = df.collect()
    assert sorted(df['city']) == ["Berlin", "London"]

    # Read with custom arg
    cond = "(= value {})"
    df = temperature.select().where(cond).to_polars(12).collect()
    assert list(df.columns) == ["timestamp", "city", "value"]
    assert sorted(df['city']) == ["London"]


def test_from_polars(transaction, kitchensink):
    if transaction.flavor != "postgresql":
        pytest.skip("Sqlite not supported with polars")
    df = polars.LazyFrame(
        {
            "varchar": ["ham"],
            "bigint": [1],
            "float": [1.0],
            "int": [1],
            "timestamp": ["1970-01-01 00:00:00"],
            "timestamptz": ["1970-01-01 00:00:00+00:00"],
            "bool": [True],
            "date": ["1970-01-01"],
            "json": [{}],
            "uuid": ["F1172BD3-0A1D-422E-8ED6-8DC2D0F8C11C"],
            "max": ["max"],
            "true": ["true"],
            "blob": [b"blob"],
        }
    )

    # UPSERT
    kitchensink.upsert().from_polars(df)
    (row,) = kitchensink.select()
    BRUTZ = zoneinfo.ZoneInfo(key="Europe/Brussels")
    assert row == (
        "ham",
        1,
        1.0,
        1,
        datetime(1970, 1, 1, 0, 0),
        datetime(1970, 1, 1, 1, 0, tzinfo=BRUTZ),
        True,
        date(1970, 1, 1),
        {},
        UUID("F1172BD3-0A1D-422E-8ED6-8DC2D0F8C11C"),
        "max",
        "true",
        b"blob",
    )

    # SELECT with operator
    new_df = kitchensink.select(
        "(date_bin '5 days' timestamptz '1900-01-01')",
    ).to_polars().collect()

    new_df.columns = ["ts"]
    ts = new_df['ts']
    assert str(ts.dtype) == "Datetime(time_unit='us', time_zone='Europe/Brussels')"

    assert ts[0].isoformat() == '1969-12-30T01:00:00+01:00'
