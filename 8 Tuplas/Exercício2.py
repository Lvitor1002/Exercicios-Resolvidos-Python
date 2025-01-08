'''
Crie um programa que vai gerar cinco números aleatórios de 1 à 10 e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla, por fim, a tupla ordenada:.
'''
from random import sample
import os

def gera_tupla():
    numeros = tuple(sample(range(0,10),5))
    return numeros
    

def main():
    numeros = gera_tupla()
    os.system('cls')
    print("Tupla:")
    for n in numeros:
        print(f"> {n} <")
    print()
    print(f">Maior número gerado:{max(numeros)}\n\n>Menor número gerado:{min(numeros)}\n\n>Tupla ordenada: ",end='')
    for i in sorted(numeros):
        print(f"{i} > ",end='')
    print()

main()
    
