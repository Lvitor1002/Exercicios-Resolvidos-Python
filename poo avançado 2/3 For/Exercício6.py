#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


import os 
def primo(n):
    if n <= 1:
       return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

os.system('cls')
n = int(input("\n>Digite um número: "))

if primo(n):
    print(f">{n} é um número primo!\n")
else:
    print(f">{n} não é um número primo!\n")


