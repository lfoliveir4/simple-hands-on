

from hands-on-3 import Smartphone

class MP3Player(Smartphone):
    def __init__(self, capacidade, interface, tamanho):
        super().__init__(interface, tamanho)
        self.capacidade = capacidade


    def getCapacidade(self):
        return self.capacidade

    def setCapacidade(self, capacidade):
        self.capacidade = capacidade