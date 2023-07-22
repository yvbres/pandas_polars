# 10. How to keep only top 2 most frequent values as it is
# and replace everything else as ‘Other’?
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_series_equal

for _ in range(1_000):  # try multiple times due to randomness

    vals = np.random.randint(1, 5, [100])

    # pandas
    pd_ser = pd.Series(vals)
    # to handle case of 3 most frequent, we sort by both count and value
    counts = (
        pd_ser
        .value_counts().to_frame()
        .reset_index(names=["val"])
        .sort_values(by=["count", "val"], ascending=False)
    )
    mask = pd_ser.isin(counts["val"].head(2))
    pd_ser = pd_ser.where(mask, "Other")
    pd_ser.name = "new"

    # polars
    pl_ser = pl.Series("new", vals)
    mask = pl_ser.is_in(
        pl_ser
        .value_counts()  # transform to DataFrame
        .sort(by=["counts", "new"], descending=True)
        .limit(2)
        ["new"]  # transform to Series
    )
    expr = (
        pl.when(mask)
        .then(pl_ser)
        .otherwise("Other")
        .alias("new")
    )
    pl_ser = pl_ser.to_frame().with_columns(expr)  # DataFrame

    assert_series_equal(pl.from_pandas(pd_ser.astype(str)), pl_ser["new"])

print("Completed.")
