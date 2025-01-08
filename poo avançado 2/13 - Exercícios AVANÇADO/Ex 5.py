'''
Implementação de Encapsulamento
Enunciado: Crie uma classe que represente um carro. Utilize encapsulamento para proteger os atributos do carro, como velocidade e quilometragem, 
e forneça métodos para acessar e modificar esses atributos de forma segura.
'''

class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.__velocidade = 0
        self.__quilometragem = 0

    def acelerar(self, valor):
        self.__velocidade += valor

    def frear(self, valor):
        self.__velocidade -= valor

    def obter_velocidade(self):
        return self.__velocidade

    def obter_quilometragem(self):
        return self.__quilometragem

    def adicionar_quilometragem(self, valor):
        self.__quilometragem += valor

# Exemplo de uso:
meu_carro = Carro("Toyota", "Preto")
meu_carro.acelerar(50)
print("Velocidade:", meu_carro.obter_velocidade())
meu_carro.adicionar_quilometragem(100)
print("Quilometragem:", meu_carro.obter_quilometragem())
