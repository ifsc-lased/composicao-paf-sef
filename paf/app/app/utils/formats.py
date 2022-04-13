import datetime

from app.models.cliente import Cliente
from app.models.empresa import Empresa
from app.models.funcionario import Funcionario
from app.models.pontoVenda import PontoVenda
from app.models.produto import Produto
from app.utils.labels import *


# import locale
#
# locale.setlocale(locale.LC_ALL, 'pt_BR')

def ifnull(f, s):
    if f is not None and type(f) != 'NoneType' and f != "None":
        return f
    return s


def format_money(value):
 
    return str(value)


def get_all(dados, columns, ops):
    data = []
    id = 0
    for d in dados:
        dc = {}
        for c in columns:
            if c['type'] != 'hide' or ['class'] != 'hide':
                if c['type'] == 'id':
                    id = getattr(d, c['field'])

                if c['type'] != 'ops':
                    if c['type'] == 'fk':
                        value = str(getattr(getattr(d, c['sec_obj']), c['sec_field']))
                    elif c['type'] == 'fkn':
                        value = str(getattr(getattr(getattr(d, c['sec_obj']), c['ter_obj']), c['sec_field']))
                    else:
                        try:
                            value = ifnull(str(getattr(d, c['field'])), '-')
                        except:
                            value = None

                    if c['type'] == 'cpf':
                        value = '{}.{}.{}-{}'.format(value[:3], value[3:6], value[6:9], value[9:])

                    if c['type'] == 'bool':
                        if getattr(d, c['field']):
                            value = "Sim"
                        else:
                            value = "Não"
                    elif c['type'] == 'cnpj':
                        value = '{}.{}.{}/{}-{}'.format(value[:2], value[2:5], value[5:8], value[8:12], value[12:])
                    elif c['type'] == 'money' or c['class'] == 'money':
                        value = format_money(value)
                    elif c['type'] == 'perc':
                        value = "{:3,.0f}".format(float(value) * 100)
                        value = value.replace(".", ",") + "%"
                    elif c['type'] == 'date_time':
                        value = datetime.datetime.strptime(value, '%Y-%m-%d %X').strftime("%d/%m/%Y %H:%M")
                    elif c['type'] == 'label':
                        try:
                            k = ifnull(getattr(d, c['field']), -1)
                        except:
                            k = None
                        if c['label_class'] == 'nfce':
                            if c['field'] == 'tp_emis':
                                value = get_tpemis(k)
                            if c['field'] == 'tp_amb':
                                value = get_amb(k)
                            if c['field'] == 'situacao':
                                value = get_sit(k)
                            if c['field'] == 'status':
                                if k == -1:
                                    value = "<span title=\"Esta NFC-e ainda não foi enviada à SVRS\">-</span>"
                                else:
                                    value = "<span title=\"" + get_xmotivo(k, False) + "\">" + str(k) + "</span>"
                            if c['field'] == 'resultado_aut_daf':
                                if k == -1:
                                    value = "<span title=\"Este resultado ainda não foi consultado junto à SEF\">-</span>"
                                else:
                                    value = "<span title=\"" + get_resultado_sef(k, False) + "\">" + str(k) + "</span>"
                        elif c['label_class'] == 'daf':
                            if c['field'] == 'situacao':
                                stdaf = k
                                value = get_situacao_daf(k)
                            if c['field'] == 'cnpj_fabricante':
                                value = get_fabricante_nome(str(k))
                            if c['field'] == 'modo_operacao':
                                mod_daf = k
                                value = get_modo_operacao(k)
                            if c['field'] == 'ocupacao':
                                perc = getattr(d, 'num_dfe') * 100 / getattr(d, 'max_dfe')
                                gd = ""
                                for i in range(0, round(perc)):
                                    gd = gd + " rgba(220,0,0," + str(round(perc / 100, 1)) + "), "
                                for i in range(round(perc), 99):
                                    gd = gd + " #fff, "
                                gd = gd + " #fff "
                                value = "<div style='padding:5px; border:1px solid #ddd; background-image: linear-gradient(to right, " + gd + ")'><span style='display:inline-block; background-color:rgba(255,255,255,0.5);'>" + str(
                                    perc).replace(".", ",") + "%</span></div>"
                        elif c['label_class'] == 'empresa':
                            if c['field'] == 'ambiente':
                                value = get_amb(k)

                    if c['class'] == 'link':
                        dc[c['field']] = '<a class=\'fk_link text-info\' href=/' + c['sec_link'] + '/' + str(
                            getattr(getattr(d, c['sec_obj']), c['sec_id'])) + '>' + value + '</a>'
                    elif c['type'] == 'fkn':
                        dc[c['field']] = '<a class=\'fk_link text-info\' href=/' + c['sec_link'] + '/' + str(
                            getattr(getattr(getattr(d, c['sec_obj']), c['ter_obj']),
                                    c['sec_id'])) + '>' + value + '</a>'
                    else:
                        try:
                            dc[c['field']] = value
                        except:
                            dc[c['field']] = ""

        if id == 0:
            id = getattr(d, 'id')
        id = str(id)

        if len(ops) > 0:
            dc["ops"] = ""
            for o in ops:
                if o["btn"] == 'edt':
                    dc["ops"] = dc["ops"] + '<a title=\'Editar\' class=\'btn text-primary\' href=\'/' + o[
                        "rota"] + '/' + id + '\'><i class=\'fas fa-pencil-alt fa-lg\'></i></a> &nbsp;'
                if o["btn"] == 'sel':
                    dc["ops"] = dc["ops"] + '<a title=\'Visualizar\' target=\'_blank\' class=\'btn\' href=\'/' + o[
                        "rota"] + '/' + id + '\'><i class=\'fas fa-search-plus fa-lg\'></i></a> &nbsp;'
                if o["btn"] == 'del':
                    ok = True
                    if o["rota"].find("Empresa") != -1:
                        ok = Empresa.testeRelacoesDelete(id)
                        label = "empresa"
                    elif o["rota"].find("Pdv") != -1:
                        ok = PontoVenda.testeRelacoesDelete(id)
                        label = "PDV"
                    elif o["rota"].find("Funcionario") != -1:
                        ok = Funcionario.testeRelacoesDelete(id)
                        label = "funcionário"
                    elif o["rota"].find("Cliente") != -1:
                        ok = Cliente.testeRelacoesDelete(id)
                        label = "cliente"
                    elif o["rota"].find("Produto") != -1:
                        ok = Produto.testeRelacoesDelete(id)
                        label = "produto"
                    if ok:
                        dc["ops"] = dc[
                                        "ops"] + '<a title=\'Excluir\' role="button" label=\'' + label + '\' class=\'del btn text-danger\' data-toggle="modal" data-target="#janelaModal" codigo=\'' + id + '\' rota=\'/' + \
                                    o["rota"] + '/' + id + '\'><i class=\'fas fa-trash-alt fa-lg\'></i></a> &nbsp; '
                if o["btn"] == 'vis':
                    dc["ops"] = dc["ops"] + '<a title=\'Download XML\' target=\'_blank\' class=\'btn\' href=\'/' + \
                                o[
                                    "rota"] + '/' + id + '\'><i class=\'fa fa-lg fa-file-invoice-dollar text-warning\'></i></a> &nbsp;'
                if o["btn"] == 'ret' and getattr(d, 'ret_sefaz') is not None:
                    dc["ops"] = dc[
                                    "ops"] + '<a title=\'Download XML de retorno SVRS\' target=\'_blank\' class=\'btn\' href=\'/' + \
                                o[
                                    "rota"] + '/' + id + '\'><i class=\'fa fa-lg fa-file text-info\'></i></a> &nbsp;'
                if o["btn"] == 'pdf':
                    dc["ops"] = dc["ops"] + '<a title=\'Download DANFC-e\' target=\'_blank\' class=\'btn\' href=\'/' + \
                                o[
                                    "rota"] + '/' + id + '\'><i class=\'fa fa-file-pdf fa-lg text-danger\'></i></a> &nbsp;'
                if o["btn"] == 'pdfi':
                    dc["ops"] = dc[
                                    "ops"] + '<a title=\'Download DANFE - formato NF-e\' target=\'_blank\' class=\'btn\' href=\'/' + \
                                o["rota"] + '/' + id + '\'><i class=\'fa fa-file-pdf fa-lg text-info\'></i></a> &nbsp;'
                if o["btn"] == 'nfce':
                    dc["ops"] = dc["ops"] + '<a title=\'Visualizar NFC-e\' target=\'_blank\' class=\'btn\' href=\'/' + \
                                o["rota"] + '/' + id + '\'><i class=\'fas fa-file fa-lg\'></i></a> &nbsp;'
                if o["btn"] == 'env' and c == 9 and getattr(d, 'situacao') == 0:
                    dc["ops"] = dc["ops"] + '<a title=\'Enviar NFC-e para SVRS\' class=\'btn\' href=\'/' + \
                                o[
                                    "rota"] + '/' + id + '\'><i class=\'fa fa-paper-plane text-info fa-lg\'></i></a> &nbsp;'
                if o["btn"] == 'atl':
                    dc["ops"] = dc["ops"] + '<a title=\'Atualizar informações do DAF\' class=\'btn\' href=\'/' + \
                                o["rota"] + '/' + id + '\'><i class=\'fa fas fa-sync text-info fa-lg\'></i></a> &nbsp;'
                if o["btn"] == 'regdaf' and stdaf == 0:
                    dc["ops"] = dc["ops"] + '<a title=\'Registrar\' class=\'btn text-primary\' href=\'/' + o[
                        "rota"] + '/' + id + '\'><i class=\'fas fa-pencil-alt fa-lg\'></i></a> &nbsp;'
                if o["btn"] == 'remdaf' and stdaf != 0 and stdaf != 2:
                    dc["ops"] = dc[
                                    "ops"] + '<a title=\'Remover Registro\' class=\'rem btn text-danger\' codigo=\'' + id + '\' rota=\'/' + \
                                o["rota"] + '/' + id + '\'><i class=\'fas fa-trash-alt fa-lg\'></i></a> &nbsp; '
                if o["btn"] == 'reset':
                    dc["ops"] = dc[
                                    "ops"] + '<a title=\'Restaurar padrões de fábrica\' class=\'reset btn text-danger\' codigo=\'' + id + '\' rota=\'/' + \
                                o["rota"] + '/' + id + '\'><i class=\'fas fa-history fa-lg\'></i></a> &nbsp; '
                if o["btn"] == 'altMod' and mod_daf == 0:
                    dc["ops"] = dc[
                                    "ops"] + '<a title=\'Alterar Modo de Operação para Compartilhado\' class=\'btn text-primary\' href=\'/' + \
                                o[
                                    "rota"] + '/' + id + '\'><i class=\'fas fa-lock fa-lg\'></i></a> &nbsp;'
                if o["btn"] == 'altMod' and mod_daf == 1:
                    dc["ops"] = dc[
                                    "ops"] + '<a title=\'Alterar Modo de Operação para Dedicado\' class=\'btn text-primary\' href=\'/' + \
                                o[
                                    "rota"] + '/' + id + '\'><i class=\'fas fa-lock-open fa-lg\'></i></a> &nbsp;'

        data.append(dc)
        for c in columns:
            if c['type'] == 'hide':
                columns.remove(c)
            if c['field'] == 'ops' and len(ops) == 0:
                columns.remove(c)

    return data
