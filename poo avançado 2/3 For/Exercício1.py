#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

def pares():
    print("\n>Números pares entre 1 à 50: ",end='')
    for i in range(0,51,2):
        print(i)
    print("\n")


pares()