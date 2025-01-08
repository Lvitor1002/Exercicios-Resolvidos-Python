"""
Crie um programa para gerenciar informações de carros, onde cada carro possui um nome e uma potência. O programa permite realizar as seguintes operações:

Adicionar um novo carro, informando seu nome e potência.
Exibir informações de um carro específico.
Excluir um carro da lista.
Ligar um carro.
Desligar um carro.
Listar todos os carros cadastrados.
Sair do programa.
O programa deve exibir um menu com as opções disponíveis e solicitar ao usuário que escolha uma delas digitando o número correspondente. 
Ao finalizar uma operação, o menu deve ser exibido novamente até que o usuário opte por sair.

Implemente as classes e métodos necessários para realizar as operações mencionadas. Utilize a estrutura fornecida como base para o desenvolvimento do programa.
"""

import os


class Carro:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velocidade = int(potencia) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print("Nome:", self.nome)
        print("Potência:", self.potencia)
        print("Velocidade:", self.velocidade)
        print("Ligado:", 'sim' if self.ligado else 'não')


carros = []


def novo():
    os.system("cls") or None
    n = str(input("Nome: ")).strip().lower().capitalize()
    p = int(input("Potência: "))
    c = Carro(n, p)
    carros.append(c)
    print("-" * 60)
    print("Carro adicionado")
    os.system("pause")


def info():
    os.system("cls") or None
    op = int(input("Digite o número do carro que deseja ver as informações: ")) - 1
    try:
        carros[op].info()
    except IndexError:
        print("Carro não existe!\n")
    os.system("pause")


def excluir():
    os.system("cls") or None
    op1 = int(input("Digite o número do carro que deseja excluir: ")) - 1
    try:
        del carros[op1]
    except IndexError:
        print("Carro não existe!\n")
    print("-" * 60)
    print("Carro excluído!\n")
    os.system("pause")


def ligar():
    os.system("cls") or None
    op2 = int(input("Digite o número do carro que deseja ligar: ")) - 1
    try:
        carros[op2].ligar()
        print(f"Carro {carros[op2].nome} Ligado!")
    except IndexError:
        print("Carro não existe!\n")
    print("-" * 60)

    os.system("pause")


def desligar():
    os.system("cls") or None
    op3 = int(input("Digite o número do carro que deseja desligar: ")) - 1
    try:
        carros[op3].desligar()
        print(f"Carro {carros[op3].nome} Desligado!")
    except IndexError:
        print("Carro não existe!\n")
    print("-" * 60)

    os.system("pause")


def listar():
    os.system("cls") or None
    print('=' * 60)
    print("Todos os carros: ")
    for i, carro in enumerate(carros, 1):
        print(f"{i}ª Carro")
        carro.info()
        print('-' * 60)
    print('=' * 60)
    os.system("pause")


def quantidade():
    return len(carros)


def sair():
    print("-" * 60)
    print("Saindo..!\n")
    exit()


def menu():
    print("-" * 60)
    print(f"Quantidade atual de carros: {quantidade()}")
    print('''
1 - Novo Carro
2 - Informações do Carro
3 - Excluir Carro
4 - Ligar Carro
5 - Desligar Carro
6 - Listar Carro
7 - Sair
''')
    op4 = int(input("Escolha uma opção digitando o número: "))
    return op4


def exibir():
    print("-" * 60)
def exibir():
    print("-" * 60)
    while True:
        op = menu()
        print("-" * 60)
        if op == 1:
            novo()
        elif op == 2:
            info()
        elif op == 3:
            excluir()
        elif op == 4:
            ligar()
        elif op == 5:
            desligar()
        elif op == 6:
            listar()
        elif op == 7:
            op5 = str(input("Deseja sair? [Sim][Não]?\n")).strip().lower()
            if op5 == 'sim':
                sair()
        else:
            print("Opção inválida, tente novamente!")


exibir()


