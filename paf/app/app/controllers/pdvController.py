import base64
from random import *

from flask import redirect, render_template, request, session

from app import app
from app import db
from app.models.empresa import Empresa
from app.models.pontoVenda import PontoVenda as Pdv
from app.utils.formats import get_all
from app.utils.geradores import gerar_nome
from app.views.formularios.pdvForm import PdvForm


@app.route('/listarPdv')
def listar_pdv():
    data = get_all(Pdv.query.all(), Pdv.columns,
                   [{"btn": "edt", "rota": "edicaoPdv"}, {"btn": "del", "rota": "exclusaoPdv"}])
    return render_template('listagem.html', data=data, columns=Pdv.columns, title='PDVs',
                           add='', gerar='/gerarPdv', label='PDV')


@app.route('/selecionarPdv/<int:pdv>', methods=['GET'])
def selecionar_pdv(pdv=0):
    data = get_all(Pdv.query.filter_by(id=pdv), Pdv.columns,
                   [{"btn": "edt", "rota": "edicaoPdv"}, {"btn": "del", "rota": "exclusaoPdv"}])
    return render_template('listagem.html', data=data, columns=Pdv.columns, title='PDVs',
                           add='', gerar='', label='PDV ' + data[0]['nome'])


@app.route('/gerarPdv')
def gerar_pdv():
    if session.get("empresa") is None:
        from app.inicializacao import Inicializacao
        Inicializacao.set_login()

    empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
    nome = gerar_nome(1)
    serial = 125488  # random.randint(10000, 99999)
    # serial = random.randint(10000, 99999)
    id_pdv = base64.urlsafe_b64encode(bytearray(getrandbits(8) for i in range(32))).replace(b"=", b"").decode()[:10]

    pdv = Pdv(nome, serial, id_pdv, empresa)

    db.session.add(pdv)
    db.session.commit()

    return redirect("/listarPdv")


@app.route('/exclusaoPdv/<int:pdv_id>', methods=['GET'])
def exclusao_pdv(pdv_id=0):
    pdv = Pdv.query.filter_by(id=pdv_id).first()

    db.session.delete(pdv)

    db.session.commit()

    return redirect("/listarPdv")


@app.route('/edicaoPdv/<int:pdv_id>')
def edicao_pdv(pdv_id=0):
    cli = Pdv.query.filter_by(id=pdv_id).first()
    form = PdvForm()
    return render_template('registro.html', action="/editarPdv/" + str(id), title='Edição de Pdv - ' + cli.nome,
                           form_title="Editar Pdv - " + cli.nome,
                           form=form, columns=Pdv.columns, dados=cli)


@app.route('/editarPdv/<int:pdv_id>', methods=['POST'])
def editar_pdv(pdv_id=0):
    nome = request.form.get('nome')
    serial = request.form.get('serial')
    idpdv = request.form.get('id_pdv')
    empresa = request.form.get("empresa")

    cli = Pdv.query.filter_by(id=pdv_id).first()
    cli.nome = nome
    cli.serial = serial
    cli.idpdv = idpdv
    empresa_obj = Empresa.query.filter_by(id=empresa).first()
    cli.empresa = empresa_obj

    db.session.commit()
    return redirect("/listarPdv")
