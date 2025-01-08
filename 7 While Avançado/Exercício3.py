
'''
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

import os

def cadastro():
    print("\n>Preencha abaixo: ")
    soma_pesoas = soma_idade = soma_masculino = soma_mulheres = 0

    while True:
        
        idade = int(input(">Idade: "))
        sexo = str(input("Sexo: [M][F]: ")).strip().casefold()
        soma_pesoas += 1

        if idade > 18:
            soma_idade += 1
        if sexo == 'm':
            soma_masculino += 1
        if sexo == 'f' and idade < 20:
            soma_mulheres += 1 

        os.system('cls')
        op = str(input("\n>Deseja continuar? [Sim][Não]\n")).strip().lower()
        if op == 'sim':
            continue
        else:
            print(">Saindo..\n")
            break
    return soma_pesoas, soma_idade, soma_masculino, soma_mulheres

def exibir():
    soma_pesoas, soma_idade, soma_masculino, soma_mulheres = cadastro()
    print(f"Quantidade de pessoas maiores de 18 anos de idade: {soma_idade}\n")
    print(f"Quantidade de homens cadastrados: {soma_masculino}\n")
    print(f"Quantidade de mulheres com menos de 20 anos: {soma_mulheres}\n")
    print(f"\nTotal de pessoas: {soma_pesoas}\n")

os.system('cls')
exibir()