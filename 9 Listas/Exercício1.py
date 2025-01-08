'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''
import os 

def adicionar_valores():
    os.system('cls')
    lista = []
    while True:
        try:
            print(">Digite alguns valores:\n>Para interromper digite [999]\n",end='')
            while True:
                valor = int(input("> "))
                if valor == 999:
                    return lista
                if valor not in lista:
                    lista.append(valor)
                    os.system('cls')
                    print(f">Valor {valor} adicionado!\n\n>>[999] - Parar<<\n")
                else:
                    os.system('cls')
                    print(f">Valor {valor} já existente na lista! Tente novamente!\n")
        except ValueError:
            os.system('cls')
            print(">Entrada inválida! Tente novamente!\n")
            continue

def exibir():
    while True:
        valores = adicionar_valores()
        os.system('cls')
        print("-="*60)
        print(f"Valores adicionados: |",end='')
        for i in sorted(valores):
            print(f"{i}",end='|')
        print()
        op = input(f">Deseja continuar? [Sim][Não] -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n").strip().lower()
        print("-="*60)
        if op == 'sim' or op == 's':
            continue
        else:
            os.system('cls')
            print("\n>Saindo..!")
            exit()


exibir()



