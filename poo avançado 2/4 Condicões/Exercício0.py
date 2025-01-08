'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''
from random import randint 
from time import sleep
import os

def pensando():
    print("\n>Máquina pensando em um número de 0 à 5...")
    sleep(1)
    return randint(0, 5)


def escolha():
    while True:
        numero = pensando()
        sleep(0.5)
        print("\n>Tente adivinhar um número de 0 à 5 escolhido pelo computador: ", end='')
        try:
            escolha = int(input("> "))
            if 0 <= escolha <= 5: 
                if escolha == numero:
                    print(f"\n>Acertou!!\n>Sua escolha: {escolha}\n>Escolha do pc: {numero}\n")
                    return
                else:
                    print(f"\n>Errou!!\n>Sua escolha: {escolha}\n>Escolha do pc: {numero}\n\n>Tente novamente!\n")
            else:
                print(">Digite apenas no intervalo de 0 à 5!\n")
        except ValueError:
            print(">Entrada inválida! Tente novamente!\n")


def main():
    escolha()


os.system('cls' if os.name == 'nt' else 'clear')
main()

