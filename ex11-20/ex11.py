# 11. How to bin a numeric series to 10 groups of equal size?
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_series_equal

vals = np.random.random(20)
quantiles = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
mini = vals.min()
maxi = vals.max()
num_bins = 10
bin_width = (maxi - mini) / num_bins
bins = [mini + i * bin_width for i in range(num_bins + 1)]
labels = ["1st", "2nd", "3rd", "4th", "5th",
          "6th", "7th", "8th", "9th", "10th"]
# pandas
pd_ser = pd.Series(vals)
pd_cut = pd.cut(pd_ser, bins=bins, labels=labels, include_lowest=True)

# polars
pl_ser = pl.Series(vals)
pl_cut = pl_ser.cut(bins=bins[1:-1], labels=labels)

assert_series_equal(pl.from_pandas(pd_cut.astype(str)), pl_cut.cast(pl.Utf8))
print("Completed.")
