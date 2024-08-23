import itertools

class Autor:
    id_iter = itertools.count(start=1)

    def __init__(self, nome: str, email: str, telefone: str, biografia:str) -> None:
        self.__id: int = next(Autor.id_iter)
        self.__nome: str = nome
        self.__email: str = email
        self.__telefone: str = telefone
        self.__biografia: str = biografia


    def __str__(self) -> str:
        return f'{self.id} | {self.nome} | {self.email} | {self.telefone} | {self.biografia}'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
    
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email
    
    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        self.__telefone = telefone

    @property
    def biografia(self) -> str:
        return self.__biografia

    @biografia.setter
    def biografia(self, biografia: str) -> None:
        self.__biografia = biografia


