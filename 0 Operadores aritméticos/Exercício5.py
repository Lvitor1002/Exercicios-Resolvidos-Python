# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e (mostre quantos dólares ela pode comprar). Não é apenas converter.
# valor/3.27


import os 

def carteira():
    while True:
        try:
            valor = float(input("\nDigite o valor atual da sua carteira..\n>R$: "))
            return valor 
        except ValueError:
            print("Entrada inválida!\n")
        

def conversao(valor):
    return f"> Valor em dólares ${valor*5.29:.2f}\n"

def cambio(valor):
    return f"> Com R${valor} reais é possível comprar ${(valor / 3.29):.2f} dólares!"


def main(valor):
    op = str(input("Deseja converter para dólares? [Sim][Não]\n")).strip().capitalize().lower()
    if op == 'sim':
        print("-="*60)
        print(f"> Você possui R${valor} reais em sua carteira\n")
        print(conversao(valor))
        print(cambio(valor))
        print("-="*60) 
    elif op == 'não':
        print("-="*60)
        print(f"> Valor em real R${valor}")
        print("-="*60)
    else:
        print("Opção inválida. Por favor, responda com 'Sim' ou 'Não'.")
    return 
 

os.system('cls')
c = carteira()
main(c)