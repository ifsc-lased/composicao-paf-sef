from enum import Enum


class TIPO_t(Enum):
    """ Tipos de comandos suportados
    """
    ENVIARMSG = 0x01
    ENVIARBINARIO = 0x02
    PING = 0x03
    ERRO = 0x04


class TAMANHO_t(Enum):
    """ Tipos de tamanhos suportados
    """
    TAM_1 = 0x01
    TAM_2 = 0x02
    TAM_4 = 0X04


class ERRO_t(Enum):
    """ Tipos de erros previstos
    """
    ER_CMD_INVALIDO = 0x01
    ER_TAM_INVALIDO = 0x02
    ER_TIMEOUT = 0X04
    ER_DESCONHECIDO = 0x05
    ER_OCUPADO = 0x06
