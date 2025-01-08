'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''
import os

def letras_editada(n):
    return f"\n>Nome maiúsculo: {n.upper()}\n" 

def quantidade_letras(n):
    sem_espacos = n.replace(' ','')
    return f">Total de letras: {len(sem_espacos)} letras\n" 

def quantidade_letras_primeiro(n):
    divididos = n.split()
    return f">Quantidade de letras do primeiro nome [{divididos[0]}]: {len(divididos[0])} letras\n"


def main():
    nome = str(input('\n>Digite o nome completo: '))
    letras_edit = letras_editada(nome)
    quantidade_letr = quantidade_letras(nome)
    quantidade_letras_prime = quantidade_letras_primeiro(nome)

    print(f"{letras_edit}\n{quantidade_letr}\n{quantidade_letras_prime}\n")


os.system('cls')
main()