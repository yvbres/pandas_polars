# 42. How to replace missing values of multiple numeric columns with the mean?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal
from perfrecorder import log_performance


# Replace missing values in Min.Price
# and Max.Price columns with their respective mean.
FILEPATH = '../data/cars93.csv'
cols = ['Max.Price', 'Min.Price']


@log_performance
def replace_missing_pd() -> pd.DataFrame:
    df = pd.read_csv(FILEPATH, usecols=cols)
    for col in cols:
        _ = df[col].fillna(value=df[col].mean(), inplace=True)
    return df


@log_performance
def replace_missing_pl() -> pl.DataFrame:
    return (
        pl.read_csv(FILEPATH,
                    null_values=['NA', 'NaN', 'NAN', '', 'None'],
                    columns=cols)
        .with_columns(
            pl.col('Min.Price').fill_null(pl.col('Min.Price').mean()),
            pl.col('Max.Price').fill_null(pl.col('Max.Price').mean())
        )
    )


def main():
    pd_df = replace_missing_pd()
    pl_df = replace_missing_pl()
    assert_frame_equal(pl.from_pandas(pd_df), pl_df)
    print('Completed.')


if __name__ == '__main__':
    main()
