# 24. How to filter words that contain atleast 2 vowels from a series?
import pandas as pd
import polars as pl
from polars.testing import assert_series_equal

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
words = ['Apple', 'Orange', 'Plan', 'Python', 'Money']

# pandas
pd_ser = pd.Series(words, name="words").str.lower()
pd_mask = (
    pd_ser.str.count('|'.join(vowels)) >= 2
)
pd_ser = pd_ser[pd_mask]

# polars
pl_ser = pl.Series("words", words).str.to_lowercase()
regex_vowels = f"[{','.join(vowels)}]"
pl_ser = pl_ser.filter(
    pl_ser.str.count_match(regex_vowels) >= 2
)

assert_series_equal(pl.from_pandas(pd_ser), pl_ser)

print("Completed.")
