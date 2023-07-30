# 41. How to count the number of missing values in each column?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal
from perfrecorder import log_performance


FILEPATH = '../data/cars93.csv'


@log_performance
def count_missing_cols_pd() -> pd.DataFrame:
    return pd.read_csv(FILEPATH).isnull().sum().to_frame().T


@log_performance
def count_missing_cols_pl() -> pl.DataFrame:
    return (
        pl.read_csv(FILEPATH,
                    null_values=['NA', 'NaN', 'NAN', '', 'None'])
        .null_count()
        .select(pl.all().cast(pl.Int64))
    )


def main():
    pd_df = count_missing_cols_pd()
    pl_df = count_missing_cols_pl()
    assert_frame_equal(pl.from_pandas(pd_df), pl_df)
    print('Completed.')


if __name__ == '__main__':
    main()
