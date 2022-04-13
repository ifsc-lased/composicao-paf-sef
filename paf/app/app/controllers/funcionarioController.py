import re

from bradocs4py import GeradorCpf
from flask import request, redirect, render_template, session

from app import app
from app import db
from app.models.empresa import Empresa
from app.models.endereco import Endereco
from app.models.funcionario import Funcionario
from app.utils.formats import get_all
from app.utils.geradores import gerar_nome, gerar_email, gerar_endereco, gerar_telefone
from app.views.formularios.funcionarioForm import FuncionarioForm


@app.route('/listarFuncionario')
def listar_funcionario():
    data = get_all(Funcionario.query.all(), Funcionario.columns,
                   [{"btn": "edt", "rota": "edicaoFuncionario"}, {"btn": "del", "rota": "exclusaoFuncionario"}])
    return render_template('listagem.html', data=data, columns=Funcionario.columns, title='Funcionários',
                           add='', gerar='/gerarFuncionario', label='Funcionário')


@app.route('/selecionarFuncionario/<int:func_id>', methods=['GET'])
def selecionar_funcionario(func_id=0):
    data = get_all(Funcionario.query.filter_by(id=func_id), Funcionario.columns,
                   [{"btn": "edt", "rota": "edicaoFuncionario"}, {"btn": "del", "rota": "exclusaoFuncionario"}])
    return render_template('listagem.html', data=data, columns=Funcionario.columns, title='Funcionários',
                           add='', gerar='', label='Funcionário ' + data[0]['nome'])


@app.route('/gerarFuncionario')
def gerar_funcionario():
    nome = gerar_nome(3)
    telefone_principal = gerar_telefone()
    email = gerar_email(nome)
    login = re.sub('( )', '', nome)[0:6].lower()
    empresa = Empresa.query.filter_by(id=session.get("empresa")).first()
    cpf = GeradorCpf.gerar().rawValue

    funcionario = Funcionario(nome, telefone_principal, email, login, empresa, cpf)
    db.session.add(funcionario)

    end = gerar_endereco()
    endereco = Endereco(end.get("endereco"), end.get("cep"), end.get("bairro"), end.get("complemento"),
                        end.get("logradouro"), end.get("numero"),
                        funcionario.pessoaFisica.pessoa, end.get("municipio"))
    db.session.add(endereco)

    db.session.commit()

    return redirect("/listarFuncionario")


@app.route('/salvarFuncionario', methods=['POST'])
def salvar_funcionario():
    nome = request.form.get('nome')
    telefone_principal = request.form.get('telefone_principal')
    email = request.form.get('email')
    login = request.form.get('login')
    empresa = Empresa.query.filter_by(id=int(request.form.get('empresa'))).first()
    cpf = request.form.get('cpf')

    funcionario = Funcionario(nome, telefone_principal, email, login, empresa, cpf)
    db.session.add(funcionario)
    db.session.commit()

    return redirect("/listarFuncionario")


@app.route('/edicaoFuncionario/<int:func_id>')
def edicao_funcionario(func_id=0):
    cli = Funcionario.query.filter_by(id=func_id).first()
    form = FuncionarioForm()
    return render_template('registro.html', action="/editarFuncionario/" + str(func_id),
                           title='Edição de Funcionário - ' + cli.nome,
                           form_title="Editar Funcinário- " + cli.nome,
                           form=form, columns=Funcionario.columns, dados=cli)


@app.route('/editarFuncionario/<int:func_id>', methods=['POST'])
def editar_funcionario(func_id=0):
    nome = request.form.get('nome')
    telefone_principal = request.form.get('telefone_principal')
    email = request.form.get('email')
    login = request.form.get('login')
    empresa = Empresa.query.filter_by(id=int(request.form.get('empresa'))).first()
    cpf = request.form.get('cpf')

    fun = Funcionario.query.filter_by(id=func_id).first()
    fun.nome = nome
    fun.telefone_principal = telefone_principal
    fun.email = email
    fun.login = login
    fun.cpf = re.sub("([.-])", "", cpf)
    fun.empresa = empresa

    db.session.commit()

    return redirect("/listarFuncionario")


@app.route('/exclusaoFuncionario/<int:id>', methods=['GET'])
def exclusao_funcionario(id=0):
    endereco = Endereco.query.filter_by(pessoa_fk_id=id).first()
    db.session.delete(endereco)

    funcionario = Funcionario.query.filter_by(id=id).first()

    db.session.delete(funcionario)

    db.session.commit()

    return redirect("/listarFuncionario")
