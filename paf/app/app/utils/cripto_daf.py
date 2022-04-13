import hashlib
import hmac
import random

from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding


class ChaveRSA():

    def __init__(self, chave: str):
        """ Encapsula uma chave criptográfica

        Args:
            chave (str): chave criptográfica na forma de string
        """
        self.chave_str = chave
        self.chave_bytes = chave.encode('utf-8')


class Certificado():

    def __init__(self, cert: str):
        """ Encapsula um certificado digital

        Args:
            cert (str): certificado digital na forma de string
        """
        certificado_x509 = x509.load_pem_x509_certificate(cert.encode('utf-8'))

        self.assinatura = certificado_x509.signature
        self.chave_publica = ChaveRSA(certificado_x509.public_key().public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.PKCS1).decode('utf-8'))
        self.certificado_str = cert
        self.certificado_bytes = certificado_x509.public_bytes(
            serialization.Encoding.PEM)
        self.conteudo_assinado = certificado_x509.tbs_certificate_bytes


class CriptoDAF:
    ''' 
        Classe para operações criptográficas do DAF Virtual
    '''

    def __init__(self):
        pass

    @staticmethod
    def geraAssinaturaRSA_PKCS1_V1_5(msg: bytes, privkey: ChaveRSA) -> bytes:
        """ Método para geração de assinatura digital com o esquema PKCS1-v1_5 (RFC 8017)

        Args:
            msg (bytes): Mensagem a ser assinada
            privkey (bytes): Chave privada (PEM)

        Returns:
            bytes: Assinatura digital
        """

        private_key = serialization.load_pem_private_key(privkey.chave_bytes, password=None)
        signature = private_key.sign(
            msg,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        return signature

    @staticmethod
    def cifraRSAAES_OAEP(pubkey: ChaveRSA, msg: bytes) -> bytes:
        """ Método para cifragem de uma mensagem no esquema de cifragem RSAAES_OAEP

        Args:
            pubkey (bytes): Chave pública RSA no formato PEM
            msg (bytes): Mensagem a ser cifrada

        Returns:
            bytes: Mensagem cifrada
        """

        pub_key = serialization.load_pem_public_key(
            pubkey.chave_bytes
        )

        cipher = pub_key.encrypt(msg,
                                 padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                              label=None))
        return cipher

    @staticmethod
    def geraHMAC_SHA256(key: bytes, msg: bytes) -> bytes:
        """ Método para geração de resumo HMAC-SHA256

        Args:
            key (bytes): Chave para a geração do resumo
            msg (bytes): Mensagem a ser resumida

        Returns:
            bytes: Resumo criptográfico
        """
        return hmac.new(key, msg, hashlib.sha256).digest()

    @staticmethod
    def verificaHMAC_SHA256(key: bytes, msg: bytes, resumo: bytes) -> bool:
        """ Método para verificação de HMAC-SHA256

        Args:
            key (bytes): Chave para o resumo criptográfico
            msg (bytes): Mensagem a ser resumida
            resumo (bytes): Resumo criptográfico a ser verificado

        Returns:
            bool: Resultado da comparação
        """
        return CriptoDAF.geraHMAC_SHA256(key, msg) == resumo

    @staticmethod
    def geraResumoSHA256(msg: bytes) -> bytes:
        """ Método para geração de resumo criptográfico SHA-256

        Args:
            msg (bytes): Mensagem a ser resumida
        Returns:
            bytes: Resumo criptográfico
        """
        return hashlib.sha256(msg).digest()

    @staticmethod
    def verificaResumoSHA256(msg: bytes, resumo: bytes) -> bytes:
        """ Método para verificação de SHA-256
        Args:
            msg (bytes): Mensagem a ser resumida
            resumo (bytes): Resumo a ser verificado

        Returns:
            bytes: Resultado da comparação
        """
        return CriptoDAF.geraResumoSHA256(msg) == resumo

    @staticmethod
    def geraNumeroAleatorio(len: int) -> bytes:
        """Método para geração de bytes aleatórios

        Args:
            len (int): Número de bytes a serem gerados

        Returns:
            bytes: Bytes gerados aleatóriamente
        """
        rand = bytearray(random.getrandbits(8) for i in range(len))
        return rand
