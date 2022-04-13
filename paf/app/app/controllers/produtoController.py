import random
import re

from flask import request, redirect, render_template

from app import app
from app import db
from app.models.produto import Produto
from app.utils.formats import get_all
from app.utils.geradores import gerar_nome
from app.views.formularios.produtoForm import ProdutoForm


@app.route('/listarProduto')
def listar_produto():
    data = get_all(Produto.query.all(), Produto.columns,
                   [{"btn": "edt", "rota": "edicaoProduto"}, {"btn": "del", "rota": "exclusaoProduto"}])
    return render_template('listagem.html', data=data, columns=Produto.columns, title='Produtos',
                           add='/cadastroProduto', gerar='/gerarProduto', label='Produto')


@app.route('/selecionarProduto/<int:id>', methods=['GET'])
def selecionar_produto(id=0):
    data = get_all(Produto.query.filter_by(id=id), Produto.columns,
                   [{"btn": "edt", "rota": "edicaoProduto"}, {"btn": "del", "rota": "exclusaoProduto"}])
    return render_template('listagem.html', data=data, columns=Produto.columns,
                           add='/cadastroProduto', label='Produto', title='Produto ' + data[0]['nome'])


@app.route('/cadastroProduto')
def cadastro_produto():
    form = ProdutoForm()
    return render_template('registro.html', action="/salvarProduto", title='Cadastrar Produto',
                           form_title="Cadastrar Produto",
                           form=form, columns=Produto.columns, dados='')


@app.route('/gerarProduto')
def gerar_produto():
    nome = gerar_nome(2)
    marca = gerar_nome(1)
    cfop = '5102'
    cean = 'SEM GTIN'
    ncm = random.randint(10000000, 99999999)
    valor_unitario = 1.99
    perc_trib = random.randint(1, 52) / 100
    icms_modalidade = '102'
    icms_csosn = '400'
    icms_cst = '07'
    unidade = 'UN'

    produto = Produto(nome, marca, cfop, cean, ncm, valor_unitario, perc_trib, icms_modalidade, icms_csosn, icms_cst,
                      unidade)
    db.session.add(produto)
    db.session.commit()

    return redirect("/listarProduto")


@app.route('/salvarProduto', methods=['POST'])
def salvar_produto():
    nome = request.form.get('nome')
    marca = request.form.get('marca')
    cfop = request.form.get('cfop')
    cean = request.form.get('cean')
    ncm = request.form.get('ncm')
    valor_unitario = request.form.get('valor_unitario')
    valor_unitario = re.sub(",", ".", re.sub("(\.)", "", valor_unitario))

    produto = Produto(nome, marca, cfop, cean, ncm, valor_unitario)
    db.session.add(produto)
    db.session.commit()

    return redirect("/listarProduto")


@app.route('/edicaoProduto/<int:id>')
def edicao_produto(id=0):
    pro = Produto.query.filter_by(id=id).first()
    form = ProdutoForm()
    return render_template('registro.html', action="/editarProduto/" + str(id),
                           title='Editar Produto - ' + pro.nome,
                           form_title="Editar Produto - " + pro.nome,
                           form=form, columns=Produto.columns, dados=pro)


@app.route('/editarProduto/<int:id>', methods=['POST'])
def editar_produto(id=0):
    nome = request.form.get('nome')
    marca = request.form.get('marca')
    cfop = request.form.get('cfop')
    cean = request.form.get('cean')
    ncm = request.form.get('ncm')
    valor_unitario = request.form.get('valor_unitario')

    pro = Produto.query.filter_by(id=id).first()
    pro.nome = nome
    pro.marca = marca
    pro.cfop = cfop
    pro.cean = cean
    pro.ncm = ncm
    pro.valor_unitario = re.sub(",", ".", re.sub("(\.)", "", valor_unitario))

    db.session.commit()

    return redirect("/listarProduto")


@app.route('/exclusaoProduto/<int:id>', methods=['GET'])
def exclusao_produto(id=0):
    produto = Produto.query.filter_by(id=id).first()

    db.session.delete(produto)

    db.session.commit()

    return redirect("/listarProduto")
