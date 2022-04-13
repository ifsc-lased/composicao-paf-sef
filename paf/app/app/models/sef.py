import datetime

from app import db


class Sef(db.Model):
    __tablename__ = 'xml_distribuicao'
    __bind_key__ = "ws"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    protocolo_autorizacao = db.Column(db.String(15), unique=True, nullable=False)
    xml = db.Column(db.String(6500000000), nullable=False)
    data_inclusao = db.Column(db.DateTime, nullable=False)
    data_processamento = db.Column(db.DateTime, nullable=True)

    def __init__(self, protocolo, xml):
        self.protocolo_autorizacao = protocolo
        self.xml = xml
        self.data_inclusao = datetime.datetime.now().strftime("%Y-%m-%d %X")

    def __repr__(self) -> str:
        return super().__repr__()
