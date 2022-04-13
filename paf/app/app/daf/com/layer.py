from .poller import Callback


class Layer(Callback):
    '''
    Classe Layer, que deve ser implementada por todas
    as subcamadas do protocolo
    '''

    def __init__(self, obj, tout=0):
        '''
        Construtor onde são definidos as camadas superior e inferior
        '''
        Callback.__init__(self, obj, tout)
        self.superior = None
        self.inferior = None

    def set_superior(self, superior):
        '''
        Define camada superior
        :param superior: objeto da camada superior
        '''
        self.superior = superior

    def set_inferior(self, inferior):
        '''
        Define camada inferior
        :param inferior: objeto da camada inferior
        '''
        self.inferior = inferior

    def handle(self):
        pass

    def handle_timeout(self):
        pass

    def envia(self, data):
        '''
        Mensagens que são recebidas da camada superior
        :param data: mensagem a ser tratada
        '''
        pass

    def notifica(self, data):
        '''
        Mensagens que são recebidas da camada inferior
        :param data: mensagem a ser tratada
        '''
        pass

    def notifica_erro(self):
        '''
        Informa a camada superior que um erro fatal
        ocorreu em sua camada inferior
        '''
        pass

    def disable_all_superior(self):
        '''
        Desabilita o monitoramento do obejto Callback de todas
        as camadas superiores
        '''
        self.disable()
        if not self.superior is None:
            self.superior.disable_all_superior()

    def enable_all_superior(self):
        '''
        Habilita o monitoramento do obejto Callback de todas
        as camadas superiores
        '''
        self.enable()
        if not self.superior is None:
            self.superior.enable_all_superior()

    def disable_all_inferior(self):
        '''
        Desabilita o monitoramento do obejto Callback de todas
        as camadas superiores
        '''
        self.disable()
        if not self.inferior is None:
            self.inferior.disable_all_superior()

    def enable_all_inferior(self):
        '''
        Habilita o monitoramento do obejto Callback de todas
        as camadas superiores
        '''
        self.enable()
        if not self.inferior is None:
            self.inferior.enable_all_superior()
