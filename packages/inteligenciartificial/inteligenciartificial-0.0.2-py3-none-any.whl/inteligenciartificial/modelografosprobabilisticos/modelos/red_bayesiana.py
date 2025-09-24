from typing import Dict, List, Optional
import pandas as pd
from ..grafo import Grafo
from ..distribuciones.discreta import (
    DistribucionDiscreta,
    DistribucionMarginalDiscreta,
    DistribucionCondicionalDiscreta,
    estimar_marginal,
    estimar_condicional,
)
from ..utils import ensure_categorical, unique_vals

class RedBayesiana:
    """
    Red Bayesiana discreta con CPTs estimadas por conteos + Dirichlet(alpha).
    """
    def __init__(self, grafo: Grafo, alpha: float = 1.0):
        self.grafo = grafo
        self.alpha = alpha
        self._cpts: Dict[str, DistribucionDiscreta] = {}

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None):
        df = X.copy()
        if y is not None:
            # Si hay target, lo anexamos (ej. 'play')
            # El nombre del target debe existir como nodo (en el grafo)
            target_name = y.name
            df[target_name] = y
        df = ensure_categorical(df)

        for v in self.grafo.nodos():
            padres = self.grafo.padres(v)
            if len(padres) == 0:
                self._cpts[v] = estimar_marginal(df, v, self.alpha)
            else:
                self._cpts[v] = estimar_condicional(df, v, padres, self.alpha)
        return self

    def getDistribucion(self, variable: str) -> DistribucionDiscreta:
        return self._cpts[variable]

    def predict(self, X: pd.DataFrame, objetivo: Optional[str] = None):
        """
        Predice argmax para la variable objetivo (si None, intenta detectar una variable 'play').
        """
        if objetivo is None:
            objetivo = "play" if "play" in self._cpts else next(iter(self._cpts.keys()))
        assert objetivo in self._cpts, "Variable objetivo no encontrada en CPTs"

        X = ensure_categorical(X)
        clases = None
        # Determinar dominios de la variable objetivo
        dist = self._cpts[objetivo]
        if isinstance(dist, DistribucionMarginalDiscreta):
            clases = list(dist.tabla_prob.keys())
        elif isinstance(dist, DistribucionCondicionalDiscreta):
            # Extraemos todos los valores vistos en la tabla
            clases = sorted(set(k[-1] for k in dist.tabla_prob.keys()))
        else:
            raise ValueError("Distribución objetivo no válida para predicción")

        preds = []
        for _, row in X.iterrows():
            scores = {}
            for c in clases:
                # calcular P(objetivo=c, evidencias=row) proporcional (sin normalizar)
                p = 1.0
                for v, d in self._cpts.items():
                    padres = self.grafo.padres(v)
                    if len(padres) == 0:
                        if v == objetivo:
                            p *= d.prob(c)
                        else:
                            p *= d.prob(row[v])
                    else:
                        cond = {p_: (c if p_ == objetivo else row[p_]) for p_ in padres}
                        xval = c if v == objetivo else row[v]
                        p *= d.prob(xval, **cond)
                scores[c] = p
            preds.append(max(scores, key=scores.get))
        return preds

    def __repr__(self):
        return f"RedBayesiana({self.grafo})"

