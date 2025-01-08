'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

co = float(input("Digite um valor para o cateto oposto: "))
ca = float(input("Digite um valor para o cateto adjacente: "))
hip = ((ca**2+co**2) ** 0.5)

print(f"O comprimento da hipotenusa é: {hip:.2f}\n")
