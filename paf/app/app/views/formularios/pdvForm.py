from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from app.models.empresa import Empresa


def get_empresas():
    return Empresa.query.all()


class PdvForm(FlaskForm):
    id = StringField('Código', render_kw={'disabled': ''})
    nome = StringField('Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    serial = StringField('Serial', validators=[DataRequired('Serial não pode ficar vazio')])
    id_pdv = StringField('idPDV', validators=[DataRequired('idPDV não pode ficar vazio')])
    empresa = QuerySelectField('Empresa', validators=[DataRequired('Empresa não pode ficar vazio')],
                               query_factory=get_empresas, get_label='nome')
