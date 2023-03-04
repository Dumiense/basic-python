class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f'contruindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = '001'

    def __pode_sacar(self, valor):
        total = self.__saldo + self.__limite
        return valor <= total

    def extrato(self):
        print(f'o saldo da conta {self.__numero} é {self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'o valor de {valor} não pode ser sacado')

    def transfere(self, valor, conta):
        if self.__saldo > valor:
            self.saca(valor)
            conta.deposita(valor)
            print('transferencia realisada com sucesso!')
        else:
            print('saldo insulficiente!')

    @property
    def saldo(self):
            return self.__saldo

    @property
    def titular(self):
            return self.__titular

    @property
    def limite(self):
            return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return '001'