'''
Busca em Profundidade (DFS) em um Grafo:

Implemente a busca em profundidade (DFS) em um grafo não direcionado representado por meio de listas de adjacência. 
A busca em profundidade é um algoritmo para percorrer ou pesquisar em árvores ou estruturas de dados semelhantes, 
onde o algoritmo explora tanto quanto possível ao longo de cada ramo antes de retroceder. 
Este algoritmo é útil para encontrar componentes conexos em um grafo.
'''
from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
    
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
    
    def dfs_util(self, vertice, visitado):
        visitado.add(vertice)
        print(vertice, end=" ")
        for vizinho in self.grafo[vertice]:
            if vizinho not in visitado:
                self.dfs_util(vizinho, visitado)

    def dfs(self, inicio):
        visitado = set()
        self.dfs_util(inicio, visitado)

# Exemplo de uso:
g = Grafo()
g.adicionar_aresta(0, 1)
g.adicionar_aresta(0, 2)
g.adicionar_aresta(1, 2)
g.adicionar_aresta(2, 0)
g.adicionar_aresta(2, 3)
g.adicionar_aresta(3, 3)
print("Busca em Profundidade a partir do vértice 2:")
g.dfs(2)  # Saída: 2 0 1 3
