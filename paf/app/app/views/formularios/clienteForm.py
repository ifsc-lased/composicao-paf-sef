from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ClienteForm(FlaskForm):
    id = StringField('Código', render_kw={'disabled': ''})
    nome = StringField('Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    telefone_principal = StringField('Telefone', validators=[DataRequired('Telefone não pode ficar vazio')])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio')])
    cpf = StringField('CPF', validators=[DataRequired('CPF não pode ficar vazio')])
