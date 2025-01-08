'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
import random, os 

def lendo():
    print("\n>Digite 4 nomes para o sorteio: ")
    alunos = [str(input(f">{i}ª: ")).strip().lower().capitalize() for i in range(1,5)]
    return alunos

def sorteando(alunos):
    return random.choice(alunos)


def main():
    os.system('cls')
    while True:
        alunos = lendo()
        escolhido = sorteando(alunos)
        
        print("-="*60)
        print(f">Alunos Sorteados: {escolhido}")
        print("-="*60)

        while True:
            op = str(input("\n>Deseja refazer o sorteio? [Sim][Não]\n")).strip().lower()
            if op == 'sim':
                break
            else:
                print(">Fim..!\n")
                return

main()
