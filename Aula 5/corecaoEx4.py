# Desenvolver um programa que armazene pessoas.
# As pessoas devem informar nome, e-mail e idade.
# O programa deve ser o seguinte:

# 1 - Inclusão 
# 2 - Exclusão
# 3 - Exibição de todos os requisetos 
# 4 - Alteração dos dados de um pessoa
# 5 - Sair

pessoas = []

while True:
    print("Menu de opções")
    print("1 - Incluir")
    print("2 - Excluir")
    print("3 - Exibir todos os registros")
    print("4 - Alterar os dados de uma pessoa")
    print("5 - Exibir uma pessoa")
    print("6 - Sair")
    opcao = int(input("Digite uma opção: "))
    match opcao:
        case 1:
            n = input("Digite o nome: ")
            i = int(input("Digite a idade: "))
            e = input("Digite o email: ")
            pessoa = {"nome": n, "idade": i, "email": e}
            pessoas.append(pessoa)
            print("Pessoa incluída com sucesso!")
            print('*' * 80)
        case 2:
            indice = int(input('Digite o código da pessoa à ser excluída: '))
            pessoas.pop(indice)
            print('Pessoa excluída com sucesso!')
            print('*' * 80)
        case 3:
            for indice, p in enumerate(pessoas):
                print(f'ID: {indice} | Nome: {p["nome"]} | Idade: {p["idade"]} | E-mail: {p["email"]}')

            print('*' * 80)
        case 4:
            indice = int(input('Digite o código da pessoa à ser alterada: '))
            novo_email = input('Digite o novo e-mail: ')
            pessoas[indice]['email'] = novo_email
            print('Pessoa atualizada com sucesso!')
            print('*' * 80)
        case 5:
            indice = int(input('Digite o código da pessoa à ser exibida: '))
            print(f'ID: {indice} | Nome: {pessoas[indice]["nome"]} | Idade: {pessoas[indice]["idade"]} | E-mail: {pessoas[indice]["email"]}')
            print('*' * 80)
        case _:
            break





