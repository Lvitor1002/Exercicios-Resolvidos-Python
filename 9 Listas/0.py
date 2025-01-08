# add um item no índice escolhido:
lista = [0, 1, 2, 3, 4, 5, 6, 8, 7, 4]
lista.insert(0, 'Luiz')


# Outras maneiras de eliminar um intem da lista:
lista.remove('Luiz')  # elimina o valor Luiz da lista

del lista[3]  # elimina o valor do índice 3 da lista

lista.pop(3)  # elimina o último valor da lista


# PARA ORDENAR LISTA:
valores = [8, 2, 4, 9, 3, 5]
valores.sort()  # ordenando crescente

valores.sort(reverse=True)  # ordenando descrescente


# Criando uma cópia de uma lista:
a = [1, 5, 8, 9, 7]
b = a[:]  # cópia
b[2] = 8
print(f'''Lista 4: {a}\n      ##Lista normal'
          Lista B: {b}\n''')  # Lista alterada'


len(lista)  # Conta o total de elementos da lista


# ADD valores diretamente com append
valores = []
for i in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
print(valores)

# Para tirar o colchete dos nomes:
print(f"\nTimes em ordem alfabética:\n")
for i in sorted(lista):
    print(f"{i}\n")
