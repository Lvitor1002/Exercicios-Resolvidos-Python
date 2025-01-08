'''
Implementação de Árvore de Busca Binária:

Escreva uma classe em Python que represente uma árvore de busca binária (BST). 
Uma árvore de busca binária é uma estrutura de dados que mantém os valores em nós organizados em uma árvore. 
Cada nó tem no máximo dois filhos, um à esquerda e outro à direita. 
A propriedade fundamental da BST é que, para cada nó, todos os valores na subárvore à esquerda são menores que o valor do nó e
 todos os valores na subárvore à direita são maiores. 
Implemente métodos para inserção, busca e remoção de elementos.
'''

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)
    
    def _inserir(self, no, chave):
        if no is None:
            return No(chave)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        else:
            no.direita = self._inserir(no.direita, chave)
        return no

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)
    
    def _remover(self, no, chave):
        if no is None:
            return no
        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            no.chave = self._menor_no_valor(no.direita).chave
            no.direita = self._remover(no.direita, no.chave)
        return no

    def _menor_no_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

# Exemplo de uso:
arvore = ArvoreBuscaBinaria()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(70)
arvore.inserir(60)
arvore.inserir(80)
print(arvore.buscar(70))  # Saída: <__main__.No object at 0x7f8e3e6ec610>
arvore.remover(70)
print(arvore.buscar(70))  # Saída: None
