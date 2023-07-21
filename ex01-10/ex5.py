# 5. How to assign name to the series’ index?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal

name = "alphabets"

# pandas
pd_ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
pd_ser.name = name

# polars
pl_ser = pl.Series(name, list('abcedfghijklmnopqrstuvwxyz'))

assert_series_equal(pl.from_pandas(pd_ser), pl_ser)
print("Completed.")
