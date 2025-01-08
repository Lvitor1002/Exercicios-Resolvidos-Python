while True:
    print()
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    print("\n\nExemplo: ||( + )||( - )||( * )||( / )||")
    op = input("Digite um operador desejado: ")
    sair = input("Deseja sair? [s]im | [n]ão\n")

    #código para: Somente numeros são permitidos.
    if not n1.isnumeric() or not n2.isnumeric():
        print("Ops.. Apenas números são permitidos.!\nTente novamente.\n")
        continue
    n1 = int(n1)
    n2 = int(n2)
    
    #Código para as opções de operações
    if op == "-":
        print(f"{n1}-{n2} = {n1-n2}")
    elif op == "+":
        print(f"{n1}+{n2} = {n1+n2}")
    elif op == "/":
        print(f"{n1}/{n2} = {n1/n2}")
    elif op == "*":
        print(f"{n1}x{n2} = {n1*n2}")
    else:
        print("\nTente novamente escolhendo um dos operadores: ||( + )||( - )||( * )||( / )||\n")

    #código para sair
    if sair == "s":
        print("Saindo...")
        break