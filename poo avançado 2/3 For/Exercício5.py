#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = primeiro + (10-1) * razao #--> Fórmula comum da Progressão aritmética: an = a +(n - 1).d
for i in range(primeiro,decimo+razao,razao):
    print(f"{i}",end = ' -> ')
print("Acabcou\n")