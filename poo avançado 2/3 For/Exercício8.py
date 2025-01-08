'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date 
import os

def leitura():
    atual = date.today().year
    soma_maior = 0
    soma_menor = 0
    print("\nAno de nascimento: ")
    for i in range(1,8):
        ano = int(input(f"\n>{i}ª "))

        idade = atual - ano
        if idade < 18:
            soma_menor += 1
        else:
            soma_maior += 1
    return f"\n>Total de pessoas menores de idade: {soma_menor}\n>Total de pessoas maiores de idade: {soma_maior}\n"



os.system('cls')
print(leitura())
