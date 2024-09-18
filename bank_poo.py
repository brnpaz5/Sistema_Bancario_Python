from datetime import datetime
from abc import ABC

class Conta:
    def __init__(self, agencia, conta, limite=500, limite_saques = 3):
        self.saldo = 0
        self.agencia = agencia
        self.conta = conta
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_dia = 0
   
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor Inválido!")
    
    def saque(self, valor):
        saldo = self.saldo
        limite = self.limite
        limite_saques = self.limite_saques
        dia_saques = self.saques_dia

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saques =  dia_saques > limite_saques

        if excedeu_saldo:
            print("Saldo Insuficiente!")
        elif excedeu_limite:
            print("O valor é maior do que o limite permitido!")
        elif excedeu_limite_saques:
            print("Limite de saques diarios atingido!")
        elif valor > 0:
            self.saldo -= valor
            self.saques_dia += 1
            print(f"Saque realizado: R$ {valor}")

    
    def extrato(self):
        print(f"----------- Extrato --- Saldo: R$ {self.saldo}")

    def __str__(self):
        return f"{[ f'{chave} : {valor}' for chave, valor in self.__dict__.items()]}"
    
    @classmethod
    def main(cls):
        bk = cls('0001', '1580')
        while True:
            option = """
            [d] - Depositar
            [s] - Saque
            [e] - Extrato
            [q] - Sair
            ==>

        """
            choice = input(option)

            if choice == 'd':
                value = input("Digite o valor: \n")
                if value.isdigit():
                    bk.depositar(float(value))
            if choice == 's':
                value = input("Digite o valor: \n")
                if value.isdigit():
                    bk.saque(float(value))

            elif choice == 'e':
                bk.extrato()
    
            elif choice == 'q':
                break

    
if __name__ == "__main__":
    Conta.main()