from enum import Enum


class ESTADO_t(Enum):
    IDLE = 0X01
    RX_TAMANHO = 0x02
    RX_DADO = 0x03


class TIPO_t(Enum):
    """ Tipos de comandos suportados
    """
    ENVIARMSG = b'\x01'
    ENVIARBINARIO = b'\x02'
    PING = b'\x03'


class TAMANHO_t(Enum):
    """ Tipos de tamanhos suportados
    """
    TAM_2 = 0x02
    TAM_4 = 0X04
