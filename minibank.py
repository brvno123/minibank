class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação (depósito ou saque) em uma conta específica do cliente.
        """
        if conta not in self.contas:
            print(f"❌ A conta informada não pertence ao cliente {self.nome}.")
            return

        transacao.registrar(conta)  # A transação sabe como se registrar
        print(f"✅ Transação realizada com sucesso para o cliente {self.nome}.")

    def adicionar_conta(self, conta):
        """
        Adiciona uma nova conta à lista de contas do cliente.
        """
        self.contas.append(conta)
        print(f"🏦 Conta adicionada com sucesso ao cliente {self.nome}.")

from historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        """
        Realiza um saque da conta, caso haja saldo suficiente.
        """
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        if valor > self._saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        """
        Realiza um depósito na conta, desde que o valor seja positivo.
        """
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0  # controla quantos saques foram feitos

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente considerando o limite e o limite de saques diários.
        """
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        if self._saques_realizados >= self._limite_saques:
            print("\n@@@ Operação falhou! Limite de saques diários atingido. @@@")
            return False

        if valor > self._saldo + self._limite:
            print("\n@@@ Operação falhou! Saldo + limite insuficiente. @@@")
            return False

        self._saldo -= valor
        self._saques_realizados += 1
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}
"""

from transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """
        Registra o depósito na conta e adiciona a transação ao histórico.
        """
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            print(f"💰 Depósito de R$ {self.valor:.2f} registrado no histórico.")

from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma transação ao histórico, registrando tipo, valor e data/hora.
        """
        registro = {
            "tipo": type(transacao).__name__,  # 'Deposito' ou 'Saque'
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        self._transacoes.append(registro)
        print(f"📄 Transação registrada: {registro['tipo']} de R$ {registro['valor']:.2f} em {registro['data']}")

    def imprimir_extrato(self):
        """
        Exibe todas as transações do histórico.
        """
        print("\n====== Extrato ======")
        if not self._transacoes:
            print("Nenhuma transação realizada.")
            return

        for t in self._transacoes:
            print(f"{t['data']} | {t['tipo']}: R$ {t['valor']:.2f}")

from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, cpf, endereco)  # chama o construtor da classe Cliente
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"Pessoa Física: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}, Endereço: {self.endereco}"

from transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """
        Realiza um saque na conta e registra a transação no histórico caso tenha sucesso.
        """
        sucesso_transacao = conta.sacar(self.valor)  # tenta sacar o valor da conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            print(f"💸 Saque de R$ {self.valor:.2f} registrado no histórico.")
        else:
            print(f"❌ Saque de R$ {self.valor:.2f} não realizado.")

from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        """Deve retornar o valor da transação."""
        pass

    @abstractmethod
    def registrar(self, conta):
        """Deve registrar a transação na conta fornecida."""
        pass

import textwrap
from ContaCorrente import ContaCorrente
from PessoaFisica import PessoaFisica
from Deposito import Deposito
from Saque import Saque

def menu():
    menu = """\n
    ================ MENU ================
    
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [7]\tSair

    ======================================

    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    transacao_valida(clientes, "Informe o valor do depósito: ", Deposito)
    # cpf = input("Informe o CPF do cliente: ")
    # cliente = filtrar_cliente(cpf, clientes)

    # if not cliente:
    #     print("\n@@@ Cliente não encontrado! @@@")
    #     return

    # valor = float(input("Informe o valor do depósito: "))
    # transacao = Deposito(valor)

    # conta = recuperar_conta_cliente(cliente)
    # if not conta:
    #     return

    # cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    transacao_valida(clientes, "Informe o valor do saque: ", Saque)
    # cpf = input("Informe o CPF do cliente: ")
    # cliente = filtrar_cliente(cpf, clientes)

    # if not cliente:
    #     print("\n@@@ Cliente não encontrado! @@@")
    #     return

    # valor = float(input("Informe o valor do saque: "))
    # transacao = Saque(valor)

    # conta = recuperar_conta_cliente(cliente)
    # if not conta:
    #     return

    # cliente.realizar_transacao(conta, transacao)

def transacao_valida(clientes, input_valor, valor_transacao):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input(input_valor))
    transacao = valor_transacao(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\t{transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    if (contas != []):
        for conta in contas:
          print("=" * 100)
          print(textwrap.dedent(str(conta)))
    else:
        print("\n=== Não existe conta! ===")        


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()