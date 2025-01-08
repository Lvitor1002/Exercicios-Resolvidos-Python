import random

def jogo():
    opcoes = ["Pedra", "Papel", "Tesoura"]

    while True:
        print("\nEscolha sua jogada: ")
        for i, op in enumerate(opcoes):
            print(f"{i + 1}: {op}")
        print("0: Sair do jogo\n")
        


        jogador = input("Digite o número da sua escolha: ")

        if jogador == '0':
            print("\nJogo encerrado. Obrigado por jogar!\n")
            break
        # Tratamento para entradas inválidas
        try:
            jogador = int(jogador)
            if jogador < 1 or jogador >3:
                print("Escolha inválida. Por favor, escolha um número entre 1 e 3.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 1 e 3.")
            continue


        computador = random.randint(1,3)
        print("-=-"*20)
        print(f"\n\tVocê escolheu: {opcoes[jogador - 1]}")
        print(f"\tO computador escolheu: {opcoes[computador - 1]}\n")
        print("-=-"*20)
        if jogador == computador:
            print("="*20)
            print("\nEmpate!\n")
            print("="*20)
        elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and jogador == 2):
            print("="*20)
            print("\nVocê venceu!\n")
            print("="*20)
        else:
            print("="*20)
            print("\nComputador venceu!\n")
            print("="*20)


if __name__ == "__main__":
    print("\nBem-vindo ao jogo Jokenpô!\n")
    jogo()