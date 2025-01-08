# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

import os 
def numero(n):
    if n % 2 == 0:
        print(f"\n>Número {n} é Par!\n")
    else:
        print(f"\n>Número {n} é Ímpar!\n")


try:
    os.system('cls')
    n = int(input("\n>Digiteu um número: "))
    numero(n)
except ValueError:
    print("\n>Entrada inválida!\n")
