'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela 
os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''
def fibo(n):
    lista_fibona = [0, 1]  # Começamos com os dois primeiros números da sequência

    while len(lista_fibona) < n:
        proximo = lista_fibona[-1] + lista_fibona[-2]
        lista_fibona.append(proximo)

    return lista_fibona[:n] #Lendo apenas os valores novos 

n = int(input("Digite um valor: "))
resultado = fibo(n)
print(f"Os primeiros '{n}' elementos são: {resultado}")
