from typing import Dict, Tuple, List
import pandas as pd
import numpy as np
from ..utils import ensure_categorical, unique_vals

class DistribucionDiscreta:
    """
    Clase base de distribuciones discretas.
    """
    def __init__(self, variable: str):
        self.variable = variable

    def prob(self, **kwargs) -> float:
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}(variable={self.variable})"


class DistribucionMarginalDiscreta(DistribucionDiscreta):
    """
    P(X)
    """
    def __init__(self, variable: str, tabla_prob: Dict[str, float]):
        super().__init__(variable)
        self.tabla_prob = tabla_prob

    def prob(self, x: str) -> float:
        return float(self.tabla_prob.get(x, 0.0))

    def __str__(self):
        return f"P({self.variable})={self.tabla_prob}"


class DistribucionConjuntaDiscreta(DistribucionDiscreta):
    """
    P(X, Y, ...)
    """
    def __init__(self, variables: List[str], tabla_prob: Dict[Tuple[str, ...], float]):
        super().__init__(variable=",".join(variables))
        self.variables = variables
        self.tabla_prob = tabla_prob

    def prob(self, **kwargs) -> float:
        key = tuple(kwargs[v] for v in self.variables)
        return float(self.tabla_prob.get(key, 0.0))

    def __str__(self):
        return f"P({','.join(self.variables)}) con {len(self.tabla_prob)} entradas"


class DistribucionCondicionalDiscreta(DistribucionDiscreta):
    """
    P(X | Pa)
    """
    def __init__(self, variable: str, padres: List[str], tabla_prob: Dict[Tuple[str, ...], float]):
        super().__init__(variable)
        self.padres = padres
        self.tabla_prob = tabla_prob  # keys: (*valores_padres, valor_de_variable)

    def prob(self, x: str, **cond) -> float:
        key = tuple([cond[p] for p in self.padres] + [x])
        return float(self.tabla_prob.get(key, 0.0))

    def __str__(self):
        return f"P({self.variable} | {','.join(self.padres)}) con {len(self.tabla_prob)} entradas"


# Helpers de estimación (conteos + suavizado)
def estimar_marginal(df: pd.DataFrame, var: str, alpha: float = 1.0) -> DistribucionMarginalDiscreta:
    df = ensure_categorical(df)
    valores = unique_vals(df[var])
    counts = df[var].value_counts().reindex(valores, fill_value=0).astype(float)
    probs = (counts + alpha) / (counts.sum() + alpha * len(valores))
    return DistribucionMarginalDiscreta(var, dict(zip(valores, probs.values)))


def estimar_condicional(df: pd.DataFrame, var: str, padres: List[str], alpha: float = 1.0) -> DistribucionCondicionalDiscreta:
    df = ensure_categorical(df)
    valores_var = unique_vals(df[var])
    valores_padres = [unique_vals(df[p]) for p in padres]
    from itertools import product
    tabla = {}
    for combo_padres in product(*valores_padres):
        sub = df.copy()
        for p, val in zip(padres, combo_padres):
            sub = sub[sub[p] == val]
        counts = sub[var].value_counts().reindex(valores_var, fill_value=0).astype(float)
        probs = (counts + alpha) / (counts.sum() + alpha * len(valores_var))
        for x, px in zip(valores_var, probs.values):
            tabla[tuple(list(combo_padres) + [x])] = float(px)
    return DistribucionCondicionalDiscreta(var, padres, tabla)

