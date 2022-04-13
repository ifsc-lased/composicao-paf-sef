import os

import serial
import serial.tools.list_ports

from .arq import Arq
from .enq_enum import TIPO_t
from .enquadramento import Enquadramento
from .layer import Layer
from .poller import Poller


class PDAFCDC(Layer):

    def __init__(self, timeout_api_daf, porta=None):
        Layer.__init__(self, None, 0)

        self.enable()  # Ativa o monitoramento do objeto
        self.enable_timeout()  # Desativa o Timeout
        self.token_autorizacao = bytearray()
        self.count = 0
        self.pol = Poller()
        self.msg_to_daf = None
        self.recv_from_arq = None
        self.tipo_mensgem = None
        self.a = None
        self.e = None
        self.ser = None
        self.config(porta)
        self.tentativas = 0
        self.max_tentativas = 3
        self.timeout_api_daf = timeout_api_daf

    # Essa função não está implementada corretamente, trata-se de um esboço para testes.

    def add_to_sched(self, cb):
        self.pol.adiciona(cb)

    def envia_mensagem(self, msg):
        self.msg_to_daf = bytearray(msg.encode())
        self.tipo_mensgem = TIPO_t.ENVIARMSG.value
        self.pol.despache()
        return self.recv_from_arq

    def envia_ping(self, msg):
        self.msg_to_daf = bytearray(msg.encode())
        self.tipo_mensgem = TIPO_t.PING.value
        self.pol.despache()
        return self.recv_from_arq

    def envia_ping(self, msg):
        self.msg_to_daf = bytearray(msg.encode())
        self.tipo_mensgem = TIPO_t.ENVIARBINARIO.value
        self.pol.despache()
        return self.recv_from_arq

    def notifica(self, data, tipo):
        self.recv_from_arq = None
        if data is not None:
            self.recv_from_arq = data.decode('utf-8')
            self.tipo_mensgem = None
        self.pol.stop_poller()
        self.base_timeout = 0
        self.reload_timeout()

    def handle_timeout(self):
        self.base_timeout = self.timeout_api_daf
        self.reload_timeout()
        self.inferior.envia(self.msg_to_daf, self.tipo_mensgem)

 

    def config(self, porta):
        max_tentativas_arq = 3
        timeout_enq = 0.5
        timeout_arq = 2

        ports = serial.tools.list_ports.comports()
        portas_encontradas = ""

        for i in range(len(ports)):
            p = str(ports[i])
            portas_encontradas = portas_encontradas + ", " + p
            try:
                if (os.name == 'posix'):
                    if (ports[i].product == 'DAF-SC'):
                        porta = ports[i].name
                        break
                else:
                    prod = ports[i].description[0:6]
                    if prod == 'DAF-SC':
                        porta = ports[i].name
                        break
            except:
                pass

        if porta is not None:
            try:
                if (os.name == 'posix'):
                    self.ser = serial.Serial(
                        port='/dev/' + porta,
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=None
                    )
                else:
                    self.ser = serial.Serial(
                        port=porta,
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=None
                    )

                self.ser.flush()
                self.e = Enquadramento(self.ser, timeout_enq)
                self.a = Arq(max_tentativas_arq, timeout_arq)

                # Define organização das subcamadas
                self.set_inferior(self.a)
                self.a.set_superior(self)
                self.a.set_inferior(self.e)
                self.e.set_superior(self.a)

                self.add_to_sched(self)
                self.add_to_sched(self.a)
                self.add_to_sched(self.e)
                print("DAF conectado na porta: " + self.ser.port)
            except Exception as e:
                print(
                    "Erro ao conectar com o DAF na porta " + porta + ". Portas encontradas: " + portas_encontradas[2:])
                raise(-1)
        else:
            print('DAF não encontrado. Portas encontradas: ' + portas_encontradas[2:])
            raise(-1)
