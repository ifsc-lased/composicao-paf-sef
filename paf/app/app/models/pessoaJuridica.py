import re

from app import db
from app.models.pessoa import Pessoa


class PessoaJuridica(Pessoa):
    __tablename__ = 'pessoa_juridica'
    __bind_key__ = "paf"

    pessoa_fk_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    pessoa = db.relationship(Pessoa, lazy=True)
    cnpj = db.Column(db.String(14))
    nome_fantasia = db.Column(db.String(255))
    inscricao_estadual_sc = db.Column(db.String(9))

    def __init__(self, nome, telefone, email, cnpj, nome_fantasia, inscricao_estadual_sc):
        super().__init__(nome, telefone, email)
        self.cnpj = '1215'
        self.cnpj = re.sub("([\.\-\/])", "", cnpj)
        self.nome_fantasia = nome_fantasia
        self.inscricao_estadual_sc = inscricao_estadual_sc
    #
    # def __repr__(self):
    #     return '<Pessoa %r>' % self.nome
