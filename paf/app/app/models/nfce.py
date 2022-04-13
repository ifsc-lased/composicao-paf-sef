import datetime

from app import db
from app.models.venda import Venda


class Nfce(db.Model):
    __tablename__ = 'nfce'
    __bind_key__ = "paf"

    columns = [
        {
            "field": "id",
            "title": "#",
            "sortable": True,
            "type": "id",
            "class": "hide"
        },
        {
            "field": "nnf",
            "title": "Núm.",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "dh_emi",
            "title": "Data/Hora",
            "sortable": True,
            "type": "date_time",
            "class": "date_time"
        },
        {
            "field": "tp_emis",
            "title": "Tp. Emis.",
            "sortable": True,
            "type": "label",
            "label_class": "nfce",
            "class": ""
        },
        {
            "field": "tp_amb",
            "title": "Ambiente",
            "sortable": True,
            "type": "label",
            "label_class": "nfce",
            "class": ""
        },
        {
            "field": "situacao",
            "title": "Situação",
            "sortable": True,
            "type": "label",
            "label_class": "nfce",
            "class": ""
        },
        {
            "field": "status",
            "title": "R. SVRS",
            "sortable": True,
            "type": "label",
            "label_class": "nfce",
            "class": ""
        },
        {
            "field": "venda",
            "title": "Venda",
            "sortable": True,
            "type": "fk",
            "sec_obj": "venda",
            "sec_field": "id",
            "sec_id": "id",
            "sec_value": "venda_fk_id",
            "sec_link": "selecionarVendaItem",
            "class": "link"
        },
        {
            "field": "resultado_aut_daf",
            "title": "R. SEF",
            "sortable": True,
            "type": "label",
            "label_class": "nfce",
            "class": ""
        },
        {
            "field": "retida_daf",
            "title": "Retida?",
            "sortable": True,
            "type": "bool",
            "class": ""
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
    chave_acesso = db.Column(db.Integer, nullable=True)
    dh_emi = db.Column(db.DateTime, nullable=False)
    tp_emis = db.Column(db.Integer, nullable=False)
    tp_amb = db.Column(db.Integer, nullable=False)
    nnf = db.Column(db.Integer, nullable=False)
    situacao = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    resultado_aut_daf = db.Column(db.Integer, nullable=False)
    xml = db.Column(db.String(6500000000), nullable=False)
    xml_distribuicao = db.Column(db.String(6500000000), nullable=False)
    ret_sefaz = db.Column(db.String(6500000000), nullable=True)
    protocolo = db.Column(db.String(15), nullable=True)
    id_aut_daf = db.Column(db.String(600), nullable=True)
    aut_apg_daf = db.Column(db.String(600), nullable=True)
    retida_daf = db.Column(db.Boolean, nullable=True)

    venda_fk_id = db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=True)
    venda = db.relationship(Venda, lazy=True)

    def __init__(self, chave_acesso, tp_emis, tp_amb, venda, nnf, xml):
        self.dh_emi = datetime.datetime.now().strftime("%Y-%m-%d %X")
        self.chave_acesso = chave_acesso
        self.tp_emis = tp_emis
        self.tp_amb = tp_amb
        self.venda = venda
        self.nnf = nnf
        self.xml = xml
        self.ret_sefaz = None
        self.situacao = 0  # não enviado
        self.status = None
        self.protocolo = None
        self.xml_distribuicao = None
        self.retida_daf = True
        #
    # def __repr__(self):
    #     return '<Cliente %r>' % self.pessoa_fk_id
