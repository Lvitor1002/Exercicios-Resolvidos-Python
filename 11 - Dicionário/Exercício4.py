'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
import os 
def dados():
    pessoa = {}
    mulheres = []
    
    os.system('cls')
    while True:
        nome = str(input(">Digite o seu nome: ")).strip().lower().capitalize()
        if not nome.isalpha():
            os.system('cls')
            print(">Entrada inválida! Tente novamente...\n")
            continue
        else:
            pessoa['Nome:'] = nome 
            break
    
    while True:
        sexo = str(input(">Digite o seu sexo: [M][F]")).strip().upper()
        if not sexo.isalpha():
            os.system('cls')
            print(">Entrada inválida! Tente novamente...\n")
            continue
        
        elif sexo in ['M','F']:
            pessoa['Sexo:'] = sexo 
            
            break
        
        else:
            os.system('cls')
            print(">Entrada inválida! Tente novamente...\n")
            continue
    
    while True:
        try:
            idade = int(input(">Digite a sua idade: "))
            if idade >= 1:
                pessoa['Idade:'] = idade
                break
        except ValueError:
            os.system('cls')
            print(">Entrada inválida! Tente novamente...\n")
            continue
    
    
    if pessoa['Sexo:'] == 'F':
        mulheres = [nome,sexo,idade]
    
    return pessoa, mulheres

def varias_pessoas():
    lista_pessoas = []
    lista_mulheres = []
    
    os.system('cls')
    while True:
        dicionario_pessoa, mulheres = dados()
        
        if dicionario_pessoa:
            lista_pessoas.append(dicionario_pessoa)
            
        if mulheres:
            lista_mulheres.append(mulheres)
     
        op = str(input(">Deseja continuar? [Sim][Não]\n")).strip().lower()
        if op == 'sim':
            continue 
        elif op == 'não':
            return lista_pessoas, lista_mulheres
        else:
            os.system('cls')
            print(">Entrada inválida! Tente novamente...\n")
            continue      

def main():
    pessoas, mulheres = varias_pessoas()
    
    os.system('cls')
    soma = 0
    
    print('~'*45)
    print(f"|{len(pessoas)}| pessoas adicionadas:\n")
    for i, pe in enumerate(pessoas):
        for c, v in pe.items():
            print(f"  \t\t{c} {v}")
        soma += pe['Idade:']
        print('-='*15) 
    
    print(f">Média das idade: {soma/len(pessoas):.2f}\n\n")
    
    print('~'*45)
    if mulheres:
        print(">Mulheres adicionadas:\n")
        for i, pe in enumerate(mulheres):
            print(f" \t\tNome: {pe[0]}\n \t\tSexo: {pe[1]}\n \t\tIdade: {pe[2]}")
            print('-='*15)
    else:
        print(">Não há mulheres!\n")
    
    print()
    print('~'*45)
    print(f'Lista com as pessoas maiores de {soma/len(pessoas):.0f} anos de idade:')
    media = soma/len(pessoas)
    for i, pe in enumerate(pessoas):
        for c, v in pe.items():
            if pe['Idade:'] > media:
                print(f"{c} {v}")
        print()
    print('-='*15) 
    

main()
        
    

            
        