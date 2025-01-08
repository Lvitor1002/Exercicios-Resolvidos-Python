#Contagem de quantidade Par e ímpar usando while:
par = impar = 0
soma_par = soma_impar = 0
n = 1
while n != 0:
    n = int(input("Digite um número:"))
    if n != 0: 
        if n % 2 == 0:
            par += 1 # Quantidade de Pares
            soma_par += n # Soma de todos os pares
        elif n % 1 ==0:
            impar += 1
            soma_impar += n
print(f"\n\nQuantidade de números Pares:{par}. Soma total: {soma_par}")
print(f"Quantidade de números Ímpares:{impar}. Soma total: {soma_impar}\n\n")

    