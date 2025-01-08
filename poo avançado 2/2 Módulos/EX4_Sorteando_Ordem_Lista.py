'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random, os

def lendo():
    print("\n>Digite 4 nomes para o sorteio: ")
    lista = [str(input(f">{i}ª ").strip().lower().capitalize()) for i in range(1,5)]
    return lista

def sorteio_ordenando(lista):
    random.shuffle(lista)

    print("="*60)
    print(f">Ordem de apresentação sorteada:\n")
    for i, aluno in enumerate(lista, start=1):
        print(f"{i}ª Aluno: {aluno}")
    print("="*60)


def main():
    
    while True:
        os.system('cls')
        alunos = lendo()
        sorteio_ordenando(alunos)        
        while True:
            op = str(input("Deseja continuar? [Sim][Não]\n")).strip().lower()
            if op == 'sim':
                break
            else:
                return
            
main()