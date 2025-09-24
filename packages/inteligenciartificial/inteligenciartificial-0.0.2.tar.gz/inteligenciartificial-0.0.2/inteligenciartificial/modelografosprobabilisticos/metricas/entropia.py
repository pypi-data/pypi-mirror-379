import numpy as np
import pandas as pd
from typing import List
from ..utils import ensure_categorical, unique_vals

def _entropy(probs):
    probs = np.asarray(probs, dtype=float)
    probs = probs[probs > 0]
    return float(-(probs * np.log2(probs)).sum()) if probs.size else 0.0

class Entropia:
    """
    Usa -H(X|Pa) como score a maximizar (más alto = mejor).
    """
    def score(self, df: pd.DataFrame, var: str, padres: List[str]) -> float:
        df = ensure_categorical(df)
        if not padres:
            p = df[var].value_counts(normalize=True).values
            return -_entropy(p)
        # H(X|Pa) = sum_p P(p) H(X|p)
        H = 0.0
        grupos = df.groupby(padres)
        N = len(df)
        for _, sub in grupos:
            w = len(sub) / N
            p = sub[var].value_counts(normalize=True).values
            H += w * _entropy(p)
        return -H  # mayor es mejor

    @staticmethod
    def mejor(nuevo: float, actual: float) -> bool:
        return nuevo > actual + 1e-12

