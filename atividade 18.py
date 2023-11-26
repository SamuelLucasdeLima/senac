class DispositivoEletronico:
    def __init__(self, nome):
        self.__nome = nome
    
    def ligar(self):
        pass

class Impressora(DispositivoEletronico):
    def __init__(self, nome):
        super().__init__(nome)
    
    def ligar(self):
        return f"{self._DispositivoEletronico__nome} está imprimindo."

class Televisão(DispositivoEletronico):
    def __init__(self, nome):
        super().__init__(nome)
    
    def ligar(self):
        return f"{self._DispositivoEletronico__nome} está transmitindo a um programa."

class ConsoleGame(DispositivoEletronico):
    def __init__(self, nome):
        super().__init__(nome)
    
    def ligar(self):
        return f"{self._DispositivoEletronico__nome} está executando um jogo."

class Drone(DispositivoEletronico):
    def __init__(self, nome):
        super().__init__(nome)
    
    def ligar(self):
        return f"{self._DispositivoEletronico__nome} está sobrevoando."

class AparelhoAudio(DispositivoEletronico):
    def __init__(self, nome):
        super().__init__(nome)
    
    def ligar(self):
        return f"{self._DispositivoEletronico__nome} está tocando um áudio."

def mostrar(dispositivos):
    for aparelho in dispositivos:
        print(aparelho.ligar())


dispositivos = [Televisão("Samsumg Smart Tv"), Impressora("EcoTank L3210"), ConsoleGame("PlayStation 5"), Drone("Dji Air 2S Fly"), AparelhoAudio("JBL BomBox 3")]
mostrar(dispositivos)