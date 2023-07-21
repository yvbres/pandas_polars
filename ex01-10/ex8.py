# 8. How to get the minimum, 25th percentile, median,
# 75th, and max of a numeric series?
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_series_equal

random = np.random.normal(10, 5, 25)
# pandas
ser = pd.Series(random)
pd_stats = pd.Series([
    ser.min(),
    ser.quantile(0.25),
    ser.median(),
    ser.quantile(0.75),
    ser.max()
])

# polars
ser = pl.Series(random)
pl_stats = pl.Series([
    ser.min(),
    ser.quantile(0.25),
    ser.median(),
    ser.quantile(0.75),
    ser.max()
])


assert_series_equal(pl.from_pandas(pd_stats), pl_stats)
print("Completed.")
