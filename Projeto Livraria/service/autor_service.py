from model.autor import Autor
from dao.autor_dao import AutorDAO

class AutorService:
    def __init__(self) -> None:
        self.__autor_dao: AutorDAO = AutorDAO()

    def menu(self):
        print('[Autor] Escolha uma das seguintes opções: \n'
              '1 - Listar todo os autor\n'
              '2 - Adicionar novo autor\n'
              '3 - Excluir autor\n'
              '4 - Ver autor por ID\n'
              '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        match escolha:
            case '0':
                return
            case '1':
                self.listar()
            case '2':
                self.adicionar()
            case '3':
                self.remover()
            case '4':
                self.mostar_por_id()
            case _:
                print('Opção inválida. Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('Listando autor...')
        autores = self.__autor_dao.listar()
        if len(autores) == 0:
            print('Nenhuma categoria encontrada!')

        for autor in autores:
            print(autor)

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('Adicionando autor...')
        nome = input('Digite o nome do autor de livro: ')
        # id = self.__categoria_dao.ultimo_id() + 1
        # nova_categoria = Categoria(id, nome)
        novo_autor = Autor(nome)
        self.__autor_dao.adicionar(novo_autor)
        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('Removendo categoria...')
        autor_id = int(input('Digite o ID da categoria para excluir: '))
        if self.__autor_dao.remover(autor_id):
            print('Categoria excluída com sucesso!')
        else:
            print('Categoria não encontrada!')

        input('Pressione uma tecla para continuar...')

    def mostar_por_id(self):
        print('Mostrar autor por ID...')
        autor_id = int(input('Digite o ID do autor para buscar: '))
        cat = self.__autor_dao.buscar_por_id(autor_id)

        if cat:
            print(cat)
        else:
            print('Autor não encontrada!')

        input('Pressione uma tecla para continuar...')


if __name__ == '__main__':
    service = AutorService()
    service.menu
