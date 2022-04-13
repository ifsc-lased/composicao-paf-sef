from app import db
from app.models.produto import Produto
from app.models.venda import Venda


class VendaItem(db.Model):
    __tablename__ = 'venda_item'
    __bind_key__ = "paf"

    columns = [
        {
            "field": "id",
            "title": "#",
            "sortable": True,
            "type": "id",
            "class": ""
        },
        {
            "field": "produto",
            "title": "Produto",
            "sortable": True,
            "type": "fk",
            "sec_obj": "produto",
            "sec_field": "nome",
            "sec_id": "id",
            "sec_value": "produto_fk_id",
            "sec_link": "selecionarProduto",
            "class": "link"
        },
        {
            "field": "quantidade",
            "title": "Qnt",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "valor_unitario",
            "title": "Valor Unitário (R$)",
            "sortable": True,
            "type": "fk",
            "sec_obj": "produto",
            "sec_field": "valor_unitario",
            "sec_id": "id",
            "sec_value": "produto_fk_id",
            "sec_link": "selecionarProduto",
            "class": "money"
        },
        {
            "field": "valor_item",
            "title": "Valor (R$)",
            "sortable": True,
            "type": "money",
            "class": "money"
        }
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer, nullable=False)
    valor_item = db.Column(db.Float, nullable=False)

    venda_fk_id = db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=True)
    venda = db.relationship(Venda, lazy=True)

    produto_fk_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=True)
    produto = db.relationship(Produto, lazy=True)

    def __init__(self, quantidade, valor_item, venda, produto):
        self.quantidade = quantidade
        self.valor_item = valor_item
        self.venda = venda
        self.produto = produto
        #
    # def __repr__(self):
    #     return '<Cliente %r>' % self.pessoa_fk_id
