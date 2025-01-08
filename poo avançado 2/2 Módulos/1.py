import math
n = int(input("Digite um número: "))
raiz = math.sqrt(n)

print(f"\n\nA raiz de √{n} é {(raiz):.3f}")
print("-------------------------------------------")
print(f"Raiz arredondada para cima: {math.ceil(raiz)}")
print(f"Raiz arredondada para baixo: {math.floor(raiz)}")
print("-------------------------------------------\n\n")
