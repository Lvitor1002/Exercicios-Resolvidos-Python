# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

import os 

def medidas():
    print("\n>Digite 3 medidas para um triângulo: ")
    lista = [int(input(f">{i}ª: ")) for i in range(1,4)]
    return lista 


def triangulo(lista):
    if lista[0] < (lista[1] + lista[2]) and lista[1] < (lista[0] + lista[2]) and lista[2] < (lista[0] + lista[1]):
        print(f"\n>Triângulo formado!\n")
    else:
        print(f"\nNão foi possível formar um triângulo!\n")

os.system('cls')
medida = medidas()
triangulo(medida)