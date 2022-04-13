from .arq_enum import ESTADO_t, CONTROLE_t
from .enq_enum import TIPO_t
from .layer import Layer


class Arq(Layer):

    def __init__(self, max_tentativas, timeout):
        self.seq_rx = 0
        self.seq_tx = 0
        self.tipo = 0
        self.limite_tentativas = max_tentativas
        self.tentativas = 0  # Número de tentativas

        self.tout = timeout

        self.estado = ESTADO_t.IDLE.value  # Estado inicial da FSM
        self.msg = bytearray()
        self.superior = None
        self.inferior = None
        self.campo_dados = bytearray()

        Layer.__init__(self, None, timeout)

        self.enable()
        self.disable_timeout()  # Desativa o Timeout

    def handle_fsm(self, campo_controle, campo_dados):
        '''
        Máquina de estado que trata o envio e recepção de mensagens
        :param data: mensagem recebida
        '''
        self.campo_dados = campo_dados
        if self.estado == ESTADO_t.IDLE.value:
            self.__idle(campo_controle, campo_dados)
        else:
            self.__wait(campo_controle, campo_dados)

    def __idle(self, campo_controle, campo_dados):
        '''
        Estado inicial de transmissão e para recepção
        :param data: mensagem recebida
        '''
        # Caso tenha recebido o ACK, envia uma nova mensagem
        if campo_controle is None:
            if (self.seq_tx == 1):
                campo_controle = CONTROLE_t.DATA_1.value
            else:
                campo_controle = CONTROLE_t.DATA_0.value

            self.monta_quadro(campo_controle, campo_dados)
            self.estado = ESTADO_t.WAIT.value
            self.recarrega_timeout(self.tout)
            self.superior.disable_all_superior()
            self.inferior.envia(self.msg, self.tipo)  # Envia para a subcamada inferior (Enquadramento)
        else:
            # Recebe uma nova mensagem e envia um ACK
            if ((self.seq_rx == 1) and (campo_controle == CONTROLE_t.DATA_1.value)) or (
                    (self.seq_rx == 0) and (campo_controle == CONTROLE_t.DATA_0.value)):
                self.estado = ESTADO_t.IDLE.value
                # print("\nRecebi:", self.campo_dados)
                self.__ack(False)
                self.disable_timeout()
                self.superior.notifica(self.campo_dados, self.campo_tipo)

                # Recebe uma mensagem já recebida e reenvia um ACK
            elif ((self.seq_rx == 0) and (campo_controle == CONTROLE_t.DATA_1.value)) or (
                    (self.seq_rx == 1) and (campo_controle == CONTROLE_t.DATA_0.value)):
                self.estado = ESTADO_t.IDLE.value
                self.disable_timeout()
                self.__ack(True)

            # Recebeu o ACK errado, reenvia a mensagem
            else:
                self.__reenvia()

    def __wait(self, campo_controle, campo_dados):
        print("campo controle", campo_controle)
        if campo_controle is not None:
            # Se recebeu o ACK correto, está apto a enviar uma nova mensagem
            if ((self.seq_tx == 1) and (campo_controle == CONTROLE_t.ACK_1.value)) or (
                    (self.seq_tx == 0) and (campo_controle == CONTROLE_t.ACK_0.value)):
                print('Recebi: ACK', int(self.seq_tx))
                self.seq_tx = not self.seq_tx
                self.estado = ESTADO_t.IDLE.value
                self.disable_timeout()


            # Recebe uma nova mensagem e envia um ACK
            elif ((self.seq_rx == 1) and (campo_controle == CONTROLE_t.DATA_1.value)) or (
                    (self.seq_rx == 0) and (campo_controle == CONTROLE_t.DATA_0.value)):
                self.estado = ESTADO_t.WAIT.value
                print("\nRecebi:", self.campo_dados)
                self.__ack(False)
                self.recarrega_timeout(self.tout)
                self.superior.notifica(self.campo_dados)

            # Recebe uma mensagem já recebida e reenvia um ACK
            elif ((self.seq_rx == 0) and (campo_controle == CONTROLE_t.DATA_1.value)) or (
                    (self.seq_rx == 1) and (campo_controle == CONTROLE_t.DATA_0.value)):
                print("reenvia")
                self.estado = ESTADO_t.WAIT.value
                self.recarrega_timeout(self.tout)
                self.__ack(True)

    def monta_quadro(self, controle, data):
        '''
        Monta o quadro com as características do ARQ_MAC
        :param controle: Define tipo DATA ou ACK e número de sequência
        :param data: Quadro originado pela subcamada superior (API DAF)
        :return:
        '''
        self.msg.clear()
        self.msg.append(controle)
        self.msg = self.msg + data

    def __ack(self, reenvio):
        '''
        Define o cabeçalho de controle para um ACK
        :param reenvio: garante que o ACK correto seja enviado
        '''
        ack = bytearray()
        seq_envio = self.seq_rx

        # Corrige o número de sequência para o reenvio de ACK
        if (reenvio):
            seq_envio = not self.seq_rx

        if (seq_envio == 1):
            controle = CONTROLE_t.ACK_1.value
        else:
            controle = CONTROLE_t.ACK_0.value
        ack.append(controle)

        # Altera o número de sequência de rx quando não for um reenvio de ACK
        if (not reenvio):
            self.seq_rx = not self.seq_rx
        self.inferior.envia(ack, TIPO_t.ENVIARMSG.value)  # Envia para a subcamada inferior (Enquadramento)

    def __reenvia(self):
        '''
        Realiza o reenvio da mensagem em caso
        de Timeout ou de ACK incorreto
        '''
        print('Reenviando:', self.msg)
        self.tentativas += 1
        self.recarrega_timeout(self.tout)
        self.inferior.envia(self.msg, self.tipo)

    def handle(self):
        pass

    def handle_timeout(self):
        '''
        Monitora o timeout e
        reenvia a mensagem quando necessário
        '''
        print('timeout arq')
        if self.estado == ESTADO_t.WAIT.value:
            # Caso atinja o limite de tentativas de reenvio, declara ERRO FATAL
            if (self.tentativas == self.limite_tentativas - 1):
                print('\nERRO FATAL: limite de tentativas atingido\n')
                self.tentativas = 0
                self.disable_timeout()
                self.seq_rx = not self.seq_rx
                self.estado = ESTADO_t.IDLE.value
                self.superior.notifica(None, None)
            else:
                self.recarrega_timeout(self.tout)
                self.estado = ESTADO_t.WAIT.value
                self.__reenvia()

    def recarrega_timeout(self, timeout):
        '''
        Carrega um novo valor de timeout e o recarrega
        :param timeout: tempo de espera
        '''
        self.timeout = timeout
        self.reload_timeout()
        self.enable_timeout()

    def envia(self, data, tipo):
        '''
        Trata mensagens vindas da subcamada superior (API-DAF)
        :param data: mensagem a ser enviada
        '''
        self.tipo = tipo
        self.handle_fsm(None, data)

    def notifica(self, campo_controle, campo_dados, campo_tipo):
        '''
        Trata mensagens vindas da subcamada inferior (Enquadramento)
        :param data: mensagem recebida a ser verificada
        '''
        self.campo_tipo = campo_tipo
        self.handle_fsm(campo_controle, campo_dados)

    def retorna_dados(self):
        return self.campo_dados
