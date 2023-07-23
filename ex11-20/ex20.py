# 20. How to compute difference of differences between
# consequtive numbers of a series?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal


vals = [1, 3, 6, 10, 15, 21, 27, 35]

# pandas
pd_ser = pd.Series(vals).diff()

# polars
pl_ser = pl.Series(vals).diff()

assert_series_equal(pl.from_pandas(pd_ser), pl_ser.cast(pl.Float64))

print("Completed.")
