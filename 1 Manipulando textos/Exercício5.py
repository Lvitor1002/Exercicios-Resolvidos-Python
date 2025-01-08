# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

import os 

def primeiro_ultimo_nome(n):
    return f"\n>Primeiro nome: {(n[0]).capitalize()}\n\n>Último nome: {(n[-1]).capitalize()}\n" 


os.system('cls')
nome = str(input("\n>Digite o seu nome: ")).lower().split()
print(primeiro_ultimo_nome(nome))