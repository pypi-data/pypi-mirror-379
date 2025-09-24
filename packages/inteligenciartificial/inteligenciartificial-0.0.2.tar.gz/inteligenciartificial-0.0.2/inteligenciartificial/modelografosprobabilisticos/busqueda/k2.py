from typing import List, Dict, Set
import pandas as pd
from ..grafo import Grafo
from ..modelos.red_bayesiana import RedBayesiana
from ..utils import ensure_categorical
from ..metricas.entropia import Entropia
from ..metricas.bic import BIC

class K2:
    """
    Implementación sencilla del algoritmo K2:
    - Requiere un orden topológico de variables.
    - Agrega padres greedily hasta 'max_padres' si mejora la métrica.
    Métricas soportadas: Entropia (reduce H) y BIC (aumenta score).
    """
    def __init__(self, orden: List[str], max_padres: int, df: pd.DataFrame, metrica):
        self.orden = orden
        self.max_padres = max_padres
        self.df = ensure_categorical(df)
        self.metrica = metrica  # instancia de Entropia() o BIC()

        self._grafo = self._aprender_estructura()

    def _aprender_estructura(self) -> Grafo:
        aristas = []
        for i, v in enumerate(self.orden):
            candidatos = self.orden[:i]  # solo anteriores en el orden
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

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        rb = RedBayesiana(self._grafo)
        rb.fit(X, y)
        return rb

    def __repr__(self):
        return f"RedBayesiana({self._grafo})"

