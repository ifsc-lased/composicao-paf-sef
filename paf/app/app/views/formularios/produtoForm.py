from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired


class ProdutoForm(FlaskForm):
    id = StringField('Código', render_kw={'disabled': ''})
    nome = StringField('Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    marca = StringField('Marca', validators=[DataRequired('Marca não pode ficar vazio')])
    cfop = StringField('CFOP', validators=[DataRequired('CFOP não pode ficar vazio')])
    cean = StringField('cEAN', validators=[DataRequired('cEAN não pode ficar vazio')])
    ncm = StringField('NCM', validators=[DataRequired('NCM não pode ficar vazio')])
    valor_unitario = FloatField('Valor Unitário (R$)', validators=[DataRequired('Valor unitário não pode ficar vazio')])
