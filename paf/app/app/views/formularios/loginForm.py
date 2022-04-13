from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from app.models.funcionario import Funcionario
from app.models.pontoVenda import PontoVenda


def get_pdvs():
    return PontoVenda.query.all()


def get_funcionarios():
    return Funcionario.query.all()


class LoginForm(FlaskForm):
    id = StringField('Código', render_kw={'disabled': ''})

    funcionario = QuerySelectField('Funcionário', validators=[DataRequired('Funcionário não pode ficar vazio')],
                                   query_factory=get_funcionarios, get_label='nome')
    pdv = QuerySelectField('PDV', validators=[DataRequired('PDV não pode ficar vazio')],
                           query_factory=get_pdvs, get_label='nome')
