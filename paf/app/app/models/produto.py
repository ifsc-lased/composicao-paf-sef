from app import db


class Produto(db.Model):
    __tablename__ = 'produto'
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
            "field": "nome",
            "title": "Nome",
            "sortable": True,
            "type": "nome",
            "class": ""
        },
        {
            "field": "marca",
            "title": "Marca",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "valor_unitario",
            "title": "Valor (R$)",
            "sortable": False,
            "type": "money",
            "class": "money"
        },
        {
            "field": "cfop",
            "title": "CFOP",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "cean",
            "title": "cEAN",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "ncm",
            "title": "NCM",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "perc_trib",
            "title": "perc_trib",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "icms_modalidade",
            "title": "icms_modalidade",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "icms_csosn",
            "title": "icms_csosn",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "icms_cst",
            "title": "icms_cst",
            "sortable": False,
            "type": "",
            "class": ""
        },
        {
            "field": "unidade",
            "title": "unidade",
            "sortable": False,
            "type": "",
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

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    marca = db.Column(db.String(45), nullable=False)
    cfop = db.Column(db.String(4), nullable=False)
    cean = db.Column(db.String(14), nullable=False)
    ncm = db.Column(db.String(8), nullable=False)
    valor_unitario = db.Column(db.Float, nullable=False)
    perc_trib = db.Column(db.Float, nullable=False)
    icms_modalidade = db.Column(db.String(10), nullable=False)
    icms_csosn = db.Column(db.String(10), nullable=False)
    icms_cst = db.Column(db.String(10), nullable=False)
    unidade = db.Column(db.String(10), nullable=False)

    def __init__(self, nome, marca, cfop, cean, ncm, valor_unitario, perc_trib, icms_modalidade, icms_csosn, icms_cst,
                 unidade):
        self.nome = nome
        self.marca = marca
        self.cfop = cfop
        self.cean = cean
        self.ncm = ncm
        self.valor_unitario = valor_unitario
        self.perc_trib = perc_trib
        self.icms_modalidade = icms_modalidade
        self.icms_csosn = icms_csosn
        self.icms_cst = icms_cst
        self.unidade = unidade
        #

    # def __repr__(self):
    #     return '<Cliente %r>' % self.pessoa_fk_id
    @staticmethod
    def testeRelacoesDelete(id):
        from app.models.vendaItem import VendaItem
        vendas = len(VendaItem.query.filter_by(produto_fk_id=id).all())

        return vendas == 0
