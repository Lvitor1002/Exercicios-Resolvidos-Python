'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

import os 
#           [0]Par ,[1] Impar
produtos = ('Livro',9.99,
            'Caderino', 10.49,
            'Panela', 80.99,
            'Chaleira', 10.99,
            'Maquina', 70.99,
            'Caderno', 90.99,
            'Lustre', 60.99,
            'Arroz', 20.99,
            'Luva', 70.99,
            'Mesa', 550.99,
            'Pia', 870.99,
            'Colchão', 100.99,
            'Seda', 887.99,
            'Panela', 81.99)

def exibir():
    os.system('cls')
    print(f'{"-=-=-= Lista de Produtos -=-=-=":^30}\n')
    for p in range(0,len(produtos)):
        if p % 2 == 0:
            print(f">{produtos[p]:.<20} ", end='')
        else:
            print(f"R$ {produtos[p]}")
    

exibir()