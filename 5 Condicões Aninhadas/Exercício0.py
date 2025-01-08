'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
import os 

def leitura():
    valor = float(input("\n>Valor da casa: R$"))
    salario = float(input("\n>Salário atual: R$"))
    tempo = int(input("\n>Em quantos anos deseja financiar? "))
    parcelas = valor/(tempo*12)
    return salario, parcelas, tempo


def emprestimo(salario, parcelas,tempo):
    if parcelas > salario*0.30:
        print(f"\n>Empréstimo negado!\n")
    else:
        print(f"\n>Empréstimo aprovado!\n\n>Fatura a ser cobrada por {tempo*12} meses/{tempo} anos: R${parcelas:.2f}\n")


os.system('cls')
s,p,t = leitura()
emprestimo(s,p,t)