'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
import os 

tupla_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')

def leitura():
    os.system('cls')
    while True:
        try:
            ler = int(input("Digite um número de 0 à 20: "))
            if ler >=0 and ler <= 20:
                print(f">Valor: {ler} - {tupla_extenso[ler].capitalize()}\n")
            else:
                print(f">Fora do limite permitido: [0 à 20]\n>Tente novamente..\n")
                continue
        except ValueError:
            print(f">Erro. Entrada inválida.\n>Digite um número!\n")
            continue

leitura()