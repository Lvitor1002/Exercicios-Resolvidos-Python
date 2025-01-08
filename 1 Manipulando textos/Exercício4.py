'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

'''
import os

def vezes_A(f):
    return f"\n>Letra [a] aparece {f.count('a')}x vezes.\n" 
 

def primeira_e_ultima_posi(f):
    sem_espaco = f.replace(' ','')
    return f">Primeira posição de [a]: {sem_espaco.find('a')+1}ª\n\n>Última posição de [a]: {sem_espaco.rfind('a')+1}ª\n"


def main():
    frase = str(input("\n>Digite uma frase qualquer: ")).lower()
    print(vezes_A(frase))
    print(primeira_e_ultima_posi(frase))
    

os.system('cls')
main()