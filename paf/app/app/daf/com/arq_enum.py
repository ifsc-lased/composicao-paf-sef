from enum import Enum


class ESTADO_t(Enum):
    IDLE = 0X01
    WAIT = 0x02


class CONTROLE_t(Enum):
    """ Tipos de cabeçalhos de Controle,
    onde os 4 primeiros bytes representam o tipo
    e os 4 últimos a sequência.
    """
    DATA_0 = 0x00  # 0000 0000
    DATA_1 = 0x08  # 0000 0100
    ACK_0 = 0x80  # 1000 0000
    ACK_1 = 0x88  # 1000 0100
