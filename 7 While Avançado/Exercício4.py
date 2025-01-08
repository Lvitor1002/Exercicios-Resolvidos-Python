'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

import os 
def cadastro():
    nome_produto = ""
    preco_barato = float("inf")
    total_compra = quantidade_mil = 0

    print("\n>Preencha abaixo: ")
    while True:
        nome = str(input(">Nome: ")).strip().casefold()
        valor = float(input("Preço: R$ "))
        total_compra += valor
        
        if valor > 1000:
            quantidade_mil += 1
        
        if valor < preco_barato:
            nome_produto = nome 
            preco_barato = valor
        
        op = str(input("Deseja Sair? Sim ou Não\n")).strip().lower()
        if op == 'sim':
            print("\nSaindo..\n")
            break
        else:
            continue   
    return nome_produto, preco_barato, total_compra, quantidade_mil


def exibir():
    nome_produto, preco_barato, total_compra, quantidade_mil = cadastro()
    print(f">Total da compra: R${total_compra}\n")
    print(f">Quantidade produtos que custam mais de R$1000: {quantidade_mil}\n")
    print(f">Produto mais barado: >{nome_produto} saindo por R$:{preco_barato}\n")
 

os.system('cls')
exibir()