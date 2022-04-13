from app import db
from app.models.empresa import Empresa
from app.models.funcionarioPdv import FuncionarioPdv
from app.models.pessoaFisica import PessoaFisica


class Funcionario(PessoaFisica):
    __tablename__ = 'funcionario'
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
            "field": "login",
            "title": "Login",
            "sortable": True,
            "type": "",
            "class": ""
        },
        {
            "field": "senha",
            "title": "Senha",
            "sortable": False,
            "type": "password",
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

    pessoa_fisica_fk_id = db.Column(db.Integer, db.ForeignKey('pessoa_fisica.pessoa_fk_id'), primary_key=True)
    pessoaFisica = db.relationship(PessoaFisica, lazy=True)
    login = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    empresa_fk_id = db.Column(db.Integer, db.ForeignKey('empresa.pessoa_juridica_fk_id'))
    empresa = db.relationship(Empresa, lazy=True)

   
    logins = db.relationship(FuncionarioPdv, back_populates="funcionario")

  

    def __init__(self, nome, telefone, email, login, empresa, cpf='12345697'):
        super().__init__(nome, telefone, email, cpf)
        self.empresa = empresa
        self.login = login
        self.senha = '1234'

  
    @staticmethod
    def testeRelacoesDelete(id):
        from app.models.funcionarioPdv import FuncionarioPdv
        from app.models.venda import Venda
        logins = len(FuncionarioPdv.query.filter_by(funcionario_fk_id=id).all())
        vendas = len(Venda.query.filter_by(funcionario_pdv_fk_id=id).all())

        return logins == 0 and vendas == 0
