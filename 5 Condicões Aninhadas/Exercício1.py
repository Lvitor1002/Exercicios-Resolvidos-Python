'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.

'''
import os 

def conversao(n):
    binario = bin(n)
    octal = oct(n)
    hexa = hex(n)
    op = int(input("\n>Escolha a base de conversão:\n>[1]Binário\n>[2]Octal\n>[3]Hexadecimal\n"))
    if op == 1:
        return f"\n> Número [{n}] em Binário: {(binario[2:].upper())}\n" 
    if op == 2:
        return f"\n> Número [{n}] em Octal: {(octal[2:]).upper()}\n" 
    if op == 3:
        return f"\n> Número [{n}] em Hexadecimal: {(hexa[2:]).upper()}\n" 
    else:
        print(f"\n>Escolha uma opção válida!\n")


os.system('cls')
numero = int(input("\n>Digite um número: "))
print(conversao(numero))