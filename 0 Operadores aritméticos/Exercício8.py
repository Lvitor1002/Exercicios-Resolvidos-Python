# Faça um algoritmo que leia o salário de uma pessoa e mostre seu novo salário com 15% de aumento.

def aumento(n):
    return f"\n> R${n} com 15% de aumento: R${n*1.15:.0f}\n"

salario = float(input("\nDigite o seu salário: "))
print(aumento(salario))