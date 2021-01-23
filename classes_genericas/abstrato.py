from abc import ABC, abstractclassmethod
from exceptions.exception import UmErroEspecificoError
from enum import Enum, auto

class AcountType(Enum):
    contaSalario = 'Conta Salario'
    contaPoupancaFixada = 'Conta poupanca indexada'
    contaPoupanca_comun = 'Conta poupanca'
    contaCorrente = 'Conta corrente'


class Conta(ABC):
    def __new__(cls, *args, **kwargs): #construtor da classe
        return object.__new__(cls)
    
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
    def sacar(self, valor): pass

class ContaPoupanca(Conta):
    def __new__(cls, *args, **kwargs): #construtor da classe
        if not hasattr(cls, '_jaExiste'): # padrão singleton: garante a existencia de apenas uma instacia da classe
            cls._jaExiste = object.__new__(cls)

        return cls._jaExiste

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

    def transferenciaEntreContas(self, contaDestino):
        if not isinstance(contaDestino, AcountType):
            raise ValueError(f'Não existe {contaDestino} como variação de conta no momento, por favor tente outra')

        return print(f'Transferencia para {contaDestino.value} realizada com sucesso!')

    def sacar(self, valor):
        try:
            if (self.saldo + self.limite) < valor:
                print('Saldo insuficiente')
                return

            self.saldo -= valor
            self.extrato()
        except UmErroEspecificoError as e:
            print(f'Erro: {e}')
