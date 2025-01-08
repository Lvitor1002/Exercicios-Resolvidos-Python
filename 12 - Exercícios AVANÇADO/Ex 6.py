'''Escreva uma função em Python que receba uma lista de números e retorne uma lista contendo apenas os números primos dessa lista.'''


def primos(numeros):
    if numeros <= 1:
        return False
    else:
        for i in range(2, int(numeros ** 0.5)+ 1):
            if numeros % i == 0:
                return False
    return True


def exibir(lista):
    p = []
    for i in lista:
        if primos(i):
            p.append(i)
    return p

lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print("="*60)
print(f"Números primos: {exibir(lista)}")
print("="*60)