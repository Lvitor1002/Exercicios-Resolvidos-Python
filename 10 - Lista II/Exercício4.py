'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from time import sleep
import os, random 

def sorteio_mega():
    valores = []
    os.system("cls")
    while True:
        try:
            jogos = int(input(">Quantos jogos serão gerados? \n"))
            os.system("cls")
            for _ in range(jogos):
                valores.append(random.sample(range(1,61),6))
            break
        except ValueError:
            os.system("cls")
            print(">Entrada inválida!\n>Tente novamente..\n")
            continue
    return valores


def exibir():
    valores = sorteio_mega()
    print("-="*30)
    for jogos, numeros in enumerate(valores):
        print(f"{jogos+1}ª Partida: {numeros}")
        sleep(0.50)
    print("-="*30)

exibir()
