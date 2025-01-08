'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

import os 

def dados():
    aluno = []
    notas = []
    os.system('cls')
    while True:
        nome = str(input("Digite o seu nome: ")).strip().lower().capitalize()
        if not nome.isalpha():
            os.system('cls')
            print(">Entrada inválida. Esperava uma 'string'!\n")
            continue
        else:
            aluno.append(nome)
            break
    
    os.system('cls')
    print(f">Digite 2 notas para {nome}: ")
    soma = 0
    for i in range(1,3):
        while True:
            try:
                nota = input(f">{i}ª ").replace(",",".")
                
                nota = float(nota)
                notas.append(nota)
                soma += nota
                break 
            except ValueError:
                os.system('cls')
                print(">Entrada inválida. Esperava um 'inteiro'!\n")
                continue
    
    media = soma/2
    aluno.append(notas)
    aluno.append(media)
    
    
    
    return aluno


def varios_alunos():
    alunos = []
    
    while True:
        unico_aluno = dados()
        
        if unico_aluno:
            alunos.append(unico_aluno)
        else:
            os.system('cls')
            print(">Nenhum aluno foi adicionado!\n")
            continue
        
        
        op = str(input(">Deseja continuar? [Sim][Não]\n")).strip().lower()
        if op not in ['sim','não']:
            os.system('cls')
            print(">Entrada inválida! Digite 'Sim' ou 'Não'\n")
            continue
        elif op == 'não':
            return alunos
        
 
def exibir():
    alunos = varios_alunos()
    
    os.system('cls')
    print(">Boletim dos alunos:\n")
    for i, a in enumerate(alunos):
        print(f">{i+1}ª| {a[0]} - Média: {a[2]:^5}")
    
    while True:
        try:
            
            op = input("\n>Escolha um aluno pelo número do índice de sua posição para vizualizar as notas\n>Para finalizar digite 'sair'\n> ").strip().lower()
            if op == 'sair':
                print(">Saindo..")
                break
            
            op = int(op)
            if 1 <= op <= len(alunos):
                os.system('cls')
                    
                escolhido = alunos[op - 1]
                print(">Boletim dos alunos:\n")
                for i, a in enumerate(alunos):
                    print(f">{i+1}ª| {a[0]} - Média: {a[2]:^5}")
                print()
                
                print("-="*10)
                print(f">Notas do aluno(a) {escolhido[0]}: ")
                for i, nota in enumerate(escolhido[1],start=1):
                    print(f"            Nota {i}: {nota:.2f}")
                
                print("-="*10)
            else:
                os.system('cls')
                print("> Opção inválida! Escolha um número dentro do intervalo disponível.")
                
                    
        except ValueError:
            print(">Entrada inválida. Esperava um 'inteiro'!\n")
            continue
        
exibir()