from app import db
from app.models.municipio import Municipio


# from app.models.pessoa import Pessoa


class Endereco(db.Model):
    __tablename__ = 'endereco'
    __bind_key__ = "paf"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    endereco = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(255), nullable=False)
    bairro = db.Column(db.String(255), nullable=False)
    complemento = db.Column(db.String(255), nullable=False)
    logradouro = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(255), nullable=False)

    pessoa_fk_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
    pessoa = db.relationship('Pessoa', back_populates="enderecos")

    municipio_fk_codigo_ibge = db.Column(db.Integer, db.ForeignKey('municipio.codigo_ibge'))
    municipio = db.relationship(Municipio, lazy=True)

    def __init__(self, endereco, cep, bairro, complemento, logradouro, numero, pessoa, municipio):
        self.endereco = endereco
        self.cep = cep
        self.bairro = bairro
        self.complemento = complemento
        self.logradouro = logradouro
        self.numero = numero
        self.pessoa = pessoa
        self.municipio = municipio

    def __repr__(self) -> str:
        return super().__repr__()
