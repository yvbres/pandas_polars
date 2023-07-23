# 29. How to replace missing spaces
# in a string with the least frequent character?
import pandas as pd
import polars as pl
from collections import Counter


# Replace the spaces in my_str with the least frequent character.
my_str = 'dbc deb abed gade'

least_common_char = (
    Counter(my_str).most_common()
    [-1]  # the last tuple
    [0]  # first elt in tuple: the character (the other is the occurence)
)

# pandas
pd_ser = pd.Series(list(my_str)).str.replace(' ', least_common_char)
pd_new_str = ''.join(pd_ser.tolist())

# polars
pl_ser = pl.Series(list(my_str)).str.replace(' ', least_common_char)
pl_new_str = ''.join(pl_ser.to_list())

assert pd_new_str == pl_new_str

print("Completed.")
