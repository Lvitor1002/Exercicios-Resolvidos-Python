'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem e quantidade correta.
'''

var = str(input("Digite uma expressão matemática: "))
contador = 0

for simbolo in var:
    if simbolo == '(':
        contador += 1  # Incrementa para cada '('
    elif simbolo == ')':
        contador -= 1  # Decrementa para cada ')'

        if contador < 0:  # Detecta fechamento sem abertura correspondente
            break

if contador == 0:
    print("\nExpressão válida!! Parabéns!\n")
else:
    print("\nExpressão inválida!!\n")
