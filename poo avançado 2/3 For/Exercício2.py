#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

import os
def calculo():
    soma = 0
    print("\n>Números multiplos de 3 de 1 à 500: ",end='')
    for i in range(1,501):
        if i % 3 == 0:
            soma += i
            print(f"{i}",end='-')
    print()
    print(f"\nSoma dos números: {soma}\n")    

os.system('cls')
calculo()