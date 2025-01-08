'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
d) Tupla Ordenada

'''

import os 

def gera_tupla():
    os.system('cls')
    print(">Digite 4 valores:\n")
    tupla = tuple(int(input(f">{i+1}ª: ")) for i in range(4))
    return tupla

def exibir():
    os.system('cls')
    tupla = gera_tupla()
    if 9 in tupla:
        if tupla.count(9) == 1:
            print(f"\n>O valor 9 Apareceu {tupla.count(9)} vez.\n")
        else:
            print(f"\n>O valor 9 Apareceu {tupla.count(9)} vezes.\n")
    else:
        print(">9 Não foi encontrado.\n")
    if 3 in tupla:
        print(f">O valor 3 Apareceu primeiramente na posição {tupla.index(3)+1}ª.\n")
    else:
        print(">3 Não foi encontrado.\n")

    pares = [valor for valor in tupla if valor % 2 == 0]
    print(f">Valores pares: {pares}\n")

    print(">Tupla ordenada: ",end=':')
    for i in sorted(tupla):
        print(f"{i}",end=': ')
    print()

exibir()