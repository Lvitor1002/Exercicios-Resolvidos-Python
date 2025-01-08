'''
Escreva uma função em Python que receba um dicionário onde as chaves são números e os valores são listas de números, 
e retorne o produto de todos os elementos dessas listas.
'''


def funcao(dados):
    dici = {}
    for c,v in dados.items():
        multiplica = 1 #<- se fosse zero o resultado seria zero
        for numeros in v:
            multiplica *= numeros
        dici[c] = multiplica
    return dici



dados = {1: [2, 3], 2: [4, 5], 3: [6, 7]}

print("\nValores: ")
for c,v in dados.items():
    print(f"{c}: {v}")

print("\nProduto dos valores das listas: ")
for c,v in funcao(dados).items():
    print(f"{c}-> {v}")

