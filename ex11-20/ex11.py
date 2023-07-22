# 11. How to bin a numeric series to 10 groups of equal size?
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_series_equal


LABELS = ["1st", "2nd", "3rd", "4th", "5th",
          "6th", "7th", "8th", "9th", "10th"]


def get_bins(vals: np.ndarray) -> list[int]:
    mini = vals.min()
    maxi = vals.max()
    num_bins = 10
    bin_width = (maxi - mini) / num_bins
    bins = [mini + i * bin_width for i in range(num_bins + 1)]
    # due to rounding, it may have been computed lower than actual maxi
    bins[-1] = float(maxi)
    return bins


for _ in range(1_000):  # try multiple times due to randomness
    vals = np.random.random(20)

    bins = get_bins(vals)
    # pandas
    pd_ser = pd.Series(vals)
    pd_cut = pd.cut(pd_ser, bins=bins, labels=LABELS, include_lowest=True)

    # polars
    pl_ser = pl.Series(vals)
    pl_cut = pl_ser.cut(bins=bins[1:-1], labels=LABELS)

    assert_series_equal(
        pl.from_pandas(pd_cut.astype(str)),
        pl_cut.cast(pl.Utf8)
    )

print("Completed.")
