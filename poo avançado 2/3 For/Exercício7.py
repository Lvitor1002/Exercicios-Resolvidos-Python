#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
Exemplos de palíndromos: 
APOS A SOPA, 
A SACADA DA CASA, 
A TORRE DA DERROTA, 
O LOBO AMA O BOLO, 
ANOTARAM A DATA DA MARATONA.

'''
import os

def palindromo():
    frase = str(input("\n>Digite um nome quarquer: ")).split()

    frase_junta = ''.join(frase)
    frase_inversa=''

    for letra in range(len(frase_junta)-1,-1,-1):
        frase_inversa += frase_junta[letra]
    
    if frase_junta == frase_inversa:
        print(f"\n>A frase '{frase}' é palíndromo!\n\n>Frase Original: {frase}\n\n>Frase invertida: {frase_inversa}\n")
        
    else:
        print(f"\n>A frase '{frase}' não é palíndromo!\n\n>Frase Original: {frase}\n\n>Frase invertida: {frase_inversa}\n")

os.system('cls')
palindromo()