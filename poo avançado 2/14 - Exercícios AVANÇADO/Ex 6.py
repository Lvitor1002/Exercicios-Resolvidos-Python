'''
Busca em Largura (BFS) em um Grafo:

Implemente a busca em largura (BFS) em um grafo não direcionado representado por meio de listas de adjacência. 
A busca em largura é um algoritmo para percorrer ou pesquisar em árvores ou estruturas de dados semelhantes, 
onde todos os nós adjacentes ao nó atual são visitados antes de passar para os nós vizinhos. 
Este algoritmo é útil para encontrar o caminho mais curto em um grafo não ponderado.
'''

from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
    
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
    
    def bfs(self, inicio):
        visitado = set()
        fila = [inicio]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitado:
                print(vertice, end=" ")
                visitado.add(vertice)
                fila.extend([x for x in self.grafo[vertice] if x not in visitado])

# Exemplo de uso:
g = Grafo()
g.adicionar_aresta(0, 1)
g.adicionar_aresta(0, 2)
g.adicionar_aresta(1, 2)
g.adicionar_aresta(2, 0)
g.adicionar_aresta(2, 3)
g.adicionar_aresta(3, 3)
print("Busca em Largura a partir do vértice 2:")
g.bfs(2)  # Saída: 2 0 3 1
