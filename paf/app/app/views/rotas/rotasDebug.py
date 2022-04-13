from flask import render_template, redirect

from app import app, db


@app.route('/padraoFabrica')
def reset_conectado():
    passos = [
        {
            "rota": "passo_padraofab",
            "descricao": "Restaurar configurações de fábrica do DAF",
            "ator": "daf"
        },
        {
            "rota": "passo_consutlar_daf",
            "descricao": "Consultar e atualizar informações",
            "ator": "daf"
        }
    ]

    return render_template("cenario_teste.html", titulo="Restaurar configurações de fábrica", passos=passos,
                           tipo="Sucesso")


@app.route('/padraoFabricaNovo')
def reset_conectado_novo():
    passos = [
        {
            "rota": "passo_padraofab9997",
            "descricao": "Restaurar configurações de fábrica do DAF e gerar novo idDAF",
            "ator": "daf"
        },
        {
            "rota": "passo_consutlar_daf",
            "descricao": "Consultar e atualizar informações",
            "ator": "daf"
        }
    ]

    return render_template("cenario_teste.html", titulo="Restaurar configurações de fábrica - novo idDAF",
                           passos=passos, tipo="Sucesso")


@app.route('/consultarDAFConectado')
def consultar_daf_conectado():
    passos = [
        {
            "rota": "passo_consutlar_daf",
            "descricao": "Consultar e atualizar informações",
            "ator": "daf"
        }
    ]

    return render_template("cenario_teste.html", titulo="Consultar DAF", passos=passos, tipo="Sucesso")


@app.route('/consultarDAFConectadoModal')
def consultar_daf_conectado_modal():
    passos = [
        {
            "rota": "passo_consutlar_daf",
            "descricao": "Consultar e atualizar informações",
            "ator": "daf"
        }
    ]

    return render_template("cenario_teste_modal.html", titulo="Consultar DAF", passos=passos, tipo="Sucesso")


@app.route('/consultarDAFConectadoSEF')
def consultar_daf_conectado_sef():
    passos = [
        {
            "rota": "passo_consutlar_daf_sef",
            "descricao": "Consultar DAF junto à SEF e atualizar informações",
            "ator": "sef"
        }
    ]

    return render_template("cenario_teste.html", titulo="Consultar DAF junto à SEF", passos=passos, tipo="Sucesso")


@app.route('/interromperProcesso')
def interromper_processo():
    passos = [
        {
            "rota": "passo_cancelar_processo",
            "descricao": "Cancelar processo atual no DAF",
            "ator": "daf"
        }
    ]

    return render_template("cenario_teste.html", titulo="Cancelar processo atual no DAF", passos=passos, tipo="Sucesso")


@app.route("/multiplasnota/<int:qnt>", methods=["GET"])
def multiplasnota(qnt=0):
    from app.controllers.nfceController import gerar_nfe
    from app.controllers.vendaController import nova_venda
    for i in range(0, qnt):
        venda = nova_venda()
        db.session.add(venda)
        nfce = gerar_nfe(venda)
        if nfce is not None:
            db.session.add(nfce)
            db.session.commit()
        else:
            db.session.rollback()
    return redirect("/listarNfce")
