'''
Faça um programa que leia 10 valores numéricos e guarde-os em uma lista. 
No final, mostre a lista ordenada e qual foi o maior e o menor valor digitado e as suas respectivas POSIÇÕES na lista. 
'''
import os
def leitura():
    os.system('cls')
    numeros = []
    print(f"\n>Digite 10 valores: ")
    for i in range(1,11):
        while True:
            try:
                valor = int(input(f">{i}ª: "))    
                numeros.append(valor)
                break
            except ValueError:
                os.system('cls')
                print(f">Erro. Entrada de número real esperada.")
                continue
    return numeros
    

def main():
    lista = leitura()
    posi_maior = lista.index(max(lista)) 
    posi_menor = lista.index(min(lista))

    os.system('cls')
    print("\nLista ordenada: > ",end='')
    for i in sorted(lista):
        print(f"{i} | ",end='')
    print()

    print("\nLista original: > ",end='')
    for i in lista:
        print(f"{i} | ",end='')
    print()

    
    print(f"\n>Maior valor: {max(lista)}. Posição {posi_maior+1}ª\n\n>Menor valor: {min(lista)}. Posição {posi_menor+1}ª\n")

main()