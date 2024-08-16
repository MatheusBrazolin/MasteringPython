class Carro:
    def __init__(self, montadora, modelo, ano, cor) -> None:
        self.__montadora = montadora
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__velocidade = 0

    def __str__(self) -> str:
        return (f'Montadora: {self.__montadora} | '
                f'Modelo: {self.__modelo} | '
                f'Ano: {self.__ano} | '
                f'Cor: {self.__cor} | '
                f'Velocidade: {self.__velocidade}')

    def acelerar(self):
        self.__velocidade += 5

    def frear(self):
        self.__velocidade -= 5

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def montadora(self):
        return self.__montadora

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def cor(self):
        return self.__cor

    @montadora.setter
    def montadora(self, montadora):
        self.__montadora = montadora

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @ano.setter
    def ano(self, ano: int):
        if ano < 1900:
            self.__ano = 1900
        else:
            self.__ano = ano

    @cor.setter
    def cor(self, cor):
        self.__cor = cor


class CarroCombustao(Carro):
    def __init__(self, montadora, modelo, ano, cor, combustivel) -> None:
        super().__init__(montadora, modelo, ano, cor)
        self.combustivel = combustivel

    def __str__(self) -> str:
        return super().__str__() + f' | Combustível: {self.combustivel}'
        # return (f'Montadora: {self.montadora} | '
        #         f'Modelo: {self.modelo} | '
        #         f'Ano: {self.ano} | '
        #         f'Cor: {self.cor} | '
        #         f'Velocidade: {self.__velocidade} | '
        #         f'Combustível: {self.combustivel}')


class CarroEletrico(Carro):
    def __init__(self, montadora, modelo, ano, cor, capacidade_bateria) -> None:
        super().__init__(montadora, modelo, ano, cor)
        self.capacidade_bateria = capacidade_bateria



chevete = CarroCombustao('Chevrolet', 'Chevette', 1970, 'Amarelo', 'Gasolina')

print(chevete)

tesla = CarroEletrico('Tesla', 'Model S', 2022, 'Preto', 100)

print(tesla)

print(vars(chevete))

chevete.acelerar()
chevete.acelerar()

print(chevete.velocidade)
print(chevete.montadora)

chevete.frear()

print(chevete.velocidade)

print(chevete)