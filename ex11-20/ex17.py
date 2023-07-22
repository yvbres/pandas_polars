# 17. How to compute the mean squared error on a truth and predicted series?
import pandas as pd
import polars as pl
import numpy as np


# Compute the mean squared error of truth and pred series.

for _ in range(1_000):

    truth_vals = range(10)
    pred_vals = range(10) + np.random.random(10)

    # pandas
    pd_truth = pd.Series(truth_vals)
    pd_pred = pd.Series(pred_vals)

    pd_mse = (
        (pd_pred - pd_truth)**2
    ).mean()

    # polars
    pl_truth = pl.Series(truth_vals)
    pl_pred = pl.Series(pred_vals)

    pl_mse = (
        (pl_truth - pl_pred)**2
    ).mean()

    assert (pd_mse - pl_mse) < 1.e-5

print("Completed.")
