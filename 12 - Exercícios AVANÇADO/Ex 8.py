'''Escreva uma função em Python que receba uma lista de strings e retorne uma lista contendo as strings ordenadas por ordem alfabética, 
ignorando maiúsculas e minúsculas.'''


def ordenadas(lista):
    return sorted(lista, key=str.lower) # lower para padronizar todas como minúsculas


lista = ["Maçã", "banana", "Abacaxi", "uva", "laranja"]

print('='*60)
print(f"Palavras em ordem: ",end='')
for i in ordenadas(lista):
    print(f"{i}",end=' |')
print()
print('='*60)