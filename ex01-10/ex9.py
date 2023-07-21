# How to get frequency counts of unique items of a series?
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_series_equal

vals = np.take(list('abcdefgh'), np.random.randint(8, size=30))
# pandas
ser = pd.Series(vals)
pd_count = ser.value_counts()
pd_count.name = "counts"

# polars
ser = pl.Series(vals)
pl_count = ser.value_counts().sort(by="counts", descending=True)  # DataFrame

assert_series_equal(pl.from_pandas(pd_count), pl_count["counts"].cast(pl.Int64))
print("Completed.")
