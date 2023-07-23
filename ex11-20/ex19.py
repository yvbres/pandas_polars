# 19. How to calculate the number of characters in each word in a series?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal


chars = ['how', 'to', 'kick', 'ass?']

# pandas
pd_ser = pd.Series(chars).str.len()

# polars
pl_ser = pl.Series(chars).str.lengths()

assert_series_equal(pl.from_pandas(pd_ser), pl_ser.cast(pl.Int64))

print("Completed.")
