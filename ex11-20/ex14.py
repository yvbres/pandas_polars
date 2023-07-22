# 14. How to extract items at given positions from a series
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal


vals = list('abcdefghijklmnopqrstuvwxyz')
pos = [0, 4, 8, 14, 20]

# pandas
pd_ser = pd.Series(vals)[pos]
pd_ser.name = "vals"

# polars
pl_ser = pl.Series("vals", vals)
pl_ser = (
    pl_ser
    .to_frame().with_row_count("index")
    .filter(
        pl.col("index").is_in(pos)
    )
    ["vals"]
)

assert_series_equal(pl.from_pandas(pd_ser), pl_ser)
print("Completed.")
