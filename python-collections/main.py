from abc import ABCMeta, abstractmethod

class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'>>código: {self._codigo}  saldo: {self._saldo}<<'


    @abstractmethod
    def passa_mes(self):
        pass

class ContaCorrente(Conta):
    def passa_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimentos(Conta):
    def passa_mes(self):
        pass