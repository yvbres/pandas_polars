# 18. How to convert the first character of each element
# in a series to uppercase?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal

# Change the first character of each word to upper case in each word of ser.

chars = ['how', 'to', 'kick', 'ass?']

# pandas
pd_ser = pd.Series(chars, name="chars").str.title()

# polars
pl_ser = pl.Series("chars", chars).str.to_titlecase()

assert_series_equal(pl.from_pandas(pd_ser), pl_ser)

print("Completed.")
