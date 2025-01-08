# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

import os 

def leitura(n):
    if 'silva' in n:
        print(f"\n>[Silva] encontrado\n>{(n).capitalize()}\n")
    else:
        print(f">[Silva] não encontrado!\n")


os.system('cls')
nome = str(input("\n>Digite o seu nome completo: ")).lower().strip()

leitura(nome)