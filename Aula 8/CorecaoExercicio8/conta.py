class Conta:
    def __init__(self, nome='', agencia='', numero='', saldo=0):
        self.__nome = nome
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo
        self.__historico = []

    def __repr__(self):
        return f'Conta({self.nome}, {self.agencia}, {self.numero}, {self.saldo})'

    def __str__(self) -> str:
        return f'Titular da conta {self.nome} | Agência: {self.agencia} | Número: {self.numero}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.strip()

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def historico(self):
        return self.__historico

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
        self.__historico.append('+ $' + str(valor))

    def sacar(self, valor):
        self.__saldo = self.__saldo - valor
        self.__historico.append('- $' + str(valor))

    def transferir(self, contaDestino, valor):
        self.sacar(valor)
        contaDestino.depositar(valor)

    def exibirSaldo(self):
        return 'R$ ' + str(self.__saldo)

    def __add__(self, valor):
        self.__saldo = self.__saldo + valor
        self.__historico.append('+ $' + str(valor))

    def __sub__(self, valor):
        self.__saldo = self.__saldo - valor
        self.__historico.append('- $' + str(valor))


if __name__ == '__main__':
    c = Conta('Well', '003', '2323', 500)
    print(repr(c))
