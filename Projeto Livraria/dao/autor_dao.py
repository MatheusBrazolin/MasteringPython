from model.autor import Autor

class AutorDAO:
    def __init__(self) -> None:
        self.__autores: list[Autor] = list()  # Nosso Banco de Dados

    def listar(self) -> list[Autor]:  # SELECT * FROM categoria
        return self.__autores

    def adicionar(self, autores: Autor) -> None:  # INSERT INTO categoria
        self.__autores.append(Autor)

    def remover(self, autores_id: int) -> bool:
        encontrado = False

        for cat in self.__autores:
            if cat.id == autores_id:
                index = self.__autores.index(cat)
                self.__autores.pop(index)
                encontrado = True
                break

        return encontrado

    def buscar_por_id(self, autor_id) -> Autor:
        cat = None
        for c in self.__autores:
            if c.id == autor_id:
                cat = c
                break

        return cat