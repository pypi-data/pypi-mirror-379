import numpy as np
import pandas as pd
from typing import List
from ..utils import ensure_categorical, unique_vals

class BIC:
    """
    BIC por variable:
    score = log-likelihood_max - (k/2)*log(N)
    k = (r_i - 1) * q  (ri = cardinalidad variable, q = producto cardinalidades de padres)
    Más alto = mejor.
    """
    def score(self, df: pd.DataFrame, var: str, padres: List[str]) -> float:
        df = ensure_categorical(df)
        N = len(df)
        ri = len(unique_vals(df[var]))
        q = 1
        for p in padres:
            q *= len(unique_vals(df[p]))

        # log-likelihood máximo por conteos
        ll = 0.0
        if not padres:
            counts = df[var].value_counts().values.astype(float)
            probs = counts / counts.sum()
            ll = np.sum(counts[counts > 0] * np.log(probs[counts > 0]))
        else:
            for _, sub in df.groupby(padres):
                counts = sub[var].value_counts().values.astype(float)
                s = counts.sum()
                if s > 0:
                    probs = counts / s
                    ll += np.sum(counts[counts > 0] * np.log(probs[counts > 0]))

        k = (ri - 1) * q
        bic = ll - 0.5 * k * np.log(max(N, 1))
        return float(bic)

    @staticmethod
    def mejor(nuevo: float, actual: float) -> bool:
        return nuevo > actual + 1e-12

