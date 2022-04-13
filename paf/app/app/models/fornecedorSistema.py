from app import db
from app.models.pessoaJuridica import PessoaJuridica


class FornecedorSistema(PessoaJuridica):
    __tablename__ = 'fornecedor_sistema'
    __bind_key__ = "paf"

    pessoa_juridica_fk_id = db.Column(db.Integer, db.ForeignKey('pessoa_juridica.pessoa_fk_id'), primary_key=True)
    pessoaJuridica = db.relationship(PessoaJuridica, lazy=True)
    id_csrt = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, telefone, email, cnpj, nome_fantasia, inscricao_estadual_sc, id_csrt):
        super().__init__(nome, telefone, email, cnpj, nome_fantasia, inscricao_estadual_sc)
        self.id_csrt = id_csrt
