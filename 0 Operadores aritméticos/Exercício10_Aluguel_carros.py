'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

'''

import os 
def leitura():
    quilometros = int(input("\n>Digite a quantidade de KM percorridos pelo carro: "))
    dias = int(input(">Quantos dias o carro ficou alugado? "))
    return quilometros, dias

def calculo(quilometros, dias):
    print("\nConsiderando a taxa de locação de R$60 por dia..\nConsiderando também a taxa de R$0.15 a cada KM rodado..\n")
    return dias*60 + (quilometros*0.15)

def main():
    quilometros, dias = leitura()
    valor = calculo(quilometros, dias) 
    print(f">Valor final a pagar por alugar um carro por {dias} dias rodando {quilometros}KM: R${valor} reais\n")

os.system('cls')
main() 