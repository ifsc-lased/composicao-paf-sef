import datetime

from app import db


class Daf(db.Model):
    __tablename__ = 'daf'
    __bind_key__ = "paf"

    columns = [
        {
            "field": "id_daf",
            "title": "idDaf",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "modo_operacao",
            "title": "Modo Op.",
            "sortable": True,
            "type": "label",
            "label_class": "daf",
            "class": ""
        },
        {
            "field": "cnpj_fabricante",
            "title": "Fabricante",
            "sortable": False,
            "type": "label",
            "label_class": "daf",
            "class": ""
        },
        {
            "field": "modelo",
            "title": "Modelo",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "contador",
            "title": "Cont.",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "situacao",
            "title": "Situação",
            "sortable": False,
            "type": "label",
            "label_class": "daf",
            "class": ""
        },
        {
            "field": "num_dfe",
            "title": "Qnt DF-e",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "ocupacao",
            "title": "Ocupação",
            "sortable": False,
            "type": "label",
            "label_class": "daf",
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
    id_daf = db.Column(db.String(22), nullable=False)
    modo_operacao = db.Column(db.Integer, nullable=False)
    versao_sb = db.Column(db.Integer, nullable=False)
    hash_sb = db.Column(db.String(43), nullable=False)
    cnpj_fabricante = db.Column(db.String(14), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    contador = db.Column(db.Integer, nullable=False)
    certificado_sef = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(10), nullable=False)
    ultimo_token = db.Column(db.String(255), nullable=False)
    max_dfe = db.Column(db.Integer, nullable=False)
    num_dfe = db.Column(db.Integer, nullable=False)
    porta = db.Column(db.String(255), nullable=False)
    data_extravio = db.Column(db.DateTime, nullable=True)
    data_registro = db.Column(db.DateTime, nullable=True)
    data_insercao = db.Column(db.DateTime, nullable=True)
    chave_paf = db.Column(db.String(255), nullable=True)
    situacao = db.Column(db.Integer, nullable=True)

    def __init__(self, id_daf=None, modo_operacao=None, versao_sb=None, hash_sb=None, cnpj_fabricante=None, modelo=None,
                 contador=None, certificado_sef=None, estado=None, ultimo_token=None, max_dfe=None, num_dfe=None,
                 porta=None):
        self.id_daf = id_daf
        self.modo_operacao = modo_operacao
        self.versao_sb = versao_sb
        self.hash_sb = hash_sb
        self.cnpj_fabricante = cnpj_fabricante
        self.modelo = modelo
        self.contador = contador
        self.certificado_sef = certificado_sef
        self.estado = estado
        self.ultimo_token = ultimo_token
        self.max_dfe = max_dfe
        self.num_dfe = num_dfe
        self.porta = porta
        self.data_insercao = datetime.datetime.now().strftime("%Y-%m-%d %X")
    #
    # def __repr__(self):
    #     return '<Cliente %r>' % self.pessoa_fk_id
