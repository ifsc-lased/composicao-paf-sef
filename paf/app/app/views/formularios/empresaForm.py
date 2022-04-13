from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired


class EmpresaForm(FlaskForm):
    id = StringField('Código', render_kw={'disabled': ''})
    nome = StringField('Razão Social', validators=[DataRequired('Nome não pode ficar vazio')])
    nome_fantasia = StringField('Nome Fantasia', validators=[DataRequired('Nome não pode ficar vazio')])
    telefone_principal = StringField('Telefone', validators=[DataRequired('Telefone não pode ficar vazio')])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio')])
    cnpj = StringField('CNPJ', validators=[DataRequired('CPF não pode ficar vazio')])
    inscricao_estadual_sc = StringField('IE-SC', validators=[DataRequired('IE-SC não pode ficar vazio')])
    csc = StringField('csc', validators=[DataRequired('Código de segurança do contribuinte não pode ficar vazio')])
    csc_id = StringField('csc_id',
                         validators=[DataRequired('Código de segurança do contribuinte não pode ficar vazio')])
    tp_emis = StringField('tp_emis', validators=[DataRequired('tp_emis não pode ficar vazio')])
    ambiente = RadioField(label="Ambiente de emissão", choices=[('1', 'Produção'), ('2', 'Homologação')])
    id_paf = StringField('idPAF')
    endereco_sefaz = StringField('Autorizadora')
