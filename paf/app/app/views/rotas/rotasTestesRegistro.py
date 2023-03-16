from flask import render_template

from app import app
from app.controllers.sefController import SefController

ws_sef = SefController()


@app.route('/registrarNovoDaf<string:tipo>', methods=['GET'])
def registrarNovoDaf(tipo=""):
    passos = [
        {
            "rota": "passo_padraofab9997",
            "descricao": "Restaurando padrão de fábrica - gerando novo idDaf",
            "ator": "daf"
        }
        , {
            "rota": "passo_consultar_daf",
            "descricao": "Consultando informações do DAF",
            "ator": "daf"
        }
        , {
            "rota": "passo_registrar_ini_sef",
            "descricao": "Iniciar registro junto à SEF",
            "ator": "sef"
        }
        , {
            "rota": "passo_registrar_ini_daf",
            "descricao": "Iniciar registro no daf",
            "ator": "daf"
        }
        , {
            "rota": "passo_registrar_conf_sef",
            "descricao": "Confirmar registro na sef",
            "ator": "sef"
        }
        , {
            "rota": "passo_chave_paf",
            "descricao": "Armazenar chavePaf do registro",
            "ator": "paf"
        }
        , {
            "rota": "passo_registrar_conf_daf",
            "descricao": "Confirmar registro no daf",
            "ator": "daf"
        }
    ]
    return render_template('cenario_teste_modal.html', titulo="Registrar novo DAF", passos=passos, tipo=tipo)


@app.route('/registrarDaf<string:tipo>', methods=['GET'])
def registrarDaf(tipo=""):
    passos = [
        {
            "rota": "passo_consultar_daf",
            "descricao": "Consultando informações do DAF",
            "ator": "daf"
        }
        , {
            "rota": "passo_registrar_ini_sef",
            "descricao": "Iniciar registro junto à SEF",
            "ator": "sef"
        }
        , {
            "rota": "passo_registrar_ini_daf",
            "descricao": "Iniciar registro no daf",
            "ator": "daf"
        }
        , {
            "rota": "passo_registrar_conf_sef",
            "descricao": "Confirmar registro na sef",
            "ator": "sef"
        }
        , {
            "rota": "passo_chave_paf",
            "descricao": "Armazenar chavePaf do registro",
            "ator": "paf"
        }
        , {
            "rota": "passo_registrar_conf_daf",
            "descricao": "Confirmar registro no daf",
            "ator": "daf"
        }
    ]

    return render_template('cenario_teste_modal.html', titulo="Registrar DAF", passos=passos, tipo=tipo)


@app.route('/removerRegistro<string:tipo>', methods=['GET'])
def removerRegistro(tipo=""):
    passos = [
        {
            "rota": "passo_consultar_daf",
            "descricao": "Consultando informações do DAF",
            "ator": "daf"
        }
        ,
        {
            "rota": "passo_remover_ini_sef",
            "descricao": "Iniciar processo de remoção de registro junto à SEF",
            "ator": "sef"
        }
        , {
            "rota": "passo_remover_ini_daf",
            "descricao": "Iniciar processo de remoção de registro junto no DAF",
            "ator": "daf"
        }
        , {
            "rota": "passo_remover_conf_sef",
            "descricao": "Confirmar remoção junto à SEF",
            "ator": "sef"
        }
        , {
            "rota": "passo_remover_conf_daf",
            "descricao": "Confirmar remoção do registro no DAF",
            "ator": "daf"
        }
    ]

    return render_template('cenario_teste_modal.html', titulo="Remover registro do DAF", passos=passos, tipo=tipo)


@app.route('/alterarModoOp<string:tipo>', methods=['GET'])
def alterarModoOp(tipo=""):
    passos = [
        {
            "rota": "passo_modoop_ini_sef",
            "descricao": "Iniciar processo de alteração do modo de operação junto à SEF",
            "ator": "sef"
        }
        , {
            "rota": "passo_modoop_ini_daf",
            "descricao": "Iniciar processo de alteração do modo de operação junto no DAF",
            "ator": "daf"
        }
        , {
            "rota": "passo_modoop_conf_sef",
            "descricao": "Confirmar de alteração do modo de operação junto à SEF",
            "ator": "sef"
        }
        , {
            "rota": "passo_modoop_conf_daf",
            "descricao": "Confirmar de alteração do modo de operação do registro no DAF",
            "ator": "daf"
        }
    ]

    return render_template('cenario_teste_modal.html', titulo="Alterar modo de operação do DAF", passos=passos,
                           tipo=tipo)
