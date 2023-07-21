# 10. How to keep only top 2 most frequent values as it is
# and replace everything else as ‘Other’?
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_series_equal


vals = np.random.randint(1, 5, [200])

# pandas
ser = pd.Series(vals)
mask = ser.isin(ser.value_counts().head(2).index)
pd_ser = ser.where(mask, "Other")
pd_ser.name = "new"

# polars
ser = pl.Series("new", vals)
mask = ser.is_in(
    ser
    .value_counts()  # transform to DataFrame
    .sort(by="counts", descending=True)
    .limit(2)
    ["new"]  # transform to Series
)
expr = (
    pl.when(mask)
    .then(ser)
    .otherwise("Other")
    .alias("new")
)
pl_ser = ser.to_frame().with_columns(expr)  # DataFrame


assert_series_equal(pl.from_pandas(pd_ser.astype(str)), pl_ser["new"])
print("Completed.")
