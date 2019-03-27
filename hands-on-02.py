

##Crie a classe jogador com os atributos: nome, cidade, telefone  e e-mail. Usepelo
##menos 2 métodos na sua classe. Crie um objeto da sua classe e faça uma
##chamada dos métodos que mostre os dados dos atributos.


class Jogador:
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email


    def setNome(self, nome):
        self.nome = nome

    def setCidade(self, cidade):
        self.cidade = cidade

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setEmail(self, email):
        self.email = email

    def getNome(self):
        return self.nome

    def getCidade(self):
        return self.cidade

    def getTelefone(self):
        return self.telefone

    def getEmail(self):
        return self.email
