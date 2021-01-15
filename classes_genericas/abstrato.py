from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")

        self._saldo = valor
    
    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numérico")

        self._saldo += valor
        self.extrato() 

    def extrato(self):
        print(f'Agencia: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')       

    @abstractclassmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.extrato()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=10000):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.extrato()