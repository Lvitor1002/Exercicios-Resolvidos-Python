import os 

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

div = n1 / n2 
pot = n1 ** n2 


os.system('cls')
print(f">Divisão: {n1}/{n2} = {div}\n>Potência: {n1}^{n2} = {pot}\n")
