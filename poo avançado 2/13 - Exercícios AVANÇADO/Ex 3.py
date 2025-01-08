'''
Implementação de Herança Múltipla
Enunciado: Crie uma classe que demonstre o conceito de herança múltipla em Python. 
Implemente métodos e atributos em diferentes superclasses e mostre como a classe filha herda esses elementos.
'''
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo
    
    def ligar(self):
        pass 

    def desligar(self):
        pass 

class Motorizado:
    def __init__(self, tipo_motor):
        self.tipo_motor = tipo_motor

    def acelerar(self):
        pass 

    def frear(self):
        pass 

class Terrestre:
    def __init__(self, numero_rodas):
        self.numero_rodas = numero_rodas

    def virar(self):
        pass 

class Carro(Veiculo, Motorizado, Terrestre):
    def __init__(self, marca, modelo, tipo_motor, numero_rodas):
        Veiculo.__init__(self,marca,modelo)
        Motorizado.__init__(self,tipo_motor)
        Terrestre.__init__(self,numero_rodas)
    
    def ligar(self):
        return 'Carro Ligado'
    
    def desligar(self):
        return 'carro Desligado'
    
    def acelerar(self):
        return 'carro Acelerando'

    def frear(self):
        return 'carro Freando'

    def virar(self):
        return 'carro Virando'

# Criando uma instância de Carro
meu_carro = Carro("Honda",'Civic','Flex',4)
    
# Acessando atributos e métodos da classe Carro e suas superclasses
print("\n\nMarca:", meu_carro.marca)
print("Modelo:", meu_carro.modelo)
print("Tipo de motor:", meu_carro.tipo_motor)
print("Número de rodas:", meu_carro.numero_rodas)
print("-"*70)
print("Ligar:", meu_carro.ligar())
print("Acelerar:", meu_carro.acelerar())
print("Frear:", meu_carro.frear())
print("Virar:", meu_carro.virar())
