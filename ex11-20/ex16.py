# 16. How to get the positions of items of series A in another series B?
import pandas as pd
import polars as pl


# Get the positions of items of ser2 in ser1 as a list.
vals1 = [10, 9, 6, 5, 3, 1, 12, 8, 13]
vals2 = [1, 3, 10, 13]
# pandas
pd_ser1 = pd.Series(vals1)
pd_ser2 = pd.Series(vals2)
pd_idxs = (
    pd_ser1
    [pd_ser1.isin(pd_ser2)]
    .index
    .tolist()
)

# polars
pl_ser1 = pl.Series(vals1)
pl_ser2 = pl.Series(vals2)
pl_idxs = (
    pl_ser1
    .to_frame().with_row_count(name='index')
    .filter(pl_ser1.is_in(pl_ser2))
    ['index']
    .to_list()
)

assert sorted(pd_idxs) == sorted(pl_idxs)
print("Completed.")
