from typing import List, Tuple, Dict, Set

class Grafo:
    """
    Grafo dirigido simple para estructuras de Redes Bayesianas.
    Nodos: strings; Aristas: tuplas (padre, hijo).
    """
    def __init__(self, aristas: List[Tuple[str, str]] = None):
        self._aristas: Set[Tuple[str, str]] = set(aristas or [])
        self._nodos: Set[str] = set()
        for u, v in self._aristas:
            self._nodos.add(u); self._nodos.add(v)

    def nodos(self) -> List[str]:
        return sorted(self._nodos)

    def aristas(self) -> List[Tuple[str, str]]:
        return sorted(self._aristas)

    def padres(self, nodo: str) -> List[str]:
        return sorted(u for u, v in self._aristas if v == nodo)

    def hijos(self, nodo: str) -> List[str]:
        return sorted(v for u, v in self._aristas if u == nodo)

    def agregar_arista(self, u: str, v: str):
        self._nodos.add(u); self._nodos.add(v)
        # Nota: no chequeamos DAG estrictamente por simplicidad
        self._aristas.add((u, v))

    def __repr__(self):
        return f"Grafo(nodos={self.nodos()}, aristas={self.aristas()})"

