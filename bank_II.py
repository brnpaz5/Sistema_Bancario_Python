from abc import ABC, classmethod, property
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente,
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
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n operação falhou! Você não tem saldo suficiente.")
        
        elif valor > 0:
            self.saldo -= valor
            print("\n Saque realizado com sucesso!\n")
            return True
        else:
            print("\n Operação Falhou! O valor informado é inválido. \n")
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n Deposito Realizado com sucesso!")
        else:
            print("\n Operação Falhou! O Valor informado é invalido.")
            return False

        return True
    


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacao if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

class Historico:
    def __init__(self) -> None:
        pass

class Transacao(ABC):
    def __init__(self) -> None:
        super().__init__()

class Saque(Transacao):
    def __init__(self) -> None:
        super().__init__()

class Deposito(Transacao):
    def __init__(self) -> None:
        super().__init__()


        