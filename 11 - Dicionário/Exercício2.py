'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a pessoa não possuir carteira, o dicionário retornará apenas valores iniciais, caso contrário o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date
import os

def dados():

    dicionario = {}

    os.system('cls')
    while True:
        nome = str(input("Digite o seu nome: ")).lower().capitalize().strip()
        if not nome.isalpha():
            os.system('cls')
            print(">Entrada inválida!\nEsperava uma 'String'\n")
            continue
        else:
            dicionario["Nome:"] = nome
            break
        
    
    os.system('cls')
    while True:
        ano = int(input(">Digite o ano de nascimento: "))
        if len(str(ano)) == 4:
            dicionario['Ano de Nascimento:'] = ano
            dicionario["Idade:"] = date.today().year - int(ano)
            idade = int(dicionario["Idade:"])
            break
        else:
            os.system('cls')
            print(f">Erro. Entrada inválida ou excedeu o limite númerico de 4 digitos: {ano}!\n>Tente novamente..\n")
            continue            
    

    op = str(input(">Possui carteira de trabalho? ")).strip().lower()
    if op in ['S','s','sim','Sim','SIM']:
        os.system('cls')
        while True:
            try:
                carteira = int(input(">Digite o número da carteira de trabalho: "))
                dicionario['Carteira de Trabalho:'] = carteira

                
                break
            except ValueError:
                os.system('cls')
                print(">Entrada inválida! Esperava um número inteiro! >Tente novamente!\n")
                continue


        os.system('cls')
        while True:
            admissao = input(">Digite o ano de sua admissão trabalhista: ").strip()
            if len(str(admissao)) == 4:
                dicionario['Adimissão:'] = admissao
                break
            else:
                os.system('cls')
                print(f">Erro. Entrada inválida ou excedeu o limite númerico de 4 digitos: {ano}!\n>Tente novamente..\n")
                continue 


        os.system('cls')
        while True:
                try:
                    salario = input(">Digite o seu salário: ").strip().replace(',', '.')
                    salario = float(salario)
                    dicionario["Salário: "] = salario

                    break
                except ValueError:
                    print(">Entrada inválida! Esperava um número inteiro! >Tente novamente!\n")
                    continue
        
        tempo_admissao = date.today().year - int(admissao)
        dicionario['Idade de Aposentadoria:'] = idade + (35 - tempo_admissao) # 35 Mínimo a servir (-) tempo de contrato. Somando com a idade, resulta no ano da aposentadoria
        dicionario['Ano de Aposentadoria:'] = date.today().year - (idade - dicionario['Idade de Aposentadoria:'])
     
    else:
        os.system('cls')
        print(">Sem carteira de trabalho!\n")

    return dicionario

def exibir():
    pessoa = dados()
    os.system('cls')
    print(">Dados cadastrados: \n")
    for c,v in pessoa.items():
        print(f"{c:<25}{v}")