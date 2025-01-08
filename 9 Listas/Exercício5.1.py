'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem e quantidade correta.
'''

# Modo fácil de fazer:
var = str(input("Digite uma expressão matemática: "))
if var.count("(") == var.count(")"):
    print("\nExpressão válida!! Parabéns!\n")
else:
    print("\nExpressão inválida!!\n")
