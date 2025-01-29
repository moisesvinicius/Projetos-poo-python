from abc import ABC, abstractmethod

"""
Desafio: Criar um sistema bancário onde diferentes tipos de contas 
compartilham métodos de saque e depósito, mas possuem regras específicas 
para cada tipo de conta.
"""

# Classe abstrata representando uma conta bancária
class ContaBancaria(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        """Método abstrato para saque"""
        pass

    @abstractmethod
    def depositar(self, valor):
        """Método abstrato para depósito"""
        pass

# Conta Corrente permite saque a descoberto com limite de cheque especial
class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if self.saldo + 500 >= valor:  # Limite de R$500
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"
        return "Saldo insuficiente."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"

# Conta Poupança não permite saque a descoberto
class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"
        return "Saldo insuficiente."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"

# Criando contas e testando operações
conta1 = ContaCorrente("João", 1000)
conta2 = ContaPoupanca("Maria", 500)

print(conta1.sacar(1300))  # Permite devido ao cheque especial
print(conta2.sacar(600))   # Não permite, pois não tem saldo suficiente