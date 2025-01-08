'''
Escreva uma função em Python que receba uma lista de números e retorne uma lista com os números ordenados de forma decrescente, 
sem modificar a lista original.
'''


def listas(lista):
    ordenada = lista[:]
    return sorted(ordenada,reverse=True) 


lista = [1,4,8,5,6]

def exibir(lista):
    print("-="*60)
    print("Lista original: ",end='')
    for i in lista:
        print(f"{i}",end=' | ')
    print("\n\nLista decrescente: ",end='')
    for i in listas(lista):
        print(f"{i}",end=' | ')
    print()
    print("-="*60)


exibir(listas(lista))

