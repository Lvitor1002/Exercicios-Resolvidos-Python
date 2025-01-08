a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b

# Para saber a quantidade de vezes de um número que está nessa tupla:
# Exemplo: quantos vezes aparece o '5'
print(f"O número {b[0]} aparece {c.count(5)}x\n")


# Para saber a posição de um número:
print(f"Poisção: {c.index(5)}ª\n")
