'''
Escreva um programa que leia dois números inteiros e compare-os. 
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais

'''

import os 

def comparando():
    print(f"\n>Digite 2 valores: ")
    lista = [int(input(f">{i}ª: ")) for i in range(1,3)]
    return lista 

def exibir(lista):
    if lista[0] > lista[1]:
        print(f'\n>Primeiro valor [{lista[0]}] é Maior!\n')
    if lista[0] < lista[1]:
        print(f'\n>Segundo valor [{lista[1]}] é Maior!\n')
    if lista[0] == lista[1] == lista[0]:
        print(f'\n>Valores iguais! [{lista[0]}] | [{lista[1]}] \n')


os.system('cls')
numeros = comparando()
exibir(numeros)