'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

'''
import os 

def calculo(s):
    if s > 1250:
        return f"\n>Aumento de 10% no salário: R${s*1.10:.2f}\n" 
    if s <= 1250:
        return f"\n>Aumento de 15% no salário: R%{s*1.15:.2f}\n"
    

os.system('cls')
salario = int(input("\n>Digite o seu salário: R$"))
print(calculo(salario))