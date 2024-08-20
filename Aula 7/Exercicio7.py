class Pessoa:
    def __init__(self, nome, telefone, idade):
        self._nome = None
        self._telefone = None
        self._idade = None
        self.nome = nome
        self.telefone = telefone
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade
     