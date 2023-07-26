# 31. How to fill an intermittent time series so all missing dates
# show up with values of previous non-missing date?
from dateutil.parser import parse
import pandas as pd
import polars as pl
from polars.testing import assert_frame_equal


# ser has missing dates and values. Make all missing dates appear
# and fill up with value from previous date.
vals = [1, 10, 3, None]
dates = ['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']

# pandas
ser = pd.Series(vals, index=pd.to_datetime(dates), name="vals")
pd_df = (
    pd.DataFrame({
        "dates": pd.date_range(ser.index.min(), ser.index.max(), freq='1d')
    })
    .set_index("dates")
    .join(ser, how="left")
    .fillna(method="ffill")
    .reset_index()
)

# polars
pl_ini = pl.DataFrame({"vals": vals,
                       "dates": (parse(d).date() for d in dates)})
pl_df = (
    pl.DataFrame({
        "dates": pl.date_range(
            pl_ini['dates'].min(), pl_ini['dates'].max(),
            interval='1d', eager=True
        )
    })
    .join(pl_ini, on="dates", how="left")
    .fill_null(strategy="forward")
    .with_columns(
        pl.col('dates').cast(pl.Datetime(time_unit='ns')),
        pl.col('vals').cast(pl.Float64)
    )
)

assert_frame_equal(pl.from_pandas(pd_df), pl_df)

print("Completed.")
