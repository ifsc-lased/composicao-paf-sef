import json

from app.utils.base64URL_daf import Base64URLDAF
from app.utils.cripto_daf import CriptoDAF, ChaveRSA
from app.utils.imagem import ImagemSB
from app.utils.jwt_daf import JWTDAF


class SEF:
    """ Esta classe simula o papel da SEF no escopo do projeto DAF. Pode ser utilizada para auxiliar no desenvolvimento do PAF junto do DAF-pi
    """

    global path_sef_priv
    path_sef_priv = 'app/daf/resources/sef-priv.pem'

    global mop

    @staticmethod
    def apagarAutorizacaoRetida(aut):
        """ Autoriza a remoção de uma autorização retida. O PAF poderia mandar apenas o idAut e não o token JWT gerado pelo DAF. Neste caso, o método recebe o token JWT apenas para que não seja necessário filtrar o idAut anteriormente

        Args:
            token (str): resposta do DAF para o pedido de autorização de DFe

        Returns:
            [str]: resposta da SEF ao pedido do PAF
        """
    
        msg = {}
        msg['msg'] = 5
        msg['aut'] = aut

        with open('app/daf/resources/chave-sef.str') as file:
            chSEF = file.read()
        chSEF = bytes.fromhex(chSEF)
        autApag = CriptoDAF.geraHMAC_SHA256(
            chSEF, aut.encode('utf-8'))
        msg['apg'] = Base64URLDAF.base64URLEncode(autApag)

        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def atualizarCertificado():
        """ Gera um novo certificado digital para o DAF-pi

        Returns:
            [str]: resposta da SEF ao pedido do PAF
        """

        def geraCertificado(privkey: ChaveRSA, pubkey: ChaveRSA, organizationName: str, organizationUnitName: str,
                            countryName: str, stateName: str, localityName: str, commonName: str) -> bytes:
            from cryptography import x509
            from cryptography.hazmat.backends import default_backend
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives import serialization
            from cryptography.x509.oid import NameOID
            import datetime

            privkey = serialization.load_pem_private_key(
                privkey.chave_bytes, password=None)
            pubkey = serialization.load_pem_public_key(pubkey.chave_bytes)

            builder = x509.CertificateBuilder()
            builder = builder.subject_name(x509.Name([x509.NameAttribute(NameOID.ORGANIZATION_NAME, organizationName),
                                                      x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,
                                                                         organizationUnitName), x509.NameAttribute(
                    NameOID.COUNTRY_NAME, countryName), x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, stateName),
                                                      x509.NameAttribute(NameOID.LOCALITY_NAME, localityName),
                                                      x509.NameAttribute(NameOID.COMMON_NAME, commonName)]))

            builder = builder.issuer_name(x509.Name([x509.NameAttribute(NameOID.ORGANIZATION_NAME, organizationName),
                                                     x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,
                                                                        organizationUnitName), x509.NameAttribute(
                    NameOID.COUNTRY_NAME, countryName), x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, stateName),
                                                     x509.NameAttribute(NameOID.LOCALITY_NAME, localityName),
                                                     x509.NameAttribute(NameOID.COMMON_NAME, commonName)]))

            one_day = datetime.timedelta(1, 0, 0)
            builder = builder.not_valid_before(
                datetime.datetime.today() - one_day)
            builder = builder.not_valid_after(
                datetime.datetime.today() + (one_day * 365 * 10))

            builder = builder.serial_number(x509.random_serial_number())
            builder = builder.public_key(pubkey)

            cert = builder.sign(
                private_key=privkey, algorithm=hashes.SHA256(), backend=default_backend())

            return cert.public_bytes(serialization.Encoding.PEM)

        priv, pub = CriptoDAF.geraChaveRSA(2048)

        with open(path_sef_priv) as file:
            priv_atual = ChaveRSA(file.read())

        certificado = geraCertificado(
            priv_atual, pub, 'SEF', 'GESAC', 'BR', 'Santa Catarina', 'Florianopolis', 'sef.sc.gov.br')

        with open(path_sef_priv, 'w') as file:
            file.write(priv.chave_str)

        with open('app/daf/resources/sef-pub.pem', 'w') as file:
            file.write(pub.chave_str)

        with open('app/daf/resources/sef-cert.pem', 'w') as file:
            file.write(certificado.decode('utf-8'))

        cert = certificado.decode('utf-8')
        msg = {}
        msg['msg'] = 10
        msg['crt'] = cert

        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def alterarModoOperacao(modo_operacao):
        mop = modo_operacao
        nonce = CriptoDAF.geraNumeroAleatorio(16)
        payload = {'nnc': Base64URLDAF.base64URLEncode(nonce)}
        with open('app/daf/resources/chave-sef.str') as file:
            sef_priv = file.read()

        token = JWTDAF.geraJWT(payload, 'HS256', sef_priv)

        msg = {"msg": 12, 'jwt': token}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def confirmarAlteracaoModoOperacao(novo_modo):
        payload = {'mop': novo_modo}

        with open('app/daf/resources/chave-sef.str') as file:
            sef_priv = file.read()

        token = JWTDAF.geraJWT(payload, 'HS256', sef_priv)

        msg = {"msg": 13, 'jwt': token}
        return json.dumps(msg, separators=(',', ':'))

    @staticmethod
    def gera_novo_firmware():
        """ Gera um novo "firmware" para o DAF-pi. O papel da SEF nesse caso seria assinar o firmware recebido pelo fabricante do DAF e assina-lo. Este método engloba a geração e assinatura tanto da SEF quanto com a chave de ateste

        Returns:
            [bytes]: novo "firmware". A estrutura do binário é "versão + resumo do código + assinatura sef + assinatura ateste + código"
        """
        import secrets

        with open(path_sef_priv) as file:
            sef_priv = ChaveRSA(file.read())
        versao = 2
        versao = versao.to_bytes(2, byteorder='big')
        codigo = secrets.token_bytes(1024 * 4)

        ass = CriptoDAF.geraAssinaturaRSA_PKCS1_V1_5(versao + codigo, sef_priv)

        resumoCript = CriptoDAF.geraResumoSHA256(codigo)

        with open('app/daf/resources/ateste-priv.pem') as file:
            ateste_priv = ChaveRSA(file.read())

        ass_ateste = CriptoDAF.geraAssinaturaRSA_PKCS1_V1_5(versao + codigo, ateste_priv)
        blob = versao + resumoCript + ass + ass_ateste + codigo

        imagem = ImagemSB(raw_binario=blob, path_arquivos="app/daf/resources/imagem/sb")

        return blob
