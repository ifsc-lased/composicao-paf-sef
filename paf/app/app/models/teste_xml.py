from app import db


class TesteWs(db.Model):
    __tablename__ = 'teste_ws'
    __bind_key__ = "ws"

    columns = [
        {
            "field": "id",
            "title": "#",
            "sortable": False,
            "type": "id",
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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    xml = db.Column(db.String(6500000000), nullable=True)

    def __init__(self, xml):
        self.xml = xml

        #
    # def __repr__(self):
    #     return '<Cliente %r>' % self.pessoa_fk_id
