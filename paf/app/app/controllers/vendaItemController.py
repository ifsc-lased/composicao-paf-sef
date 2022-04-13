from flask import render_template

from app import app
from app.models.venda import Venda
from app.models.vendaItem import VendaItem
from app.utils.formats import format_money
from app.utils.formats import get_all


@app.route('/selecionarVendaItem/<int:id>', methods=['GET'])
def selecionar_venda_item(id=0):
    venda = Venda.query.filter_by(id=id).first()
    data = get_all(VendaItem.query.filter_by(venda_fk_id=id), VendaItem.columns, [])
    return render_template('listagem.html', data=data, columns=VendaItem.columns,
                           add='', gerar='', label='',
                           title='Visualizar venda ' + str(id) + ' - ' + venda.data_hora.strftime(
                               "%d/%m/%Y %H:%M") + ' - ' + format_money(venda.valor_total))
