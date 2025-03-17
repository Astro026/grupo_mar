from flask import Blueprint, render_template, request, session, url_for, redirect
from flask_login import login_user, logout_user, current_user



from app import lm, db
from app.models.models import User
auth_bp = Blueprint('auth', __name__, template_folder='templates')

#Artigo de segurança
@lm.user_loader
def user_loader(id):
    usuario = db.session.query(User).filter_by(id=id).first()
    return usuario

#autheticador de usuario
@auth_bp.route('/', methods=[ 'GET', 'POST'])
def root():
    #Busca o valores informados(front-end)
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    
    #Verifica os alores informados(back-end)
    usuario = db.session.query(User).filter_by(user=user, pwd=pwd).first()
    if not usuario:# se invalido
        return 'Usuario ou Senha Invalidos'
    
    login_user(usuario)
    # Se valido
    return redirect(url_for(f'{current_user.setor}.root'))

#Deslogar
@auth_bp.route('/logout', methods=[ 'GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))