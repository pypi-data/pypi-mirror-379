# inteligenciartificial/modelografosprobabilisticos/busqueda/k2.py

from typing import List, Optional
import pandas as pd
from ..grafo import Grafo
from ..modelos.red_bayesiana import RedBayesiana
from ..utils import ensure_categorical

class K2:
    """
    Implementación sencilla del algoritmo K2:
    - Requiere un orden topológico de variables.
    - Agrega padres greedily hasta 'max_padres' si mejora la métrica.
    - Permite fijar 'alpha' (seudocuentas) para la estimación de CPTs de la RedBayesiana resultante.
    """
    def __init__(self, orden: List[str], max_padres: int, df: pd.DataFrame, metrica, alpha: Optional[float] = None):
        self.orden = orden
        self.max_padres = max_padres
        self.df = ensure_categorical(df)
        self.metrica = metrica
        self.alpha = alpha  # si None, se usará 1.0 por defecto en fit() si no se especifica

        self._grafo = self._aprender_estructura()

    def _aprender_estructura(self) -> Grafo:
        aristas = []
        for i, v in enumerate(self.orden):
            candidatos = self.orden[:i]
            padres = []
            score_actual = self.metrica.score(self.df, v, padres)
            mejora = True
            while mejora and len(padres) < self.max_padres:
                mejor_cand = None
                mejor_score = score_actual
                for c in candidatos:
                    if c in padres:
                        continue
                    nuevo_set = padres + [c]
                    s = self.metrica.score(self.df, v, nuevo_set)
                    if self.metrica.mejor(s, mejor_score):
                        mejor_score = s
                        mejor_cand = c
                if mejor_cand is not None:
                    padres.append(mejor_cand)
                    score_actual = mejor_score
                else:
                    mejora = False
            for p in padres:
                aristas.append((p, v))
        return Grafo(aristas)

    def fit(self, X: pd.DataFrame, y: pd.Series = None, alpha: Optional[float] = None):
        """
        Devuelve una RedBayesiana con CPTs estimadas.
        'alpha' aquí tiene prioridad sobre el de __init__; si ambos son None, se usa 1.0.
        """
        a = 1.0 if (alpha is None and self.alpha is None) else (self.alpha if alpha is None else alpha)
        rb = RedBayesiana(self._grafo, alpha=a)
        rb.fit(X, y)
        return rb

    def __repr__(self):
        return f"RedBayesiana(grafo={self._grafo}, alpha={self.alpha})"

