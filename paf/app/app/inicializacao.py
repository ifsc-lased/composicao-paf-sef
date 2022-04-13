from flask import jsonify
from sqlalchemy import desc

from app import session


class Inicializacao:
    @staticmethod
    def set_login():
        from app.models.funcionarioPdv import FuncionarioPdv
        login = FuncionarioPdv.query.order_by(desc(FuncionarioPdv.data_hora_login)).first()

        session["funcionario_pdv"] = login.id
        session["empresa"] = login.pdv.empresa.id
        session["pdv"] = login.pdv.id_pdv
        session["pdv_nome"] = login.pdv.nome
        session["user"] = login.funcionario.login

        return jsonify(pdv=login.pdv.id_pdv, pdv_nome=login.pdv.nome, user=login.funcionario.login)
