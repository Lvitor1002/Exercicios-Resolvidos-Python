lanche = ('hamburguer', 'suco', 'pizza', 'pudim')


# Forma fácil:
for i in lanche:
    print(f"Eu comi {i}")
print("Comi bastante..\n----------------------------------------------------------\n")


# Forma fácil se quiser a posição:
for i, comida in enumerate(lanche):
    print(f"Eu comi {comida} na posição: {i}\n")
print("Comi bastante..\n----------------------------------------------------------\n")


# Forma difícil
for count in range(0, len(lanche)):
    print(f"Comi bastante {lanche[count]}")
print("Comi bastante..\n----------------------------------------------------------\n")


# Forma difícil para me dar a posição com count:
for count in range(0, len(lanche)):
    print(f"Comi bastante {lanche[count]} na posição: {count}")
print("Comi bastante..\n")
