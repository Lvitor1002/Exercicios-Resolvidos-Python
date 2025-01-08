'''
Escreva uma função em Python que receba uma lista de números e retorne a soma dos quadrados desses números.
'''
def funcao(lista):
    return sum(i ** 2 for i in lista)
    


lista = [1,2,3,4,5]

print(f"\nNúmeros: ",end='')
for i in lista:
    print(f"{i}",end=' | ')

print(f"\n\nSoma dos quadrados: {funcao(lista)}\n")