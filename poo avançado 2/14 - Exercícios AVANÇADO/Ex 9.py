'''
Implementação de uma Estrutura de Dados de Gráfico e Algoritmo de Dijkstra:

Escreva uma classe que represente um grafo ponderado e implemente o algoritmo de Dijkstra para encontrar o caminho mais 
curto de um vértice de origem para todos os outros vértices no grafo. O algoritmo de Dijkstra é um algoritmo de caminho mínimo que encontra o 
caminho mais curto entre um vértice de origem e todos os outros vértices em um grafo ponderado com arestas não negativas.
'''

from collections import defaultdict
import heapq

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
    
    def adicionar_aresta(self, u, v, peso):
        self.grafo[u].append((v, peso))
    
    def dijkstra(self, inicio):
        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[inicio] = 0
        pq = [(0, inicio)]
        while pq:
            distancia_atual, vertice_atual = heapq.heappop(pq)
            if distancia_atual > distancias[vertice_atual]:
                continue
            for vizinho, peso in self.grafo[vertice_atual]:
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(pq, (distancia, vizinho))
        return distancias

# Exemplo de uso:
g = Grafo()
g.adicionar_aresta('A', 'B', 5)
g.adicionar_aresta('A', 'C', 3)
g.adicionar_aresta('B', 'C', 2)
g.adicionar_aresta('B', 'D', 6)
g.adicionar_aresta('C', 'D', 7)
g.adicionar_aresta('C', 'E', 4)
g.adicionar_aresta('D', 'E', 1)
print("Distâncias mínimas a partir de 'A':", g.dijkstra('A'))
