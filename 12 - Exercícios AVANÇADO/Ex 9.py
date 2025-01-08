'''Escreva uma função em Python que receba uma lista de números e retorne a mediana desses números'''

def media(lista):
    ordenada = sorted(lista) # é preciso primeiro ordenar os valores [MODA]
    numero = len(ordenada)
    if numero % 2 == 0:
        return (ordenada[numero//2 -1] + ordenada[numero//2]) / 2  # Se o número de elementos é par, a mediana é a média dos dois elementos centrais
    else:
        return ordenada[numero//2] # Se o número de elementos é ímpar, a mediana é o elemento central


lista = [5, 2, 8, 1, 3, 7, 9, 4, 6]
print("="*60)
print("Mediana dos números:", media(lista))
print("="*60)