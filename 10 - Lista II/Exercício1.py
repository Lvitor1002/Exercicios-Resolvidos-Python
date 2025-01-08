
'''
 Crie um programa onde o usuário possa digitar sete valores numéricos e
   cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
import os

def add_na_lista():
    lista = [[],[]]

    os.system('cls')
    print('>Digite 7 valores númericos: ')
  
    for i in range(1,8):
        while True:
          try:
            n = int(input(f">{i}ª: "))
            if n % 2 == 0:
                lista[0].append(n)
            if n % 2 != 0:
                lista[1].append(n)
            break
          except ValueError:
              os.system('cls')
              print(">Entrada inválida! Tente novamente..")
              continue
    return lista


def exibir():
    valores = add_na_lista()

    os.system('cls')

    print(">Lista Par: >",end='')
    for i in sorted(valores[0]):
        print(f"{i}",end='|')
    print()
    
    print(">Lista Impar: >",end='')
    for i in sorted(valores[1]):
        print(f"{i}",end='|')
    print()

exibir()


     
