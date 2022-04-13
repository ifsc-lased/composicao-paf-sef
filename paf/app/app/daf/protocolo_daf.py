import json

import jwt

from app.sef.sef import SEF
from app.utils.base64URL_daf import Base64URLDAF
from app.utils.cripto_daf import CriptoDAF


class ProtocoloDaf:

    def __init__(self, pdafcdc):
        self.pdafcdc = pdafcdc

    def enviar_mensagem(self, msg):
        ''' Envia a mensagem para o DAF por meio da classe PDAFCDC

        Returns:
            [json]: resposta do DAF ou -1 em caso de timeout
        '''
        resposta = self.pdafcdc.envia_mensagem(msg)
        if resposta is None:
            return json.dumps({"res": -1})
        else:
            return resposta

    @staticmethod
    def iniciarRegistro(tkDesafio):
        """ Gera uma mensagem de início do registro DAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {"msg": 1, 'jwt': tkDesafio}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def confirmarRegistro(token):
        """ Gera uma mensagem de confirmação do registro DAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        payload = jwt.decode(token, verify=False)
        chave_paf = payload['chp']

        msg = {"msg": 2, "jwt": token}
        return json.dumps(msg, separators=(',', ':')), chave_paf

    @staticmethod
    def solicitarAutenticacao():
        """ Gera uma mensagem solicitando autentitcação ao DAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {"msg": 3}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def autorizarDFE(nnc, essencial, completo, idpdv, chPAF):
        """ Gera uma mensagem de solicitação autorização de DF-e

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        respDes = CriptoDAF.geraHMAC_SHA256(
            chPAF, Base64URLDAF.base64URLDecode(nnc) + completo)

        payload = {}
        payload["msg"] = 4
        payload["fdf"] = Base64URLDAF.base64URLEncode(essencial.encode('utf-8'))
        payload["hdf"] = Base64URLDAF.base64URLEncode(completo)
        payload["pdv"] = idpdv
        payload["red"] = Base64URLDAF.base64URLEncode(respDes)

        return json.dumps(payload, separators=(',', ':'))

    @staticmethod
    def apagarAutorizacaoRetida(aut, apg):
        """ Gera uma mensagem de solicitação para apagar uma autorização retida na MT do DAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {}
        msg['msg'] = 5
        msg['aut'] = aut
        msg['apg'] = apg
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def consultarInformacoes():
        """ Gera mensagem de consultar informações do DAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {"msg": 8}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def padrao_fabrica():
        """ Gera um pedido de "reset" do DAF-pi. Essa mensagem é exclusiva do DAF-pi para auxiliar no desenvolvimento de PAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {}
        msg["msg"] = 9999
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def padrao_fabrica_novo_id():
        """ Gera um pedido de "reset" do DAF-pi gerando um novo idDaf. Essa mensagem é exclusiva do DAF-pi para auxiliar no desenvolvimento de PAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {}
        msg["msg"] = 9997
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def vai_para_violado():
        """ Gera um pedido de mudança de estado do DAF-pi para violado. Essa mensagem é exclusiva do DAF-pi  para auxiliar no desenvolvimento de PAF

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {"msg": 9998}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def descarregarRetidos(idAut):
        """ Gera mensagem de descarregar retidos

        Args:
            idAut (str): identificação da autorização

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        idAut = idAut
        msg = {"msg": 11, "aut": idAut}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def atualizarSB():
        """ Gera mensagem de atualizar SB

        Returns:
            [str]: mensagem a ser enviada ao DAF
        """
        msg = {"msg": 9}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def atualizarCertificado():
        """ Gera pedido de atualizar certificado digital

        Returns:
            [str]: resposta da SEF ao pedido
        """
        return SEF.atualizarCertificado()

    @staticmethod
    def removerRegistro(token):
        msg = {"msg": 6, 'jwt': token}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def cancelar_processo():
        msg = {"msg": 14}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def confirmarRemocaoRegistro(token):
        msg = {"msg": 7, "jwt": token}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def alterarModoOperacao(token):
        msg = {"msg": 12, 'jwt': token}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def confirmarAlterarModoOperacao(token):
        msg = {"msg": 13, 'jwt': token}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def mensagem_blob(cod):
        """ Gera uma mensagem com erros para enviar ao DAF. Pode ser usada para auxiliar no desenvolvimento do PAF

        Args:
            cod (int): código da mensagem

        Returns:
            [str]: mensagem que deve ser encaminhada ao DAF
        """
        msg = {"msg": cod, 'foo': 'foo', 'bar': 'bar', 'blob': 'blob'}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def gera_novo_firmware():
        """ Gera novo "firmware" pro DAF-pi

        Returns:
            [bytes]: resposta da SEF ao pedido
        """
        return SEF.gera_novo_firmware()
