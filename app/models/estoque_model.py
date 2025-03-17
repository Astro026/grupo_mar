
from app.db import db
from datetime import datetime


class tb_categoria_interno_produto__estoque_producao(db.Model):
    __tablename__ = 'tb_categoria_interno_produto__estoque_producao'
    __bind_key__ = 'estoque_producao'

    id_tb_categoria_interno_produto = db.Column('ID_tb_categoria_interno_produto', db.Integer, primary_key = True)
    categoria_interno_tb_categoria_interno_produto = db.Column('categoria_interno_tb_categoria_interno_produto', db.VARCHAR(120), nullable = False, unique= True)
   

    def __init__(self, categoria_interno):
        tratar_categoria_interno = categoria_interno
        self.categoria_interno_tb_categoria_interno_produto = tratar_categoria_interno.strip().capitalize()



class tb_nome_interno_produto__estoque_producao(db.Model):
    __tablename__ = 'tb_nome_interno_produto__estoque_producao'
    __bind_key__ = 'estoque_producao'

    id_tb_nome_interno_produto = db.Column('ID_tb_nome_interno_produto', db.Integer, primary_key = True)
    nome_interno_tb_nome_interno_produto = db.Column('NOME_INTERNO_tb_nome_interno_produto', db.VARCHAR(120), nullable = False, unique= True)
    
    def __init__(self, nome_interno):
        tratar_nome_interno = nome_interno
        self.nome_interno_tb_nome_interno_produto = tratar_nome_interno.strip().capitalize()



class tb_entrada_nota__estoque_producao(db.Model):
    __tablename__ = 'tb_entrada_nota__estoque_producao'
    __bind_key__   = 'estoque_producao'

    id_tb_entrada_nota             = db.Column('ID_tb_entrada_nota',db.Integer, primary_key = True)
    numero_tb_entrada_nota         = db.Column('NUMERO_tb_entrada_nota', db.VARCHAR(20), nullable=False, unique=True)
    serie_tb_entrada_nota          = db.Column('SERIE_tb_entrada_nota', db.VARCHAR(5), nullable=False)
    fornecedor_tb_entrada_nota     = db.Column('FORNECEDOR_tb_entrada_nota', db.VARCHAR(120), nullable=False)
    cnpj_tb_entrada_nota           = db.Column('CNPJ_tb_entrada_nota',db.VARCHAR(20), nullable=False)
    valor_tb_entrada_nota          = db.Column('VALOR_tb_entrada_nota', db.FLOAT, nullable=False)
    chave_acesso_tb_entrada_nota   = db.Column('CHAVE_ACESSO_tb_entrada_nota', db.VARCHAR(60), unique=True)
    data_entrada_tb_entrada_nota   = db.Column('DATA_ENTRADA_tb_entrada_nota', db.VARCHAR(10))
    img_tb_entrada_nota            = db.Column('IMG_tb_entrada_nota', db.VARCHAR(200))
    codigo_usuario_tb_entrada_nota = db.Column('CODIGO_USUARIO', db.VARCHAR(120), nullable=False)

    produtos = db.relationship('tb_produto_nota_entrada__estoque_producao', backref='tb_entrada_nota__estoque_producao', lazy=True)

    def __init__(self, numero, serie, fornecedor,cnpj, valor,chave,data_entrada,img,usuario):
        self.numero_tb_entrada_nota =numero
        self.serie_tb_entrada_nota = serie
        self.fornecedor_tb_entrada_nota = fornecedor
        self.cnpj_tb_entrada_nota = cnpj
        self.valor_tb_entrada_nota = valor
        self.chave_acesso_tb_entrada_nota = chave
        self.data_entrada_tb_entrada_nota = data_entrada
        self.img_tb_entrada_nota = img
        self.codigo_usuario_tb_entrada_nota = usuario        




class tb_produto_nota_entrada__estoque_producao(db.Model):
    __tablename__ = 'tb_produto_nota_entrada__estoque_producao'
    __bind_key__   = 'estoque_producao'

    id_tb_produto_entrada_nota = db.Column('ID_tb_produto_entrada_nota', db.Integer, primary_key=True)
    numero_nota_tb_produto_nota_entrada = db.Column(db.VARCHAR(20), db.ForeignKey('tb_entrada_nota__estoque_producao.NUMERO_tb_entrada_nota'))
    nome_externo_produto_tb_produto_nota_entrada = db.Column('NOME_EXTERNO_PRODUTO_tb_produto_nota_entrada', db.VARCHAR(200))
    nome_interno_produto_tb_produto_nota_entrada = db.Column('NOME_INTERNO_PRODUTO_tb_produto_nota_entrada', db.Integer, db.ForeignKey('tb_nome_interno_produto__estoque_producao.ID_tb_nome_interno_produto'))
    
    categoria = db.relationship('tb_nome_interno_produto__estoque_producao', backref='tb_produto_nota_entrada__estoque_producao')
    
    def __init__(self, numero_nota, nome_externo, nome_interno):
        self.numero_nota_tb_produto_nota_entrada = numero_nota
        self.nome_externo_produto_tb_produto_nota_entrada = nome_externo
        self.nome_interno_produto_tb_produto_nota_entrada = nome_interno

    











"""class User(db.Model):
    __tablename__ = 'users'
    __bindargs__ = 'estoque_producao'
    
    id            = db.Column('id', db.Integer,primary_key=True)
    codigo_geral  = db.Column('codigo_geral', db.VARCHAR(45), unique=True, nullable=False)
    """