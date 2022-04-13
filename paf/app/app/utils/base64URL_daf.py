import base64


class Base64URLDAF:

    def __init__(self):
        pass

    @staticmethod
    def base64URLDecode(input: str) -> bytes:
        """ Método para decodificação de Base64URL

        Args:
            input (str): Mensagem a ser decodificada

        Returns:
            bytes: Mensagem decodificada
        """
        if isinstance(input, str):
            input = input.encode("ascii")
        rem = len(input) % 4
        if rem > 0:
            input += b"=" * (4 - rem)
        return base64.urlsafe_b64decode(input)

    @staticmethod
    def base64URLEncode(input: bytes) -> str:
        """ Método para codificação de mensagens para base64URL

        Args:
            input (bytes): Mensagem a ser codificada
        Returns:
            str: Mensagem codificada
        """
        return base64.urlsafe_b64encode(input).replace(b"=", b"").decode('utf-8')
