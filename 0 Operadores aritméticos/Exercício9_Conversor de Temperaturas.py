# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

import os

def graus(t):
    return f"\n> {t}º Graus.\n"

def conversao(t):
    return f'{((9*t)/5)+32:.1f}'

os.system('cls')
temperatura = float(input("> Digite a temperatura atual: "))
convertido = conversao(temperatura)

print(graus(temperatura))
print(f"> Temperatura em Fahrenheit: {convertido}º\n")