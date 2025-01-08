'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''

import os 

def add_lista():
    lista1 = []
    os.system('cls')
    print("Digite alguns números: ",end='')
    while True:
        try:
            n = int(input("> "))
            if n != 999:
                lista1.append(n)
                os.system('cls')
                print(f">Número {n} adicionado com sucesso!!\n>[Digite 999 para finalizar]\n")
                
            else:
                return lista1
        except ValueError:
            os.system('cls')
            print(">Entrada inválida!\n>Tente novamente..\n")
            continue


def lista_par_impar(lista1):
    lista_par = []
    lista_impar = []
    for i in lista1:
        if i % 2 == 0:
            lista_par.append(i)
        if i % 2 != 0:
            lista_impar.append(i)
    return lista_par, lista_impar


def main():
    os.system('cls')
    lista_original = add_lista()
    lista_par, lista_impar = lista_par_impar(lista_original)
    

    os.system('cls')
    print(f"Lista original >|",end='')
    for i in lista_original:
        print(f"{i}",end='|')
    print()
    
    print(f"\nLista Par >|",end='')
    for i in lista_par:
        print(f"{i}",end='|')
    print()

    print(f"\nLista Impar >|",end='')
    for i in lista_impar:
        print(f"{i}",end='|')
    print()


main()
