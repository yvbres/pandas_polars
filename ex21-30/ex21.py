# 21. How to convert a series of date-strings to a timeseries?
from dateutil.parser import parse
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal


dates = ['01 Jan 2010', '02-02-2011', '20120303',
         '2013/04/04', '2014-05-05', '2015-06-06T12:20']

# pandas
pd_ser = pd.to_datetime(dates, format="mixed")

# polars
pl_ser = pl.Series(parse(dt) for dt in dates)

assert_series_equal(pl.from_pandas(pd_ser), pl_ser.cast(pl.Datetime(time_unit="ns")))

print("Completed.")
