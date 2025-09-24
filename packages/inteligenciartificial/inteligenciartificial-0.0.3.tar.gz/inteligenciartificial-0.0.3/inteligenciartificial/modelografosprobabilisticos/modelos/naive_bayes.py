import pandas as pd
from typing import Optional, List, Dict
from ..grafo import Grafo
from ..distribuciones.discreta import (
    DistribucionMarginalDiscreta,
    DistribucionCondicionalDiscreta,
    estimar_marginal,
    estimar_condicional,
)
from ..utils import ensure_categorical, unique_vals
from math import prod

class NaiveBayes:
    """
    Naive Bayes categórico: P(C) * Π_i P(X_i | C)
    """
    def __init__(self, clase: str, alpha: float = 1.0):
        self.clase = clase
        self.alpha = alpha
        self._grafo = None
        self._P_clase: Optional[DistribucionMarginalDiscreta] = None
        self._P_feature: Dict[str, DistribucionCondicionalDiscreta] = {}

    def fit(self, X: pd.DataFrame, y: pd.Series):
        Xy = X.copy()
        Xy[self.clase] = y
        Xy = ensure_categorical(Xy)

        # Grafo: clase -> todas las X
        aristas = [(self.clase, col) for col in X.columns]
        self._grafo = Grafo(aristas)

        # P(C)
        self._P_clase = estimar_marginal(Xy, self.clase, self.alpha)

        # P(X_i | C)
        for col in X.columns:
            self._P_feature[col] = estimar_condicional(Xy, col, [self.clase], self.alpha)
        return self

    def predict(self, X: pd.DataFrame):
        assert self._P_clase is not None
        X = ensure_categorical(X)
        clases = list(self._P_clase.tabla_prob.keys())
        preds = []
        for _, row in X.iterrows():
            scores = {}
            for c in clases:
                p = self._P_clase.prob(c)
                for col in X.columns:
                    p *= self._P_feature[col].prob(row[col], **{self.clase: c})
                scores[c] = p
            preds.append(max(scores, key=scores.get))
        return preds

    def __repr__(self):
        return f"NaiveBayes(clase={self.clase}, alpha={self.alpha})"

