import random

from flask import session, render_template, redirect
from sqlalchemy import desc

from app import app, db
from app.controllers.nfceController import gerar_nfe
from app.models.cliente import Cliente
from app.models.funcionarioPdv import FuncionarioPdv
from app.models.produto import Produto
from app.models.venda import Venda
from app.models.vendaItem import VendaItem
from app.utils.formats import get_all


@app.route('/listarVenda')
def listar_venda():
    data = get_all(Venda.query.order_by(desc(Venda.data_hora)).all(), Venda.columns,
                   [{"btn": "sel", "rota": "selecionarVendaItem"}, {"btn": "nfce", "rota": "selecionarNfce"}])
    return render_template('listagem.html', data=data, columns=Venda.columns, title='Vendas',
                           add='', gerar='/gerarVenda', g2='/gerarVendaSemDaf', label='Venda')


@app.route('/gerarVenda')
def gerar_venda_ok():
    return gerar_venda()


@app.route('/gerarVendaSemDaf')
def gerar_venda_sd():
    return gerar_venda(True)


def nova_venda(qnt_itens=0):
    desconto = random.randint(0, 15) / 100
    valor_total = 0

    clientes = Cliente.query.all()
    cliente = clientes[random.randint(0, len(clientes) - 1)]
    if session.get("funcionario_pdv") is None:
        raise Exception("A sessão expirou.")
    venda = Venda(desconto, valor_total, cliente,
                  FuncionarioPdv.query.filter_by(id=session.get("funcionario_pdv")).first())
    db.session.add(venda)

    if qnt_itens == 0:
        qnt = random.randint(1, 15)
    else:
        qnt = qnt_itens
    produtos = Produto.query.all()
    qntProd = len(produtos) - 1

    for i in range(0, qnt):
        produto = produtos[random.randint(0, qntProd)]
        quantidade = random.randint(1, 5)
        valor = produto.valor_unitario * quantidade
        valor_total = valor_total + valor
        vi = VendaItem(quantidade, valor, venda, produto)
        db.session.add(vi)

    venda.valor_total = valor_total - (valor_total * desconto)
    return venda


def gerar_venda(sem_daf=False):
    venda = nova_venda()
    db.session.add(venda)
    nfce = gerar_nfe(venda, sem_daf)
    if nfce is not None:
        db.session.add(nfce)
        db.session.commit()
    else:
        db.session.rollback()

    return redirect("/listarVenda")


def delete_venda(id=0):
    venda_item = VendaItem.query.filter_by(venda_fk_id=id).all()
    for vi in venda_item:
        db.session.delete(vi)
    venda = Venda.query.filter_by(id=id).first()
    db.session.delete(venda)
    db.session.commit()
