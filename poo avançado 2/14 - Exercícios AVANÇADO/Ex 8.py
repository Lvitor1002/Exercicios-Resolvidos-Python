'''
Implementação de uma Fila de Prioridade usando Heap Binária:

Escreva uma classe que represente uma fila de prioridade utilizando uma heap binária. 
Uma fila de prioridade é uma estrutura de dados que mantém uma coleção de elementos onde cada elemento tem uma prioridade associada. 
Os elementos com prioridade mais alta são removidos primeiro. 
Uma heap binária é uma árvore binária completa onde o pai é sempre menor (ou maior) que os seus filhos. 
Utilize a heap binária para implementar métodos para inserir elementos com prioridades diferentes e remover o elemento com a maior prioridade.
'''

import heapq

class FilaPrioridade:
    def __init__(self):
        self._fila = []
        self._indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self._fila, (-prioridade, self._indice, item))
        self._indice += 1

    def remover(self):
        return heapq.heappop(self._fila)[-1]

# Exemplo de uso:
fp = FilaPrioridade()
fp.inserir('A', 5)
fp.inserir('B', 10)
fp.inserir('C', 1)
print(fp.remover())  # Saída: B
print(fp.remover())  # Saída: A
print(fp.remover())  # Saída: C
