from flask import Flask, request, render_template
from flask_login import LoginManager
from sqlalchemy import text

import os
import pandas as pd
from app.db import db
from app.models.estoque_model import *

app = Flask(__name__)
app.secret_key = '1223absc'
lm = LoginManager(app)


#Variavel AWS
"""
app.config['SQLALCHEMY_BINDS'] = {'estoque_producao':'mysql+pymysql://admin:226226uy@astrocode.cdee0eaoc82b.us-east-2.rds.amazonaws.com:3306/estoque_producao'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:328473@localhost/grupo_mar'
app.config['SQLALCHEMY_BINDS'] = {
    'estoque_producao':'mysql+pymysql://root:328473@localhost/estoque_producao',
    #'grupo_mar1': 'mysql+pymysql://root:328473@localhost/grupo_mar1'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:226226uy@astrocode.cdee0eaoc82b.us-east-2.rds.amazonaws.com:3306/grupo_mar'
app.config['SQLALCHEMY_BINDS'] = {'estoque_producao':'mysql+pymysql://admin:226226uy@astrocode.cdee0eaoc82b.us-east-2.rds.amazonaws.com:3306/estoque_producao'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#Informando o flask qual é minha pasta padrão para upload de arquivos
UPLOAD_FOLDER_FINANCEIRO = 'uploads/financeiro'
ALLOWED_EXTENCIONS = ['csv']
app.config['UPLOAD_FOLDER_FINANCEIRO'] = UPLOAD_FOLDER_FINANCEIRO
#criando pasta caso não exista
os.makedirs(UPLOAD_FOLDER_FINANCEIRO, exist_ok=True)




def criar_schema(nome_schema):
    with app.app_context():
        db.session.execute(text(f"CREATE SCHEMA IF NOT EXISTS {nome_schema};"))
        db.session.commit()

def start_padrao():
    categorias = Nome_Categoria.query.all()
    nomes = Nome_Produto.query.all()
    #Verificando se as categorias são existentes
    if len(categorias) <=0 and len(nomes) <=0:
        #Criando as categorias
        lista_categorias = ['Frutas', 'Embalagens', 'Rotulos']
        for categoria in lista_categorias:
            nova_categoria = Nome_Categoria(categoria)
            db.session.add(nova_categoria)
        #Criando os nomes
        lista_nomes = ['Morango', 'Banana', 'CX Natureza', 'CX Doce Gelato']
        for nome in lista_nomes:
            novo_nome = Nome_Produto(nome)
            db.session.add(novo_nome)
        db.session.commit()
    return
    


with app.app_context():
    criar_schema('estoque_producao')
    db.create_all()
    start_padrao()
