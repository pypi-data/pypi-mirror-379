import numpy as np
import pandas as pd
from collections import Counter
from typing import Iterable

def ensure_categorical(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for c in out.columns:
        if not pd.api.types.is_categorical_dtype(out[c]):
            out[c] = out[c].astype("category")
    return out

def unique_vals(series: pd.Series):
    if pd.api.types.is_categorical_dtype(series):
        return list(series.cat.categories)
    return sorted(series.dropna().unique().tolist())

def accuracy_score(y_true: Iterable, y_pred: Iterable) -> float:
    y_true = list(y_true)
    y_pred = list(y_pred)
    n = len(y_true)
    if n == 0 or n != len(y_pred):
        return 0.0
    return sum(int(a == b) for a, b in zip(y_true, y_pred)) / n

