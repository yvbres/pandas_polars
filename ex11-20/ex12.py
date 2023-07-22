# 12. How to convert a numpy array to a dataframe of given shape? (L1)
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal

# Reshape the series ser into a dataframe with 7 rows and 5 columns
import numpy as np
cols = ["1", "2", "3", "4", "5"]

for _ in range(10):  # try 10 times due to randomness

    vals = np.random.randint(1, 10, 35)

    # pandas
    pd_ser = pd.Series(vals)
    pd_df = pd.DataFrame(pd_ser.values.reshape(7, 5), columns=cols)

    # polars
    pl_ser = pl.Series(vals)
    pl_df = pl.DataFrame(pl_ser.to_numpy().reshape(7, 5), cols)

    assert_frame_equal(pl.from_pandas(pd_df), pl_df)

print("Completed.")
