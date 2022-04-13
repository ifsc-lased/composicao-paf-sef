import random

from flask import redirect, render_template, request, session
from sqlalchemy import desc

from app import app
from app import db
from app.models.funcionario import Funcionario
from app.models.funcionarioPdv import FuncionarioPdv
from app.models.pontoVenda import PontoVenda as Pdv
from app.utils.formats import get_all
from app.views.formularios.loginForm import LoginForm


@app.route('/listarLogin')
def listar_login():
    data = get_all(FuncionarioPdv.query.order_by(desc(FuncionarioPdv.data_hora_login)).all(), FuncionarioPdv.columns,
                   [])
    return render_template('listagem.html', data=data, columns=FuncionarioPdv.columns,
                           title='Login (Funcionário - PDV)',
                           add='', gerar='/gerarLogin', label='Login (Funcionário - PDV)')


@app.route('/gerarLogin')
def gerar_login():
    funcionarios = Funcionario.query.all()
    funcionario = funcionarios[random.randint(0, len(funcionarios) - 1)]

    pdvs = Pdv.query.all()
    pdv = pdvs[random.randint(0, len(pdvs) - 1)]

    funcionario_pdv = FuncionarioPdv(pdv, funcionario)
    # atualizar p/ session ficar com o último login
    session["funcionario_pdv"] = funcionario_pdv.id
    session["empresa"] = funcionario_pdv.pdv.empresa.id
    session["pdv"] = funcionario_pdv.pdv.id_pdv

    db.session.add(funcionario_pdv)
    db.session.commit()

    return redirect("/listarLogin")


@app.route('/edicaoLogin/<int:log_id>')
def edicao_login(log_id=0):
    cli = FuncionarioPdv.query.filter_by(id=log_id).first()
    form = LoginForm()
    return render_template('registro.html', action="/editarLogin/" + str(log_id), title='Edição de Login',
                           form_title="Editar Login",
                           form=form, columns=FuncionarioPdv.columns, dados=cli)


@app.route('/editarLogin/<int:id>', methods=['POST'])
def editar_login(id=0):
    funcionario_id = request.form.get("funcionario")
    pdv_id = request.form.get("pdv")

    funcionario = Funcionario.query.filter_by(id=funcionario_id).first()
    pdv = Pdv.query.filter_by(id=pdv_id).first()

    login = FuncionarioPdv.query.filter_by(id=id).first()
    login.funcionario = funcionario
    login.pdv = pdv
    db.session.commit()

    return redirect("/listarLogin")
