# Criar um programa para cadastrar contas bancárias. O programa deve solicitar nome do
# cliente, agência e número da conta. Todas as contas devem iniciar com o saldo zerado. As
# contas devem permitir depósitos e saques. O programa deve ter o seguinte menu:
# 1 - Incluir conta
# 2 - Alterar conta
# 3 - Excluir conta
# 4 - Exibir todas as contas
# 5 - Exibir uma conta
# 6 - Depósito
# 7 - Saque
# 8 - Saldo
# 9 - Histórico (Extrato)
# 10 - Transferência
# 11 - Sair

# Para desenvolvimento desse programa, utilizar o paradigma de orientação à objetos, Lista,
# Estrutura de Repetição e Estrutura de Decisão.

class ContaBancaria:
    def __init__(self, nome, agencia, numero):
        self.nome = nome
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0.0
        self.historico = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R${valor:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: R${valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def extrato(self):
        return f"Saldo: R${self.saldo:.2f}"

    def exibir_historico(self):
        return "\n".join(self.historico)

    def __str__(self):
        return f"Nome: {self.nome}, Agência: {self.agencia}, Número: {self.numero}, Saldo: R${self.saldo:.2f}"


class Banco:
    def __init__(self):
        self.contas = {}

    def incluir_conta(self, nome, agencia, numero):
        if numero in self.contas:
            print("Conta já existe.")
        else:
            self.contas[numero] = ContaBancaria(nome, agencia, numero)
            print("Conta criada com sucesso.")

    def alterar_conta(self, numero, nome=None, agencia=None):
        if numero in self.contas:
            if nome:
                self.contas[numero].nome = nome
            if agencia:
                self.contas[numero].agencia = agencia
            print("Conta alterada com sucesso.")
        else:
            print("Conta não encontrada.")

    def excluir_conta(self, numero):
        if numero in self.contas:
            del self.contas[numero]
            print("Conta excluída com sucesso.")
        else:
            print("Conta não encontrada.")

    def exibir_todas_contas(self):
        for conta in self.contas.values():
            print(conta)

    def exibir_conta(self, numero):
        if numero in self.contas:
            print(self.contas[numero])
        else:
            print("Conta não encontrada.")

    def deposito(self, numero, valor):
        if numero in self.contas:
            self.contas[numero].deposito(valor)
            print("Depósito realizado com sucesso.")
        else:
            print("Conta não encontrada.")

    def saque(self, numero, valor):
        if numero in self.contas:
            self.contas[numero].saque(valor)
            print("Saque realizado com sucesso.")
        else:
            print("Conta não encontrada.")

    def extrato(self, numero):
        if numero in self.contas:
            print(self.contas[numero].extrato())
        else:
            print("Conta não encontrada.")

    def exibir_historico(self, numero):
        if numero in self.contas:
            print(self.contas[numero].exibir_historico())
        else:
            print("Conta não encontrada.")

    def transferencia(self, numero_origem, numero_destino, valor):
        if numero_origem in self.contas and numero_destino in self.contas:
            if valor > 0 and self.contas[numero_origem].saldo >= valor:
                self.contas[numero_origem].saque(valor)
                self.contas[numero_destino].deposito(valor)
                print("Transferência realizada com sucesso.")
            else:
                print("Saldo insuficiente ou valor inválido.")
        else:
            print("Conta(s) não encontrada(s).")


def menu():
    banco = Banco()
    while True:
        print("\nMenu:")
        print("1 - Incluir conta")
        print("2 - Alterar conta")
        print("3 - Excluir conta")
        print("4 - Exibir todas as contas")
        print("5 - Exibir uma conta")
        print("6 - Depósito")
        print("7 - Saque")
        print("8 - Saldo")
        print("9 - Histórico (Extrato)")
        print("10 - Transferência")
        print("11 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do cliente: ")
            agencia = input("Agência: ")
            numero = input("Número da conta: ")
            banco.incluir_conta(nome, agencia, numero)
        
        elif opcao == '2':
            numero = input("Número da conta a ser alterada: ")
            nome = input("Novo nome (deixe em branco para não alterar): ")
            agencia = input("Nova agência (deixe em branco para não alterar): ")
            banco.alterar_conta(numero, nome if nome else None, agencia if agencia else None)
        
        elif opcao == '3':
            numero = input("Número da conta a ser excluída: ")
            banco.excluir_conta(numero)
        
        elif opcao == '4':
            banco.exibir_todas_contas()
        
        elif opcao == '5':
            numero = input("Número da conta a ser exibida: ")
            banco.exibir_conta(numero)
        
        elif opcao == '6':
            numero = input("Número da conta para depósito: ")
            valor = float(input("Valor do depósito: "))
            banco.deposito(numero, valor)
        
        elif opcao == '7':
            numero = input("Número da conta para saque: ")
            valor = float(input("Valor do saque: "))
            banco.saque(numero, valor)
        
        elif opcao == '8':
            numero = input("Número da conta para exibir saldo: ")
            banco.extrato(numero)
        
        elif opcao == '9':
            numero = input("Número da conta para exibir histórico: ")
            banco.exibir_historico(numero)
        
        elif opcao == '10':
            numero_origem = input("Número da conta de origem: ")
            numero_destino = input("Número da conta de destino: ")
            valor = float(input("Valor da transferência: "))
            banco.transferencia(numero_origem, numero_destino, valor)
        
        elif opcao == '11':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()



# PRIMEIRA TENTATIVA 

# pessoas = []

# while True:
#     print("Menu de opções")
#     print(" 1 - Incluir conta")
#     print("2 - Alterar conta")
#     print("3 - Excluir conta")
#     print("4 - Exibir todas as contas")
#     print("5 - Exibir uma conta")
#     print("7 - Saque")
#     print("8 - Saldo")
#     print("9 - Histórico (Extrato)")
#     print("10 - Transferência")
#     print("11 - Sair")
#     opcao = int(input("Digite uma opção: "))

#     match opcao:
#         case 1:
#             c = input("Digite a conta: ")
#             pessoa = {"Conta":c}
#             pessoas.append(pessoa)
#             print("Conta incluída com sucesso!")

#         case 2:
#             indice = int(input('Digite a conta à ser alterada: '))
#             nova_conta = input('Digite a nova conta: ')
#             pessoas[indice]['conta'] = nova_conta
#             print('Pessoa atualizada com sucesso!')
#             print('-' * 25)
        
#         case 3:
#             indice = int(input('Digite a conta da pessoa à ser excluída: '))
#             pessoas.pop(indice)
#             print('Conta excluída com sucesso!')
#             print('-' * 25)
        
        # case 5:
        #     indice = int(input('Digite o código da conta à ser exibida: '))
        #     print(f'ID: {indice} | Nome: {pessoas[indice]["nome"]} | Idade: {pessoas[indice]["idade"]} | E-mail: {pessoas[indice]["email"]} | Residencia: {pessoas[indice]["residencia"]} | Profissão: {pessoas[indice]["profissão"]}')
        #     print('*' * 80)

