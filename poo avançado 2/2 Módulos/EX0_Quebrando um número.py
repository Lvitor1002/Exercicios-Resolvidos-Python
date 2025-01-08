'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.

'''
import os
def transformacao(n):
    return f"\n>nNúmero real: [{n}], convertido para inteiro: [{int(n)}]\n"

os.system('cls')
numero = float(input("\n>Digite um número: "))
print(transformacao(numero))
