import re

from bradocs4py import GeradorCpf
from flask import request, redirect, render_template

from app import app
from app import db
from app.models.cliente import Cliente
from app.models.endereco import Endereco
from app.utils.formats import get_all
from app.utils.geradores import gerar_nome, gerar_email, gerar_endereco, gerar_telefone
from app.views.formularios.clienteForm import ClienteForm


@app.route('/listarCliente')
def listar_cliente():
    data = get_all(Cliente.query.all(), Cliente.columns,
                   [{"btn": "edt", "rota": "edicaoCliente"}, {"btn": "del", "rota": "exclusaoCliente"}])
    return render_template('listagem.html', data=data, columns=Cliente.columns, title='Clientes',
                           add='/cadastroCliente', gerar='/gerarCliente', label='Cliente')


@app.route('/cadastroCliente')
def cadastro_cliente():
    form = ClienteForm()
    return render_template('registro.html', action="/salvarCliente", title='Cadastrar Cliente',
                           form_title="Cadastrar Cliente",
                           form=form, columns=Cliente.columns, dados='')


@app.route('/salvarCliente', methods=['POST'])
def salvar_cliente():
    nome = request.form.get('nome')
    telefone_principal = request.form.get('telefone_principal')
    email = request.form.get('email')
    cpf = request.form.get('cpf')

    cliente = Cliente(nome, telefone_principal, email, cpf)
    db.session.add(cliente)
    db.session.commit()

    return redirect("/listarCliente")


@app.route('/gerarCliente')
def gerar_cliente():
    nome = gerar_nome(3)
    telefone_principal = gerar_telefone()
    email = gerar_email(nome)
    cpf = GeradorCpf.gerar().rawValue

    cliente = Cliente(nome, telefone_principal, email, cpf)
    db.session.add(cliente)

    end = gerar_endereco()
    endereco = Endereco(end.get("endereco"), end.get("cep"), end.get("bairro"), end.get("complemento"),
                        end.get("logradouro"), end.get("numero"),
                        cliente.pessoaFisica.pessoa, end.get("municipio"))
    db.session.add(endereco)
    db.session.commit()

    return redirect("/listarCliente")


@app.route('/edicaoCliente/<int:id>')
def edicao_cliente(id=0):
    cli = Cliente.query.filter_by(id=id).first()
    form = ClienteForm()
    return render_template('registro.html', action="/editarCliente/" + str(id), title='Edição de Cliente - ' + cli.nome,
                           form_title='Editar Cliente - ' + cli.nome,
                           form=form, columns=Cliente.columns, dados=cli)


@app.route('/editarCliente/<int:id>', methods=['POST'])
def editar_cliente(id=0):
    nome = request.form.get('nome')
    telefone_principal = request.form.get('telefone_principal')
    email = request.form.get('email')
    cpf = request.form.get('cpf')

    cli = Cliente.query.filter_by(id=id).first()
    cli.nome = nome
    cli.telefone_principal = telefone_principal
    cli.email = email
    cli.cpf = re.sub("([.-])", "", cpf)

    db.session.commit()

    return redirect("/listarCliente")


@app.route('/exclusaoCliente/<int:id>', methods=['GET'])
def exclusao_cliente(id=0):
    endereco = Endereco.query.filter_by(pessoa_fk_id=id).first()
    if endereco is not None:
        db.session.delete(endereco)

    cliente = Cliente.query.filter_by(id=id).first()

    db.session.delete(cliente)

    db.session.commit()

    return redirect("/listarCliente")
