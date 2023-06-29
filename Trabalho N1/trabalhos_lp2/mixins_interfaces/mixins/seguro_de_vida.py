from tributavel import TributavelMixIn


class SeguroDeVida(TributavelMixIn):
    _total_seguros = 0
    def	__init__(self, valor, titular):
        self._numero = SeguroDeVida._total_seguros + 1
        self._valor	= valor
        self._titular = titular
        SeguroDeVida._total_seguros += 1

    def	valor_imposto(self):
        return	34 + self._valor* 0.05
