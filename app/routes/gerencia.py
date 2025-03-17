from flask import Blueprint, render_template, request, session, url_for, redirect
from flask_login import login_required, current_user

from app.models.models import User, Perfil

from app import db, lm
from app.models.models import User


gerencia_bp = Blueprint('gerencia', __name__, template_folder='templates')

#Raiz
@gerencia_bp.route('/', methods=[ 'GET', 'POST'])
@login_required
def root():
    print(current_user)
    return render_template('private/gerencia/home.html')



#Cria, edita, Apaga e bloqueia usuarios
@gerencia_bp.route('/usuarios', methods=['POST', 'GET'])
@login_required
def usuarios():


    if request.method == 'GET':
        lista_usuarios = User.query.all()
        return render_template('/private/gerencia/usuarios.html', lista_usuarios=lista_usuarios)
    
    if request.method == 'POST':
        #Tabela user
        usuario = request.form['user'].lower()
        pwd = request.form.get('pwd')
        confirmar_pwd = request.form['confirmar_pwd']
        email = request.form['email'].lower()
        setor = request.form['setor'].lower()#O campo [setor] no front-end é capturado apos CNH(tabela perfl) porem ele pertence a tabela users
        cargo = request.form['cargo'].lower()#O campo [cargo] no front-end é capturado apos CNH(tabela perfl) porem ele pertence a tabela users
        
        #tabela perfil
        nome = request.form['nome'].capitalize()
        sobre_nome = request.form['sobre_nome'].capitalize()
        dt_nascimento = request.form['dt_nascimento']
        tell = request.form['tell']
        cnh = request.form['cnh']
        
        #Verifica se as duas senhas são iguais caso sim o usuairo é criado
        if pwd == confirmar_pwd:
            novo_usuario = User(user=usuario, pwd=pwd, email=email,setor=setor, cargo=cargo)
            db.session.add(novo_usuario)
            novo_perfil = Perfil(nome=nome,  sobre_nome=sobre_nome, data_nascimento=dt_nascimento, tell=tell, cnh=cnh)
            db.session.add(novo_perfil)
            db.session.commit()
        return f'{request.form.listvalues()}'


#Não desenvolvido ainda
@gerencia_bp.route('/editar_perfil', methods=['POST', 'GET'])
@login_required
def editar_perfil():
   
    if request.method == 'POST':
        user = request.form.get('editar_usuario')
        
        usuario = db.session.query(User).filter_by(codigo_geral=user).first()
        return f'{usuario.cargo}'

#Não desenvolvido ainda
@gerencia_bp.route('/delete_perfil', methods=['POST', 'GET'])
@login_required
def delete_perfil():
   
    if request.method == 'POST':
        user = request.form.get('deletar_usuario')
        usuario = db.session.query(User).filter_by(codigo_geral=user).first()

        #CONFIRMAÇÃO
        confirmar_delete = request.form.get('confirmar_delete')
        if confirmar_delete == f'deletar {usuario.user}':
            db.session.delete(usuario)
            db.session.commit()
            return f'Usuario {usuario.user} deletado com sucesso!'
        else:
            return f'{user}ALGO DEU ERRADO TENTE NOVAMENTE'
        

#Direcionamento padrão de cargo para rota
@gerencia_bp.before_request
@login_required

def check_cargo():
    
    if current_user.cargo != 'gerente':
            return redirect(url_for(f'{current_user.cargo}.root'))        