# Faça um programa que calcule a média entre 4 números usando FOR.

def media():
    soma = 0
    print("Digite 4 números: ",end='')
    for i in range(1,5):
        n = int(input(f">{i}ª: "))
        soma += n
    media = soma/4

    return f'\nMédia dos 4 números: {media}\n'

print(media())