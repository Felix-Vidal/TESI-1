from tributavel import TributavelInterface
class ManipuladorDeTributaveis:

    def calcular_imposto(self, lista_tributaves):
        total = 0
        for obj in lista_tributaves:
            if (isinstance(obj,TributavelInterface)):
                total += obj.valor_imposto()
            else:
                print(f'{obj.__class__.__name__} não herda de TributavelInterface')
        return total