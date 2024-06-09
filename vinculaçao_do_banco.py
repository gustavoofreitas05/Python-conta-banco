class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaCorrente:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(('Depósito', valor))

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(('Saque', valor))
        else:
            print("Saldo insuficiente.")

    def visualizar_extrato(self):
        print("Extrato:")
        for operacao, valor in self.extrato:
            print(f"{operacao}: R${valor:.2f}")

# Criar um cliente
cliente1 = Cliente("Pedro", "123.007.288-00")

# Criar uma conta corrente para o cliente
conta1 = ContaCorrente(cliente1, 1000)

# Executar algumas operações na conta
conta1.depositar(1000)
conta1.sacar(650)
conta1.sacar(5000)  # Saldo insuficiente

# Visualizar saldo e extrato
print("Saldo atual:", conta1.saldo)
conta1.visualizar_extrato()
