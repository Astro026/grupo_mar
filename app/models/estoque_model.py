
from app.db import db
from datetime import datetime



class Estoque(db.Model):
    __tablename__ = 'Estoque'
    __bind_key__ = 'estoque_producao'

    id = db.Column('id', db.Integer, primary_key=True)
    id_nome_produto = db.Column('id_nome_produto',db.Integer, db.ForeignKey('nome_produto.id_nome_produto'), nullable=False)
    id_nome_categoria = db.Column('id_nome_categoria',db.Integer, db.ForeignKey('nome_categoria.id_nome_categoria'), nullable=False)
    quantidade = db.Column('quantidade', db.Integer, nullable=False)

    nome_produto = db.relationship('Nome_Produto', backref=db.backref('estqoue', lazy=True))
    categoria = db.relationship('Nome_Categoria', backref=db.backref('estoque', lazy=True))
    
    def __init__(self, id_produto, id_categoria, quantidade):
        self.id_nome_produto = int(id_produto)
        self.id_nome_categoria = int(id_categoria)
        self.quantidade = int(quantidade)


class Nome_Categoria(db.Model):
    __tablename__ = 'nome_categoria'
    __bind_key__  = 'estoque_producao'

    id_nome_categoria = db.Column('id_nome_categoria', db.Integer, primary_key = True)
    nome_categoria    = db.Column('nome_categoria', db.VARCHAR(120), nullable = False, unique= True)
   

    def __init__(self, nome_categoria):
        self.nome_categoria = nome_categoria.strip().capitalize()


class Nome_Produto(db.Model):
    __tablename__ = 'nome_produto'
    __bind_key__ = 'estoque_producao'

    id_nome_produto = db.Column('id_nome_produto', db.Integer, primary_key = True)
    nome_produto = db.Column('nome_produto', db.VARCHAR(120), nullable = False, unique= True)
    
    def __init__(self, nome_produto):
        self.nome_produto = nome_produto.strip().capitalize()


#notas


#produtos