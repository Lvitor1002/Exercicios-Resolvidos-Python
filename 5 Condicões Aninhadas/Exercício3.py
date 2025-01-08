'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import os 
from datetime import date 

def leitura(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano 
    return idade


def alistamento(idade):
    ano_atual = date.today().year
    if idade < 18:
        print(f"\n>{idade} anos. Ainda faltam {18-idade} anos para o seu alistamento que será no ano de {(ano_atual) + (18-idade)}!\n")
    elif idade == 18:
        print(f"\n>{idade} anos. Alistamento pendente!\n")
    elif idade <= 21:
        print(f"\n>Você tem até o ano de {ano_atual + 3} para se alistar!\n")
    else:
        print(f"\n>{idade} anos. Irregular! Seu ano de alistamento foi no ano de {ano_atual - (idade -18)}!\n")
        

def main():
    ano = int(input("\n>Digite o seu ano de nascimento: "))
    idade = leitura(ano)
    alistamento(idade)


os.system("cls")
main()