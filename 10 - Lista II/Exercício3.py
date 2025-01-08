'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

import os 

def manipulando_matriz():
    matriz = []
    
    os.system('cls')
    print(">Preencha a amtriz: ")
    for l in range(1,4):
        linha = []
        for c in range(1,4):
            while True:
                try:
                    valor = int(input(f"[{l}][{c}]ª: "))
                    linha.append(valor)
                    break
                except ValueError:
                    os.system('cls')
                    print(">Entrada inválida!\n")
                    continue
        matriz.append(linha)
    return matriz


def exibir():
    
    matriz = manipulando_matriz()
    os.system('cls')
    
    soma_total = 0 
    soma_terceira_coluna = 0
    
    print("-="*60)
    print(">Matriz:\n")
    for l in matriz:
        soma_terceira_coluna += l[2]
        
        for c in l:
            print(f"| {c:^5}",end=' | ')
            if c % 2 == 0:
                soma_total += c  
        print()
        
    maior_valor = max(matriz[1]) 
    print(f"\n>Soma dos valores pares: {soma_total}\n\n>Soma dos valores da terceira coluna: {soma_terceira_coluna}\n\n>Maior valor da segunda linha: {maior_valor}")
    print("-="*60)
    

exibir()