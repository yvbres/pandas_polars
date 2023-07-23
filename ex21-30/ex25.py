# 25. How to filter valid emails from a series?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal

emails = ['buying books at amazom.com',
          'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com']
pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'

# pandas
pd_ser = pd.Series(emails)
pd_ser = pd_ser[pd_ser.str.match(pattern)]
pd_ser.name = "emails"

# polars
pl_ser = pl.DataFrame({"emails": emails}).filter(
    pl.col("emails").str.contains(pattern)
)["emails"]

assert_series_equal(pl.from_pandas(pd_ser), pl_ser)

print("Completed.")
