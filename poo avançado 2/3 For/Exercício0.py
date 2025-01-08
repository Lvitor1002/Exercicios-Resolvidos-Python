'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles
'''
import os
from time import sleep

def regressiva():
    print("\n>Contagem regressiva: ")
    for i in range(11,0,-1):
        sleep(1)
        print(i-1)
    print("-=-= Feliz ano novo :) -=-=\n")

os.system('cls')
regressiva()