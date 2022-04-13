import os
import sys

import redis
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Separator
from flask_qrcode import QRcode
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from app.daf.com.pdafcdc import PDAFCDC
from app.daf.protocolo_daf import ProtocoloDaf

app = Flask(__name__)

bds = {
    "paf": "mysql+pymysql://dafpaf:E37vEB3dnm@localhost:3306/daf-paf",
    "ws": "mysql+pymysql://dafws:7rVQW48ph2@localhost:3306/daf-ws",
}
redis_host = 'localhost'
redis_port = 6379
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 'True'
app.config["DEBUG"] = 'True'
endereco_sef = '127.0.0.1:8080'
for variable, value in os.environ.items():
    if variable.startswith("FLASK_"):
        env_name = variable.split("FLASK_")[1]
        if env_name.startswith("SQLALCHEMY_BINDS_"):
            bind = env_name.split("SQLALCHEMY_BINDS_")[1]
            bds[bind] = value
        elif env_name == "REDIS_HOST":
            redis_host = value
        elif env_name == "REDIS_PORT":
            redis_port = int(value)
        elif env_name == 'ENDERECO_SEF':
            endereco_sef = value
        else:
            if value == "True":
                value = True
            elif value == "False":
                value = False
            app.config[env_name] = value
app.config["SQLALCHEMY_BINDS"] = bds
app.config["PERMANENT_SESSION_LIFETIME"] = 1800

rd = redis.Redis(host=redis_host, port=redis_port, db=1)
db = SQLAlchemy(app)
boostrap = Bootstrap(app)
fa = FontAwesome(app)
nav = Nav()
nav.init_app(app)
QRcode(app)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

daf_conectado = False
try:
    pdafcdc = PDAFCDC(3)
    paf = ProtocoloDaf(pdafcdc)
    daf_conectado = True
except Exception as e:
    pass

if daf_conectado:

    # imports para o menu
    from app.controllers.funcionarioController import listar_funcionario
    from app.controllers.clienteController import listar_cliente
    from app.controllers.empresaController import listar_empresa
    from app.controllers.produtoController import listar_produto
    from app.controllers.vendaController import listar_venda
    from app.controllers.vendaItemController import selecionar_venda_item

    from app.controllers.nfceController import listar_nfce
    from app.controllers.pdvController import listar_pdv
    from app.controllers.loginController import listar_login
    from app.controllers.dafController import listar_daf
    from app.views.rotas.rotasDebug import reset_conectado, reset_conectado_novo
    from app.views.rotas.rotasDebug import consultar_daf_conectado, consultar_daf_conectado_sef
    from app.views.rotas.rotasIndexTestes import cenario_autorizacao

    # import das rotas p/ modal
    from app.views.rotas.rotasTestesAutorizacao import *
    from app.views.rotas.rotasTestesRegistro import *
    from app.controllers.cenariosTeste.passosBasico import *
    from app.controllers.cenariosTeste.passosAutorizacao import *
    from app.controllers.cenariosTeste.passosRegistro import *

    # imports debug sef
    from app.views.rotas.debugSef import *


@nav.navigation()
def meunavbar():
    menu = Navbar('PAF')
    menu.items = [View('Home', 'inicio')]
    if daf_conectado:
        menu.items.append(Subgroup('Configurações'
                                   , View('Empresa', 'listar_empresa')
                                   , View('Pdv', 'listar_pdv')
                                   , View('Funcionários', 'listar_funcionario')
                                   , View('Login', 'listar_login')
                                   , View('DAF', 'listar_daf')))
        menu.items.append(Subgroup('Cadastros'
                                   , View('Clientes', 'listar_cliente')
                                   , View('Produto', 'listar_produto')))
        menu.items.append(Subgroup('Operacional'
                                   , View('Vendas', 'listar_venda')
                                   , View('NFC-e', 'listar_nfce')))
        menu.items.append(Subgroup('Debug'
                                   , View('Restaurar DAF', 'reset_conectado')
                                   , View('Restaurar - novo idDaf', 'reset_conectado_novo')
                                   , Separator()
                                   , View('Consultar DAF', 'consultar_daf_conectado')
                                   , View('Consultar DAF - SEF', 'consultar_daf_conectado_sef')
                                   , Separator()
                                   , View('Cancelar Processo', 'interromper_processo')
                                   ))
        menu.items.append(Subgroup('Debug SEF'
                                   , View('DAF', 'listar_daf_sef')
                                   , View('Registro', 'listar_registro_sef')
                                   , View('Forçar desfazer registro na SEF', 'desfazer_registro')))
    return menu


# páginas de erro
@app.errorhandler(404)
def page_not_found(e):
    return render_template('erro.html', e=e, titulo="Página não encontrada..."), 404


@app.route('/')
def inicio():
    if daf_conectado:
        return redirect("/cenario_autorizacao")
    return render_template('sem_daf.html')

@app.route('/login')
def login():
    from app.inicializacao import Inicializacao
    return Inicializacao.set_login()
