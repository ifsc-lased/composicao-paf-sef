import datetime

from app import db
from app.models.pontoVenda import PontoVenda


class FuncionarioPdv(db.Model):
    __tablename__ = 'funcionario_pdv'
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
            "field": "funcionario",
            "title": "Funcionario",
            "sortable": True,
            "type": "fk",
            "sec_obj": "funcionario",
            "sec_field": "nome",
            "sec_id": "pessoa_fisica_fk_id",
            "sec_value": "funcionario_fk_id",
            "sec_link": "selecionarFuncionario",
            "class": "link"
        },
        {
            "field": "pdv",
            "title": "PDV",
            "sortable": True,
            "type": "fk",
            "sec_obj": "pdv",
            "sec_field": "nome",
            "sec_id": "id",
            "sec_value": "ponto_venda_fk_id",
            "sec_link": "selecionarPdv",
            "class": "link"
        },
        {
            "field": "data_hora_login",
            "title": "Data/Hora",
            "sortable": True,
            "type": "date_time",
            "class": "date_time"
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
    ponto_venda_fk_id = db.Column(db.Integer, db.ForeignKey('ponto_venda.id'))
    pdv = db.relationship(PontoVenda, back_populates="logins")

    funcionario_fk_id = db.Column(db.Integer, db.ForeignKey('funcionario.pessoa_fisica_fk_id'))
    funcionario = db.relationship('Funcionario', back_populates="logins")

    data_hora_login = db.Column(db.DateTime, nullable=False)

    def __init__(self, pdv, funcionario):
        self.pdv = pdv
        self.funcionario = funcionario
        self.data_hora_login = datetime.datetime.now().strftime("%Y-%m-%d %X")

    def __repr__(self) -> str:
        return super().__repr__()
