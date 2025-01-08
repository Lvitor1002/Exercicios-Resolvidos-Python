'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.
'''
import os
def pares():
    soma = 0
    print("\nDigite 6 Números: ")
    lista = []
    for i in range(1,6):
        try:
            numero = int(input('> '))
            if numero % 2 == 0:
                lista.append(numero)
                soma += numero
        except ValueError:
            print("Entrada inválida!\n")
    return f"Soma dos números Pares {lista}: {soma}" 
    
os.system('cls')
print(pares())