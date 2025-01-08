'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.
'''
import os
import random 
 
def maquina_pensando():
    return random.randint(0,10)

def jogador_advinha():
    soma = 0
    while True:
        maquina = maquina_pensando()
        try:
            jogador = int(input("\n>Tente adivinhar o número escolhido pela máquina de 0 à 10: "))
            if jogador >= 0 and jogador <= 10:
                if jogador == maquina:
                    print(f"\n>Jogador acertou!!\n>Jogador escolheu: {jogador}\n>Máquina escolheu: {maquina}\n")
                    break
                else:
                    soma += 1
                    print(f"\n>Jogador errou!!\n>Jogador escolheu: {jogador}\n>Máquina escolheu: {maquina}\n>Tente novamente!!\n")
                    continue
            else:
                print("\n>Entrada inválida! Fora do intervalo de 0 à 10!!\n")
        except ValueError:
            print("\n>Entrada inválida!\n")
    print(f">Foi preciso {soma} tentativas!\n")


os.system('cls')
jogador_advinha()
