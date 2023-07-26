# 33. How to import only every nth row from a csv file to create a dataframe?
import __init__  # noqa: F401
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal
from perfrecorder import log_performance


# Import every 50th row of BostonHousing dataset as a dataframe.
FILE_PATH: str = '../data/boston_housing.csv'


@log_performance
def read_pd() -> pd.DataFrame:
    pd_chunks = pd.read_csv(FILE_PATH, chunksize=50)
    pd_df = pd.DataFrame()
    for pd_chunk in pd_chunks:
        pd_df = pd.concat([pd_df, pd_chunk])
    return pd_df


@log_performance
def read_pl() -> pl.DataFrame:
    reader = pl.read_csv_batched(FILE_PATH, batch_size=50)
    pl_df = pl.DataFrame()
    pl_chunks = reader.next_batches(5)
    while pl_chunks:
        for chunk in pl_chunks:
            pl_df = pl.concat([pl_df, chunk])
        pl_chunks = reader.next_batches(5)

    return pl_df


def main():
    pd_df = read_pd()
    pl_df = read_pl()
    assert_frame_equal(pl.from_pandas(pd_df), pl_df)
    print('Completed.')


if __name__ == '__main__':
    main()
