from app import db


class Uf(db.Model):
    __tablename__ = 'uf'
    __bind_key__ = "paf"

    codigo_ibge = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sigla = db.Column(db.String(2), nullable=False)

    def __init__(self, codigo_ibge, nome, sigla):
        self.codigo_ibge = codigo_ibge
        self.nome = nome
        self.sigla = sigla

    def __repr__(self) -> str:
        return super().__repr__()
