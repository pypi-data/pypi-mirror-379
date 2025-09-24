class Grafo:
    def __init__(self, aristas=None):
        self._aristas=set(aristas or [])
        self._nodos=set()
        for u,v in self._aristas:
            self._nodos.add(u); self._nodos.add(v)
    def nodos(self):
        return sorted(self._nodos)
    def aristas(self):
        return sorted(self._aristas)
    def padres(self,n):
        return sorted(u for u,v in self._aristas if v==n)
    def hijos(self,n):
        return sorted(v for u,v in self._aristas if u==n)
    def agregar_arista(self,u,v):
        self._nodos.add(u); self._nodos.add(v); self._aristas.add((u,v))
    def __repr__(self):
        return f'Grafo(nodos={self.nodos()}, aristas={self.aristas()})'
