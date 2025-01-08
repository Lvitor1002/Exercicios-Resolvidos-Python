# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
import os

def leitura(n):
    if n[:5] == 'santo':
        print(f"\n>Nome [Santo] reconhecido em [{(n).capitalize()}]\n")
    else:
        print(f">Nome [Santo] não encontrado!\n")


nome = str(input("\n>Digite o nome de uma cidade: ")).strip().lower()

os.system('cls')
leitura(nome)