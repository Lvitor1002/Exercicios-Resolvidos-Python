# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

import os

def leitura():
    while True:
        try:
            numero = int(input("\n>Digite um número de 1 à 9999: "))
            if 1 <= numero <= 9999:
                unidade = numero % 10 
                dezena = (numero // 10) % 10
                centena = (numero // 100) % 10
                milhar = (numero // 1000) % 10
                return unidade, dezena, centena, milhar
            else:
                print(">Fora de alcance, tente novamente!\n")
        except ValueError:
            print("\n>Entrada inválida! É permitido apenas números!\n")
    


def exibe():
    unidade, dezena, centena, milhar = leitura()
    print(f"Milhar: {milhar}")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")

os.system("cls")
exibe()