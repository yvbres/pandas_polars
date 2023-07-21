# 4. How to combine many series to form a dataframe?
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_frame_equal

# pandas
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
pd_df = pd.DataFrame({
    "col1": ser1,
    "col2": ser2,
})

# polars
ser1 = pl.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pl.Series(np.arange(26))

pl_df = pl.DataFrame({
    "col1": ser1,
    "col2": ser2,
})

assert_frame_equal(pl.from_pandas(pd_df), pl_df)
print("Completed.")
