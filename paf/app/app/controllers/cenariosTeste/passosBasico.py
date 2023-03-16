import json

import requests
from flask import jsonify, request
from lxml import etree
from sqlalchemy import desc

from app import app, db, paf
from app.controllers.dafController import atualizacao_daf
from app.controllers.sefController import SefController
from app.models.daf import Daf
from app.models.temp import Temp
from app.utils.labels import get_res_daf

ws_sef = SefController()
temp = Temp()


@app.route('/passo_cancelar_processo', methods=['POST'])
def passo_cancelar_processo():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        token = request.values.get('token')
        msg = paf.cancelar_processo()
        res_daf = paf.enviar_mensagem(msg)
        res_daf_json = json.loads(res_daf)
        pedido = {"texto": msg, "tipo": "json"}
        resposta = {"texto": res_daf, "tipo": "json"}
        resultado = get_res_daf(res_daf_json["res"])
        res_id = res_daf_json["res"]
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_padraofab9997', methods=['POST', 'GET'])
def passo_padraofab9997():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        msg = paf.padrao_fabrica_novo_id()
        res_daf = paf.enviar_mensagem(msg)
        res_daf_json = json.loads(res_daf)
        pedido = {"texto": msg, "tipo": "json"}
        resposta = {"texto": res_daf, "tipo": "json"}
        resultado = get_res_daf(res_daf_json["res"])
        res_id = res_daf_json["res"]
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_padraofab', methods=['POST', 'GET'])
def passo_padraofab():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        msg = paf.padrao_fabrica()
        res_daf = paf.enviar_mensagem(msg)
        res_daf_json = json.loads(res_daf)
        pedido = {"texto": msg, "tipo": "json"}
        resposta = {"texto": res_daf, "tipo": "json"}
        resultado = get_res_daf(res_daf_json["res"])
        res_id = res_daf_json["res"]
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_consultar_daf', methods=['POST'])
def passo_consultar_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
        msg = paf.consultarInformacoes()
        res_daf = paf.enviar_mensagem(msg)
        res_daf_json = json.loads(res_daf)
        resultado = get_res_daf(res_daf_json["res"])
        res_id = res_daf_json["res"]
        if res_id == 0:
            daf = atualizacao_daf(daf, False, False, res_daf_json)
            db.session.add(daf)
            db.session.commit()
        resposta = {"texto": res_daf, "tipo": "json"}
        pedido = {"texto": msg, "tipo": "json"}
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)

@app.route('/passo_consultar_autorizacoes_daf', methods=['POST'])
def passo_consultar_autorizacoes_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    ini = 1
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
        fim = daf.num_dfe
        msg = paf.consultarAutorizacoes(ini,fim)
        res_daf = paf.enviar_mensagem(msg)
        res_daf_json = json.loads(res_daf)
        resultado = get_res_daf(res_daf_json["res"])
        res_id = res_daf_json["res"]
        if res_id == 0:
            daf = atualizacao_daf(daf, False, False, None, None, res_daf_json)
        resposta = {"texto": res_daf, "tipo": "json"}
        pedido = {"texto": msg, "tipo": "json"}
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)

@app.route('/passo_consultar_daf_sef', methods=['POST'])
def passo_consultar_daf_sef():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
        res = ws_sef.consultar_dispositivo(daf.id_daf)
        res_sef_str = res[1].text
        res_sef_xml = etree.fromstring(res_sef_str)
        ped_sef = res[0]

        res_sef = {"ultimaVersaoSB": 0
            , "dataRegistro": ""
            , "modeloDaf": ""
            , "cnpjFabricante": ""
            , "cnpjContribuinte": ""
            , "cnpjResponsavel": ""
            , "idCSRT": 0
            , "xSituacao": "INATIVO"
                   }
        resultado = res_sef_xml.find('.//xMotivo').text
        if res_sef_xml.find('.//cStat').text == '1000':
            x_situacao = res_sef_xml.find('.//xSituacao')
            if x_situacao is not None:
                x_situacao = x_situacao.text
                ultima_versao_sb = res_sef_xml.find('.//ultimaVersaoSB').text
                data_registro = res_sef_xml.find('.//dataRegistro').text
                modelo_daf = res_sef_xml.find('.//modeloDaf').text
                cnpj_fabricante = res_sef_xml.find('.//cnpjFabricante').text
                cnpj_contribuinte = res_sef_xml.find('.//cnpjContribuinte').text
                cnpj_responsavel = res_sef_xml.find('.//cnpjResponsavel').text
                id_csrt = int(res_sef_xml.find('.//idCSRT').text)

                res_sef = {"ultimaVersaoSB": int(ultima_versao_sb)
                    , "dataRegistro": data_registro
                    , "modeloDaf": modelo_daf
                    , "cnpjFabricante": cnpj_fabricante
                    , "cnpjContribuinte": cnpj_contribuinte
                    , "cnpjResponsavel": cnpj_responsavel
                    , "idCSRT": id_csrt
                    , "xSituacao": x_situacao
                           }
        else:
            raise Exception(resultado)

        daf = atualizacao_daf(daf, False, False, None, res_sef)
        db.session.add(daf)
        db.session.commit()
        pedido = {"texto": ped_sef, "tipo": "xml"}
        resposta = {"texto": res_sef_str, "tipo": "xml"}
    except requests.exceptions.ConnectionError:
        res_id = 1
        erro = True
        resultado = "Erro ao conectar com a SEF"
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)
