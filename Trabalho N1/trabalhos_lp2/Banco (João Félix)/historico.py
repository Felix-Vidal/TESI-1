class Historico:
    def __init__(self):
        self.transacoes = []

    def imprime(self):
        if (len(self.transacoes) != 0):
            for i in self.transacoes:
                print(i)
            print()
        else:
            print("essa conta não tem extrato")
            print()