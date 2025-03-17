
from flask import render_template, redirect, url_for, request, session
from app import app
from sqlalchemy import text

from datetime import datetime
from app.models.models import User
from app.db import db


#Imports para o register
from app.routes.auth import auth_bp
from app.routes.gerencia import gerencia_bp
from app.routes.estoque import estoque_bp
from app.routes.logistica import logistica_bp

#Tela raiz
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        return redirect(url_for('auth.root',user=user ,pwd=pwd))
        

#Rota que deve ser apagada
@app.route('/register', methods=['get', 'post'])   
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        pwd = request.form['pwd']
        email = request.form['email']
        cargo = request.form['cargo']

        novo_usuario = User(user=usuario, pwd=pwd, email=email, cargo=cargo)
        db.session.add(novo_usuario)
        db.session.commit()
        print(session)
        return f'{usuario} {pwd}'

#Register
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(gerencia_bp, url_prefix='/gerencia')
app.register_blueprint(estoque_bp, url_prefix='/estoque')
app.register_blueprint(logistica_bp, url_prefix='/logistica')


def criar_schema(nome_schema):
    with app.app_context():
        db.session.execute(text(f"CREATE SCHEMA IF NOT EXISTS {nome_schema};"))
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        #criar_schema('estoque')
        db.create_all()
    app.run(debug=True, port=5153)
    