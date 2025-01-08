'''Escreva uma função em Python que receba uma lista de tuplas, onde cada tupla contém o nome e a idade de uma pessoa, 
e retorne uma lista com os nomes das pessoas que têm idade maior que 18 anos.'''


def lista(dados):
    return filter(lambda x: x[1] > 18, dados)

dados = [("João", 25), ("Maria", 17), ("Pedro", 20), ("Ana", 16)]

print("="*60)
print("Maiores de 18 anos: \n")
for nome, idade in lista(dados):
    print(f"Nome: {nome} | Idade: {idade}")
print("="*60)