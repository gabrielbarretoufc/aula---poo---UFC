# banco

class Banco:
    def __init__(self):
        self.contas = [None] * 100
        self.indice = 0

    def cadastrar(self, conta):
        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1

            if achou is True:
                return self.contas[i]
        else:
            return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)

        if conta:
            conta.creditar(valor)
        else:
            print('Conta inexistente!')

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)

        if conta:
            conta.debitar(valor)
        else:
            print('Conta inexistente!')

    def saldo(self, numero):
        pass

    def transferir(self, origem, destino, valor):
        pass
