import datetime

from app import db
from app.models.nfce import Nfce


class Requisicao(db.Model):
    __tablename__ = 'requisicao'
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
            "field": "pedido",
            "title": "Pedido",
            "sortable": True,
            "type": "date_time",
            "class": "date_time"
        },
        {
            "field": "resposta",
            "title": "Resposta",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "servico",
            "title": "Serviço",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "nfce",
            "title": "NFC-e",
            "sortable": True,
            "type": "fk",
            "sec_obj": "nfce",
            "sec_field": "chave_acesso",
            "sec_id": "chave_acesso",
            "sec_value": "nfce_fk_chave_acesso",
            "sec_link": "listarNfce",
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
    pedido = db.Column(db.Text, nullable=False)
    resposta = db.Column(db.Text, nullable=True)
    servico = db.Column(db.String(255), nullable=False)
    dhEmi = db.Column(db.DateTime, nullable=False)

    nfce_fk_chave_acesso = db.Column(db.Integer, db.ForeignKey('requisicao.id'), nullable=True)
    nfce = db.relationship(Nfce, lazy=True)

    def __init__(self, pedido, resposta, servico, nfce, data_hora):
        self.data_hora = datetime.datetime.now().strftime("%Y-%m-%d %X")
        self.pedido = pedido
        self.resposta = resposta
        self.servico = servico
        self.nfce = nfce
        #
    # def __repr__(self):
    #     return '<Cliente %r>' % self.pessoa_fk_id
