'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

def fatorial():
    numero = int(input("\n>Digite um número para o fatorial: \n"))
    f = 1
    for i in range(numero,0,-1):
        f *= i
    print(f"\n{numero}!= {f}\n")

fatorial()