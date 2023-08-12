# 45. How to change the order of columns of a dataframe?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
import numpy as np
from polars.testing import assert_frame_equal
from perfrecorder import log_performance


# Create a generic function to interchange two columns,
# without hardcoding column names.
@log_performance
def reorder_cols_pd(df: pd.DataFrame, new_cols: list[str]) -> pd.DataFrame:
    return df.filter(items=new_cols, axis='columns')


@log_performance
def reorder_cols_pl(df: pl.DataFrame, new_cols: list[str]) -> pl.DataFrame:
    return df.select(new_cols)


def main():
    original = pd.DataFrame(
        np.arange(20).reshape(-1, 5),
        columns=list('abcde')
    )
    new_cols = list('cbade')

    pd_df = reorder_cols_pd(original, new_cols)
    pl_df = reorder_cols_pl(pl.from_pandas(original), new_cols)
    assert_frame_equal(pl.from_pandas(pd_df), pl_df)
    print('Completed.')


if __name__ == '__main__':
    main()
