'''Escreva uma função em Python que receba uma lista de dicionários representando produtos 
(com chaves "nome" e "preco") e retorne o nome do produto mais caro.'''


def produto_caro(lista):
    maior = max(lista, key=lambda x: x["preco"])
    menor = min(lista, key=lambda x: x['preco'])
    return f"\n>Maior valor: {maior['nome']}\n>Menor valor: {menor['nome']}"


lista = [{"nome": "Celular", "preco": 1000}, {"nome": "Notebook", "preco": 1500}, {"nome": "Tablet", "preco": 800}]



print("="*60)
for i in lista:
    for c,v in i.items():
        print(f"{(c.capitalize())}: {v}",end=' | ')
    print()
print(produto_caro(lista))
print("="*60)
