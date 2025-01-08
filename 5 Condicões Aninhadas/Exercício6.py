'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
Mostre que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
import os 

def leitura():
    print("\nDigite três valores: ")
    lista = [int(input(f"\n>{i}ª: ")) for i in range(1,4)]
    return lista

def triangulo(lista):
    if lista[0] < (lista[1] + lista[2]) and lista[1] < (lista[0] + lista[2]) and lista[2] < (lista[0] + lista[1]):
        print("\n>Triângulo formado..!")
        if lista[0] == lista[1] == lista[2] == lista[0]:
            print("\n>Triângulo EQUILÁTERO formado..!")
        elif lista[0] != lista[1] != lista[2] != lista:
            print("\n>Triângulo ESCALENO formado..!")
        else:
            print("\n>Triângulo ISÓSCELES formado..!")
    else:
        print("\n>Erro, não é um Triângulo..!\n")


os.system('cls')
valores = leitura()
triangulo(valores)
