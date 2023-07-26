# 32. How to compute the autocorrelations of a numeric series?
import pandas as pd
import polars as pl
import numpy as np


# Compute autocorrelations for the first 10 lags of ser.
# Find out which lag has the largest correlation.
vals = np.arange(20) + np.random.normal(1, 10, 20)

# pandas
ser = pd.Series(vals)
pd_corrs = pd.Series(ser.autocorr(i) for i in range(1, 11))
pd_max_corr = pd_corrs.argmax()

# polars
pl_df = pl.DataFrame({"vals": vals}).with_columns(
    pl.col("vals").shift(1).alias("vals1"),
    pl.col("vals").shift(2).alias("vals2"),
    pl.col("vals").shift(3).alias("vals3"),
    pl.col("vals").shift(4).alias("vals4"),
    pl.col("vals").shift(5).alias("vals5"),
    pl.col("vals").shift(6).alias("vals6"),
    pl.col("vals").shift(7).alias("vals7"),
    pl.col("vals").shift(8).alias("vals8"),
    pl.col("vals").shift(9).alias("vals9"),
    pl.col("vals").shift(10).alias("vals10"),
)
pl_corrs = pl.Series(np.corrcoef(pl_df.to_numpy()))
print("Not the same ... Missing native autocorrelation method in polars.")
