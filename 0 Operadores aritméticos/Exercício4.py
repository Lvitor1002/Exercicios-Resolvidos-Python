# Faça um programa que leia um número int e mostre na tela a sua tabuada.

def tabuada(n):
    print("-="*60)
    print(f"Tabuada do {n}: \n")
    for i in range(0,11):
        print(f"{n} x {i:^2} = {n*i:^2}")
    print("-="*60)



t = int(input("\nDigite um número para a tabuada desejada: "))
tabuada(t)