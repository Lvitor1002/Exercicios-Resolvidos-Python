'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

'''
import os 

def distancia():
    d = int(input("\n>Digite a distância Percorrida em KM's: "))
    return d 


def calculo_passagem(d):
    if d <= 200:
        print(f"\n>Taxa para a distância de {d}KM: R${(d*0.50):.2f}\n")
    else:
        print(f"\n>Taxa para a distância de {d}KM: R${(d*0.45):.2f}\n")


def main():
    distancia_percorrida = distancia()
    calculo_passagem(distancia_percorrida)


os.system('cls')
main()