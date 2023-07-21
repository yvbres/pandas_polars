# 2. How to create a series from a list, numpy array and dict?
import polars as pl
import pandas as pd
import numpy as np
from polars.testing import assert_series_equal

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# pandas
ser_list = pd.Series(mylist)
ser_arr = pd.Series(myarr)
ser_dict = pd.Series(mydict)
ser_dict.name = "dict"

# polars
s_list = pl.Series("list", mylist)
s_arr = pl.Series("arr", myarr)
s_dict = pl.Series("dict", mydict.values())  # dict is interpreted as a Struct in polars

assert_series_equal(pl.from_pandas(ser_dict), s_dict)
print("Completed.")
