import json

import jwt
import requests
from flask import jsonify, request, redirect, session
from lxml import etree
from sqlalchemy import asc, desc
from sqlalchemy import or_, and_

from app import app, db, paf
from app.controllers.dafController import ext_essencial
from app.controllers.nfceController import iniciar_nfce, assinar_nfce, add_qrcode, enviar_nfce
from app.controllers.sefController import SefController
from app.controllers.vendaController import nova_venda, delete_venda
from app.models.daf import Daf
from app.models.empresa import Empresa
from app.models.nfce import Nfce
from app.models.temp import Temp
from app.models.venda import Venda
from app.utils.base64URL_daf import Base64URLDAF
from app.utils.cripto_daf import CriptoDAF
from app.utils.labels import get_res_daf, get_xmotivo
from app.utils.xml_utils import exportar_xml

ws_sef = SefController()
temp = Temp()


# autorização
@app.route('/passo_gerar_venda', methods=['GET', 'POST'])
def passo_gerar_venda0():
    return redirect("/passo_gerar_venda/0")


@app.route('/passo_gerar_venda/<int:qnt>', methods=['GET', 'POST'])
def passo_gerar_venda(qnt=0):
    token = request.values.get('token')

    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        venda = nova_venda(qnt)
        db.session.commit()
        pedido = {"texto": "Gerar nova venda com itens aleatórios", "tipo": "texto"}
        resposta = {"texto": "Gerada a venda " + str(venda.id) + " com o valor total R$" + str(venda.valor_total),
                    "tipo": "texto"}
        resultado = "Venda Gerada com sucesso"
        token = venda.id
    except BaseException as e:
        res_id = 1
        erro = True
        resultado = "Ocorreu um erro..."
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_emitir_nfce', methods=['POST'])
def passo_emitir_nfce():
    venda_id = int(request.values.get('token'))
    infos = ""
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        venda = Venda.query.filter_by(id=venda_id).first()
        nfce, empresa, nnf = iniciar_nfce(venda)
        infos_json = {"nfce": exportar_xml(nfce),
                      "empresa": empresa.pessoa_juridica_fk_id,
                      "nnf": nnf,
                      "venda_id": venda_id,
                      "retida": False}

        infos = json.dumps(infos_json)
        pedido = {"texto": "Iniciada emissão da NFC-e", "tipo": "texto"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = "NFC-e iniciada com sucesso"
    except BaseException as e:
        delete_venda(venda_id)
        res_id = 1
        erro = True
        resultado = "Ocorreu um erro..."
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_emitir_nfce_off', methods=['POST'])
def passo_emitir_nfce_off():
    venda_id = int(request.values.get('token'))
    infos = ""
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        venda = Venda.query.filter_by(id=venda_id).first()
        nfce, empresa, nnf = iniciar_nfce(venda, False, True)
        infos_json = {"nfce": exportar_xml(nfce),
                      "empresa": empresa.pessoa_juridica_fk_id,
                      "nnf": nnf,
                      "venda_id": venda_id}

        infos = json.dumps(infos_json)
        pedido = {"texto": "Iniciada emissão da NFC-e", "tipo": "texto"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = "NFC-e iniciada com sucesso"
    except BaseException as e:
        delete_venda(venda_id)
        res_id = 1
        erro = True
        resultado = "Ocorreu um erro..."
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_emitir_nfce_max', methods=['POST'])
def passo_emitir_nfce_max():
    venda_id = int(request.values.get('token'))
    infos = ""
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        venda = Venda.query.filter_by(id=venda_id).first()
        nfce, empresa, nnf = iniciar_nfce(venda, True)

        infos_json = {"nfce": exportar_xml(nfce),
                      "empresa": empresa.pessoa_juridica_fk_id,
                      "nnf": nnf,
                      "venda_id": venda_id}
        infos = json.dumps(infos_json)
        pedido = {"texto": "Iniciada emissão da NFC-e", "tipo": "texto"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = "NFC-e iniciada com sucesso"
    except BaseException as e:
        delete_venda(venda_id)
        res_id = 1
        erro = True
        resultado = "Ocorreu um erro..."
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_solicitar_autenticacao_daf', methods=['POST'])
def passo_solicitar_autenticacao_daf():
    infos = request.values.get('token')
    infos_json = json.loads(infos)

    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    try:
        ped_daf = paf.solicitarAutenticacao()
        res_daf = paf.enviar_mensagem(ped_daf)
        res_daf_json = json.loads(res_daf)
        if res_daf_json['res'] == 0:
            infos_json["nnc"] = res_daf_json["nnc"]

        infos = json.dumps(infos_json)
        pedido = {"texto": ped_daf, "tipo": "json"}
        resposta = {"texto": res_daf, "tipo": "json"}
        resultado = get_res_daf(res_daf_json["res"])
        res_id = res_daf_json["res"]
    except BaseException as e:
        delete_venda(infos_json["venda_id"])
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_autorizar_dfe', methods=['POST'])
def passo_autorizar_dfe():
    infos = request.values.get('token')
    infos_json = json.loads(infos)
    daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    erro = False
    try:
        venda = Venda.query.filter_by(id=infos_json["venda_id"]).first()
        essencial, completo = ext_essencial(infos_json["nfce"])

        res_completo = CriptoDAF.geraResumoSHA256(completo.encode('utf-8'))

        ped_daf = paf.autorizarDFE(infos_json['nnc'], essencial, res_completo,
                                   venda.funcionario_pdv.pdv.id_pdv, Base64URLDAF.base64URLDecode(daf.chave_paf))
        res_daf = paf.enviar_mensagem(ped_daf)
        res_daf_json = json.loads(res_daf)
        if res_daf_json['res'] == 0:
            daf.num_dfe = daf.num_dfe + 1
            daf.contador = daf.contador + 1
            if daf.num_dfe == daf.max_dfe:
                daf.situacao = 6
                daf.estado = "boqueado"
            db.session.commit()
            infos_json["token"] = res_daf_json["jwt"]
            infos = json.dumps(infos_json)
            pl = jwt.decode(res_daf_json["jwt"], algorithms=['HS256','RS256','ES384','ES256'], options={"verify_signature": False})
            pedido = {"antes": "Conjunto essencial: " + essencial + "\nDocumento completo: " + completo,
                      "texto": ped_daf,
                      "tipo": "json"}
            resposta = {"depois": "\nConteúdo do token JWT:", "depois_js": json.dumps(pl), "texto": res_daf,
                        "tipo": "json"}
        else:
            erro = True
        resultado = get_res_daf(res_daf_json["res"])
        res_id = res_daf_json["res"]
    except BaseException as e:
        delete_venda(infos_json["venda_id"])
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_incorporar_fragmento', methods=['POST'])
def passo_incorporar_fragmento():
    infos = request.values.get('token')
    infos_json = json.loads(infos)
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        nfce = etree.fromstring(infos_json["nfce"])
        tec = nfce.getchildren()[0].find('{http://www.portalfiscal.inf.br/nfe}infRespTec')
        # verifica se já existe a tag de informações complementares
        info_ad = nfce.getchildren()[0].find('{http://www.portalfiscal.inf.br/nfe}infAdic')
        if info_ad is None:
            info_ad = etree.Element('infAdic')
            tec.addprevious(info_ad)
        etree.SubElement(info_ad, 'infAdFisco').text = infos_json["token"]
        infos_json["nfce"] = exportar_xml(nfce)
        infos_json["retida"] = True
        infos = json.dumps(infos_json)
        pedido = {"texto": "Incorporar a autorização " + infos_json["token"], "tipo": "texto"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = "Fragmento incorporado com sucesso"
    except BaseException as e:
        delete_venda(infos_json["venda_id"])
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_assinar_dfe', methods=['POST'])
def passo_assinar_dfe():
    infos = request.values.get('token')
    infos_json = json.loads(infos)
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        nfce_antes = infos_json["nfce"]
        nfce = etree.fromstring(nfce_antes)
        if session.get("empresa") is None:
            from app.inicializacao import Inicializacao
            Inicializacao.set_login()

        certificado, senha = Empresa.query.filter_by(id=session.get("empresa")).first().get_certificado()
        nfce = assinar_nfce(nfce, certificado, senha)
        infos_json["nfce"] = exportar_xml(nfce)
        infos = json.dumps(infos_json)
        pedido = {"texto": nfce_antes, "tipo": "xml"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = "NFC-e assinada com sucesso"
    except BaseException as e:
        delete_venda(infos_json["venda_id"])
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_gerar_qrcode', methods=['POST'])
def passo_gerar_qrcode():
    infos = request.values.get('token')
    infos_json = json.loads(infos)
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        nfce_antes = infos_json["nfce"]
        nfce = etree.fromstring(nfce_antes)
        empresa = Empresa.query.filter_by(pessoa_juridica_fk_id=int(infos_json["empresa"])).first()
        nfce = add_qrcode(nfce, empresa)
        infos_json["nfce"] = exportar_xml(nfce)
        obj_nfce = Nfce(nfce.getchildren()[0].get('Id')[3:], empresa.tp_emis, empresa.ambiente,
                        Venda.query.filter_by(id=infos_json["venda_id"]).first(), infos_json["nnf"],
                        infos_json["nfce"])
        obj_nfce.retida_daf = infos_json['retida']
        db.session.add(obj_nfce)
        db.session.commit()
        infos_json["nfce_id"] = obj_nfce.id
        infos = json.dumps(infos_json)
        pedido = {"texto": nfce_antes, "tipo": "xml"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = "QRCode adicionado com sucesso"
    except BaseException as e:
        delete_venda(infos_json["venda_id"])
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_gerar_qrcode_off', methods=['POST'])
def passo_gerar_qrcode_off():
    infos = request.values.get('token')
    infos_json = json.loads(infos)
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        nfce_antes = infos_json["nfce"]
        nfce = etree.fromstring(nfce_antes)
        empresa = Empresa.query.filter_by(pessoa_juridica_fk_id=int(infos_json["empresa"])).first()
        nfce = add_qrcode(nfce, empresa)
        infos_json["nfce"] = exportar_xml(nfce)
        obj_nfce = Nfce(nfce.getchildren()[0].get('Id')[3:], 9, empresa.ambiente,
                        Venda.query.filter_by(id=infos_json["venda_id"]).first(), infos_json["nnf"],
                        infos_json["nfce"])
        db.session.add(obj_nfce)
        db.session.commit()
        infos_json["nfce_id"] = obj_nfce.id
        infos = json.dumps(infos_json)
        pedido = {"texto": nfce_antes, "tipo": "xml"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = "QRCode adicionado com sucesso - <a class=\"passo_icone\" href=\"/danfeNFCe/" \
                    + str(infos_json["nfce_id"]) \
                    + "\" title=\"Download DANFCE\"><i class=\"fas fa-file-pdf text-danger\"></i></a>" \
                      "<a class=\"passo_icone\" href=\"/xmlNFCe/" + str(infos_json["nfce_id"]) \
                    + "\" title=\"Download NFCe\"><i class=\"fas fa-file-invoice-dollar text-warning\"></i></a>"
    except BaseException as e:
        delete_venda(infos_json["venda_id"])
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_enivar_sefaz', methods=['POST'])
def passo_enivar_sefaz():
    infos = request.values.get('token')
    infos_json = json.loads(infos)
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        nfce_antes = infos_json["nfce"]
        nota = Nfce.query.filter_by(id=infos_json["nfce_id"]).first()
        nota = enviar_nfce(nota)
        infos_json["nfce"] = nota.xml_distribuicao
        infos_json["chave"] = nota.chave_acesso
        db.session.commit()
        infos = json.dumps(infos_json)
        pedido = {"texto": nfce_antes, "tipo": "xml"}
        resposta = {"texto": infos_json["nfce"], "tipo": "xml"}
        resultado = get_xmotivo(nota.status) \
                    + " - <a class=\"passo_icone\" href=\"/danfeNFCe/" \
                    + str(infos_json["nfce_id"]) \
                    + "\" title=\"Download DANFCE\"><i class=\"fas fa-file-pdf text-danger\"></i></a>" \
                      "<a class=\"passo_icone\" href=\"/xmlNFCe/" \
                    + str(infos_json["nfce_id"]) \
                    + "\" title=\"Download NFCe\"><i class=\"fas fa-file-invoice-dollar text-warning\"></i></a>"

    except BaseException as e:
        delete_venda(infos_json["venda_id"])
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_enivar_sefaz/<id_nfce>', methods=['POST', 'GET'])
def passo_enivar_sefaz_id(id_nfce=0):
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        nota = Nfce.query.filter_by(id=id_nfce).first()
        nfce_antes = nota.xml
        nota = enviar_nfce(nota)
        db.session.commit()
        pedido = {"texto": nfce_antes, "tipo": "xml"}
        resposta = {"texto": nota.xml_distribuicao, "tipo": "xml"}
        resultado = get_xmotivo(nota.status) + " - <a class=\"passo_icone\" href=\"/danfeNFCe/" + str(
            nota.id) + "\" title=\"Download DANFCE\"><i class=\"fas fa-file-pdf text-danger\"></i></a>" \
                       "<a class=\"passo_icone\" href=\"/xmlNFCe/" + str(
            nota.id) + "\" title=\"Download NFCe\"><i class=\"fas fa-file-invoice-dollar text-warning\"></i></a>"
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token="", erro=erro)


@app.route('/passo_obter_resultado', methods=['POST'])
def passo_obter_resultado():
    infos = request.values.get('token')

    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
        notas = Nfce.query.filter(
            or_(Nfce.retida_daf == 1, or_(Nfce.resultado_aut_daf == None, Nfce.resultado_aut_daf == "2021"))).order_by(
            Nfce.dh_emi).limit(50).all()
        notas_apagar = len(
            Nfce.query.filter(and_(Nfce.retida_daf, Nfce.aut_apg_daf != None)).order_by(Nfce.dh_emi).limit(50).all())
        if len(notas) == 0:
            resultado = "Não foram encontradas NFC-e pendentes"
            res_id = 1
            erro = True
        else:
            chaves = []
            for n in notas:
                chaves.append(n.chave_acesso)

            res = ws_sef.obter_resultado(daf, chaves)
            res_sef = res[1].text
            res_sef_xml = etree.fromstring(res_sef)
            ped_sef = res[0]
            resultado = res_sef_xml.find('.//xMotivo').text

            res_ok = 0
            res_erro = 0
            if res_sef_xml.find('.//cStat').text == '1000':
                res_id = 0
                erro = False
                rets = res_sef_xml.findall('.//retDFe')
                for r in rets:
                    chave = r.find('.//chDFe').text
                    nfce = Nfce.query.filter_by(chave_acesso=chave).first()
                    nfce.resultado_aut_daf = r.find('.//cStatAut').text
                    if r.find('.//hAut') is not None:
                        nfce.id_aut_daf = r.find('.//idAut').text
                        nfce.aut_apg_daf = r.find('.//hAut').text
                        res_ok = res_ok + 1
                    else:
                        res_erro = res_erro + 1
                    db.session.commit()

                resultado = str(len(notas)) + " consultadas, " + str(res_ok) + " autorizadas e " + str(
                    res_erro) + " sem autorização SEF"
                if res_ok == 0 and notas_apagar == 0:
                    erro = True
                    res_id = 1

            pedido = {"texto": ped_sef, "tipo": "xml"}
            resposta = {"texto": res_sef, "tipo": "xml"}
    except requests.exceptions.ConnectionError:
        res_id = 1
        erro = True
        resultado = "Erro ao conectar com a SEF"
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=infos, erro=erro)


@app.route('/passo_apagar_retidas', methods=['POST'])
def passo_apagar_retidas():
    token = request.values.get('token')

    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
        notas = Nfce.query.filter(and_(Nfce.retida_daf, Nfce.aut_apg_daf != None)).order_by(
            Nfce.dh_emi).limit(
            50).all()
        if len(notas) == 0:
            resultado = "Não foram encontradas NFC-e retidas a serem apagadas"
        else:
            res_ok = 0
            res_erro = 0
            r_ped_daf = ""
            r_res_daf = ""
            for n in notas:
                ped_daf = paf.apagarAutorizacaoRetida(n.id_aut_daf, n.aut_apg_daf)
                r_ped_daf = r_ped_daf + ped_daf + '\n'
                res_daf = paf.enviar_mensagem(ped_daf)
                r_res_daf = r_res_daf + res_daf + '\n'
                res_daf_json = json.loads(res_daf)
                if res_daf_json["res"] == 0 or res_daf_json["res"] == 6:
                    n.retida_daf = False
                if res_daf_json["res"] == 0:
                    daf.num_dfe = daf.num_dfe - 1
                    if daf.num_dfe < daf.max_dfe:
                        daf.situacao = 1
                        daf.estado = "pronto"
                    res_ok = res_ok + 1
                else:
                    res_id = res_daf_json["res"]
                    res_erro = res_erro + 1

            resultado = str(len(notas)) + " retidas, " + str(res_ok) + " apagadas, " + str(res_erro) + " com erro"

            db.session.commit()

            pedido = {"texto": r_ped_daf, "tipo": "texto"}
            resposta = {"texto": r_res_daf, "tipo": "texto"}
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token=token, erro=erro)


@app.route('/passo_consultar_pendentes', methods=['POST'])
def passo_consultar_pendentes():
    pedido = {"texto": "", "tipo": "texto"}
    resposta = {"texto": "", "tipo": "texto"}
    res_id = 0
    erro = False
    try:
        notas = Nfce.query.filter_by(situacao=0).order_by(asc(Nfce.dh_emi)).all()
        res = []
        for n in notas:
            res.append({
                "nnf": n.nnf,
                "dh_emi": n.dh_emi.strftime("%d/%m/%Y %H:%M"),
                "chave_acesso": n.chave_acesso
            })
        pedido = {"texto": "Buscando NFC-e emitidas off-line", "tipo": "texto"}
        resposta = {"antes": "NFC-e pendentes: ", "texto": res, "tipo": "json"}
        resultado = "Encontradas " + str(len(notas)) + " NFC-e pendentes"
    except BaseException as e:
        resultado = "Ocorreu um erro..."
        res_id = 1
        erro = True
        resposta["texto"] = "Erro: " + str(e.args)

    return jsonify(pedido=pedido, resposta=resposta, resultado=resultado, res_id=res_id, token="", erro=erro)
