from flask import Flask
from flask_login import LoginManager
from sqlalchemy import text

from app.db import db
from app.models.estoque_model import *

app = Flask(__name__)
app.secret_key = '1223absc'
lm = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:226226uy@astrocode.cdee0eaoc82b.us-east-2.rds.amazonaws.com:3306/grupo_mar'
app.config['SQLALCHEMY_BINDS'] = {
    'estoque_producao':'mysql+pymysql://admin:226226uy@astrocode.cdee0eaoc82b.us-east-2.rds.amazonaws.com:3306/estoque_producao',
   }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



def criar_schema(nome_schema):
    with app.app_context():
        db.session.execute(text(f"CREATE SCHEMA IF NOT EXISTS {nome_schema};"))
        db.session.commit()

def start_padrao():
    categorias_pra_adc = ['Frutas', 'Embalagens', 'Ingredientes', 'Rótulos']
    nomes_interno_pra_adc = ['Morango', 'Banana', 'Kiwi']
     
    for nome in consulta_nomes:
        print(f'Consulta -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= {nome.nome_interno_tb_nome_interno_produto}')



with app.app_context():
    criar_schema('estoque_producao')
    #start_padrao()
    db.create_all()


#consulta = tb_nome_interno_produto__estoque_producao.query.filter_by(id_tb_nome_interno_produto=1)
