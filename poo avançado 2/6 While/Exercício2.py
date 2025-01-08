'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''


import os

def limpa_tela():
    """Limpa a tela do terminal dependendo do sistema operacional."""
    # Detecta o sistema operacional e limpa a tela apropriadamente
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def leitura():
    """Lê dois números do usuário e retorna como uma lista."""
    while True:
        try:
            print("\n>Digite dois valores:")
            numeros = [float(input(f'>{i}ª número: ')) for i in range(1, 3)]
            return numeros
        except ValueError:
            print("\n>Entrada inválida! Por favor, insira números válidos.")

def menu():
    """Exibe o menu de opções na tela."""
    print(''' 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa\n''')

def main():
    lendo = leitura()
    
    while True:
        limpa_tela()
        print("\n>Escolha uma das opções abaixo:")
        menu()

        try:
            op = int(input("\n>Digite a opção desejada: "))
        except ValueError:
            print("\n>Opção inválida! Por favor, insira um número de 1 a 5.")
            continue

        if op == 1:
            # Soma os números
            limpa_tela()
            print(f"\n>Soma dos números: {sum(lendo):.1f}")
        
        elif op == 2:
            # Multiplica os números
            limpa_tela()
            print(f"\n>Multiplicação dos números: {(lendo[0] * lendo[1]):.1f}")
        
        elif op == 3:
            # Encontra o maior número
            limpa_tela()
            print(f"\n>Maior número: {max(lendo):.1f}")
        
        elif op == 4:
            # Lê novos números
            limpa_tela()
            lendo = leitura()
        
        elif op == 5:
            # Sai do programa
            limpa_tela()
            while True:
                op2 = input("\n>Deseja sair? [Sim/Não]: ").strip().lower()
                if op2 in ['sim', 's']:
                    print("\n>Saindo...!")
                    return  # Sai do loop principal e finaliza o programa
                elif op2 in ['não', 'nao', 'n']:
                    break
                else:
                    print("\n>Opção inválida! Por favor, responda com 'Sim' ou 'Não'.")
        else:
            print("\n>Opção inválida! Por favor, escolha uma opção de 1 a 5.")

# Inicia o programa
limpa_tela()
main()

    