# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

def leitura(p):
    return f"> Valor atual do produto R${p}\n" 

def desconto(p):
    return f"> Produto com 5% de desconto: R${p*0.95}"
    
preco = float(input("\n> Digite o preço do produto: "))

print("-="*60)
print(leitura(preco))
print(desconto(preco))
print("-="*60)
