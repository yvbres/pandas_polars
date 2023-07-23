# 22. How to get the day of month, week number,
# day of year and day of week from a series of date strings?
from dateutil.parser import parse
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal


dates = ['01 Jan 2010', '02-02-2011', '20120303',
         '2013/04/04', '2014-05-05', '2015-06-06T12:20']

# pandas
pd_df = pd.DataFrame({"datetime": pd.to_datetime(dates, format="mixed")})
pd_df = pd_df.assign(
    day = pd_df.datetime.dt.day,
    week_num = pd_df.datetime.map(lambda x: x.isocalendar().week),
    day_num_of_year = pd_df.datetime.dt.day_of_year,
    day_name = pd_df.datetime.dt.day_name()
)

# polars
pl_df = pl.DataFrame({"datetime": (parse(dt) for dt in dates)})
pl_df = pl_df.with_columns(
    pl.col("datetime").cast(pl.Datetime(time_unit="ns")),
    pl.col("datetime").dt.day().cast(pl.Int32).alias("day"),
    pl.col("datetime").dt.week().cast(pl.Int64).alias("week_num"),
    pl.col("datetime").dt.ordinal_day().cast(pl.Int32).alias("day_num_of_year"),
    pl.col("datetime").dt.to_string("%A").alias("day_name")
)

assert_frame_equal(pl.from_pandas(pd_df), pl_df)

print("Completed.")
