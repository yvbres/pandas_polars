# 7. How to get the items not common to both series A and series B?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal

# pandas
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser1_2 = ser1[~ser1.isin(ser2)]
ser2_1 = ser2[~ser2.isin(ser1)]
pd_diff = pd.Series([ser1_2, ser2_1]).explode()

# polars
ser1 = pl.Series([1, 2, 3, 4, 5])
ser2 = pl.Series([4, 5, 6, 7, 8])
ser1_2 = ser1.filter(~ser1.is_in(ser2))
ser2_1 = ser2.filter(~ser2.is_in(ser1))
pl_diff = pl.Series([ser1_2, ser2_1]).explode()

assert_series_equal(pl.from_pandas(pd_diff), pl_diff)
print("Completed.")
