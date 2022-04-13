import datetime
import json

from flask import render_template, redirect
from lxml import etree
from sqlalchemy import desc

from app import app, db, paf
from app.controllers.sefController import SefController
from app.models.daf import Daf
from app.models.empresa import Empresa
from app.models.fornecedorSistema import FornecedorSistema
from app.utils.base64URL_daf import Base64URLDAF
from app.utils.cripto_daf import CriptoDAF
from app.utils.formats import get_all
from app.utils.labels import get_res_daf
from app.utils.xml_utils import exportar_xml

ws_sef = SefController()


@app.route('/listarDaf')
def listar_daf():
    data = get_all(Daf.query.all(), Daf.columns,
                   [{"btn": "atl", "rota": "atualizarDaf"},
                    {"btn": "reset", "rota": "padraoFabrica"},
                    {"btn": "regdaf", "rota": "registrarDAF"},
                    {"btn": "remdaf", "rota": "removerRegistroDAF"},
                    {"btn": "altMod", "rota": "alterarModo"}])
    return render_template('listagem.html', data=data, columns=Daf.columns, title="DAF",
                           add='/addDaf', gerar='', label='DAF')


@app.route('/addDaf')
def add_daf():
    msg = paf.consultarInformacoes()
    resposta = paf.enviar_mensagem(msg)
    resjson = json.loads(resposta)

    dafs = Daf.query.filter_by(id_daf=resjson['daf']).all()
    if len(dafs) < 1:
        daf = Daf(resjson['daf'], resjson['mop'], resjson['vsb'], resjson['hsb'], resjson['fab'], resjson['mdl'],
                  resjson['cnt'], resjson['crt'], resjson['est'], 'jau', resjson['mxd'], len(resjson['rts']),
                  "",
                  str(resjson['als']))

        db.session.add(daf)
    else:
        # atualiza as informações do DAF no PAF e consulta DAF na SEF
        daf = atualizacao_daf(dafs[0], False, True, resjson)

    db.session.commit()

    return redirect("/listarDaf")


@app.route('/atualizarDaf/<int:id>', methods=['GET'])
def atualizar_daf(id=0):
    daf = Daf.query.filter_by(id=id).first()
    daf = atualizacao_daf(daf, True, True)
    db.session.commit()
    return redirect("/listarDaf")


def consultar_daf():
    msg = paf.consultarInformacoes()
    return paf.enviar_mensagem(msg)


def consultar_dispositivo(id_daf):
    res_sef_cons = etree.fromstring(ws_sef.consultar_dispositivo(id_daf)[1].text)
    res_sef = {"ultimaVersaoSB": 0,
               "dataRegistro": "",
               "cnpjContribuinte": "",
               "cnpjResponsavel": "",
               "idCSRT": 0,
               "xSituacao": "INATIVO"}
    if res_sef_cons.find('.//cStat').text == '1000':
        x_situacao = res_sef_cons.find('.//xSituacao')
        if x_situacao is not None:
            x_situacao = x_situacao.text
            ultima_versao_sb = res_sef_cons.find('.//ultimaVersaoSB').text
            data_registro = res_sef_cons.find('.//dataRegistro').text
            cnpj_contribuinte = res_sef_cons.find('.//cnpjContribuinte').text
            cnpj_responsavel = res_sef_cons.find('.//cnpjResponsavel').text
            id_csrt = int(res_sef_cons.find('.//idCSRT').text)

            res_sef = {"ultimaVersaoSB": int(ultima_versao_sb),
                       "dataRegistro": data_registro,
                       "cnpjContribuinte": cnpj_contribuinte,
                       "cnpjResponsavel": cnpj_responsavel,
                       "idCSRT": id_csrt,
                       "xSituacao": x_situacao}
    else:
        print(res_sef_cons.find('.//xMotivo').text)

    return res_sef


def atualizacao_daf(daf, consulta_daf=False, consulta_sef=False, infos_daf=None, infos_sef=None):
    if consulta_daf:
        res_daf = consultar_daf()
        infos_daf = json.loads(res_daf)

    if infos_daf is not None:
        daf.id_daf = infos_daf['daf']
        daf.modo_operacao = infos_daf['mop']
        daf.versao_sb = infos_daf['vsb']
        daf.hash_sb = infos_daf['hsb']
        daf.cnpj_fabricante = infos_daf['fab']
        daf.modelo = infos_daf['mdl']
        daf.contador = infos_daf['cnt']
        daf.certificado_sef = infos_daf['crt']
        daf.estado = infos_daf['est'].lower()
        daf.max_dfe = infos_daf['mxd']
        daf.num_dfe = len(infos_daf['rts'])

        if daf.estado == 'inativo' and not daf.data_extravio:
            daf.situacao = 0

        if daf.estado == 'pronto' and not daf.data_extravio:
            daf.situacao = 1

        if daf.estado == 'bloqueado' and not daf.data_extravio:
            daf.situacao = 6

        if daf.data_extravio:
            daf.situacao = 2

    if consulta_sef:
        res_sef = consultar_dispositivo(daf.id_daf)
        infos_sef = res_sef

    if infos_sef is not None:
        ext_sef = False
        reg_sef = False
        if infos_sef["xSituacao"] == "REGULAR" or infos_sef["xSituacao"] == "EM REGISTRO":
            reg_sef = True
        if infos_sef["xSituacao"] == "INATIVO":
            reg_sef = False
        if infos_sef["xSituacao"] == "EXTRAVIADO":
            ext_sef = True

        daf.situacao = -1

        # DAF sem registro ativo
        if not reg_sef and not ext_sef and daf.estado == 'inativo':
            daf.situacao = 0

        # Registro ok na sef, no daf e no paf
        if reg_sef and daf.estado == 'pronto' and not daf.data_extravio:
            daf.situacao = 1
            daf.data_registro = infos_sef["dataRegistro"]

        if infos_sef["ultimaVersaoSB"] > daf.versao_sb:
            daf.situacao = 3

        if daf.estado == "bloqueado" or daf.num_dfe == daf.max_dfe:
            daf.situacao = 6

        # Problemas no registro
        if (daf.estado == 'pronto' and not reg_sef) \
                or (daf.estado == 'inativo' and reg_sef) \
                or (reg_sef and ((infos_sef["cnpjContribuinte"] != Empresa.query.first().pessoaJuridica.cnpj \
                                  or infos_sef["cnpjResponsavel"] != FornecedorSistema.cnpj \
                                  or infos_sef["idCSRT"] != FornecedorSistema.id_csrt))) \
                or (not ext_sef and daf.data_extravio is not None):
            daf.situacao = 5

        # DAF extraviado na sef e extraviado ou nao no paf
        if ext_sef:
            daf.situacao = 2

        if infos_sef["xSituacao"] == "INREGULAR":
            daf.situacao = 4

    return daf


@app.route('/padraoFabrica/<int:id>', methods=['GET'])
def padrao_fabrica(id=0):
    daf = Daf.query.filter_by(id=id).first()

    msg = paf.padrao_fabrica("RSA", "1")
    res_daf = json.loads(paf.enviar_mensagem(msg))
    if res_daf["res"] == 0:
        daf.data_extravio = None
        daf.data_registro = None
        daf.data_remocao = None
        daf.situacao = 0
        daf.modo_operacao = 0
        daf.contador = 0
        daf.num_dfe = 0
        db.session.commit()

    return redirect('/listarDaf')


@app.route('/padraoFabricaNovo/<int:id>', methods=['GET'])
def padrao_fabrica_novo(id=0):
    daf = Daf.query.filter_by(id=id).first()

    msg = paf.padrao_fabrica_novo_id()
    res_daf = json.loads(paf.enviar_mensagem(msg))
    if res_daf["res"] == 0:
        daf.data_extravio = None
        daf.data_registro = None
        daf.data_remocao = None
        daf.situacao = 0
        daf.modo_operacao = 0
        daf.contador = 0
        daf.num_dfe = 0
        db.session.commit()

    return redirect('/listarDaf')


@app.route('/registrarDAF/<int:id>', methods=['GET'])
def registrar_daf(id=0):
    daf = Daf.query.filter_by(id=id).first()
    if not daf.data_registro and not daf.data_extravio:

        res_sef_ini = etree.fromstring(ws_sef.inicio_registro(daf)[1].text)
        if res_sef_ini.find('.//cStat').text == '1000':
            token = res_sef_ini.find('.//tkDesafio').text
            ped_daf_ini = paf.iniciarRegistro(token)
            res_daf_ini = json.loads(paf.enviar_mensagem(ped_daf_ini))
            if res_daf_ini['res'] == 0:
                res_sef_conf = etree.fromstring(ws_sef.confirmar_registro(daf, res_daf_ini['jwt'])[1].text)
                if res_sef_conf.find('.//cStat').text == '1001':
                    tk_chaves = res_sef_conf.find('.//tkChaves').text
                    ped_daf_conf, chave_paf = paf.confirmarRegistro(tk_chaves)

                    with open('app/daf/resources/chave-paf.str', 'w') as file:
                        file.write(Base64URLDAF.base64URLDecode(chave_paf).hex())

                    res_daf_conf = json.loads(paf.enviar_mensagem(ped_daf_conf))
                    if res_daf_conf['res'] == 0:
                        daf.data_registro = datetime.datetime.now().strftime("%Y-%m-%d")
                        daf.data_remocao = ""
                        daf.chave_paf = chave_paf
                        daf.situacao = 1
                        daf = atualizacao_daf(daf, True)
                        db.session.commit()
                    resposta = get_res_daf(res_daf_conf['res'])
                else:
                    resposta = res_sef_conf.find('.//xMotivo').text
            else:
                resposta = get_res_daf(res_daf_ini['res'])

        else:
            resposta = res_sef_ini.find('.//xMotivo').text
        print(resposta)
    else:
        print("DAF já registrado ou Extraviado")
    return redirect('/listarDaf')


@app.route('/removerRegistroDAF/<int:id>', methods=['GET'])
def remover_registrar_daf(id=0):
    daf = Daf.query.filter_by(id=id).first()
    if daf.data_registro and not daf.data_extravio:

        res_sef_ini = etree.fromstring(
            ws_sef.remover_registro(daf, "Justificativa que depois eu pergunto p/ user")[1].text)
        if res_sef_ini.find('.//cStat').text == '1000':
            token = res_sef_ini.find('.//tkDesafio').text
            ped_daf_ini = paf.removerRegistro(token)
            res_daf_ini = json.loads(paf.enviar_mensagem(ped_daf_ini))
            if res_daf_ini['res'] == 0:
                res_sef_conf = etree.fromstring(ws_sef.confirmar_remover(daf, res_daf_ini['jwt']).text)
                if res_sef_conf.find('.//cStat').text == '1002':
                    tk_evento = res_sef_conf.find('.//tkEvento').text
                    ped_daf_conf = paf.confirmarRemocaoRegistro(tk_evento)
                    res_daf_conf = json.loads(paf.enviar_mensagem(ped_daf_conf))
                    if res_daf_conf['res'] == 0:
                        daf.data_remocao = datetime.datetime.now().strftime("%Y-%m-%d")
                        daf.data_registro = None
                        daf.situacao = 0
                        daf = atualizacao_daf(daf, True)
                        db.session.commit()
                    resposta = get_res_daf(res_daf_conf['res'])
                else:
                    resposta = res_sef_conf.find('.//xMotivo').text
            else:
                resposta = get_res_daf(res_daf_ini['res'])

        else:
            resposta = res_sef_ini.find('.//xMotivo').text
        print(resposta)
    else:
        print("DAF sem registro ou extraviado")

    return redirect('/listarDaf')


@app.route('/alterarModo/<int:id>', methods=['GET'])
def alterar_modo_daf(id=0):
    daf = Daf.query.filter_by(id=id).first()
    if daf.modo_operacao == 1:
        novo_modo = 0
    else:
        novo_modo = 1

    if daf.data_registro and not daf.data_extravio:

        res_sef_ini = etree.fromstring(
            ws_sef.alterar_modo_op(daf, novo_modo,
                                   "JUSTIFICATIVA PARA ALTERAR O MODO DE OPERACAO")[1].text)

        if res_sef_ini.find('.//cStat').text == '1000':
            token = res_sef_ini.find('.//tkDesafio').text
            ped_daf_ini = paf.alterarModoOperacao(token)
            res_daf_ini = json.loads(paf.enviar_mensagem(ped_daf_ini))
            if res_daf_ini['res'] == 0:
                res_sef_conf = etree.fromstring(ws_sef.confirmar_modo_op(daf, res_daf_ini['jwt']).text)
                if res_sef_conf.find('.//cStat').text == '1006':
                    tk_modo = res_sef_conf.find('.//tkModoOperacao').text
                    ped_daf_conf = paf.confirmarAlterarModoOperacao(tk_modo)
                    res_daf_conf = json.loads(paf.enviar_mensagem(ped_daf_conf))
                    if res_daf_conf['res'] == 0:
                        daf.modo_operacao = novo_modo
                        daf = atualizacao_daf(daf, True)
                        db.session.commit()
                    resposta = get_res_daf(res_daf_conf['res'])
                else:
                    resposta = res_sef_conf.find('.//xMotivo').text
            else:
                resposta = get_res_daf(res_daf_ini['res'])

        else:
            resposta = res_sef_ini.find('.//xMotivo').text
    else:
        print("DAF sem registro ou extraviado")
    return redirect('/listarDaf')


def ext_essencial(completo):
    xml = etree.fromstring(completo)
    infnfe = xml.find('{http://www.portalfiscal.inf.br/nfe}infNFe')
    completo = exportar_xml(infnfe).replace(" xmlns=\"http://www.portalfiscal.inf.br/nfe\"", "")
    es = etree.Element('infNFe', infnfe.attrib, infnfe.nsmap)
    es.append(infnfe.find('{http://www.portalfiscal.inf.br/nfe}ide'))
    es.append(infnfe.find('{http://www.portalfiscal.inf.br/nfe}total'))
    return exportar_xml(es).replace(" xmlns=\"http://www.portalfiscal.inf.br/nfe\"", ""), completo


def autorizar_dfe(completo, idpdv):
    print("Autorizando um DFe")
    msg = paf.solicitarAutenticacao()
    resposta = paf.enviar_mensagem(msg)
    res = json.loads(resposta)
    daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

    if res['res'] == 0:
        nnc = res['nnc']
        essencial, completo = ext_essencial(completo)
        completo = CriptoDAF.geraResumoSHA256(completo.encode('utf-8'))
        msg = paf.autorizarDFE(nnc, essencial, completo, idpdv, Base64URLDAF.base64URLDecode(daf.chave_paf))
        print("Saindo do PAF:", msg)
        token_autorizacao = paf.enviar_mensagem(msg)
        print("Recebido pelo PAF:", token_autorizacao)
        print()
        t = json.loads(token_autorizacao)
        if t['res'] == 0:
            return t['jwt']
    raise Exception('ERRO AO AUTORIZAR DF-e')
