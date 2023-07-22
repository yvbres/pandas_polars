# 13. How to find the positions of numbers
# that are multiples of 3 from a series?
import pandas as pd
import polars as pl
import numpy as np

for _ in range(1_000):
    vals = np.random.randint(1, 10, 7)
    # pandas
    pd_ser = pd.Series(vals)
    pd_mask = (pd_ser % 3 == 0)
    pd_idxs = pd_ser[pd_mask].index.tolist()

    # polars
    pl_ser  = pl.Series("vals", vals)
    pl_mask = (pl_ser % 3 == 0)

    pl_idxs = (
        pl_ser
        .to_frame().with_row_count(name="index")
        .filter(pl_mask)
        ["index"]  # get Series, to transform to list
        .to_list()
    )

    assert sorted(pd_idxs) == sorted(pl_idxs)

print("Completed.")
