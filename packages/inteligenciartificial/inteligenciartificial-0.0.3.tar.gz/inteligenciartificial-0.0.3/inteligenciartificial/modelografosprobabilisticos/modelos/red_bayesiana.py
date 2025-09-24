# inteligenciartificial/modelografosprobabilisticos/modelos/red_bayesiana.py

from typing import Dict, Optional
import pandas as pd
from ..grafo import Grafo
from ..distribuciones.discreta import (
    DistribucionDiscreta,
    DistribucionMarginalDiscreta,
    DistribucionCondicionalDiscreta,
    estimar_marginal,
    estimar_condicional,
)
from ..utils import ensure_categorical

class RedBayesiana:
    """
    Red Bayesiana discreta con CPTs estimadas por conteos + Dirichlet(alpha).

    Parámetros
    ----------
    grafo : Grafo
        Estructura (DAG) de la red.
    alpha : float, opcional (default=1.0)
        Hiperparámetro de Dirichlet (seudocuentas) para suavizado al estimar las distribuciones.
        alpha=1.0 es Laplace; alpha=0.5 es Jeffreys; alpha=0 desactiva el suavizado (no recomendado).
    """
    def __init__(self, grafo: Grafo, alpha: float = 1.0):
        self.grafo = grafo
        self.alpha = float(alpha)
        self._cpts: Dict[str, DistribucionDiscreta] = {}

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None):
        """
        Estima las distribuciones (CPTs) para cada nodo usando el conjunto de datos.
        Si 'y' no es None, se asume que es una columna objetivo que también es nodo del grafo.
        """
        df = X.copy()
        if y is not None:
            df[y.name] = y
        df = ensure_categorical(df)

        for v in self.grafo.nodos():
            padres = self.grafo.padres(v)
            if len(padres) == 0:
                self._cpts[v] = estimar_marginal(df, v, alpha=self.alpha)
            else:
                self._cpts[v] = estimar_condicional(df, v, padres, alpha=self.alpha)
        return self

    def getDistribucion(self, variable: str) -> DistribucionDiscreta:
        return self._cpts[variable]

    def predict(self, X: pd.DataFrame, objetivo: Optional[str] = None):
        """
        Predice por argmáx para la variable objetivo.
        Si 'objetivo' es None, intenta usar 'play' o la primera variable disponible.
        """
        if objetivo is None:
            objetivo = "play" if "play" in self._cpts else next(iter(self._cpts.keys()))
        assert objetivo in self._cpts, "Variable objetivo no encontrada en CPTs"

        X = ensure_categorical(X)

        # Determinar clases posibles de la variable objetivo
        dist = self._cpts[objetivo]
        if isinstance(dist, DistribucionMarginalDiscreta):
            clases = list(dist.tabla_prob.keys())
        elif isinstance(dist, DistribucionCondicionalDiscreta):
            clases = sorted(set(k[-1] for k in dist.tabla_prob.keys()))
        else:
            raise ValueError("Distribución objetivo no válida para predicción")

        preds = []
        for _, row in X.iterrows():
            scores = {}
            for c in clases:
                p = 1.0
                for v, d in self._cpts.items():
                    padres = self.grafo.padres(v)
                    if len(padres) == 0:
                        xval = c if v == objetivo else row[v]
                        p *= d.prob(xval)
                    else:
                        cond = {p_: (c if p_ == objetivo else row[p_]) for p_ in padres}
                        xval = c if v == objetivo else row[v]
                        p *= d.prob(xval, **cond)
                scores[c] = p
            preds.append(max(scores, key=scores.get))
        return preds

    def __repr__(self):
        return f"RedBayesiana(alpha={self.alpha}, {self.grafo})"

