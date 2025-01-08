'''
 Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
import os 

def manipulando_matriz():
    matriz = []
    os.system('cls')
    print(">Preencha a matriz: ")
    for l in range(3):
        linha = []
        for c in range(3):
          while True:
            try:
                valores = int(input(f">[{l},{c}]ª:"))
                linha.append(valores)
                break
            except ValueError:
                os.system('cls')
                print(">Entrada inválida!\nTente novamente..\n")
                continue
        matriz.append(linha)
    return matriz


def exibir():

    matriz = manipulando_matriz()

    os.system('cls')
    print(">Matriz: ")
    for linha in matriz:
        for valor in linha:
          print(f"{valor:^5}",end=' | ')
        print()

    
exibir()
