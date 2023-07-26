# 38. How to extract the row and column number
# of a particular cell with given criterion?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from perfrecorder import log_performance


# Which manufacturer, model and type has the highest Price?
# What is the row and column number of the cell with the highest Price value?
FILEPATH = '../data/cars93.csv'


# pandas
def get_df_pd() -> pd.DataFrame:
    return pd.read_csv(FILEPATH)


@log_performance
def find_max_cell_pd(df: pd.DataFrame) -> tuple[int, int]:
    idx = df[df.Price == df.Price.max()].index[0]
    col = df.columns.tolist().index('Price')
    return (idx, col)


# polars
def get_df_pl() -> tuple[int, int]:
    return pl.scan_csv(FILEPATH).with_columns(
        pl.when(pl.col('Price') == 'NA')
        .then(None)
        .otherwise(pl.col('Price'))
        .cast(pl.Float64)
        .alias('Price')
    ).collect()


@log_performance
def find_max_cell_pl(df: pl.DataFrame) -> tuple[int, int]:
    idx = (
        df
        .with_row_count()
        .filter(pl.col('Price') == pl.col('Price').max())
        .select('row_nr')
        .to_numpy()
    )[0][0]
    col = df.columns.index('Price')
    return (idx, col)


def main():
    pd_idx, pd_col = find_max_cell_pd(get_df_pd())
    pl_idx, pl_col = find_max_cell_pl(get_df_pl())
    assert pd_idx == pl_idx
    assert pd_col == pl_col
    print('Completed.')


if __name__ == '__main__':
    main()
