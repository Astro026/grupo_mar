from sqlalchemy import create_engine, Column, VARCHAR, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime



engine = create_engine('mysql+pymysql://root:328473@localhost/grupo_mar')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id            = Column('id', Integer,autoincrement=True,unique=True,nullable=False)
    codigo_geral  = Column('codigo_geral', VARCHAR(45), primary_key=True, unique=True, nullable=False)
    user          = Column("user", VARCHAR(50), unique=True,nullable=False)
    pwd           = Column("pwd", VARCHAR(300), nullable=False)
    email         = Column("email", VARCHAR(100), nullable=False)

    def __init__(self, user, pwd, email):
        self.codigo_geral = f'{user}{datetime.now().date}'
        self.user = user
        self.pdw = pwd
        self.email = email



class Perfil(Base):
    __tablename__ = 'perfil'

    id              = Column('id',  Integer,primary_key=True, autoincrement=True)
    codigo_geral    = Column('codigo_geral', ForeignKey('users.codigo_geral'))
    
    nome            = Column("nome", VARCHAR(50), nullable=False)
    sobre_nome      = Column("sobre_nome", VARCHAR(100), nullable=False)
    data_nascimento = Column("data_nascimento", VARCHAR(30), nullable=False)
    tell            = Column("tell", VARCHAR(15), nullable=False)
               
    cnh             = Column("cnh", VARCHAR(15), nullable=False)
    cargo           = Column("cargo", VARCHAR(15), nullable=False)

    def __init__(self, nome, sobre_nome,data_nascimento,tell,cnh,cargo):
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.data_nascimento = data_nascimento
        self.tell = tell
        self. cnh = cnh
        self.cargo = cargo








Base.metadata.create_all(bind=engine)