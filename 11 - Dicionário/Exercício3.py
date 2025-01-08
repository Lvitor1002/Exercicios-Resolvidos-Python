'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
Aprimore para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

'''

import os 

def dados():
    dici = {}
    gols = []
    
    os.system("cls")
    while True:
        nome = str(input(">Digite o seu nome: ")).strip().lower().capitalize()
        if not nome.isalpha():
            os.system("cls")
            print(">Entrada inválida! Tente novamente!\n")
            continue
        else:
            dici['Nome:'] = nome
            break
    
    while True:
        try:
            partidas = int(input(">Quantas partidas foram ao total do compeonato? "))
            if partidas < 0:
                os.system("cls")
                print(">Entrada inválida! Tente novamente!\n")
                continue
            else:
                break
                
        except ValueError:
            os.system("cls")
            print(">Entrada inválida! Tente novamente!\n")
            continue
    
    
    print(">Digite os gols de cada partida:")
    soma = 0
    for i in range(partidas):
        while True:
            try:
                gol = int(input(f">{i+1}ª Partida: "))
                if gol < 0:
                    os.system("cls")
                    raise ValueError(">A quantidade de gols não pode ser negativa!")
                gols.append(gol)
                soma += gol
                break
            except ValueError as e:
                os.system("cls")
                print(f"{e} Tente novamente!\n")
    
    dici['Gols:'] = gols[:]
    dici['Total de gols:'] = soma
    
    return dici


def varios_jogadores():
    jogadores = []
    
    os.system("cls")
    while True:
        unico_jogador = dados()
        if unico_jogador:
            jogadores.append(unico_jogador)
        else:
            os.system("cls")
            print(">Não há jogador adicionado!\n")
            break
        
        op = str(input(">Deseja adiconar mais jogadores? [Sim][Não]\n")).strip()
        if op in ['s','S','Sim','SIM','sim']:
            continue
        elif op == 'não':
            return jogadores
        else:
            os.system("cls")
            print(">Entrada inválida!\n")
            continue

def exibir():
    jogadores = varios_jogadores()
    os.system("cls")
    print('-='*10)
    for i, jo in enumerate(jogadores):
        
        print(f">{i+1}ª Jogador - {jo['Nome:']}:")
        """for c, v in jo.items():
            print(f"    {c} {v}")
        print()"""
        print('-='*10)
    
    
    while True:
        
        try:
            escolha = int(input("\n>Para vizualizar os dados de um jogador digite o número da sua posição: "))
            
            
            if 1 <= escolha <= len(jogadores):
                escolhido = jogadores[escolha - 1]
                
                os.system("cls")
                while True:
                    print('-='*30)
                    print(f">Detalhes do Jogador  - {escolhido['Nome:']}:")
                    for c, v in escolhido.items():
                        print(f"\t\t\t{c} {v}")
                    print()
                    print('-='*30)
                    
                    
                    op = str(input(">Deseja vizualizar outro jogador? [Sim][Não]\n")).strip().lower()
                    os.system("cls")
                    if op == 'sim':
                        print('-='*10)
                        for i, jo in enumerate(jogadores):
                            print(f">{i+1}ª Jogador - {jo['Nome:']}:")
                            print('-='*10)
                        break
                    else:
                        exit()
                    
        except ValueError:
                os.system("cls")
                print(">Entrada inválida!\n")
                continue
            
        
exibir()
        

