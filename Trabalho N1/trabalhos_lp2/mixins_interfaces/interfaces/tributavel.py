import abc

class TributavelInterface(abc.ABC):
    '''Classe que contém operações de um objeto tributável. As
    subclasses concretas devem sobrescrever o método valor_imposto.
    '''
    @abc.abstractmethod
    def valor_imposto(self):
        '''aplica taxa de imposto sobre um determinado valor do objeto'''
        pass
