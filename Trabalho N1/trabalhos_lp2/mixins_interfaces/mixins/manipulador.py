class ManipuladorDeTributaveis:

    def calcular_imposto(self, lista_tributaves):
        total = 0
        for i in lista_tributaves:
            total += i.valor_imposto()

        return total