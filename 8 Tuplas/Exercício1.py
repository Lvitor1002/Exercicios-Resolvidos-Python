'''
Crie uma tupla preenchida com os 21 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
e) Escolha um timeS para saber a posição
'''
import os

times = ('PALMEIRAS', 'ATLÉTICO MG', 'BOTAFOGO', 'FLAMENGO', 'GRÊMIO',
              'RED BULL', 'FLUMINENSE', 'ATHLETICO PR', 'SÃO PAULO', 'INTERNACIONAL',
              'CHAPECOENSE', 'FORTALEZA', 'CUIABÁ', 'CORINTHIANS', 'CRUZEIRO',
              'SANTOS', 'VASCO', 'BAHIA', 'GOIÁS', 'CORITIBA', 'AMÉRICA MG')

def cinco_primeiros():
    os.system('cls')
    print(f">Cinco primeiros times: {times[:5]}\n")

def ultimos_quatro():
    os.system('cls')
    print(f"Últimos quatro colocados: {times[-4:]}\n")

def ordem_alfabetica():
    os.system('cls')
    print(f">Times em ordem alfabética:\n")
    alinhados = max(len(times) for times_alinhados in times)
    for times_alinhados in sorted(times):
        print(f">\t{times_alinhados.ljust(alinhados)}<")
    print()

def posicao_chapeco():
    os.system('cls')
    print(f">Posição time da Chapecoense: {times.index('CHAPECOENSE')+1}ª Posição.\n")


def posicao_time():
    os.system('cls')
    escolha = str(input(f">Digite o nome de um time e descubra a sua posição.\n\n>Times disponíveis:{times}\n\n:>")).strip().upper()
    if escolha in times:
        os.system('cls')
        print(f"Time: {escolha.capitalize()} na {times.index(escolha)+1}ª Posição.\n") 
    else:
        os.system('cls')
        print(f">Time {escolha.capitalize()} não localizado!\n")
    

def sair():
    escolha = str(input(">Deseja realmente sair? [Sim][Não]\n")).strip().lower()
    if escolha in ['sim','não','nao']:
        if escolha == 'sim':
            os.system('cls')
            print(">Saindo..\n")
            exit()
        elif escolha == 'não' or escolha == 'nao':
            os.system('cls')
            print(">Continue..\n")
    else:
        os.system('cls')
        print("Apenas [Sim][Não] é permitido.\n")



def main():
    os.system('cls')
    print("-=-"*40)
    while True:
        try:
            
            escolha = int(input('''Escolha uma das opções abaixo digitando o número correspondente:
    >[1] Os 5 primeiros times.
    >[2] Os últimos 4 colocados.
    >[3] Times em ordem alfabética. 
    >[4] Em que posição está o time da Chapecoense.
    >[5] Escolha um time para saber a posição
    >[6] Sair\n '''))
            if escolha in range(1,7):
                if escolha == 1:
                    cinco_primeiros()
                if escolha == 2:
                    ultimos_quatro()
                if escolha == 3:
                    ordem_alfabetica()
                if escolha == 4:
                    posicao_chapeco()
                if escolha == 5:
                    posicao_time()
                if escolha == 6:
                    sair()

            else:
                os.system('cls')
                print(">Fora de alcance! Escolha apenas as opções de [1 à 6]\n")
                continue
                
        except ValueError:
            os.system('cls')
            print(">Erro. Entrada inválida. Digite apenas números!\n")
            
main()
    