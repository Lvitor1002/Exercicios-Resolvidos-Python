'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
import os 
def leitura():
    print("\n>Digite alguns números:\n>Digite [999] para forçar parada.\n")
    soma = quantidade = 0
    while True:
        
        try:
            numeros = int(input())
            if numeros != 999:
                quantidade += 1
                soma += numeros
                continue
            else:
                break 
        except ValueError:
            os.system('cls')
            print("\n>Apenas números inteiros são permitidos!\n")
    return quantidade, soma
    

def exibir():
    quantidade, soma = leitura()
    os.system('cls')
    print(f">Quantidade de números: {quantidade}\n>Soma total dos números: {soma}\n")

os.system('cls')
exibir()

