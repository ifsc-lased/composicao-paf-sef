from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from app.models.empresa import Empresa


def get_empresas():
    return Empresa.query.all()


class FuncionarioForm(FlaskForm):
    id = StringField('Código', render_kw={'disabled': ''})
    nome = StringField('Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    telefone_principal = StringField('Telefone', validators=[DataRequired('Telefone não pode ficar vazio')])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio')])
    login = StringField('Login', validators=[DataRequired('Login não pode ficar vazio')])
    cpf = StringField('CPF', validators=[DataRequired('CPF não pode ficar vazio')])
    senha = PasswordField('Senha', validators=[DataRequired('Senha não pode ficar vazio')])
    empresa = QuerySelectField('Empresa', validators=[DataRequired('Empresa não pode ficar vazio')],
                               query_factory=get_empresas, get_label='nome')
