from app import db
from app.models.pessoaFisica import PessoaFisica


class Cliente(PessoaFisica):
    __tablename__ = 'cliente'
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
            "field": "cpf",
            "title": "CPF",
            "sortable": True,
            "type": "cpf",
            "class": "cpf"
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
            "field": "ops",
            "title": "Opções",
            "sortable": False,
            "type": "ops",
            "class": ""
        }
    ]

    pessoa_fisica_fk_id = db.Column(db.Integer, db.ForeignKey('pessoa_fisica.pessoa_fk_id'), primary_key=True)
    pessoaFisica = db.relationship(PessoaFisica, lazy=True)

    def __init__(self, nome, telefone, email, cpf):
        super().__init__(nome, telefone, email, cpf)

    @staticmethod
    def testeRelacoesDelete(id):
        from app.models.venda import Venda
        vendas = len(Venda.query.filter_by(cliente_fk_id=id).all())

        return vendas == 0
