'''
 Implementação de Composição
Enunciado: Modele um sistema bancário onde um Cliente possui uma ou mais Contas. 
Utilize composição para relacionar as classes Cliente e Conta.
'''
class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}") 

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor 
            print(f"\nSaque de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente.") 

    def __str__(self) -> str:
        return f"Conta {self.numero}: Saldo R${self.saldo}"  


class Cliente:
    def __init__(self,nome, cpf):
        self.nome = nome
        self.cpf = cpf 
        self.contas = [] 

    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def listar_contas(self):
        print("-="*60)
        print("Contas:\n")
        for i in self.contas:
            print(f"{i}")




conta1 = Conta('1458',4500.00)
conta2 = Conta('6598',1000.00)

cliente = Cliente('Luiz','460.035.638-18')

cliente.adicionar_conta(conta1)
cliente.adicionar_conta(conta2)

cliente.listar_contas()

conta1.depositar(1000)
conta2.sacar(500)

cliente.listar_contas()
