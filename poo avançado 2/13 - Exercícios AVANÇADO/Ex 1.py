'''
Modelagem de Sistema de Gerenciamento de Estoque
Enunciado: Modele um sistema de gerenciamento de estoque para uma loja online. 
Implemente métodos para adicionar/remover produtos do inventário, processar pedidos, calcular o total de vendas, etc.
'''

class Produto:
    def __init__(self, nome, valor, quantidade, codigo):
        self.nome = nome 
        self.valor = valor 
        self.quantidade = quantidade
        self.codigo = codigo


class Estoque:
    def __init__(self):
        self.inventario = {}
    
    def adicionar_produto(self, produto, quantidade):
        if produto.nome in self.inventario:
            self.inventario[produto.nome].quantidade += quantidade
        else:
            self.inventario[produto.nome] = produto
    
    def remover_produto(self, produto, quantidade):
        if produto.nome in self.inventario:
            if self.inventario[produto.nome].quantidade >= quantidade:
                self.inventario[produto.nome].quantidade -= quantidade
                if self.inventario[produto.nome].quantidade == 0:
                    del self.inventario[produto.nome]
                return True
            else:
                print(f"Quantidade insuficiente em estoque para o produto {produto.nome}!\n")
                return False
        else:
            print(f"Produto {produto.nome} não encontrado no estoque!\n")
            return False
    
    def processar_pedido(self, carrinho):
        total = 0 
        for produto_nome, quantidade in carrinho.items():
            if produto_nome in self.inventario:
                if self.inventario[produto_nome].quantidade >= quantidade:
                    total += self.inventario[produto_nome].valor * quantidade
                    self.remover_produto(self.inventario[produto_nome], quantidade)
                else:
                    print(f"Quantidade insuficiente em estoque para o produto {produto_nome}!")
                    return None
            else:
                print(f"Produto {produto_nome} não encontrado no estoque!")
                return None
        return total


loja1 = Estoque()
#                       class, nome, valor, quantidade, codigo, quantidade 
loja1.adicionar_produto(Produto('Caixa',19.99,3,78965447896),3)
loja1.adicionar_produto(Produto('Tênis',2999.90,12,78965254891),12)
loja1.adicionar_produto(Produto('Gelo',5.90,12,78915447893),12)
loja1.adicionar_produto(Produto('Luva',9.99,12,78965497866),2)

carrinho = {'Caixa':1,'Tênis':4,'Gelo':6,'Luva':2}
total = loja1.processar_pedido(carrinho)

if total is not None:
    print("="*60)
    print(f"Total da venda: R${total:.2f}")
    print("="*60)
