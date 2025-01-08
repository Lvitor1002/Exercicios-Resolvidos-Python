# Faça um programa que leia um número e mostre na tela o seu sucessor e seu antecessor.

import os

def sucessor(n):
    return f"O sucessor de {n} é {n+1}\n" 

def antecessor(n):
    return f"O antecessor de {n} é {n-1}" 

os.system('cls')
print("="*60)
print('>Digite um número: ')
try:
    
    n = int(input('> '))
    print(sucessor(n))
    print(antecessor(n))
    print("="*60)
except ValueError:
    print("Entrada inválida!\n")
    os.system('cls')
