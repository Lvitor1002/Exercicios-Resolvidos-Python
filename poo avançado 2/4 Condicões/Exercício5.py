# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

import os

def numero():
    print("\nDigite 3 números: ",end='')
    numeros = [int(input(f">{i}ª: ")) for i in range(1,4)]
    return numeros

def exibir(numeros):
    if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
        print(f"\n>Maior número: {numeros[0]}\n")
    if numeros[1] > numeros[0] and numeros[1] > numeros[2]:
        print(f">Maior número: {numeros[1]}\n")
    if numeros[2] > numeros[0] and numeros[2] > numeros[1]:
        print(f">Maior número: {numeros[2]}\n")
    if numeros[0] < numeros[1] and numeros[0] < numeros[2]:
        print(f">Menor número: {numeros[0]}\n")
    if numeros[1] < numeros[0] and numeros[1] < numeros[2]:
        print(f">Menor número: {numeros[1]}\n")
    if numeros[2] < numeros[0] and numeros[2] < numeros[1]:
        print(f">Menor número: {numeros[2]}\n")
    if numeros[1] == numeros[0] == numeros[2]:
        print(f"\n>Números iguais: [{numeros[0]}] | [{numeros[1]}] | [{numeros[2]}]\n") 

def main():
    n = numero()
    exibir(n)

os.system('cls')
main() 
          