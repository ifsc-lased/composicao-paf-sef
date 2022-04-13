import datetime

from app import db
from app.models.cliente import Cliente
from app.models.funcionarioPdv import FuncionarioPdv


class Venda(db.Model):
    __tablename__ = 'venda'
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
            "field": "data_hora",
            "title": "Data/Hora",
            "sortable": True,
            "type": "date_time",
            "class": "date_time"
        },
        {
            "field": "desconto",
            "title": "Desconto (R$)",
            "sortable": True,
            "type": "perc",
            "class": "perc"
        },
        {
            "field": "valor_total",
            "title": "Valor Total (R$)",
            "sortable": False,
            "type": "money",
            "class": "money"
        },
        {
            "field": "funcionario",
            "title": "Funcionário",
            "sortable": True,
            "type": "fkn",
            "sec_obj": "funcionario_pdv",
            "ter_obj": "funcionario",
            "sec_field": "nome",
            "sec_id": "funcionario_fk_id",
            "sec_value": "id",
            "sec_link": "selecionarFuncionario",
            "class": "link"
        },
        {
            "field": "pdv",
            "title": "PDV",
            "sortable": True,
            "type": "fkn",
            "sec_obj": "funcionario_pdv",
            "ter_obj": "pdv",
            "sec_field": "nome",
            "sec_id": "ponto_venda_fk_id",
            "sec_value": "id",
            "sec_link": "selecionarPdv",
            "class": "link"
        },
        {
            "field": "ops",
            "title": "Opções",
            "sortable": False,
            "type": "ops",
            "class": ""
        }
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    desconto = db.Column(db.Float, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)

    cliente_fk_id = db.Column(db.Integer, db.ForeignKey('cliente.pessoa_fisica_fk_id'), nullable=True)
    cliente = db.relationship(Cliente, lazy=True)

    funcionario_pdv_fk_id = db.Column(db.Integer, db.ForeignKey('funcionario_pdv.id'), nullable=True)
    funcionario_pdv = db.relationship(FuncionarioPdv, lazy=True)

    def __init__(self, desconto, valor_total, cliente, funcionario_pdv):
        self.data_hora = datetime.datetime.now().strftime("%Y-%m-%d %X")
        self.desconto = desconto
        self.valor_total = valor_total
        self.cliente = cliente
        self.funcionario_pdv = funcionario_pdv
