'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

import os 
def leitura(): 
    while True:
        sexo = input("\n>Digite o sexo: [M][F]").lower()            
        if sexo == 'f':
            print("\n>Correto!")
            print(">Sexo FEMININO!")
            break
        elif sexo == 'm':
            print("\n>Correto!")
            print("\n>Sexo MASCULINO!")
            break
        else:
            print("\n>Apenas M e F é permitido!\n>Tente novamente!\n")
            continue

os.system('cls')

leitura()
