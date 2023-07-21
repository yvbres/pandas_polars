# 3. How to convert the index of a series into a column of a dataframe?
from polars.testing import assert_frame_equal
import numpy as np
import pandas as pd
import polars as pl

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# pandas
ser = pd.Series(mydict)
df = pd.DataFrame(
    {
        "idx": ser.index,
        "vals": ser.values
    }, index=range(len(ser))
)

# polars
pl_ser = pl.Series("ser", [mydict])
pl_df = (
    pl_ser
    .to_frame()  # transform to pl.DataFrame
    .unnest("ser")  # transform Struct to pair col/value
    .melt()
    .rename({"variable": "idx", "value": "vals"})
)

assert_frame_equal(pl.from_pandas(df), pl_df)
print("Completed.")
