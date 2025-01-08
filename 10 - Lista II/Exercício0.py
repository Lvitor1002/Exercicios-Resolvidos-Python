'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
import os

def dados():

    os.system('cls')
    while True:
        nome = str(input(">Digite um nome: ")).strip().lower().capitalize()
        if not nome.isalpha():
            os.system('cls')
            print(">Entrada inválida!\n")
            continue
        else:
            break
    
    while True:
        peso_string = input(f">Digite o peso de {nome}: ").replace(",",".")
        try:
            peso_float = float(peso_string)
            
            break
        except ValueError:
            os.system('cls')
            print(">Entrada inválida!\n")
            continue
    
    return [nome,peso_float]
        

def varias_pessoas():
    
    todas_pessoas = []

    while True:
        pessoas = dados()

        if pessoas:
            todas_pessoas.append(pessoas)
        else:
            os.system('cls')
            print("Não há pessoas adicionadas!")
            break

        op = str(input(">Deseja adicionar mais pessoas? [Sim][Não]\n")).strip().lower()
        if op == 'sim':
            continue 
        if op == 'não':
            return todas_pessoas
        else:
            os.system('cls')
            print(">Entrada inválida. Tente novamente!\n")
            continue


def main():
    pessoas = varias_pessoas()

    pesada = max(pessoas, key=lambda x: x[1])   # posição x[1] = peso
    leve = min(pessoas, key=lambda x: x[1])

    
    os.system('cls')
    print('-='*30)
    print("> Pessoas adicionadas na lista:\n")
    for i, p in enumerate(pessoas):
        print(f"{i+1}ª {p[0]}\n---Peso: {p[1]} Kg")

    print(f"\n>Foram cadastradas [{len(pessoas)}] pessoas..")
    print(f">Pessoa mais pesada: {pesada[0]} com {pesada[1]} Kg.")
    print(f">Pessoa mais leve: {leve[0]} com {leve[1]} Kg.")
    print('-='*30)


main()