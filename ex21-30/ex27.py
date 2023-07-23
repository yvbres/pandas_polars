# 27. How to compute the euclidean distance between two series?
import pandas as pd
import polars as pl

p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# pandas
pd_euc = (
    (
        (pd.Series(q) - pd.Series(p))**2
    ).sum()**0.5
)

# polars
pl_euc = (
    ((pl.Series(q) - pl.Series(p))**2).sum()**0.5
)

assert pd_euc == pl_euc

print("Completed.")
