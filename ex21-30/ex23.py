# 23. How to convert year-month string to dates
# corresponding to the 4th day of the month?
from dateutil.parser import parse
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal


dates = ['Jan 2010', 'Feb 2011', 'Mar 2012']

# pandas
pd_ser = pd.to_datetime(dates, format="mixed") + pd.Timedelta("3d")
pd_ser.name = "dates"

# polars
pl_ser = pl.Series("dates", (parse(dt) for dt in dates))  # default day is 23
pl_ser = (
    pl_ser
    .to_frame().with_columns(
        (pl_ser - pl.duration(days=19)).cast(pl.Datetime(time_unit="ns")).alias("dates")
    )
)["dates"]

assert_series_equal(pl.from_pandas(pd_ser), pl_ser)

print("Completed.")
