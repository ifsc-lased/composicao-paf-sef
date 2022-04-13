import datetime
import json

import jwt
import requests
from flask import jsonify, request
from lxml import etree
from sqlalchemy import desc

from app import app, db, paf
from app.controllers.sefController import SefController
from app.models.daf import Daf
from app.models.temp import Temp
from app.utils.labels import get_res_daf

ws_sef = SefController()
temp = Temp()


# registro
@app.route('/passo_registrar_ini_sef', methods=['POST'])
def passo_registrar_ini_sef():
    token = request.values.get('token')

    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        res = ws_sef.inicio_registro(daf)
        res_sef_ini = res[1].text
        res_sef_ini_xml = etree.fromstring(res_sef_ini)
        ped_sef_ini = res[0]
        resultado = res_sef_ini_xml.find('.//xMotivo').text
        if res_sef_ini_xml.find('.//cStat').text == '1000' and res_sef_ini_xml.find('.//tkDesafio') is not None:
            token = res_sef_ini_xml.find('.//tkDesafio').text
            temp.set("token_registrar_ini_sef", token)
        else:
            erro = True
        pedido = {"texto": ped_sef_ini, "tipo": "xml"}
        resposta = {"texto": res_sef_ini, "tipo": "xml"}
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


@app.route('/passo_registrar_ini_daf', methods=['POST'])
def passo_registrar_ini_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    res_id = 0
    try:
        ped_daf_ini = paf.iniciarRegistro(token)
        res_daf_ini = paf.enviar_mensagem(ped_daf_ini)
        res_daf_ini_json = json.loads(res_daf_ini)
        if res_daf_ini_json['res'] == 0:
            token = res_daf_ini_json['jwt']

        pedido = {"texto": ped_daf_ini, "tipo": "json"}
        resposta = {"texto": res_daf_ini, "tipo": "json"}
        resultado = get_res_daf(res_daf_ini_json["res"])
        res_id = res_daf_ini_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_registrar_ini_daf_fake', methods=['POST'])
def passo_registrar_ini_daf_fake():
    token = temp.get("token_registrar_ini_sef")
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    res_id = 0
    try:
        ped_daf_ini = paf.iniciarRegistro(token)
        res_daf_ini = paf.enviar_mensagem(ped_daf_ini)
        res_daf_ini_json = json.loads(res_daf_ini)
        if res_daf_ini_json['res'] == 0:
            token = res_daf_ini_json['jwt']

        pedido = {"texto": ped_daf_ini, "tipo": "json"}
        resposta = {"texto": res_daf_ini, "tipo": "json"}
        resultado = get_res_daf(res_daf_ini_json["res"])
        res_id = res_daf_ini_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_registrar_conf_sef', methods=['POST'])
def passo_registrar_conf_sef():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        res = ws_sef.confirmar_registro(daf, token)
        res_sef_conf = res[1].text
        res_sef_conf_xml = etree.fromstring(res_sef_conf)
        ped_sef_conf = res[0]
        resultado = res_sef_conf_xml.find('.//xMotivo').text
        if res_sef_conf_xml.find('.//cStat').text == '1001':
            token = res_sef_conf_xml.find('.//tkChaves').text
        else:
            erro = True
        pedido = {"texto": ped_sef_conf, "tipo": "xml"}
        resposta = {"texto": res_sef_conf, "tipo": "xml"}
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


@app.route('/passo_chave_paf', methods=['POST'])
def passo_chave_paf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        payload = jwt.decode(token, verify=False)
        chavepaf = payload['chp']
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
        daf.chave_paf = chavepaf

        db.session.commit()
        pedido = {"texto": "Token recebido: " + token, "tipo": "texto"}
        resposta = {"texto": "Chave PAF regrada pela SEF no registro: " + chavepaf, "tipo": "texto"}
        resultado = "Chave armazenada com sucesso"
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_registrar_conf_daf', methods=['POST'])
def passo_registrar_conf_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    res_id = 0
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        ped_daf_conf = paf.confirmarRegistro(token)[0]
        res_daf_conf = paf.enviar_mensagem(ped_daf_conf)
        res_daf_conf_json = json.loads(res_daf_conf)

        if res_daf_conf_json['res'] == 0:
            daf.data_registro = datetime.datetime.now().strftime("%Y-%m-%d")
            daf.data_remocao = ""
            daf.situacao = 1
            daf.estado = "pronto"
            db.session.commit()

        pedido = {"texto": ped_daf_conf, "tipo": "json"}
        resposta = {"texto": res_daf_conf, "tipo": "json"}
        resultado = get_res_daf(res_daf_conf_json["res"])
        res_id = res_daf_conf_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


# remover
@app.route('/passo_remover_ini_sef', methods=['POST'])
def passo_remover_ini_sef():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        res = ws_sef.remover_registro(daf, "Justificativa informada pelo contribuinte")
        res_sef_ini = res[1].text
        res_sef_ini_xml = etree.fromstring(res_sef_ini)
        ped_sef_ini = res[0]
        resultado = res_sef_ini_xml.find('.//xMotivo').text
        if res_sef_ini_xml.find('.//cStat').text == '1000':
            token = res_sef_ini_xml.find('.//tkDesafio').text
            temp.set("token_remover_ini_sef", token)
        else:
            erro = True
        pedido = {"texto": ped_sef_ini, "tipo": "xml"}
        resposta = {"texto": res_sef_ini, "tipo": "xml"}
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


@app.route('/passo_remover_ini_daf', methods=['POST'])
def passo_remover_ini_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    res_id = 0
    try:

        ped_daf_ini = paf.removerRegistro(token)
        res_daf_ini = paf.enviar_mensagem(ped_daf_ini)
        res_daf_ini_json = json.loads(res_daf_ini)
        if res_daf_ini_json['res'] == 0:
            token = res_daf_ini_json['jwt']

        pedido = {"texto": ped_daf_ini, "tipo": "json"}
        resposta = {"texto": res_daf_ini, "tipo": "json"}
        resultado = get_res_daf(res_daf_ini_json["res"])
        res_id = res_daf_ini_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_remover_ini_daf_fake', methods=['POST'])
def passo_remover_ini_daf_fake():
    token = temp.get("token_remover_ini_sef")
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    try:

        ped_daf_ini = paf.removerRegistro(token)
        res_daf_ini = paf.enviar_mensagem(ped_daf_ini)
        res_daf_ini_json = json.loads(res_daf_ini)
        if res_daf_ini_json['res'] == 0:
            token = res_daf_ini_json['jwt']

        pedido = {"texto": ped_daf_ini, "tipo": "json"}
        resposta = {"texto": res_daf_ini, "tipo": "json"}
        resultado = get_res_daf(res_daf_ini_json["res"])
        res_id = res_daf_ini_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_remover_conf_sef', methods=['POST'])
def passo_remover_conf_sef():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        res = ws_sef.confirmar_remover(daf, token)
        res_sef_conf = res[1].text
        res_sef_conf_xml = etree.fromstring(res_sef_conf)
        ped_sef_conf = res[0]
        resultado = res_sef_conf_xml.find('.//xMotivo').text
        if res_sef_conf_xml.find('.//cStat').text == '1002':
            token = res_sef_conf_xml.find('.//tkEvento').text
        else:
            erro = True
        pedido = {"texto": ped_sef_conf, "tipo": "xml"}
        resposta = {"texto": res_sef_conf, "tipo": "xml"}
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


@app.route('/passo_remover_conf_daf', methods=['POST'])
def passo_remover_conf_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    res_id = 0
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        ped_daf_conf = paf.confirmarRemocaoRegistro(token)
        res_daf_conf = paf.enviar_mensagem(ped_daf_conf)
        res_daf_conf_json = json.loads(res_daf_conf)

        if res_daf_conf_json['res'] == 0:
            daf.data_remocao = datetime.datetime.now().strftime("%Y-%m-%d")
            daf.data_registro = None
            daf.situacao = 0
            daf.estado = "inativo"
            db.session.commit()
        pedido = {"texto": ped_daf_conf, "tipo": "json"}
        resposta = {"texto": res_daf_conf, "tipo": "json"}
        resultado = get_res_daf(res_daf_conf_json["res"])
        res_id = res_daf_conf_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


# modo de operação
@app.route('/passo_modoop_ini_sef', methods=['POST'])
def passo_modoop_ini_sef():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
        if daf.modo_operacao == 1:
            novo_modo = 0
        else:
            novo_modo = 1

        res = ws_sef.alterar_modo_op(daf, novo_modo, "JUSTIFICATIVA PARA ALTERAR O MODO DE OPERACAO")
        res_sef_ini = res[1].text
        res_sef_ini_xml = etree.fromstring(res_sef_ini)
        ped_sef_ini = res[0]
        resultado = res_sef_ini_xml.find('.//xMotivo').text
        if res_sef_ini_xml.find('.//cStat').text == '1000':
            token = res_sef_ini_xml.find('.//tkDesafio').text
            # temp.set("token_modoop_ini_sef", token)
        else:
            erro = True
        pedido = {"texto": ped_sef_ini, "tipo": "xml"}
        resposta = {"texto": res_sef_ini, "tipo": "xml"}
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


@app.route('/passo_modoop_ini_daf', methods=['POST'])
def passo_modoop_ini_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    res_id = 0
    try:

        ped_daf_ini = paf.alterarModoOperacao(token)
        res_daf_ini = paf.enviar_mensagem(ped_daf_ini)
        res_daf_ini_json = json.loads(res_daf_ini)
        if res_daf_ini_json['res'] == 0:
            token = res_daf_ini_json['jwt']
        pedido = {"texto": ped_daf_ini, "tipo": "json"}
        resposta = {"texto": res_daf_ini, "tipo": "json"}
        resultado = get_res_daf(res_daf_ini_json["res"])
        res_id = res_daf_ini_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_modoop_conf_sef', methods=['POST'])
def passo_modoop_conf_sef():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        res = ws_sef.confirmar_modo_op(daf, token)
        res_sef_conf = res[1].text
        res_sef_conf_xml = etree.fromstring(res_sef_conf)
        ped_sef_conf = res[0]
        resultado = res_sef_conf_xml.find('.//xMotivo').text
        if res_sef_conf_xml.find('.//cStat').text == '1006':
            token = res_sef_conf_xml.find('.//tkModoOperacao').text
        else:
            erro = True
        pedido = {"texto": ped_sef_conf, "tipo": "xml"}
        resposta = {"texto": res_sef_conf, "tipo": "xml"}
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


@app.route('/passo_modoop_conf_daf', methods=['POST'])
def passo_modoop_conf_daf():
    token = request.values.get('token')
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    res_id = 0
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()

        ped_daf_conf = paf.confirmarAlterarModoOperacao(token)
        res_daf_conf = paf.enviar_mensagem(ped_daf_conf)
        res_daf_conf_json = json.loads(res_daf_conf)

        if res_daf_conf_json['res'] == 0:
            daf.modo_operacao = not daf.modo_operacao
            db.session.commit()

        pedido = {"texto": ped_daf_conf, "tipo": "json"}
        resposta = {"texto": res_daf_conf, "tipo": "json"}
        resultado = get_res_daf(res_daf_conf_json["res"])
        res_id = res_daf_conf_json['res']
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)
