"""
Criar um programa para cadastrar contas bancárias. O programa deve solicitar nome do
cliente, agência e número da conta. Todas as contas devem iniciar com o saldo zerado. As
contas devem permitir depósitos e saques. O programa deve ter o seguinte menu:
1 - Incluir conta
2 - Alterar conta
3 - Excluir conta
4 - Exibir todas as contas
5 - Exibir uma conta
6 - Depósito
7 - Saque
8 - Saldo
9 - Histórico (Extrato)
10 - Transferência
11 - Sair

Para desenvolvimento desse programa, utilizar o paradigma de orientação à objetos, Lista,
Estrutura de Repetição e Estrutura de Decisão.
"""

from exercicio_07_aux import (
    incluir_conta,
    alterar_conta,
    excluir_conta,
    exibirContas,
    exibir_conta,
    depositar,
    sacar,
    consulta_saldo,
    exibir_historico,
    transferir,
)

while True:
    print("=== Cadastro de Contas Bancárias - Menu de Opções ===\n")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Exibir todos")
    print("5 - Exibir uma conta")
    print("6 - Depositar")
    print("7 - Sacar")
    print("8 - Saldo")
    print("9 - Histórico (Extrato)")
    print("10 - Transferir")
    print("11 - Sair")
    opcao = int(input("Digite uma opção: "))

    match opcao:
        case 1:
            incluir_conta()
        case 2:
            alterar_conta()
        case 3:
            excluir_conta()
        case 4:
            exibirContas()
        case 5:
            exibir_conta()
        case 6:
            depositar()
        case 7:
            sacar()
        case 8:
            consulta_saldo()
        case 9:
            exibir_historico()
        case 10:
            transferir()
        case _:
            break

    input("Digite Enter para continuar...")
    print('*' * 80)
