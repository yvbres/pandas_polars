# 34. How to change column values when importing csv to a dataframe?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal
from perfrecorder import log_performance


# Import the boston housing dataset,
# but while importing change the 'medv' (median house value) column
# so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.
FILEPATH = '../data/boston_housing.csv'


@log_performance
def read_pd() -> pd.DataFrame:
    return pd.read_csv(
        FILEPATH,
        converters={'medv': lambda x: 'High' if float(x) > 25 else 'Low'}
    )


@log_performance
def read_pl() -> pl.DataFrame:
    return pl.scan_csv(FILEPATH).with_columns(
        pl.when(pl.col('medv') > 25)
        .then('High')
        .otherwise('Low')
        .alias('medv')
    ).collect()


def main():
    pd_df = read_pd()
    pl_df = read_pl()
    assert_frame_equal(pl.from_pandas(pd_df), pl_df)
    print('Completed')


if __name__ == '__main__':
    main()
