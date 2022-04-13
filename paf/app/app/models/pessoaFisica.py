import re

from app import db
from app.models.pessoa import Pessoa


class PessoaFisica(Pessoa):
    __tablename__ = 'pessoa_fisica'
    __bind_key__ = "paf"

    pessoa_fk_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), primary_key=True)
    pessoa = db.relationship(Pessoa, lazy=True)
    cpf = db.Column(db.String(11))

    def __init__(self, nome, telefone, email, cpf):
        super().__init__(nome, telefone, email)
        self.cpf = re.sub("([.-])", "", cpf)

