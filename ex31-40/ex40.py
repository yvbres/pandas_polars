# 40. How to check if a dataframe has any missing values?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from perfrecorder import log_performance


FILEPATH = '../data/cars93.csv'


@log_performance
def has_missing_vals_pd() -> bool:
    df = pd.read_csv(FILEPATH)
    return df.isna().sum().sum() > 0


@log_performance
def has_missing_vals_pl() -> bool:
    df = pl.read_csv(FILEPATH, null_values=['NA', 'NaN', 'NAN', ''])
    return (
        df
        .null_count()  # DataFrame
        .sum(axis=1)  # Series
        .to_list()  # list
        [0]  # value
        > 0  # bool
    )


def main():
    pd_bool = has_missing_vals_pd()
    pl_bool = has_missing_vals_pl()
    assert pl_bool == pd_bool
    print('Completed.')


if __name__ == '__main__':
    main()
