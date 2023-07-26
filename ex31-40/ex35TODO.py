# 35. How to create a dataframe with rows as strides from a given series?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal
from perfrecorder import log_performance

# input
L = pd.Series(range(15))
# Desired output
# array([[ 0,  1,  2,  3],
#        [ 2,  3,  4,  5],
#        [ 4,  5,  6,  7],
#        [ 6,  7,  8,  9],
#        [ 8,  9, 10, 11],
#        [10, 11, 12, 13]])

@log_performance
def _pd() -> pd.DataFrame:
    return pd.DataFrame()


@log_performance
def _pl() -> pl.DataFrame:
    return pl.DataFrame()


def main():
    pd_df = _pd()
    pl_df = _pl()
    assert_frame_equal(pl.from_pandas(pd_df), pl_df)
    pass


if __name__ == '__main__':
    main()
