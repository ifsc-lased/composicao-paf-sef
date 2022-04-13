from app import db
from app.models.uf import Uf


class Municipio(db.Model):
    __tablename__ = 'municipio'
    __bind_key__ = "paf"

    codigo_ibge = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)

    uf_codigo_ibge = db.Column(db.Integer, db.ForeignKey('uf.codigo_ibge'), primary_key=True)
    uf = db.relationship(Uf, lazy=True)

    def __init__(self, codigo_ibge, nome, uf):
        self.codigo_ibge = codigo_ibge
        self.nome = nome
        self.uf = uf

    def __repr__(self) -> str:
        return super().__repr__()
