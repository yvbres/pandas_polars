# How to import only specified columns from a csv file?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal
from perfrecorder import log_performance


# Import ‘crim’ and ‘medv’ columns of the BostonHousing dataset as a dataframe.
FILEPATH = '../data/boston_housing.csv'

@log_performance
def read_pd() -> pd.DataFrame:
    return pd.read_csv(FILEPATH, usecols=['crim', 'medv'])


@log_performance
def read_pl() -> pl.DataFrame:
    # return pl.read_csv(FILEPATH, columns=['crim', 'medv'])
    return pl.scan_csv(FILEPATH).select(['crim', 'medv']).collect()


def main():
    pd_df = read_pd()
    pl_df = read_pl()
    assert_frame_equal(pl.from_pandas(pd_df), pl_df)
    print('Completed.')


if __name__ == '__main__':
    main()
