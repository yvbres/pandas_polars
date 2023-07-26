# 37. How to get the nrows, ncolumns, datatype, summary stats of
# each column of a dataframe? Also get the array and list equivalent.
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from polars.datatypes.classes import DataTypeClass
from perfrecorder import log_performance


# Get the number of rows, columns, datatype and
# summary statistics of each column of the Cars93 dataset.
# Also get the numpy array and list equivalent of the dataframe.
FILEPATH = '../data/cars93.csv'


# pandas
def read_pd() -> pd.DataFrame:
    return pd.read_csv(FILEPATH)


@log_performance
def get_datatypes_pd(df: pd.DataFrame) -> pd.Series:
    return df.dtypes


@log_performance
def get_rows_cols_pd(df: pd.DataFrame) -> tuple[int, int]:
    return df.shape


@log_performance
def get_stats_pd(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()


# polars
def read_pl() -> pl.DataFrame:
    return pl.read_csv(FILEPATH)


@log_performance
def get_datatypes_pl(df: pl.DataFrame) -> list[DataTypeClass]:
    return df.dtypes


@log_performance
def get_rows_cols_pl(df: pl.DataFrame) -> tuple[int, int]:
    return df.shape


@log_performance
def get_stats_pl(df: pl.DataFrame) -> pl.DataFrame:
    return df.describe()


def main():
    pd_df = read_pd()
    pl_df = read_pl()

    _ = get_datatypes_pd(pd_df)
    _ = get_datatypes_pl(pl_df)

    _ = get_rows_cols_pd(pd_df)
    _ = get_rows_cols_pl(pl_df)

    _ = get_stats_pd(pd_df)
    _ = get_stats_pl(pl_df)

    print('Completed.')


if __name__ == '__main__':
    main()
