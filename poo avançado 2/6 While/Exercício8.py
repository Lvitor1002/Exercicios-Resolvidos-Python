'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
import os 

def leitura():
    
    while True:
        soma = quantidade = 0
        maior = menor = None

        while True:
            
            print("\n>Digite alguns números:")
            try:
                numeros = int(input())
                soma += numeros
                quantidade += 1

                if maior is None or numeros > maior:
                    maior = numeros
                if menor is None or numeros < menor:
                    menor = numeros

                op = str(input(">Deseja continuar à digitar? [Sim][Não]\n")).strip().lower()
                if op == 'sim':
                    continue
                else:
                    return numeros, soma, quantidade, maior, menor
            except ValueError:
                
                print(">Erro, apenas valores inteiros são permitidos!")
                continue
        

def media(soma, quantidade):
    return soma/quantidade


def exibir():
    numeros, soma, quantidade, maior, menor = leitura()
    media_final = media(soma, quantidade)
    os.system('cls')
    print(f">A média dos números: [{numeros}] foi: {media_final:.2f}\n>Maior valor: {maior}\n>Menor valor: {menor}\n")

os.system('cls')
exibir()