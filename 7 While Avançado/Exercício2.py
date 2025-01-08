'''
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''

import random 
import os 


def leitura():
    usuario = str(input("\n>Par ou Impar?")).strip().lower()
    numero_usuario = int(input("\n>Digite um número de 1 à 10: "))
    os.system('cls')
    pc = ['par','impar']
    aleatorio_pc = random.choice(pc)

    numero_pc = random.randint(1,10)

    total = numero_pc + numero_usuario
    return usuario, aleatorio_pc, numero_pc, numero_usuario, total


def validar():
    tentativas_ganhas = 0
    
    print("-="*50)
    while True:
        usuario, aleatorio_pc, numero_pc, numero_usuario, total = leitura()
        if usuario == aleatorio_pc:
            print(">Não é permitido escolher o mesmo simbolo. Tente novamente.!")
            continue
        if (usuario == 'impar' and total % 2 != 0) or (usuario == 'par' and total % 2 == 0):
            print(f">Usuário escolheu: [{usuario}] e o Número: [{numero_usuario}]\n\n>PC escolheu: [{aleatorio_pc}] e o número: [{numero_pc}]!\n\n>Total: {total} - [Vitória do usuário]")
            print(f"\n>Total de tentativas: {tentativas_ganhas}\n")
            op = str(input("\n>Deseja continuar? [Sim][Não]:\n")).strip().lower()
            if op == 'sim':
                continue 
            else:
                exit()
        else:
            tentativas_ganhas += 1
            print(f">Usuário escolheu: [{usuario}] e o Número: [{numero_usuario}]\n\n>PC escolheu: [{aleatorio_pc}] e o número: [{numero_pc}]!\n\n>Total: {total} - [Vitória do PC]")
            print("-="*50)
       

os.system('cls')
validar()


