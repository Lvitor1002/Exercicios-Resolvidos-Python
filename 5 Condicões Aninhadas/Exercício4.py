'''
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
import os

def leitura():
    print("\nDigite duas notas: ")
    lista = [float(input(f"\n{i}ª: ")) for i in range(1,3)]
    return lista

def media(lista):
    soma = sum(lista)
    return soma/2

def main():
    notas = leitura()
    media_notas = media(notas)

    if media_notas < 5:
        print(f"\n>Aluno(a) Reprovado com média [{media_notas}]\n")
    elif media_notas >= 5 and media_notas <= 6.9:
        print(f"\n>Aluno(a) em Recuperação, com média [{media_notas}]\n")
    elif media_notas > 7:
        print(f"\n>Aluno(a) Aprovado com média [{media_notas}]\n")


os.system('cls')
main()
