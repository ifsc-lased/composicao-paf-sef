from app import db
from app.models.pessoaJuridica import PessoaJuridica


class Empresa(PessoaJuridica):
    __tablename__ = 'empresa'
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
            "field": "cnpj",
            "title": "CNPJ",
            "sortable": True,
            "type": "cnpj",
            "class": "cnpj"
        },
        {
            "field": "nome",
            "title": "Razão Social",
            "sortable": True,
            "type": "nome",
            "class": ""
        },
        {
            "field": "nome_fantasia",
            "title": "Nome Fantasia",
            "sortable": True,
            "type": "string",
            "class": ""
        },
        {
            "field": "telefone_principal",
            "title": "Telefone",
            "sortable": False,
            "type": "tel",
            "class": "phone"
        },
        {
            "field": "email",
            "title": "E-mail",
            "sortable": False,
            "type": "email",
            "class": "sem_espaco"
        },
        {
            "field": "csc_id",
            "title": "CSC-ID",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "inscricao_estadual_sc",
            "title": "IE-SC",
            "sortable": False,
            "type": "string",
            "class": "sem_espaco"
        },
        {
            "field": "ambiente",
            "title": "Ambiente",
            "sortable": True,
            "type": "label",
            "label_class": "empresa",
            "class": ""
        },
        {
            "field": "id_paf",
            "title": "idPAF",
            "sortable": True,
            "type": "hide",
            "class": ""
        },
        {
            "field": "endereco_sefaz",
            "title": "Autorizadora",
            "sortable": True,
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

    pessoa_juridica_fk_id = db.Column(db.Integer, db.ForeignKey('pessoa_juridica.pessoa_fk_id'), primary_key=True)
    pessoaJuridica = db.relationship(PessoaJuridica, lazy=True)
    csc_id = db.Column(db.Integer, nullable=False)
    csc = db.Column(db.String, nullable=False)
    ambiente = db.Column(db.Integer, nullable=False)
    id_paf = db.Column(db.String, nullable=False)
    endereco_sefaz = db.Column(db.String, nullable=False)
    tp_emis = db.Column(db.Integer, nullable=False, default=1)
    nome_certificado = db.Column(db.String, nullable=False)
    senha_certificado = db.Column(db.String, nullable=False)

    def __init__(self, nome, telefone, email, cnpj, nome_fantasia, inscricao_estadual_sc, csc, csc_id, ambiente, id_paf,
                 endereco_sefaz, tp_emis):
        super().__init__(nome, telefone, email, cnpj, nome_fantasia, inscricao_estadual_sc)
        self.csc = csc
        self.csc_id = csc_id
        self.ambiente = ambiente
        self.id_paf = id_paf
        self.endereco_sefaz = endereco_sefaz
        self.tp_emis = tp_emis

    def get_csc_id(self):
        return "{:6}".format(self.csc_id).replace(" ", "")

    def get_certificado(self):
        return "resources/" + self.nome_certificado, self.senha_certificado

    #
    # def __repr__(self):
    #     return '<Pessoa %r>' % self.nome

    @staticmethod
    def testeRelacoesDelete(id):
        from app.models.pontoVenda import PontoVenda
        from app.models.funcionario import Funcionario
        pdv = len(PontoVenda.query.filter_by(empresa_fk_id=id).all())
        funcionario = len(Funcionario.query.filter_by(empresa_fk_id=id).all())

        return pdv == 0 and funcionario == 0
