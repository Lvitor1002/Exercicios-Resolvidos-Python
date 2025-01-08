# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math, os

def exibir(a):
    radianos = math.radians(a)
    sen = math.sin(a)
    cos = math.cos(a)
    tan = math.tan(a)
    print(f"\n>Seno de {radianos:.2f}: {sen:.2f}\n>Cosseno de {radianos:.2f}: {cos:.2f}\n>Tangente de {radianos:.2f}: {tan:.2f}\n")


os.system('cls')
a = float(input("\n>Digite um ângulo qualquer: "))
exibir(a)

