from flask import render_template, redirect
from sqlalchemy import text, desc

from app import app, db
from app.models.daf import Daf

colunas_daf = [
    {
        "field": "id_daf",
        "title": "idDaf",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "contador_atual",
        "title": "contador_atual",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "data_extravio",
        "title": "data_extravio",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "justificativa_extravio",
        "title": "justificativa_extravio",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "situacao",
        "title": "situacao",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "modelo_daf_fk_id",
        "title": "modelo_daf_fk_id",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "modelo_nome",
        "title": "modelo_nome",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "ateste",
        "title": "ateste",
        "sortable": True,
        "type": "",
        "class": ""
    }
]

colunas_registro = [
    {
        "field": "id",
        "title": "id",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "chave_daf",
        "title": "chave_daf",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "chave_paf",
        "title": "chave_paf",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "chave_sef",
        "title": "chave_sef",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "contador_registro",
        "title": "contador_registro",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "data_registro",
        "title": "data_registro",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "data_remocao",
        "title": "data_remocao",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "justificativa_remocao",
        "title": "justificativa_remocao",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "modo_operacao",
        "title": "modo_operacao",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "just_ultima_alt_modo_op",
        "title": "just_ultima_alt_modo_op",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "alg",
        "title": "Algoritmo",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "tam_chave",
        "title": "tam_chave",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "alg_sit",
        "title": "alg_sit",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "daf_fk_id_daf",
        "title": "daf_fk_id_daf",
        "sortable": True,
        "type": "",
        "class": ""
    },
    {
        "field": "paf_contribuinte_fk_id_paf",
        "title": "paf_contribuinte_fk_id_paf",
        "sortable": True,
        "type": "",
        "class": ""
    }
]


@app.route('/listarDafSef')
def listar_daf_sef():
    engine = db.get_engine(app, "ws")
    sql = text(
        "select d.*,m.nome as modelo_nome, m.chave_ateste as ateste from daf d inner join modelo_daf m on m.id = d.modelo_daf_fk_id")
    with engine.connect() as connection:
        result = connection.execute(sql)
    res = [dict(r) for r in result]
    return render_template('listagem.html', data=res, columns=colunas_daf, title="DAF na SEF",
                           add='', gerar='', label='DAF na SEF')


@app.route('/listarRegistroSef')
def listar_registro_sef():
    engine = db.get_engine(app, "ws")
    sql = text(
        "select r.id, r.chave_daf, r.chave_paf, r.chave_sef,r.just_ultima_alt_modo_op, if(r.modo_operacao,\'Compartilhado\',\'Dedicado\') as modo_operacao, r.contador_registro, r.data_registro, r.data_remocao, r.justificativa_remocao, r. daf_fk_id_daf, r.paf_contribuinte_fk_id_paf, a.nome as alg, a.tam_chave, if(a.ativo,\'Ativo\',\'Inativo\') as alg_sit from registro_daf r inner join daf d on d.id_daf = r.daf_fk_id_daf inner join modelo_daf_certificados_sef mdcs on d.modelo_daf_fk_id = mdcs.modelo_daf_fk_id inner join certificado_sef_algoritmo csa on mdcs.certificado_sef_fk_id = csa.certificado_sef_fk_id inner join algoritmo a on csa.algoritmo_fk_id = a.id")
    with engine.connect() as connection:
        result = connection.execute(sql)
    res = [dict(r) for r in result]
    return render_template('listagem.html', data=res, columns=colunas_registro, title="Registros na SEF",
                           add='', gerar='', label='Registros na SEF')


@app.route('/desfazerRegistroForce')
def desfazer_registro():
    daf = Daf.query.order_by(desc(Daf.data_insercao)).first()
    daf.situacao = 0
    db.session.commit()
    engine = db.get_engine(app, "ws")

    with engine.connect() as connection:
        with connection.begin() as transaction:
            connection.execute(text("delete from registro_daf where daf_fk_id_daf = \'" + daf.id_daf + "\'; "))
            connection.execute(text("delete from aut_daf where daf_fk_id_daf = \'" + daf.id_daf + "\'; "))
            connection.execute(text("delete from daf where id_daf = \'" + daf.id_daf + "\';"))
            connection.execute(text("delete from xml_distribuicao;"))
            transaction.commit()

    engine2 = db.get_engine(app, "paf")
    with engine2.connect() as connection2:
        with connection2.begin() as transaction2:
            connection2.execute(text("delete from venda_item;"))
            connection2.execute(text("delete from nfce;"))
            connection2.execute(text("delete from venda;"))
            transaction2.commit()

    return redirect("/")
