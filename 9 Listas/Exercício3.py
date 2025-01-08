'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''


import os

def add_numeros_lista():
    os.system('cls')
    lista = []
    print("Digite alguns números: ",end='')
    while True:
        try:
            valor = int(input("> "))
            if valor == 999:
                return lista
            else:
                lista.append(valor)
                os.system('cls')
                print(">Valor adicionado!\n>Para interomper digite [999]\n")
                continue
                
        except ValueError:
            os.system('cls')
            print(">Entrada inválida!\n>Tente novamente!\n")
            continue


def main():
    valores = add_numeros_lista()
    os.system('cls')
    print(f">Quantidade de valores adicionados na lista: {len(valores)}\n")
        
    print('>Lista decrescente: |',end='')
    for i in sorted(valores, reverse=True):
        print(f"{i}",end='|')
    print()

    if 5 in valores:
        print("\n>Valor 5 encontrado!\n")
    else:
        print("\n>Valor 5 não encontrado!\n")
main()