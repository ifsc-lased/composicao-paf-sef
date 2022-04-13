import json

import jwt
from authlib.jose import jwk
from typing import Union

from .cripto_daf import ChaveRSA


class JWTDAF:

    def __init__(self):
        pass

    @staticmethod
    def geraJWT(payload: dict, alg: str, privkey: Union[ChaveRSA, bytes], pubkey: ChaveRSA = None) -> str:
        """ Método para geração de tokens JWT

        Args:
            payload (dict): Dicionário python com as chaves e valores do Payload do token
            alg (str): Algoritmo de assinatura digital
            privkey (bytes): Chave privada para geração da assinatura digital no formato PEM
            pubkey (bytes, optional): Chave pública para geração do header do token no formato PEM. Se não for passado como padrão, tem None com padrão.

        Returns:
            str: Token JWT gerado
        """
        tokenJWT = None
        if pubkey is None:
            if alg == 'RS256':
                header = {'typ': 'JWT', 'alg': alg}
                tokenJWT = jwt.encode(
                    payload, privkey.chave_bytes, algorithm=alg, headers=header).decode('utf-8')
            elif alg == 'HS256':
                header = {'typ': 'JWT', 'alg': alg}
                tokenJWT = jwt.encode(
                    payload, bytes.fromhex(privkey), algorithm=alg, headers=header).decode('utf-8')
            else:
                raise Exception(
                    "Algoritmo de assinatura digital não suportado")
        else:
            if alg == 'RS256':
                key_jwk = jwk.dumps(pubkey.chave_bytes, kty='RSA')
                header = {'jwk': key_jwk}
                tokenJWT = jwt.encode(
                    payload, privkey.chave_bytes, algorithm='RS256', headers=header).decode('utf-8')
            else:
                raise Exception(
                    "Algoritmo de assinatura digital não suportado")
        return tokenJWT

    @staticmethod
    def getJWTHeader(token: str) -> dict:
        """ Método para retorno do header do token JWT

        Args:
            token (str): Token JWT

        Returns:
            dict: Header do token JWT
        """

        header = jwt.get_unverified_header(token)
        return header

    @staticmethod
    def get_chave_pub_jwk(jwk: str) -> dict:
        chave_publica_ex = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk, separators=(',', ':')))
        return chave_publica_ex

    @staticmethod
    def verificaJWT(tokenJWT: str, pubkey: ChaveRSA, alg: str) -> dict:
        """ Método para verificação de tokens JWT

        Args:
            tokenJWT (str): Token JWT a ser verificado
            pubkey (bytes): Chave pública par da chave privada que gerou a assinatura do token JWT
            alg (str): Algoritmo de assinatura digital

        Returns:
            dict: Payload do token JWT
        """
        try:
            payload = jwt.decode(tokenJWT, pubkey,
                                 algorithms=alg, verify=True)
            return payload
        except jwt.exceptions.InvalidSignatureError:
            return False
        except jwt.exceptions.InvalidAlgorithmError:
            return False
