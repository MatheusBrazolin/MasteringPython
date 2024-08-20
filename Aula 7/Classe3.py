class Pessoa:
    def __init__(self, nome=None, telefone='', idade=0, saldo=0.0):
        self.__nome = nome
        self.__telefone = telefone
        self.__idade = idade
        self.__saldo = saldo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, s):
        self.__saldo = s

    def depositar(self, valor, nome_depositante=''):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def exibirDados(self):
        return f'Nome: {self.__nome} - Saldo:{self.__saldo}'


class PessoaFisica(Pessoa):
    def __init__(self, nome=None, telefone='', idade=0, saldo=0.0, cpf=''):
        super().__init__(nome, telefone, idade, saldo)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def depositar(self, valor, nome_depositante=''):
        valor += 0.10
        super().depositar(valor, nome_depositante)


pessoa1 = PessoaFisica('Well')
pessoa2 = PessoaFisica('Maria')

print(pessoa1.exibirDados())
print(pessoa2.exibirDados())

pessoa2.depositar(nome_depositante='Jośe', valor=20)

print(pessoa1.exibirDados())
print(pessoa2.exibirDados())

pessoa = Pessoa('Fernando')
pessoa.depositar(30)

print(pessoa.exibirDados())