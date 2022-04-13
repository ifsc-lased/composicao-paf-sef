import datetime
import os
import random
import re
from pytz import timezone
from decimal import Decimal
from pathlib import Path

from app import app
from app import db
from app.controllers.dafController import autorizar_dfe
from app.controllers.sefazRSController import SefazController
from app.models.empresa import Empresa
from app.models.fornecedorSistema import FornecedorSistema
from app.models.nfce import Nfce
from app.models.sef import Sef
from app.models.vendaItem import VendaItem
from app.utils.formats import get_all
from app.utils.formats import ifnull
from app.utils.geradores import gera_nome_max
from app.utils.xml_utils import exportar_xml
from flask import session, render_template, Response, redirect, request
from lxml import etree
from pynfe.entidades.cliente import Cliente as NFCliente
from pynfe.entidades.emitente import Emitente as NFEmitente
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.processamento.serializacao import SerializacaoXML, SerializacaoQrcode
from pynfe.utils.flags import CODIGO_BRASIL
from sqlalchemy import desc, func
from weasyprint import HTML, CSS


@app.route('/listarNfce')
def listar_nfce():
    data = get_all(Nfce.query.order_by(desc(Nfce.dh_emi)).all(), Nfce.columns,
                   [{"btn": "vis", "rota": "xmlNFCe"}, {"btn": "pdf", "rota": "danfeNFCe"},
                    {"btn": "env", "rota": "enviarNFCe"}, {"btn": "ret", "rota": "xmlRetSefaz"}])
    return render_template('listagem.html', data=data, columns=Nfce.columns, title='Notas',
                           add='', gerar='', g2='', label='Venda')


@app.route('/selecionarNfce/<int:id>', methods=['GET'])
def selecionar_nfce(id=0):
    data = get_all(Nfce.query.order_by(desc(Nfce.dh_emi)).filter_by(venda_fk_id=id), Nfce.columns,
                   [{"btn": "vis", "rota": "xmlNFCe"}, {"btn": "pdf", "rota": "danfeNFCe"},
                    {"btn": "env", "rota": "enviarNFCe"}, {"btn": "ret", "rota": "xmlRetSefaz"}])
    return render_template('listagem.html', data=data, columns=Nfce.columns, title='Notas',
                           add='', gerar='', label='Venda')


@app.route('/danfeNFCe/<int:id>', methods=['GET'])
def danfce_xml(id=0):
    nota = Nfce.query.filter_by(id=id).first()
    qnt_itens = len(VendaItem.query.filter_by(venda_fk_id=nota.venda_fk_id).all())
    height = 126 + (4 * qnt_itens)
    if nota.tp_emis == 9:
        height = height + 9

    css = Path(os.path.join(app.root_path, 'static', 'danfe.css')).read_text()
    css = css.replace('\n', '').replace("/*altura da página*/", "height: " + str(height) + "mm;")

    pdf = HTML('http://' + request.host + '/geradanfce/' + str(id)).write_pdf(
        stylesheets=[CSS(string=css)])
    if nota.status is not None:
        cod = str(nota.status)
    else:
        cod = "contingencia"
    return Response(
        pdf,
        mimetype="application/pdf",
        headers={"Content-disposition":
                     "attachment; filename=danfce-" + str(nota.chave_acesso) + "-" + cod + ".pdf"})


@app.route('/geradanfce/<int:nfce_id>', methods=['GET'])
def geradanfce(nfce_id):
    nota = Nfce.query.filter_by(id=nfce_id).first()
    xml = etree.fromstring(ifnull(nota.xml_distribuicao, nota.xml))

    xml_ide = xml.find(".//{http://www.portalfiscal.inf.br/nfe}ide")
    xml_emit = xml.find(".//{http://www.portalfiscal.inf.br/nfe}emit")
    xml_dest = xml.find(".//{http://www.portalfiscal.inf.br/nfe}dest")
    xml_total = xml.find(
        ".//{http://www.portalfiscal.inf.br/nfe}total/{http://www.portalfiscal.inf.br/nfe}ICMSTot")
    xml_pag = xml.find(
        ".//{http://www.portalfiscal.inf.br/nfe}pag/{http://www.portalfiscal.inf.br/nfe}detPag")
    xml_inf_adic = xml.find(".//{http://www.portalfiscal.inf.br/nfe}infAdic")
    qr_code_link = xml.find(
        ".//{http://www.portalfiscal.inf.br/nfe}infNFeSupl/{http://www.portalfiscal.inf.br/nfe}qrCode").text
    qr_code_site = xml.find(
        ".//{http://www.portalfiscal.inf.br/nfe}infNFeSupl/{http://www.portalfiscal.inf.br/nfe}urlChave").text

    ecnpj = xml_emit.find(".//{http://www.portalfiscal.inf.br/nfe}CNPJ").text
    empresa_cnpj = '{}.{}.{}/{}-{}'.format(ecnpj[:2], ecnpj[2:5], ecnpj[5:8], ecnpj[8:12], ecnpj[12:14])
    empresa_ie = xml_emit.find("{http://www.portalfiscal.inf.br/nfe}IE").text
    empresa_nome = xml_emit.find("{http://www.portalfiscal.inf.br/nfe}xNome").text
    xml_ender_emit = xml_emit.find("{http://www.portalfiscal.inf.br/nfe}enderEmit")

    serie = xml_ide.find("{http://www.portalfiscal.inf.br/nfe}serie").text
    serie = '{:0>3}'.format(serie)
    nf = xml_ide.find("{http://www.portalfiscal.inf.br/nfe}nNF").text
    nf = '{:0>9}'.format(nf)
    dhemit = xml_ide.find("{http://www.portalfiscal.inf.br/nfe}dhEmi").text.replace("T", " ")
    dhemit = datetime.datetime.strptime(dhemit, '%Y-%m-%d %X%z').astimezone(timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")
    chave = xml.find(".//{http://www.portalfiscal.inf.br/nfe}infNFe").get("Id")[3:]
    chave = '{} {} {} {} {} {} {} {} {} {} {} '.format(chave[:4], chave[4:8], chave[8:12], chave[12:16], chave[16:20],
                                                       chave[20:24], chave[24:28], chave[28:32], chave[32:36],
                                                       chave[36:40], chave[40:44])
    nota = {
        "nf": nf,
        "serie": serie,
        "dh_emi": dhemit,
        "chave": chave,
        "inf_cpl": xml_inf_adic.find("{http://www.portalfiscal.inf.br/nfe}infCpl").text,
        "tpambi": xml_ide.find("{http://www.portalfiscal.inf.br/nfe}tpAmb").text,
        "tpemis": xml_ide.find("{http://www.portalfiscal.inf.br/nfe}tpEmis").text
    }

    xml_prot = xml.find(".//{http://www.portalfiscal.inf.br/nfe}protNFe")
    if xml_prot is not None:
        prot = xml_prot.find(".//{http://www.portalfiscal.inf.br/nfe}nProt").text
        data_aut = xml_prot.find(".//{http://www.portalfiscal.inf.br/nfe}dhRecbto").text.replace("-03:00",
                                                                                                 "").replace("T", " ")
        nota["protocolo"] = '{} {} {}'.format(prot[:3], prot[3:13], prot[13:15])
        nota["data_aut"] = datetime.datetime.strptime(data_aut, '%Y-%m-%d %X').strftime("%d/%m/%Y %H:%M:%S")

    if xml_inf_adic.find("{http://www.portalfiscal.inf.br/nfe}infAdFisco") is not None:
        nota['ad_fisco'] = xml_inf_adic.find("{http://www.portalfiscal.inf.br/nfe}infAdFisco").text

        empresa = {
            "nome": empresa_nome,
            "ie": empresa_ie,
            "cnpj": empresa_cnpj,
            "end": xml_ender_emit.find("{http://www.portalfiscal.inf.br/nfe}xLgr").text + ", " + xml_ender_emit.find(
                "{http://www.portalfiscal.inf.br/nfe}nro").text + ", " + xml_ender_emit.find(
                "{http://www.portalfiscal.inf.br/nfe}xBairro").text + ", " + xml_ender_emit.find(
                "{http://www.portalfiscal.inf.br/nfe}xMun").text + ", " + xml_ender_emit.find(
                "{http://www.portalfiscal.inf.br/nfe}UF").text
        }
    else:
        nota['ad_fisco'] = "***NFC-e IRREGULAR - EMISSÃO SEM DAF***"
        empresa = {
            "nome": empresa_nome + " ***NFC-e IRREGULAR - EMISSÃO SEM DAF***",
            "ie": empresa_ie,
            "cnpj": empresa_cnpj,
            "end": "***NFC-e IRREGULAR - EMISSÃO SEM DAF***"
        }

    venda = {
        "valor_pago": str(round(Decimal(xml_pag.find("{http://www.portalfiscal.inf.br/nfe}vPag").text), 2)).replace(".",
                                                                                                                    ","),
        "valor_total": str(round(Decimal(xml_total.find("{http://www.portalfiscal.inf.br/nfe}vProd").text), 2)).replace(
            ".", ","),
        "desconto": str(round(Decimal(xml_total.find("{http://www.portalfiscal.inf.br/nfe}vDesc").text), 2)).replace(
            ".", ","),
        "tributos": str(round(Decimal(xml_total.find("{http://www.portalfiscal.inf.br/nfe}vTotTrib").text), 2)).replace(
            ".", ","),
        "frete": str(round(Decimal(xml_total.find("{http://www.portalfiscal.inf.br/nfe}vFrete").text), 2)).replace(".",
                                                                                                                   ",")
    }
    ccpf = xml_dest.find("{http://www.portalfiscal.inf.br/nfe}CPF").text
    cliente_cpf = '{}.{}.{}-{}'.format(ccpf[:3], ccpf[3:6], ccpf[6:9], ccpf[9:11])

    cliente = {
        "cpf": cliente_cpf,
        "nome": xml_dest.find("{http://www.portalfiscal.inf.br/nfe}xNome").text.replace(
            "HOMOLOGACAO - SEM VALOR FISCAL", ""),
        "endereco": empresa["end"]
    }

    itens = []
    dets = xml.findall(".//{http://www.portalfiscal.inf.br/nfe}det")
    for i in dets:
        prod = i.find("{http://www.portalfiscal.inf.br/nfe}prod")
        codigo = '{:0>6}'.format(prod.find("{http://www.portalfiscal.inf.br/nfe}cProd").text)
        itens.append({
            "cod": codigo,
            "nome": prod.find("{http://www.portalfiscal.inf.br/nfe}xProd").text.replace(
                "HOMOLOGACAO - SEM VALOR FISCAL", ""),
            "qnt": str(round(Decimal(prod.find("{http://www.portalfiscal.inf.br/nfe}qCom").text))),
            "un": prod.find("{http://www.portalfiscal.inf.br/nfe}uCom").text,
            "vu": str(round(Decimal(prod.find("{http://www.portalfiscal.inf.br/nfe}vUnCom").text), 2)).replace(".",
                                                                                                               ","),
            "vt": str(round(Decimal(prod.find("{http://www.portalfiscal.inf.br/nfe}vProd").text), 2)).replace(".", ",")
        })

    venda["qnt_itens"] = len(itens)

    return render_template('danfe.html', empresa=empresa, url_qrcode=qr_code_link, venda=venda, nota=nota,
                           cliente=cliente, itens=itens, endereco_qrcode=qr_code_site)


@app.route('/xmlNFCe/<int:nfce_id>', methods=['GET'])
def visualizar_xml(nfce_id=0):
    nota = Nfce.query.filter_by(id=nfce_id).first()
    return Response(
        ifnull(nota.xml_distribuicao, nota.xml),
        mimetype="text/xml",
        headers={"Content-disposition":
                     "attachment; filename=" + nota.chave_acesso + "-nfce.xml"})


@app.route('/xmlRetSefaz/<int:nfce_id>', methods=['GET'])
def visualizar_xml_ret_sefaz(nfce_id=0):
    nota = Nfce.query.filter_by(id=nfce_id).first()
    if nota.ret_sefaz is not None:
        return Response(nota.ret_sefaz,
                        mimetype="text/xml",
                        headers={"Content-disposition":
                                     "attachment; filename=" + nota.chave_acesso + "-retorno-sefaz.xml"})


def iniciar_nfce(venda=None, max_nfc=False, off=False):
    if session.get("empresa") is None:
        from app.inicializacao import Inicializacao
        Inicializacao.set_login()

    empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
    cliente = venda.cliente
    itens = VendaItem.query.filter_by(venda_fk_id=venda.id).all()

    endereco = empresa.enderecos[0]
    nnf = db.session.query(func.max(Nfce.nnf)).scalar()
    nnf = ifnull(nnf, 1) + 1
    if max_nfc:
        nnf = random.randrange(100000000, 999999999)
    serie = 999 
    fone_emit = re.sub("([()-])", "", empresa.telefone_principal)

    uf = endereco.municipio.uf.sigla
    if empresa.ambiente == 1:
        homologacao = False
    else:
        homologacao = True

    # emitente
    emitente = NFEmitente(
        razao_social='NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL',
        nome_fantasia=empresa.nome,
        cnpj=empresa.cnpj,  # cnpj apenas números
        codigo_de_regime_tributario='1',  # 1 para simples nacional ou 3 para normal
        inscricao_estadual=empresa.inscricao_estadual_sc,  # numero de IE da empresa
        endereco_logradouro=endereco.endereco,
        endereco_numero=endereco.numero,
        endereco_bairro=endereco.bairro,
        endereco_municipio=endereco.municipio.nome,
        endereco_uf=endereco.municipio.uf.sigla,
        endereco_cep=endereco.cep,
        endereco_pais=CODIGO_BRASIL,
        endereco_telefone=fone_emit
    )

    # cliente
    cli_end = cliente.enderecos[0]
    dest = NFCliente(
        razao_social=cliente.nome + ' HOMOLOGACAO - SEM VALOR FISCAL',
        tipo_documento='CPF',  # CPF ou CNPJ
        email=cliente.email,
        numero_documento=cliente.cpf,  # numero do cpf ou cnpj
        indicador_ie=9,  # 9=Não contribuinte
        endereco_logradouro=cli_end.endereco,
        endereco_numero=cli_end.numero,
        endereco_complemento=cli_end.complemento,
        endereco_bairro=cli_end.bairro,
        endereco_municipio=cli_end.municipio.nome,
        endereco_uf=cli_end.municipio.uf.sigla,
        endereco_cep=cli_end.cep,
        endereco_pais=CODIGO_BRASIL,
        endereco_telefone=cliente.get_telefone()
    )
    tp_emis = empresa.tp_emis
    if off:
        tp_emis = 9
    # Nota Fiscal
    nota_fiscal = NotaFiscal(
        emitente=emitente,
        cliente=dest,
        uf=uf.upper(),
        natureza_operacao='VENDA',  # venda, compra, transferência, devolução, etc
        forma_pagamento=0,  # 0=Pagamento à vista; 1=Pagamento a prazo; 2=Outros.
        tipo_pagamento=1,
        modelo=65,  # 55=NF-e; 65=NFC-e
        serie=str(serie),
        numero_nf=nnf,  # Número do Documento Fiscal.
        data_emissao=datetime.datetime.now(),
        data_saida_entrada=datetime.datetime.now(),
        tipo_documento=1,  # 0=entrada; 1=saida
        municipio=str(endereco.municipio.codigo_ibge),  # Código IBGE do Município
        tipo_impressao_danfe=4,
        # 0=Sem geração de DANFE;1=DANFE normal, Retrato;2=DANFE normal Paisagem;3=DANFE Simplificado;4=DANFE NFC-e;
        forma_emissao=tp_emis,  # 1=Emissão normal (não em contingência);
        cliente_final=1,  # 0=Normal;1=Consumidor final;
        indicador_destino=1,
        indicador_presencial=1,
        finalidade_emissao='1',  # 1=NF-e normal;2=NF-e complementar;3=NF-e de ajuste;4=Devolução de mercadoria.
        processo_emissao='0',  # 0=Emissão de NF-e com aplicativo do contribuinte;
        transporte_modalidade_frete=9,  # 9=Sem Ocorrência de Transporte.
    )

    # Produto
    tta = 0
    total = 0
    for i in range(0, len(itens)):
        produto = itens[i].produto
        item = itens[i]

        nota_fiscal.adicionar_produto_servico(
            codigo=str(produto.id),  # id do produto
            descricao=produto.nome + ' HOMOLOGACAO - SEM VALOR FISCAL',
            ncm=str(produto.ncm),
            cfop=produto.cfop,
            unidade_comercial=produto.unidade,
            ean=produto.cean,
            ean_tributavel=produto.cean,
            quantidade_comercial=round(Decimal(item.quantidade), 2),  # 12 unidades
            valor_unitario_comercial=round(Decimal(produto.valor_unitario), 2),  # preço unitário
            valor_total_bruto=round(Decimal(item.valor_item), 2),  # preço total
            unidade_tributavel=produto.unidade,
            quantidade_tributavel=round(Decimal(item.quantidade), 2),
            valor_unitario_tributavel=round(Decimal(produto.valor_unitario), 2),
            ind_total=1,
            icms_modalidade=produto.icms_modalidade,
            icms_origem=0,
            icms_csosn=produto.icms_csosn,
            pis_modalidade=produto.icms_cst,
            cofins_modalidade=produto.icms_cst,
            valor_tributos_aprox=round(Decimal(produto.valor_unitario * item.quantidade * produto.perc_trib), 2)
        )
        tta = tta + Decimal(produto.valor_unitario * item.quantidade * produto.perc_trib)
        total = total + Decimal(produto.valor_unitario * item.quantidade)

    nota_fiscal.totais_tributos_aproximado = round(tta, 2)
    nota_fiscal.totais_icms_total_nota = round(Decimal(venda.valor_total), 2)
    nota_fiscal.totais_icms_total_desconto = round(abs(total - Decimal(venda.valor_total)), 2)
    if max_nfc:
        nota_fiscal.totais_tributos_aproximado = 9999999999999.99
        nota_fiscal.totais_icms_total_nota = 9999999999999.99
        nota_fiscal.totais_icms_total_desconto = 9999999999999.99
        nota_fiscal.totais_icms_base_calculo = 9999999999999.99
        nota_fiscal.totais_icms_total = 9999999999999.99
        nota_fiscal.totais_icms_desonerado = 9999999999999.99
        nota_fiscal.totais_fcp_destino = 9999999999999.99
        nota_fiscal.totais_icms_inter_destino = 9999999999999.99
        nota_fiscal.totais_icms_remetente = 9999999999999.99
        nota_fiscal.totais_fcp = 9999999999999.99
        nota_fiscal.totais_icms_st_base_calculo = 9999999999999.99
        nota_fiscal.totais_icms_st_total = 9999999999999.99
        nota_fiscal.totais_fcp_st = 9999999999999.99
        nota_fiscal.totais_fcp_st_ret = 9999999999999.99
        nota_fiscal.totais_icms_total_produtos_e_servicos = 9999999999999.99
        nota_fiscal.totais_icms_total_frete = 9999999999999.99
        nota_fiscal.totais_icms_total_seguro = 9999999999999.99
        nota_fiscal.totais_icms_total_ii = 9999999999999.99
        nota_fiscal.totais_icms_total_ipi = 9999999999999.99
        nota_fiscal.totais_icms_total_ipi_dev = 9999999999999.99
        nota_fiscal.totais_icms_pis = 9999999999999.99
        nota_fiscal.totais_icms_cofins = 9999999999999.99
        nota_fiscal.totais_icms_outras_despesas_acessorias = 9999999999999.99

    # responsável técnico
    tec = FornecedorSistema.query.first()
    nota_fiscal.adicionar_responsavel_tecnico(
        cnpj=tec.cnpj,
        contato=tec.pessoaJuridica.nome,
        email=tec.pessoaJuridica.email,
        fone=tec.pessoaJuridica.telefone_principal
    )

    nota_fiscal.informacoes_complementares_interesse_contribuinte = 'Cod. Venda = ' + str(
        venda.id)

    # # serialização
    serializador = SerializacaoXML(_fonte_dados, homologacao=homologacao)
    nfce = serializador.exportar(limpar=True)
    ide = nfce.getchildren()[0].getchildren()[0]
    emit = nfce.getchildren()[0].getchildren()[1]
    emit.find('./xNome').text = empresa.nome
    vp = ide.find('./verProc')
    vp.text = "PAF projeto DAF 1.0"
    if max_nfc:
        vp.text = gera_nome_max(20)
        etree.SubElement(ide, 'dhCont').text = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + '-03:00'
        etree.SubElement(ide, 'xJust').text = gera_nome_max(256)
        ide.find('./natOp').text = gera_nome_max(60)
    if off:
        etree.SubElement(ide, 'dhCont').text = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime(
            '%Y-%m-%dT%H:%M:%S') + '-03:00'
        etree.SubElement(ide, 'xJust').text = "MOTIVO PARA ENTRAR EM CONTINGENCIA"

    return nfce, empresa, nnf


def incorporar_frag_daf(nfce, aut_daf):
    # adiciona o elemento infAdic e infAdFisco com a autorização DAF
    # busca o elemento infRespTec p/ add o infAd antes
    tec = nfce.getchildren()[0].find('infRespTec')
    # verifica se já existe a tag de informações complementares
    info_ad = nfce.getchildren()[0].find('infAdic')
    if info_ad is None:
        info_ad = etree.Element('infAdic')
        tec.addprevious(info_ad)
    etree.SubElement(info_ad, 'infAdFisco').text = aut_daf
    return nfce


def assinar_nfce(nfce, certificado, senha):
    a1 = AssinaturaA1(certificado, senha)
    xml = a1.assinar(nfce)
    return xml


def add_qrcode(xml, empresa):
    return SerializacaoQrcode().gerar_qrcode(empresa.get_csc_id(), empresa.csc, xml)


@app.route('/gerarNota/<int:venda>', methods=['GET'])
def gerar_nfe(venda=None, sem_daf=False):
    nfce, empresa, nnf = iniciar_nfce(venda)

    if not sem_daf:
        aut_daf = autorizar_dfe(exportar_xml(nfce, False),
                                venda.funcionario_pdv.pdv.id_pdv)  # retorna token jwt da autenticação do daf
        nfce = incorporar_frag_daf(nfce, aut_daf)

    certificado, senha = empresa.get_certificado()
    xml = assinar_nfce(nfce, certificado, senha)

    # gera e adiciona o qrcode no xml NT2015/003
    xml_com_qrcode = add_qrcode(xml, empresa)

    xmlfinal_str = exportar_xml(xml_com_qrcode, False)  # nota final em str

    obj_nfce = Nfce(xml_com_qrcode.getchildren()[0].get('Id')[3:], empresa.tp_emis, empresa.ambiente, venda, nnf,
                    xmlfinal_str)

    if empresa.tp_emis == 1:
        obj_nfce = enviar_nfce(obj_nfce)

    return obj_nfce


@app.route
@app.route('/enviarNFCe/<int:nfce_id>', methods=['GET'])
def renviar_nfce(nfce_id=0):
    nota = Nfce.query.filter_by(id=nfce_id).first()
    nota = enviar_nfce(nota)
    db.session.commit()
    return redirect("/listarNfce")


def enviar_nfce(nota=None):
    sefazrs = SefazController(nota.xml)
    ret = sefazrs.processar_nfe()

    nota.ret_sefaz = exportar_xml(ret, False)
    cstat = ret.find('cStat').text
    cstat_nota = ret.find(
        '{http://www.portalfiscal.inf.br/nfe}protNFe/{http://www.portalfiscal.inf.br/nfe}infProt/{http://www.portalfiscal.inf.br/nfe}cStat').text
    nota.status = cstat_nota
    if cstat == '104':  # processada
        if cstat_nota == '100':
            nota.situacao = 1  # autorizada
            nota.protocolo = ret.find(
                '{http://www.portalfiscal.inf.br/nfe}protNFe/{http://www.portalfiscal.inf.br/nfe}infProt/{http://www.portalfiscal.inf.br/nfe}nProt').text
            nota.xml_distribuicao = exportar_xml(
                sefazrs.get_xml_distribuicao(ret.find('{http://www.portalfiscal.inf.br/nfe}protNFe')), False)
            # envia p/ sef
            envia_distribuicao_sef(nota.protocolo, nota.xml_distribuicao)
        else:
            nota.situacao = 4  # rejeitada
    return nota


def envia_distribuicao_sef(protocolo, xml):
    enviados = len(Sef.query.filter_by(protocolo_autorizacao=protocolo).all())
    if enviados < 1:
        nota_sef = Sef(protocolo, xml)
        db.session.add(nota_sef)
        db.session.commit()
