'''
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.

'''
import os 
def velocidade():
    velocidade = int(input("\n>Digite a velocidade em KM: "))
    return velocidade


def multa(velocidade):
    if velocidade > 80:
        print(f"\n>Velocidade do carro: {velocidade} KM/h. Carro multado!\n>Valor da multa: R${((velocidade - 80)*7):.2f} reais!\n")
    else:
        print(f"\n>Velocidade do carro: {velocidade} KM/h.\n>Siga viagem!\n")


def main():
    velocidade_carro = velocidade()
    multa(velocidade_carro)


os.system('cls')
main()