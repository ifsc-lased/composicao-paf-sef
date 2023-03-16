from flask import render_template
from sqlalchemy import asc

from app import app
from app.controllers.sefController import SefController
from app.models.nfce import Nfce
from app.models.temp import Temp

ws_sef = SefController()
temp = Temp()


@app.route("/vendaComDaf<string:tipo>", methods=["GET"])
def vendaComDaf(tipo=""):
    passos = [
        {
            "rota": "passo_gerar_venda",
            "descricao": "Gerar nova venda",
            "ator": "paf"
        }
        , {
            "rota": "passo_emitir_nfce",
            "descricao": "Emitir NFC-e",
            "ator": "paf"
        }
        , {
            "rota": "passo_solicitar_autenticacao_daf",
            "descricao": "Autenticar PAF",
            "ator": "daf"
        }
        , {
            "rota": "passo_autorizar_dfe",
            "descricao": "Autorizar DF-e",
            "ator": "daf"
        }
        , {
            "rota": "passo_incorporar_fragmento",
            "descricao": "Incorporar a autorização do DAF no XML",
            "ator": "paf"
        }
        , {
            "rota": "passo_assinar_dfe",
            "descricao": "Assinar o XML da NFC-e",
            "ator": "paf"
        }
        , {
            "rota": "passo_gerar_qrcode",
            "descricao": "Completar NFC-e com QRCode",
            "ator": "paf"
        }
        , {
            "rota": "passo_enivar_sefaz",
            "descricao": "Solicitar autorização da SEFAZ",
            "ator": "svrs"
        }
    ]

    return render_template("cenario_teste_modal.html", titulo="Emitir NFC-e com fragmento", passos=passos, tipo=tipo)


@app.route("/vendaOfflineComDaf<string:tipo>", methods=["GET"])
def vendaOfflineComDaf(tipo=""):
    passos = [
        {
            "rota": "passo_gerar_venda",
            "descricao": "Gerar nova venda",
            "ator": "paf"
        }
        , {
            "rota": "passo_emitir_nfce_off",
            "descricao": "Emitir NFC-e",
            "ator": "paf"
        }
        , {
            "rota": "passo_solicitar_autenticacao_daf",
            "descricao": "Autenticar PAF",
            "ator": "daf"
        }
        , {
            "rota": "passo_autorizar_dfe",
            "descricao": "Autorizar DF-e",
            "ator": "daf"
        }
        , {
            "rota": "passo_incorporar_fragmento",
            "descricao": "Incorporar a autorização do DAF no XML",
            "ator": "paf"
        }
        , {
            "rota": "passo_assinar_dfe",
            "descricao": "Assinar o XML da NFC-e",
            "ator": "paf"
        }
        , {
            "rota": "passo_gerar_qrcode_off",
            "descricao": "Completar NFC-e com QRCode",
            "ator": "paf"
        }
    ]

    return render_template("cenario_teste_modal.html", titulo="Emitir NFC-e em contingência com autorização DAF",
                           passos=passos, tipo=tipo)


@app.route("/apagarRetida<string:tipo>", methods=["GET"])
def apagarRetida(tipo=""):
    passos = [
        {
            "rota": "passo_obter_resultado",
            "descricao": "Obter resultado sobre autorização DAF",
            "ator": "sef"
        }
        , {
            "rota": "passo_apagar_retidas",
            "descricao": "Apagar retidas no DAF",
            "ator": "daf"
        }
    ]

    return render_template("cenario_teste_modal.html", titulo="Apagar autorização retida", passos=passos, tipo=tipo)

@app.route("/consultarAutorizacoes<string:tipo>", methods=["GET"])
def consultarAutorizacoes(tipo=""):
    passos = [
         {
            "rota": "passo_consultar_autorizacoes_daf",
            "descricao": "Consultar autorizações",
            "ator": "daf"
        }
    ]

    return render_template("cenario_teste_modal.html", titulo="Consultar autorizações", passos=passos, tipo=tipo)

@app.route("/notas_off<string:tipo>", methods=["GET"])
def notas_off(tipo=""):
    passos = [
        {
            "rota": "passo_consultar_pendentes",
            "descricao": "Consultar NFC-e pendentes de envio para SVRS",
            "ator": "paf"
        }
    ]

    notas = Nfce.query.filter_by(situacao=0).order_by(asc(Nfce.dh_emi)).all()
    for n in notas:
        passos.append({
            "rota": "passo_enivar_sefaz/" + str(n.id),
            "descricao": "Solicitar autorização da SEFAZ para NFC-e " + str(n.nnf),
            "ator": "svrs"
        })

    return render_template("cenario_teste_modal.html", titulo="NFC-e pendentes de envio", passos=passos, tipo=tipo)
