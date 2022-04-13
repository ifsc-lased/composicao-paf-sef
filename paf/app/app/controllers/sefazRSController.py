import datetime
import random

from lxml import etree
from pynfe.processamento.assinatura import AssinaturaA1

from app.utils.labels import get_xmotivo


class SefazController:

    def __init__(self, completo):
        self.xml = etree.fromstring(completo)
        self.ver_aplic = 'SVRS-DAF'
        self.protocolo = self.gerar_protocolo()
        self.versao = None
        self.tp_amb = None
        self.chave = None
        self.nsmap = None

    def gerar_protocolo(self):
        return datetime.datetime.now().strftime("%y%m%d%H%M%f")[:-1]

    def processar_nfe(self):
        inf_nfe = self.xml.find('{http://www.portalfiscal.inf.br/nfe}infNFe')
        self.tp_amb = inf_nfe.find(
            '{http://www.portalfiscal.inf.br/nfe}ide/{http://www.portalfiscal.inf.br/nfe}tpAmb').text
        self.chave = inf_nfe.get("Id")[3:]
        self.versao = inf_nfe.get("versao")
        self.nsmap = inf_nfe.nsmap

        ret = etree.Element('retConsReciNFe', {'versao': self.versao}, self.nsmap)

        tp_amb = etree.Element('tpAmb', None, self.nsmap)
        tp_amb.text = self.tp_amb
        ret.append(tp_amb)

        ver_aplic = etree.Element('verAplic', None, self.nsmap)
        ver_aplic.text = self.ver_aplic
        ret.append(ver_aplic)

        n_rec = etree.Element('nRec', None, self.nsmap)
        n_rec.text = str(random.randint(10000000, 99999999)) + str(random.randint(1000000, 9999999))
        ret.append(n_rec)

        ret_c_stat = etree.Element('cStat', None, self.nsmap)
        ret_c_stat.text = '104'
        ret.append(ret_c_stat)

        ret_x_motivo = etree.Element('xMotivo', None, self.nsmap)
        ret_x_motivo.text = 'Lote processado'
        ret.append(ret_x_motivo)

        c_uf = etree.Element('cUF', None, self.nsmap)
        c_uf.text = inf_nfe.find(
            '{http://www.portalfiscal.inf.br/nfe}ide/{http://www.portalfiscal.inf.br/nfe}cUF').text
        ret.append(c_uf)

        ret_dh_recbto = etree.Element('dhRecbto', None, self.nsmap)
        ret_dh_recbto.text = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S-03:00")
        ret.append(ret_dh_recbto)

        ret.append(self.prot_nfce())

        return ret

    def prot_nfce(self):

        c_si_nfe = 4  # Situação da NF-e: 1=Uso autorizado; 2=Uso denegado; 3=NF-e Cancelada; 4= Rejeitada;
        c_stat = 999  # erro desconhecido

        inf_nfe = self.xml.find('{http://www.portalfiscal.inf.br/nfe}infNFe')
        inf_adic = inf_nfe.find('{http://www.portalfiscal.inf.br/nfe}infAdic')
        inf_ad_fisco = inf_adic.find('{http://www.portalfiscal.inf.br/nfe}infAdFisco')
        token = inf_ad_fisco

        if inf_ad_fisco is None:
            c_stat = 937  # novo código de rejeição p/ quando não tem a autorização DAF
        else:
            c_stat = 100

        prot_nfe = etree.Element('protNFe', {'versao': self.versao}, self.nsmap)
        inf_prot = etree.Element('infProt', {'Id': 'ID' + self.protocolo}, self.nsmap)

        tp_amb = etree.Element('tpAmb', None, self.nsmap)
        tp_amb.text = self.tp_amb
        inf_prot.append(tp_amb)

        ver_aplic = etree.Element('verAplic', None, self.nsmap)
        ver_aplic.text = self.ver_aplic
        inf_prot.append(ver_aplic)

        ch_nfe = etree.Element('chNFe', None, self.nsmap)
        ch_nfe.text = self.chave
        inf_prot.append(ch_nfe)

        dh_recbto = etree.Element('dhRecbto', None, self.nsmap)
        dh_recbto.text = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S-03:00")
        inf_prot.append(dh_recbto)

        nprot = etree.Element('nProt', None, self.nsmap)
        nprot.text = self.protocolo
        inf_prot.append(nprot)

        dig_val = etree.Element('digVal', None, self.nsmap)
        dig_val.text = self.xml.find(
            '{http://www.w3.org/2000/09/xmldsig#}Signature/{http://www.w3.org/2000/09/xmldsig#}SignedInfo/{http://www.w3.org/2000/09/xmldsig#}Reference/{http://www.w3.org/2000/09/xmldsig#}DigestValue').text
        inf_prot.append(dig_val)

        cstat = etree.Element('cStat', None, self.nsmap)
        cstat.text = str(c_stat)
        inf_prot.append(cstat)

        x_motivo = etree.Element('xMotivo', None, self.nsmap)
        x_motivo.text = get_xmotivo(c_stat)
        inf_prot.append(x_motivo)

        prot_nfe.append(inf_prot)

        certificado, senha = self.get_certificado_sefazrsfake()

        a1 = AssinaturaA1(certificado, senha)
        prot_nfe_assinado = a1.assinar(prot_nfe)

        return prot_nfe_assinado

    def get_xml_distribuicao(self, prot):
        nfe_proc = etree.Element('nfeProc', {'versao': self.versao}, self.nsmap)
        nfe_proc.append(self.xml)
        nfe_proc.append(prot)

        return nfe_proc

    def get_certificado_sefazrsfake(self):
        import json
        f = open('configuracoes.json')
        data = json.load(f)
        f.close()
        return data["certificado_sefazrsfake"]["certificado"], data["certificado_sefazrsfake"]["senha"]
