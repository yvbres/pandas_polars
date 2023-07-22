# 15. How to stack two series vertically and horizontally ?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal, assert_frame_equal

# Stack ser1 and ser2 vertically and horizontally (to form a dataframe).

# pandas
ser1 = pd.Series(range(5), name="num")
ser2 = pd.Series(list('abcde'), name="char")

pd_vert = pd.concat([ser1.astype(str), ser2], axis=0)
pd_vert.name = ser1.name
pd_hori = pd.concat([ser1, ser2], axis=1)

# polars
ser1 = pl.Series("num", range(5))
ser2 = pl.Series("char", list('abcde'))

pl_vert = pl.concat([ser1.cast(pl.Utf8), ser2], how="vertical")
pl_hori = pl.concat([ser1.to_frame(), ser2.to_frame()],
                    how="horizontal")


assert_series_equal(pl.from_pandas(pd_vert), pl_vert)
assert_frame_equal(pl.from_pandas(pd_hori), pl_hori)

print("Completed.")
