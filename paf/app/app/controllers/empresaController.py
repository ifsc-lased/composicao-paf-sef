import random
import re

from bradocs4py import GeradorCnpj
from flask import request, redirect, render_template

from app import app
from app import db
from app.models.empresa import Empresa
from app.models.endereco import Endereco
from app.utils.formats import get_all
from app.utils.geradores import gerar_nome, gerar_email, gerar_endereco, gerar_telefone, gerar_csc
from app.views.formularios.empresaForm import EmpresaForm


@app.route('/listarEmpresa')
def listar_empresa():
    colunas = Empresa.columns.copy()
    data = get_all(Empresa.query.all(), colunas,
                   [{"btn": "edt", "rota": "edicaoEmpresa"},
                    {"btn": "del", "rota": "exclusaoEmpresa", "classe": "empresa"}])
    return render_template('listagem.html', data=data, columns=colunas, title="Empresas",
                           add='', gerar='/gerarEmpresa', label='Empresa')


@app.route('/selecionarEmpresa/<int:id>', methods=['GET'])
def selecionar_empresa(id=0):
    data = get_all(Empresa.query.filter_by(id=id), Empresa.columns,
                   [{"btn": "edt", "rota": "edicaoEmpresa"}])
    return render_template('listagem.html', data=data, columns=Empresa.columns,
                           add='', label='Empresa', title='Empresa ' + data[0]['nome'])


@app.route('/cadastroEmpresa')
def cadastro_empresa():
    form = EmpresaForm()
    return render_template('registro.html', action="/salvarEmpresa", title='Cadastrar Empresa',
                           form_title="Cadastrar Empresa",
                           form=form, columns=Empresa.columns, dados='')


@app.route('/salvarEmpresa', methods=['POST'])
def salvar_empresa():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone_principal')
    email = request.form.get('email')
    cnpj = request.form.get('cnpj')
    tpEmis = request.form.get('tp_emis')
    nome_fantasia = request.form.get('nome_fantasia')
    inscricao_estadual_sc = request.form.get('inscricao_estadual_sc')
    csc = gerar_csc()
    csc_id = 1
    ambiente = request.form.get("ambiente")
    idpaf = request.form.get("id_paf")
    autorizadora = request.form.get("endereco_sefaz")

    empresa = Empresa(nome, telefone, email, cnpj, nome_fantasia, inscricao_estadual_sc, csc, csc_id, ambiente, idpaf,
                      autorizadora, tpEmis)
    db.session.add(empresa)
    db.session.commit()

    return redirect("/listarEmpresa")


@app.route('/gerarEmpresa')
def gerar_empresa():
    nome = gerar_nome(1)
    telefone = gerar_telefone()
    email = gerar_email(nome)
    cnpj = GeradorCnpj.gerar().rawValue
    nome_fantasia = gerar_nome(2)
    inscricao_estadual_sc = random.randint(100000000, 999999999)
    csc = gerar_csc()

    ambiente = "2"  # 1 =producao, 2 = homologação
    id_paf = "123456"  # fornecido pelo fabricante, diferente por consumidor
    endereco_sefaz = "enderecosefaz"

    empresa = Empresa(nome, telefone, email, cnpj, nome_fantasia, inscricao_estadual_sc, csc, 1, ambiente, id_paf,
                      endereco_sefaz, 1)
    db.session.add(empresa)

    end = gerar_endereco()
    endereco = Endereco(end.get("endereco"), end.get("cep"), end.get("bairro"), end.get("complemento"),
                        end.get("logradouro"), end.get("numero"),
                        empresa.pessoaJuridica.pessoa, end.get("municipio"))
    db.session.add(endereco)
    db.session.commit()

    return redirect("/listarEmpresa")


@app.route('/edicaoEmpresa/<int:id>')
def edicao_empresa(id=0):
    cli = Empresa.query.filter_by(id=id).first()
    form = EmpresaForm()
    return render_template('registro.html', action="/editarEmpresa/" + str(id), title='Edição de Empresa - ' + cli.nome,
                           form_title="Editar Empresa - " + cli.nome,
                           form=form, columns=Empresa.columns, dados=cli)


@app.route('/editarEmpresa/<int:id>', methods=['POST'])
def editar_empresa(id=0):
    nome = request.form.get('nome')
    telefone = request.form.get('telefone_principal')
    email = request.form.get('email')
    cnpj = request.form.get('cnpj')
    nome_fantasia = request.form.get('nome_fantasia')
    inscricao_estadual_sc = request.form.get('inscricao_estadual_sc')
    ambiente = request.form.get("ambiente")
    idpaf = request.form.get("id_paf")
    autorizadora = request.form.get("endereco_sefaz")

    cli = Empresa.query.filter_by(id=id).first()
    cli.nome = nome
    cli.telefone_principal = telefone
    cli.email = email
    cli.cnpj = re.sub("([\.\-\/])", "", cnpj)
    cli.nome_fantasia = nome_fantasia
    cli.inscricao_estadual_sc = inscricao_estadual_sc
    cli.csc = gerar_csc()
    cli.csc_id = 1
    cli.ambiente = ambiente
    cli.id_paf = idpaf
    cli.endereco_sefaz = autorizadora

    db.session.commit()

    return redirect("/listarEmpresa")


@app.route('/exclusaoEmpresa/<int:id>', methods=['GET'])
def exclusao_empresa(id=0):
    endereco = Endereco.query.filter_by(pessoa_fk_id=id).first()
    db.session.delete(endereco)

    empresa = Empresa.query.filter_by(id=id).first()

    db.session.delete(empresa)

    db.session.commit()

    return redirect("/listarEmpresa")


@app.route('/alterarTpEmis', methods=['POST'])
def alterar_tp_emis():
    tpemis = request.values.get('tpEmis')
    empresa = Empresa.query.first()
    empresa.tp_emis = tpemis

    db.session.commit()

    return "ok"
