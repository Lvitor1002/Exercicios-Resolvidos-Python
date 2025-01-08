'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

import os, random
from time import sleep

def jogo_dado():
    os.system("cls")
    jogadores = {}

    for jogador in range(1, 5):
        jogadores[f'Jogador {jogador}ª'] = random.randint(1, 6)
    
    return jogadores
    
    
def main():
    jogadores = jogo_dado()

    os.system("cls")
    print("> Resultados:\n")
    for jog, resul in jogadores.items():
        sleep(0.5)
        print(f"{jog} | Número sorteado: {resul}")
    print()
        
    
    resultado_ordenado = sorted(jogadores.items(), key=lambda item: item[1], reverse= True)
    print('-='*30)

    print(">Classificação:\n")
    for i,(c,v) in enumerate(resultado_ordenado):
        sleep(0.60)
        print(f"[{i+1}ª Lugar] - {c} {v}")
    
    print('-='*30)
    print(f"Campeão: {resultado_ordenado[0][0]} | Número sorteado: {resultado_ordenado[0][1]}")
    print('-='*30)
        
main()
    