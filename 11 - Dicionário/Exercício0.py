'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
import os 

def dados():
    d = {}
    while True:
        os.system('cls')
        nome = str(input(">Digite o seu nome: ")).strip().lower().capitalize()
        if not nome.isalpha():
            os.system('cls')
            print(">Entrada inválida! Esperava uma 'string'.\nTente novamente!\n")
            continue
        else:
            d['Nome:'] = nome
            break
    notas = []
    soma = 0
    os.system('cls')
    print(f">Digite duas notas para {d['Nome:']}:\n")
    for i in range(1,3):
        while True:
            try:
                n = input(f">{i}ª: ").replace(",",".")
                n = float(n)
                notas.append(n)
                soma += n
                break
            except ValueError:
                os.system('cls')
                print(">Entrada inválida! Esperava um 'inteiro'.\nTente novamente!\n")
                continue
            
    d['Média:'] = soma/2
    return d, notas

def classificacao(aluno,notas):
    if 0 <= aluno['Média:'] <= 4:
        aluno['Situação:'] = "Reprovado!"
    elif 4 < aluno['Média:'] <= 6:
        aluno['Situação:'] = "De exame!"
    elif 5 < aluno['Média:'] <= 10:
        aluno['Situação:'] = "Aprovado!"
    else:
        aluno['Situação:'] = "Erro, fora do intervalo!"
    return aluno


def exibir():
    
    alunos, notas = dados()
    aluno = classificacao(alunos,notas)
    
    os.system('cls')
    print(">Dados do Aluno:\n")
    while True:
        for c, v in aluno.items():
            print(f"{c} {v}")
        
        while True:
            
            op = str(input("\n>Deseja vizualizar as notas? 'Sim' ou 'Não'\n>Para finalizar digite 'sair'\n")).strip().lower()
            os.system('cls')
            if op == 'sair':
                os.system('cls')
                print(">Saindo...!")
                exit()
            if op == 'sim':
                os.system('cls')
                print("-="*10)
                print(f">Notas de {aluno['Nome:']}:\n")
                for i, n in enumerate(notas, start=1):
                    print(f"n{i}ª: {n}")
                print("-="*10)
                continue
            elif op == 'não':
                break
            else:
                os.system('cls')
                print(">Entrada inválida! \nTente novamente!\n")
                continue


exibir()