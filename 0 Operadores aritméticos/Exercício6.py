'''
Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pinta-lá, 
sabendo que cada litro de tinta, pinta uma área de 2m^2.
'''

import os

def leitura():
    print()
    largura = float(input('> Digite a largura da parede em metros: '))
    altura =  float(input("> Digite a altura da parede em metros: "))
    return largura, altura

def area(largura, altura):
    return largura * altura

def calculo(area):
    return area/2

def main():
    largura, altura = leitura()
    a = area(largura, altura)
    quantidade = calculo(a)
    print(f'> Área total: {a}m²\n> Quantidade de tinta necessária: {quantidade:.2f}L\n')


os.system('cls')
main()