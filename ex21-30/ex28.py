# 28. How to find all the local maxima (or peaks) in a numeric series?
import pandas as pd
import polars as pl

# Get the positions of peaks
# (values surrounded by smaller values on both sides) in ser
vals = [2, 10, 3, 4, 9, 10, 2, 7, 3]

# pandas
pd_idxs = (
    pd.DataFrame({"vals": vals}).assign(
        diffs_forw=lambda df: df.vals.diff(1),
        diffs_back=lambda df: df.vals.diff(-1),
    )
    .where(lambda df: (df.diffs_forw > 0) & (df.diffs_back > 0))
    .dropna()
    .index
    .tolist()
)

# polars
pl_idxs = (
    pl.DataFrame({"vals": vals})
    .with_row_count()
    .with_columns(
        pl.col("vals").diff(1).alias("diffs_forw"),
        pl.col("vals").diff(-1).alias("diffs_back"),
    ).filter((pl.col("diffs_forw") > 0) & (pl.col("diffs_back") > 0))
    ["row_nr"]
    .to_list()
)

assert pd_idxs == pl_idxs

print("Completed.")
