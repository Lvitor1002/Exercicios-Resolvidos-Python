# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import os 

def dobro(n):
    return f"Dobro de {n}: {n * 2}\n"

def triplo(n):
    return f"Triplo de {n}: {n*3}\n"

def raiz(n):
    return f"Raiz de {n}: {n**(1/2):.0f}\n"

numero = int(input("\nDigite um número: "))
os.system('cls')

op = str(input(">Escolha uma das opções abaixo:\n>[Dobro]\n>[Triplo]\n>[Raiz]\n")).strip().capitalize()

if op == 'Triplo' or op == 'triplo':
    print(triplo(numero)) 
elif op == 'Dobro' or op == 'dobro':
    print(dobro(numero)) 
elif op == 'Raiz' or op == 'raiz':
    print(raiz(numero))
else:
    print("Opção incorreta!\n")
