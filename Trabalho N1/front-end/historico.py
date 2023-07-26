import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, data, tipo_operacao, valor, saldo_final):
        transacao = f"{data}, {tipo_operacao}, {valor}, Saldo Final: {saldo_final}"
        self._transacoes.append(transacao)

    def imprime(self):
        if len(self._transacoes) != 0:
            for i in self._transacoes:
                print(i)
            print()
        else:
            print("Essa conta não tem extrato")
            print()

    def gerar_relatorio(self, operacao, valor, saldo):
        data_hora = datetime.datetime.now()
        registro = f"{data_hora:%d/%m/%Y %H:%M:%S},{operacao},{valor:.2f},{saldo:.2f}"
        self._transacoes.append(registro)

    def salvar_relatorio(self, num_conta):
        if len(self._transacoes) != 0:
            nome_arquivo = f"{num_conta}.csv"
            with open(nome_arquivo, "w") as file:
                for registro in self._transacoes:
                    file.write(f"{registro}\n")
            print(f"Relatório salvo no arquivo: {nome_arquivo}")
        else:
            print("Não há transações para gerar o relatório.")
