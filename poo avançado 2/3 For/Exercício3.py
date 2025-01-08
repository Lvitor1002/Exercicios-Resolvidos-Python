#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print("-_-"*14)
print("\t\t Tabuada \n")
tabuada = int(input("Digite um número desejado para a tabuada: "))
for i in range(1,11):
    print(f"{tabuada} x {i} = {tabuada * i}")