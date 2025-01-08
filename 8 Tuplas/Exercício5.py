'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'''
import os 
palavras = ('pastel', 'sabonete', 'panela', 'piada', 'pernambuco',
            'cachorro', 'tabuada', 'paraguai', 'esquecido')

vogais = ('a', 'e', 'i', 'o', 'u')

def exibir():
    os.system('cls')
    print(f"Vogal\t\t|\t\t Palavra")
    print('- '*20)
    for p in range(0,len(palavras)):
        for v in range(0,len(vogais)):
            if vogais[v] in palavras[p]:
                print(f"{vogais[v].upper()}",end='')

        print(f"\t\t|{palavras[p].capitalize():>23}")
        print()
                



exibir()

