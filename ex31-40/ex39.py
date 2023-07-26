# 39. How to rename a specific columns in a dataframe?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from perfrecorder import log_performance


# Rename the column Type as CarType in df
# and replace the ‘.’ in column names with ‘_’.
FILEPATH = '../data/cars93.csv'


# pandas
def get_df_pd() -> pd.DataFrame:
    return pd.read_csv(FILEPATH)


@log_performance
def get_new_cols_pd(df: pd.DataFrame) -> list[str]:
    _ = df.rename(columns={'Type': 'CarType'}, inplace=True)
    df.columns = [col.replace('.', '_') for col in df.columns]
    return sorted(df.columns.tolist())


# polars
def get_df_pl() -> pl.DataFrame:
    return pl.read_csv(FILEPATH)


@log_performance
def get_new_cols_pl(df: pl.DataFrame) -> list[str]:
    df = df.with_columns(pl.col('Type').alias('CarType')).drop('Type')
    df.columns = [col.replace('.', '_') for col in df.columns]
    return sorted(df.columns)


def main():
    pd_ls = get_new_cols_pd(get_df_pd())
    pl_ls = get_new_cols_pl(get_df_pl())
    assert pd_ls == pl_ls
    print('Completed.')


if __name__ == '__main__':
    main()
