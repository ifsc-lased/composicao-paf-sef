import requests
from flask import session
from lxml import etree
from pynfe.processamento.assinatura import AssinaturaA1

from app import endereco_sef
from app.models.empresa import Empresa
from app.models.fornecedorSistema import FornecedorSistema
from app.utils.xml_utils import exportar_xml


class SefController:

    def inicio_registro(self, daf):
        fornecedor = FornecedorSistema.query.first()
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedRegistro xmlns="" versao="1.00"><infRegistro></infRegistro></pedRegistro>""")

        inf = body.find(".//infRegistro")
        inf.set("Id", "DAF" + daf.id_daf)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = daf.id_daf

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        modelo = etree.SubElement(inf, 'modeloDaf')
        modelo.text = daf.modelo

        cnpj_fabricante = etree.SubElement(inf, 'cnpjFabricante')
        cnpj_fabricante.text = daf.cnpj_fabricante

        cnpj_contribuinte = etree.SubElement(inf, 'cnpjContribuinte')
        cnpj_contribuinte.text = empresa.cnpj

        cnpj_responsavel = etree.SubElement(inf, 'cnpjResponsavel')
        cnpj_responsavel.text = fornecedor.cnpj

        id_csrt = etree.SubElement(inf, 'idCSRT')
        id_csrt.text = str(fornecedor.id_csrt)

        modo_op = etree.SubElement(inf, 'modoOp')
        modo_op.text = str(daf.modo_operacao)

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><iniciarRegistro xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</iniciarRegistro></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFRegistroDispositivo/'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)

    def confirmar_registro(self, daf, token):
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedConfRegistro xmlns="" versao="1.00"><infConfRegistro></infConfRegistro></pedConfRegistro>""")

        inf = body.find(".//infConfRegistro")
        inf.set("Id", "DAF" + daf.id_daf)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = daf.id_daf

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        tk_aut = etree.SubElement(inf, 'tkAut')
        tk_aut.text = token

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><confirmarRegistro xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</confirmarRegistro></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFRegistroDispositivo/'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)

    def remover_registro(self, daf, justificativa):
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedRemRegistro xmlns="" versao="1.00"><infRemRegistro></infRemRegistro></pedRemRegistro>""")

        inf = body.find(".//infRemRegistro")
        inf.set("Id", "DAF" + daf.id_daf)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = daf.id_daf

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        x_just = etree.SubElement(inf, 'xJust')
        x_just.text = justificativa

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><removerRegistro xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</removerRegistro></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFRemocaoRegistro/'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)

    def confirmar_remover(self, daf, token):
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedConfRemRegistro xmlns="" versao="1.00"><infConfRemRegistro></infConfRemRegistro></pedConfRemRegistro>""")

        inf = body.find(".//infConfRemRegistro")
        inf.set("Id", "DAF" + daf.id_daf)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = daf.id_daf

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        tk_aut = etree.SubElement(inf, 'tkAut')
        tk_aut.text = token

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><confirmarRemoverRegistro xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</confirmarRemoverRegistro></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFRemocaoRegistro/'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)

    def consultar_dispositivo(self, id):
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedSituacao xmlns="" versao="1.00"><infSituacao></infSituacao></pedSituacao>""")

        inf = body.find(".//infSituacao")
        inf.set("Id", "DAF" + id)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = id

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><consultarDispositivo xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</consultarDispositivo></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFConsultaDispositivo/'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)

    def alterar_modo_op(self, daf, novo_modo, justificativa):
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedModoOperacao xmlns="" versao="1.00"><infModoOperacao></infModoOperacao></pedModoOperacao>""")

        inf = body.find(".//infModoOperacao")
        inf.set("Id", "DAF" + daf.id_daf)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = daf.id_daf

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        modo_op = etree.SubElement(inf, 'modoOp')
        modo_op.text = str(novo_modo)

        x_just = etree.SubElement(inf, 'xJust')
        x_just.text = justificativa

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><alterarModoOperacao xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</alterarModoOperacao></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFAlteracaoModoOperacao/'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)

    def confirmar_modo_op(self, daf, token):
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedConfModoOperacao xmlns="" versao="1.00"><infConfModoOperacao></infConfModoOperacao></pedConfModoOperacao>""")

        inf = body.find(".//infConfModoOperacao")
        inf.set("Id", "DAF" + daf.id_daf)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = daf.id_daf

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        tk_aut = etree.SubElement(inf, 'tkAut')
        tk_aut.text = token

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><confirmarModoOperacao xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</confirmarModoOperacao></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFAlteracaoModoOperacao/'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)

    def obter_resultado(self, daf, chaves):
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
        body = etree.fromstring(
            """<pedAutorizacao xmlns="" versao="1.00"><infAutorizacao></infAutorizacao></pedAutorizacao>""")

        inf = body.find(".//infAutorizacao")
        inf.set("Id", "DAF" + daf.id_daf)

        id_daf = etree.SubElement(inf, 'idDAF')
        id_daf.text = daf.id_daf

        id_paf = etree.SubElement(inf, 'idPAF')
        id_paf.text = empresa.id_paf

        for c in chaves:
            chave = etree.SubElement(inf, 'chDFe')
            chave.text = c

        certificado, senha = empresa.get_certificado()

        a1 = AssinaturaA1(certificado, senha)
        xml = a1.assinar(body)

        xml_str = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><obterResultadoAutorizacao xmlns="http://services.daf.lased.ifsc.edu.br/">""" \
                  + exportar_xml(xml) \
                  + """</obterResultadoAutorizacao></Body></Envelope>"""

        url = 'http://' + endereco_sef + '/DAFResultadoAutorizacao'
        headers = {'content-type': 'text/xml'}

        return xml_str, requests.post(url, data=xml_str, headers=headers)
