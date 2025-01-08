'''Escreva uma função em Python que receba uma lista de números e retorne o produto dos elementos que estão em posições ímpares.'''


def recebe_lista(lista):
    p = 1
    for i in range(len(lista)): # Para posições ímpares
        if i % 2 != 0:
            p *= lista[i] # Para posições ímpares
    return p


def exibir(lista):
    print("="*60)
    print("Números: ",end=' | ')
    for i in lista:
        print(f"{i}",end=' | ')
    print(f"\n\nNúmeros em posições ímpares: {[lista[i] for i in range(len(lista)) if i % 2 != 0]}\n")
    print(f"Soma dos número ímpares: {recebe_lista(lista)}")
    print("="*60)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exibir(lista)
    