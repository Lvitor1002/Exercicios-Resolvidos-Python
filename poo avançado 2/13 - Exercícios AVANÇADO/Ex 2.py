'''
Implementação de Padrão de Projeto Observer
Enunciado: Implemente o padrão de projeto Observer para criar um sistema em que objetos observadores são notificados sobre mudanças em um objeto sujeito. 
Use um exemplo prático, como um sistema de notificação de eventos.
'''
class Pessoa:
    def __init__(self):
        self.lista_observador = []

    def anexar(self, observador):
        if observador not in self.lista_observador:
            self.lista_observador.append(observador)
    
    def desanexar(self, observador):
        try:
            self.lista_observador.remove(observador)
        except ValueError:
            print("Erro ao remover anexo!")
    
    def notificar(self, evento):
        for observador in self.lista_observador:
            observador.atualizar(evento)



class Observador:
    def atualizar(self, evento):
        pass 



class Notificar_evento(Pessoa):
    def __init__(self): #é o método construtor da classe Notificador_Evento
        super().__init__() # chama o método construtor da classe base Pessoa
    
    def notificar_evento(self, evento):
        print("-="*60)
        print(f"Notificando observadores sobre {evento}\n")
        
        self.notificar(evento)


class Usuario(Observador):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, evento):
        
        print(f"{self.nome} recebeu notificação do {evento}\n")
        

notificador_de_eventos = Notificar_evento()

usuario1 = Usuario('Pedro')
usuario2 = Usuario('Luiz')

notificador_de_eventos.anexar(usuario1)
notificador_de_eventos.anexar(usuario2)

notificador_de_eventos.notificar_evento("novo evento: Reunião às 14h")
#notificador_de_eventos.desanexar(usuario1)
#notificador_de_eventos.desanexar(usuario2)
notificador_de_eventos.notificar_evento("novo evento: Reunião às 14h")