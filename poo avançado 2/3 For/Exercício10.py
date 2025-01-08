'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

import os
def leitura():
    soma_idade = 0
    soma_mulher = 0
    homem_velho = ''
    idade_homem_mais_velho = 0


    print("\n>Preencha abaixo: ")
    for i in range(4):
        print(f"\n-=-= <{i+1}ª> -=-=")
        nome = str(input(">Nome: ")).strip().lower().capitalize()
        idade = int(input(">Idade: "))
        sexo = str(input(">Sexo: [M][F]")).strip().upper()
        soma_idade += idade

        if sexo == "M":
            if idade > idade_homem_mais_velho:
                idade_homem_mais_velho = idade
                homem_velho = nome 

        
        if sexo == 'F' and idade < 20:
            soma_mulher += 1

    return soma_idade, soma_mulher, homem_velho


def media(soma_idade):
    return soma_idade/4


def main():
    soma_idade, soma_mulher, homem_velho = leitura()
    media_idades = media(soma_idade)

    print(f"\n>Média de idades: {media_idades:.2f}")
    print(f">Homem mais velho: {homem_velho}")
    print(f">Quantidade de mulheres menores de 20 anos: {soma_mulher}\n")

os.system('cls')
main()


