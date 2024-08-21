from conta import Conta

listaContas = []


def exibirContas():
    for c in listaContas:
        print(f"Titular: {c.nome} | Agência: {c.agencia} | Número da Conta: {c.numero}")


def getIndexConta(numero_conta):
    id = -1
    for c in listaContas:
        if c.numero == numero_conta:
            id = listaContas.index(c)
            break
    return id


def incluir_conta():
    c = Conta()
    c.nome = input("Digite o nome do titular: ")
    c.agencia = input("Digite a sua agência: ")
    c.numero = input("Digite o número da conta: ")
    listaContas.append(c)
    print("Conta inserida com sucesso!")


def alterar_conta():
    numero_conta = input("Digite o numero da conta que deseja atualizar: ")
    id = getIndexConta(numero_conta)
    if id == -1:
        print("Conta não encontrada!")
    else:
        listaContas[id].nome = input("Digite um novo nome do titular: ")
    print("Conta atualizada com sucesso!")


def excluir_conta():
    exibirContas()
    numero_conta = input("Digite o numero da conta que deseja excluir: ")
    id = getIndexConta(numero_conta)
    if id == -1:
        print("Conta não encontrada!")
    else:
        listaContas.pop(id)
    print("Conta excluída com sucesso!")


def exibir_conta():
    numero_conta = input("Digite o numero da conta que deseja exibir: ")
    id = getIndexConta(numero_conta)
    if id == -1:
        print("Conta não encontrada!")
    else:
        print(
            f"Titular: {listaContas[id].nome} | Agência: {listaContas[id].agencia} | Número da conta: {listaContas[id].numero}"
        )


def depositar():
    exibirContas()
    numero_conta = input("Digite o numero da conta que deseja depositar: ")
    id = getIndexConta(numero_conta)
    if id == -1:
        print("Conta não encontrada!")
    else:
        valor = float(input("Digite o valor do depósito?: "))
    # listaContas[id].depositar(valor)
    listaContas[id] + valor
    print("Depósito realizado com sucesso!")


def sacar():
    exibirContas()
    numero_conta = input("Digite o numero da conta que deseja sacar: ")
    id = getIndexConta(numero_conta)
    if id == -1:
        print("Conta não encontrada!")
    else:
        valor = float(input("Digite o valor do saque: "))

    listaContas[id].sacar(valor)
    listaContas[id] - valor
    print("Saque realizado com sucesso!")


def consulta_saldo():
    exibirContas()
    numero_conta = input("Digite o numero da conta que deseja consultar o saldo: ")
    id = getIndexConta(numero_conta)
    if id == -1:
        print("Conta não encontrada!")
    else:
        print(listaContas[id].exibirSaldo())


def exibir_historico():
    exibirContas()
    numero_conta = input("Digite o numero da conta que deseja obter o extrato: ")
    id = getIndexConta(numero_conta)
    if id == -1:
        print("Conta não encontrada!")
    elif len(listaContas[id].historico) == 0:
        print("Cliente sem movimentação na conta!")
    else:
        for e in listaContas[id].historico:
            print(e)


def transferir():
    exibirContas()
    numero_conta_origem = input("Digite o numero da conta origem: ")
    numero_conta_destino = input("Digite o numero da conta destino: ")
    valor = float(input("Digite o valor da transferência: "))
    id_origem = getIndexConta(numero_conta_origem)
    id_destino = getIndexConta(numero_conta_destino)
    if (id_origem == -1) or (id_destino == -1):
        print("Conta origem/destino não encontrada!")
    else:
        listaContas[id_origem].transferir(listaContas[id_destino], valor)
    print("Transferência realizada com sucesso!")