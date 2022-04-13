from app import db


# from app.models.endereco import Endereco


class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    __bind_key__ = "paf"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    telefone_principal = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    enderecos = db.relationship("Endereco", back_populates="pessoa")

    def __init__(self, nome="n", telefone_principal=9, email="e"):
        self.nome = nome
        self.telefone_principal = telefone_principal
        self.email = email

    def get_telefone(self):
        import re
        return re.sub("([\ \(\)-])", "", self.telefone_principal)

    def __repr__(self) -> str:
        return super().__repr__()
