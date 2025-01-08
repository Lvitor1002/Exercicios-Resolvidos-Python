'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
import os 
def menu():
    op = int(input('''\n>Escolha uma forma de pagamento abaixo:
                \n>[1] - À vista Dinheiro ou Cheque
                \n>[2] - À vista no cartão de Crédito
                \n>[3] - Em até 2x no cartão de Crédito
                \n>[4] - Em 3x ou mais no cartão de Crédito\n'''))
    return op


def calculo(p):
    op = menu()
    if op == 1:
        return f"\n>Opção 1: [À vista Dinheiro ou Cheque]\n>Ganhou 10% de desconto!\n>Valor do produto: {p:.2f}\n>Valor do produto com desconto: {p*0.90:.2f}\n"
    if op == 2:
        return f"\n>Opção 2: [À vista no cartão de Crédito]\n>Ganhou de 5% de desconto!\n>Valor do produto: {p:.2f}\n>Valor do produto com desconto: {p*0.95:.2f}\n"
    if op == 3:
        print(f"\n>Opção 3: [Em até 2x no cartão de Crédito]\n>Preço Normal!\n")
        try:
            op1 = int(input(">Você pode parcelar em até 2x\n>Digite quantas vezes deseja parcelar!\n>Pagamento em 1x digite [1]\n"))
            if op1 != 0 and op1 <= 2:
                return f">Valor do produto: {p:.2f}\n\n>Valor do produto parcelado em {op1}x de {p/op1:.2f}: {p:.2f} \n"
            else:
                print("\n>Erro, você pode parcelar em somente até 2x!\n")
        except ValueError:
            print("\n>Entrada inválida!\n")
    if op == 4:
        print(f"\n>Opção 4: [Em 3x ou mais no cartão de Crédito]\n>Preço com 20% de Juros!\n")
        try:
            op1 = int(input(">Você pode parcelar em 3x ou mais vezes\n>Digite quantas vezes deseja parcelar!\n"))
            if op1 >= 3:
                return f">Valor do produto: {p:.2f}\n\n>Valor do produto parcelado em {op1}x de {(p/op1)*1.20:.2f}: {((p/op1)*1.20)*op1:.2f}\n"
            else:
                print("\n>Erro, você pode parcelar no mínimo em 3x!\n")
        except ValueError:
            print("\n>Entrada inválida!\n")

os.system('cls')
produto = float(input("\n>Digite o preço do produto: "))
print(calculo(produto))