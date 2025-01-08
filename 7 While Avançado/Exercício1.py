'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. 
'''
import os 

def tabuada():
    while True:
        print("\n>Digite um número para a tabuada: ")
        try:
            numero = int(input())
            if numero >= 0:
                os.system('cls')
                print("-="*15)
                for i in range(0,11):
                    print(f"{numero} x {i} = {numero*i}")
                print("-="*15)
                continue
            else:
                os.system('cls')
                print("-="*15)
                print(f">Fim. Número negativo digitado: [{numero}]!")
                print("-="*15)
                break
        except ValueError:
            os.system('cls')
            print(">Erro, apenas números inteiros são permitidos!\nTente novamente..")
            continue





os.system('cls')
tabuada()