# 30. How to create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays)
# after that having random numbers as values?
from datetime import date
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal
import numpy as np


for _ in range(1_000):
    vals = np.random.random(10)
    # pandas
    pd_df = pd.DataFrame({
        "dates": pd.date_range('2000-01-01',
                            periods=10,
                            freq='w-SAT',
                            inclusive='both'),
        "vals": vals
    })

    # polars
    pl_df = pl.DataFrame({
        "dates": pl.date_range(date(2000, 1, 1), date(2000, 3, 4),
                            interval='1w', eager=True),
        "vals": vals
    }).with_columns(pl.col("dates").cast(pl.Datetime(time_unit='ns')))

    assert_frame_equal(pl.from_pandas(pd_df), pl_df)

print("Completed.")
