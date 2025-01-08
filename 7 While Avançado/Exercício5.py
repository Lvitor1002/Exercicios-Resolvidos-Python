'''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
import os
def caixa():
    valor = float(input("\n>Valor a ser sacado: R$"))
    c50 = c20 = c10 = c1 = 0

    if valor <= 0:
        print("\n>Erro. Valor mínimo para saque é de R$1!\n>Tente novamente!\n")
        
    while valor > 0:
        if valor >= 50:
            valor -= 50# Titando/Subtraindo do caixa o dinheiro solicitado
            c50 += 1 # Somando ao valor que será retornado para o usuário

        elif valor >= 20:
            valor -= 20# Titando/Subtraindo do caixa o dinheiro solicitado
            c20 += 1 # Somando ao valor que será retornado para o usuário
        
        elif valor >= 10:
            valor -= 10 # Titando/Subtraindo do caixa o dinheiro solicitado
            c10 += 1 # Somando ao valor que será retornado para o usuário

        elif valor >= 1:
            valor -= 1 # Titando/Subtraindo do caixa o dinheiro solicitado
            c10 += 1 # Somando ao valor que será retornado para o usuário
    
    print(f'\nVocê receberá >\n{c50} notas de 50\n{c20} de 20\n{c10} de 10\n{c1} de 1\n')

def main():
    print("\n\t\t>Caixa eletrônico!")
    while True:
        caixa()
        op = str(input(
            "\nPara continuar digite: 'Continuar'\nPara sair digite: 'Sair'\n")).strip().lower()
        if op == 'continuar':
            continue
        elif op == 'sair':
            print("\nSaindo..")
            break
        else:
            print("\nOpção inválida!")


os.system('cls')
main()