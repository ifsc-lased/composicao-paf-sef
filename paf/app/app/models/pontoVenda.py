from app import db

from app.models.empresa import Empresa


class PontoVenda(db.Model):
    __tablename__ = 'ponto_venda'
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
            "field": "serial",
            "title": "Serial",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "id_pdv",
            "title": "idPDV",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "empresa",
            "title": "Empresa",
            "sortable": True,
            "type": "fk",
            "sec_obj": "empresa",
            "sec_field": "nome",
            "sec_id": "pessoa_juridica_fk_id",
            "sec_value": "empresa_fk_id",
            "sec_link": "selecionarEmpresa",
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
    nome = db.Column(db.String(255), nullable=False)
    serial = db.Column(db.String(255), nullable=False)
    id_pdv = db.Column(db.String(10), nullable=False)

    empresa_fk_id = db.Column(db.Integer, db.ForeignKey('empresa.pessoa_juridica_fk_id'))
    empresa = db.relationship(Empresa, lazy=True)

    logins = db.relationship("FuncionarioPdv", back_populates="pdv")

    # logins = db.relationship("FuncionarioPdv", back_populates="funcionario")

    def __init__(self, nome, serial, id_pdv, empresa):
        self.serial = serial
        self.nome = nome
        self.id_pdv = id_pdv
        self.empresa = empresa

    def __repr__(self) -> str:
        return super().__repr__()

    @staticmethod
    def testeRelacoesDelete(id):
        from app.models.funcionarioPdv import FuncionarioPdv
        logins = len(FuncionarioPdv.query.filter_by(ponto_venda_fk_id=id).all())

        return logins == 0
