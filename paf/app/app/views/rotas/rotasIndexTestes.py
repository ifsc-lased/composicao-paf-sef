from flask import render_template, session
from sqlalchemy import desc

from app import app
from app.controllers.sefController import SefController
from app.models.daf import Daf
from app.models.empresa import Empresa
from app.models.temp import Temp
from app.utils.labels import get_situacao_daf

ws_sef = SefController()
temp = Temp()


@app.route('/cenario_autorizacao')
def cenario_autorizacao():
    daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
    if session.get("empresa") is not None:
        empresa_id = session.get("empresa")
    else:
        from app.inicializacao import Inicializacao
        Inicializacao.set_login()
        empresa_id = session.get("empresa")

    if empresa_id is None:
        empresa = Empresa.query.first()
    else:
        empresa = Empresa.query.filter_by(id=empresa_id).first()
    if empresa.tp_emis == 1:
        contingencia = False
        rota_venda = "vendaComDafSucesso"
    else:
        contingencia = True
        rota_venda = "vendaOfflineComDafSucesso"

    if daf.num_dfe > 0:
        retidas = True
        if daf.num_dfe > 1:
            qnt_retidas = "<b>" + str(daf.num_dfe) + "</b> autorizações retidas"
        else:
            qnt_retidas = "<b>1</b> autorização retida"
    else:
        qnt_retidas = "sem autorizações retidas"
        retidas = False

    foco = "nivel_0"
    nivel = 0
    if daf.situacao == 1:
        foco = "nivel_1"
        nivel = 1
    if daf.situacao == 6:
        foco = "nivel_2"
        nivel = 2

    bloqueado = [
        {
            "rota": "apagarRetidaSucesso",
            "nome": "Apagar autorização retida"
        }
    ]

    sem_registro = [
        {
            "rota": "registrarDafSucesso",
            "nome": "Registrar DAF"
        }
    ]

    registrado = [
        {
            "rota": "removerRegistroSucesso",
            "nome": "Remover registro",
            "id": "removerRegistro",
            "disponivel": not retidas
        },
        {
            "rota": "alterarModoOpSucesso",
            "nome": "Alterar modo de operação",
            "id": "alterarModoOp",
            "disponivel": not retidas
        },
        {
            "rota": rota_venda,
            "nome": "Emitir NFC-e",
            "id": "emitirNota",
            "disponivel": True
        }, {
            "rota": "apagarRetidaSucesso",
            "nome": "Apagar autorização retida",
            "id": "apagarRetida",
            "disponivel": retidas
        }, {
            "rota": "consultarAutorizacoesSucesso",
            "nome": "Consultar autorizações",
            "id": "consultarAutorizacoes",
            "disponivel": retidas
        }
    ]

    metodos = {
        "nivel_0": sem_registro,
        "nivel_1": registrado,
        "nivel_2": bloqueado
    }

    perc = daf.num_dfe * 100 / daf.max_dfe
    gd = ""
    for i in range(0, round(perc)):
        gd = gd + " rgba(220,0,0," + str(round(perc / 100, 1)) + "), "
    for i in range(round(perc), 99):
        gd = gd + " #fff, "
    gd = gd + " #fff "
    ocupacao = "<div style='width:100px; height:30px; padding:5px; border:1px solid #ddd; background-image: linear-gradient(to right, " + gd + ")'><span style='display:inline-block; background-color:rgba(255,255,255,0.5);'>" + str(
        perc).replace(".", ",") + "%</span></div>"

    return render_template('index_cenario_teste.html', titulo="Cenários de Teste", metodos=metodos, daf=daf,
                           id_foco=foco, situacao_label=get_situacao_daf(daf.situacao), nivel=nivel,
                           retidas=qnt_retidas, contingencia=contingencia)
