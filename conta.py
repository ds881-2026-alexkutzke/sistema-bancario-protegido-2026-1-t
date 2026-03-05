class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def obter_saldo(self):
        return self.saldo
    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
