from app.db import db
from datetime import datetime

from flask_login import UserMixin

#Classe que cria usuarios
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id            = db.Column('id', db.Integer,primary_key=True)
    codigo_geral  = db.Column('codigo_geral', db.VARCHAR(45), unique=True, nullable=False)
    user          = db.Column("user", db.VARCHAR(50), unique=True,nullable=False)
    pwd           = db.Column("pwd", db.VARCHAR(300), nullable=False)
    email         = db.Column("email", db.VARCHAR(100), nullable=False)
    setor         = db.Column("setor", db.VARCHAR(15), nullable=False)
    cargo         = db.Column("cargo", db.VARCHAR(15), nullable=False)
    status        = db.Column("status", db.Boolean, default=True, nullable=False)
    def __init__(self, user, pwd, email, setor, cargo):
        self.codigo_geral = f'{user}{datetime.now().date()}'
        self.user = user
        self.pwd = pwd
        self.email = email
        self.setor = setor
        self.cargo = cargo

#classe que cria perfis de usuarios
class Perfil(db.Model):
    __tablename__ = 'perfil'

    id              = db.Column('id',  db.Integer, primary_key=True, autoincrement=True)
    codigo_geral    = db.Column('codigo_geral', db.ForeignKey('users.codigo_geral'))
    
    nome            = db.Column("nome", db.VARCHAR(50), nullable=False)
    sobre_nome      = db.Column("sobre_nome", db.VARCHAR(100), nullable=False)
    data_nascimento = db.Column("data_nascimento", db.VARCHAR(30), nullable=False)
    tell            = db.Column("tell", db.VARCHAR(15), nullable=False, unique=True)
               
    cnh             = db.Column("cnh", db.VARCHAR(15), nullable=False, unique=True)

    def __init__(self, nome, sobre_nome,data_nascimento,tell,cnh):
        self.codigo_geral = self.codigo_geral
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.data_nascimento = data_nascimento
        self.tell = tell
        self. cnh = cnh



class Veiculos(db.Model):
    __tablename__ = 'veiculos'

    id = db.Column('id_veiculo', db.Integer, primary_key=True, autoincrement=True)
    codigo_geral_veiculo = db.Column('codigo_geral_veiculo', db.VARCHAR(20), unique=True, nullable=False)
    placa = db.Column('placa', db.VARCHAR(20), unique=True, nullable=False)
    modelo = db.Column('modelo', db.VARCHAR(40), nullable=False)
    capacidade_carga = db.Column('capacidade_carga', db.Integer)
    data_fab = db.Column('data_fab', db.VARCHAR(20))
    check_lists = db.relationship('Checklist', backref='veiculos', lazy=True, cascade="all, delete-orphan")
    

    def __init__(self, placa, modelo, capacidade_carga, data_fab):
        self.codigo_geral_veiculo = f'{placa}{datetime.now().date()}'
        self.placa = placa
        self.modelo = modelo
        self.capacidade_carga = capacidade_carga
        self.data_fab = data_fab


class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    veiculo_id = db.Column(db.VARCHAR(20), db.ForeignKey('veiculos.codigo_geral_veiculo'), nullable=False)
    data_check = db.Column(db.DateTime, default=db.func.current_timestamp())
    itens = db.relationship('ChecklistItem', backref='checklist', lazy=True, cascade="all, delete-orphan")

# ✅ Tabela de Itens do Checklist (Atributos Variáveis)
class ChecklistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.String(255))  # Pode armazenar texto, números ou status
#-------------------------
