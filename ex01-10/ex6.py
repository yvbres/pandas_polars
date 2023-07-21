# 6. How to get the items of series A not present in series B?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal

# pandas
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
pd_diff = ser1[~ser1.isin(ser2)]

# polars
ser1 = pl.Series([1, 2, 3, 4, 5])
ser2 = pl.Series([4, 5, 6, 7, 8])
pl_diff = ser1.filter(~ser1.is_in(ser2))

assert_series_equal(pl.from_pandas(pd_diff), pl_diff)
print("Completed.")
