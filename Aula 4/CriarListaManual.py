dados = []

while True:
    nome = input('digite o nome:')
    idade = int(input('Digite a idade:'))
    salario = float(input("Digite o salario:"))

    dep = [
        {'nome': 'joana', 'parentesco': 'irma'},
        {'nome': 'Mario', 'parentesco': 'irmão'},
    ]

    pessoa = { 'nome': nome, 'idade' : idade,  'salario': salario, 'dependente' : dep}
    dados.append(pessoa)

    continuar = input('Deseja continuar? (S/N)')
    if continuar.lower() == 'n':
        break

    for pessoas in dados:
        print(f"nome:  {pessoa['nome']} | Idade: {pessoa['idade']} | Salario: {pessoa['salario']}")
        print('Dependente')
        for dependente  in pessoa ['dependente']:
            print(f"Nome: {dependente['nome']} | Parentesco: {dependente['parentesco']}")


            