"""
Desenvolver um programa que armazene pessoas. As pessoas devem informar nome,
email, idade, estado de residência e profissão. Permitir serem cadastradas apenas as
pessoas de SP, MG e RJ. Utilize lista, dicionário, tupla, set, e funções nesse exercício. 
O programa deverá ter o seguinte menu:
1 - Inclusão
2 - Exclusão
3 - Exibição de todos
4 - Alteração
5 - Exibir uma pessoa
6 - Exibir profissões
7 - Sair
"""

pessoas = []

while True:
    print("Menu de opções")
    print("1 - Inclusão")
    print("2 - Exclusão")
    print("3 - Exibição de todo")
    print("4 - Alteração")
    print("5 - Exibir uma pessoa")
    print("6 - Exibir profissões")
    print("7 - Sair")
    opcao = int(input("Digite uma opção: "))
    match opcao:
        case 1:
            n = input("Digite o nome: ")
            i = int(input("Digite a idade: "))
            e = input("Digite o email: ")
            r = input("Qual seu estado? (SP/MG/Rj)")
            p = input("Qual a sua profissão? ")
            pessoa = {"nome": n, "idade": i, "email": e, "residencia": r, "profissão": p}
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
                print(f'ID: {indice} | Nome: {p["nome"]} | Idade: {p["idade"]} | E-mail: {p["email"]} | Residencia: {p["residencia"]}| Profissão {p["profissão"]}')
                print('*' * 80)
        case 4:
            indice = int(input('Digite o código da pessoa à ser alterada: '))
            novo_email = input('Digite o novo e-mail: ')
            pessoas[indice]['email'] = novo_email
            print('Pessoa atualizada com sucesso!')
            print('*' * 80)
        case 5:
            indice = int(input('Digite o código da pessoa à ser exibida: '))
            print(f'ID: {indice} | Nome: {pessoas[indice]["nome"]} | Idade: {pessoas[indice]["idade"]} | E-mail: {pessoas[indice]["email"]} | Residencia: {pessoas[indice]["residencia"]} | Profissão: {pessoas[indice]["profissão"]}')
            print('*' * 80)
        case 6:
          for indice, p in enumerate(pessoas):
                print(f'ID: {indice} |Nome: {p["nome"]} | Profissão: {p["profissão"]}')
                print('-' *40)
        case _:
            break