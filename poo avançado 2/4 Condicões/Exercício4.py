# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
import os  


def ano_bissexto(a):
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            print(f">O ano {a} é bissexto.\n")
        else:
            print(f">O ano {a} não é bissexto.\n") 


def conferir(ano):
    if ano == 1:
        ano_atual = date.today().year
        ano_bissexto(ano_atual)
    else:
        ano_bissexto(ano)
    
    

os.system('cls')
ano = int(input("\n>Digite um ano qualquer que deseja analisar:\n>Digite [1] para analisar o ano atual:\n"))
conferir(ano)