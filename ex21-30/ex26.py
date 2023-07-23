# 26. How to get the mean of a series grouped by another series?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal
import numpy as np


# Compute the mean of weights of each fruit.
fruits = np.random.choice(['apple', 'banana', 'carrot'], 10)
weights = np.linspace(1, 10, 10)

# pandas
pd_fruits = pd.Series(fruits)
pd_weights = pd.Series(weights, name="weights")
pd_ser = pd_weights.groupby(pd_fruits).mean()

# polars
pl_ser = (
    pl.Series("weights", weights)
    .to_frame()
    .groupby(pl.Series(fruits))
    .mean()
)["weights"]

assert_series_equal(pl.from_pandas(pd_ser), pl_ser)

print("Completed.")
