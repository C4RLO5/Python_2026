class ContaBancaria:
    '''
    Cria uma conta bancaria e permite fazer saques e depósitos.
    '''
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo disponível R$ {self.saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo. '

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor:,.2f} autorizado na conta {self.id} ')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Não foi possível realizar o saque de R$ {valor:,.2f}: SALDO INSUFICIENTE.')
        else:
            self.saldo -= valor
            print(f'Saque concluido com sucesso, R${valor:,.2f} na conta {self.id}')





conta_1 = ContaBancaria(112, 'Carlos', 3000)
conta_1.depositar(500)
conta_1.sacar(2)
print(conta_1)