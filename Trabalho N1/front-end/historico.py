class Historico:
    def __init__(self):
           self._transacoes = []

    def imprime(self):
        if (len(self._transacoes) != 0):
            for i in self._transacoes:
                print(i)
            print()
        else:
            print("essa conta não tem extrato")
            print()