from flask import Blueprint, render_template, request, session, url_for, redirect
from flask_login import login_required, current_user

from app import db, lm
from app.models.models import User
from app.models.estoque_model import *

estoque_bp = Blueprint('estoque', __name__, template_folder='templates')


@estoque_bp.route('/', methods=[ 'GET', 'POST'])
@login_required
def root():
    dados ='' #db.session.query(notas_entrada_produto, nome_interno.nome_interno).join(nome_interno).all()
    print('1ache',dados)
    
    for dado, dad, in dados:
         print(dado.nome_produto, '-', dad)
    return render_template('private/estoque/home.html',dados=dados)
    
@estoque_bp.route('cadastrar_nota', methods=['GET', 'POST'])
def cadastrar_nota():
    if current_user.cargo == 'gestor' and current_user.setor == 'estoque':
        if request.method == 'POST':
       
            #DADOS DA NOTA
            n_nota       = request.form.get('n_nota')
            cnpj         = request.form.get('cnpj')
            fornecdor    = request.form.get('fornecedor')
            valor_bruto  = request.form.get('valor_bruto')
            #nova_nota    = notas_entrada(n_nota=n_nota, cnpj=cnpj, fornecedor=fornecdor, valor_bruto=valor_bruto)
            #db.session.add(nova_nota)
            #db.session.commit()

            #Produtos
            nome_produto          = request.form.get('nome_produto')
            nt_nome_interno       = int(request.form.get('nt_nome_interno'))
            produto_categoria     = int(request.form.get('produto_categoria'))
            quantidade            = float(request.form.get('quantidade'))
            peso                  = float(request.form.get('peso'))
            preco                 = float(request.form.get('preco'))                                                                
            #novo_produto = notas_entrada_produto(nota_id=nova_nota.id,nome_produto=nome_produto, nt_nome_interno=nt_nome_interno,produto_categoria=produto_categoria,quantidade=quantidade, peso=peso,preco=preco)
            #db.session.add(novo_produto)
            #db.session.commit()                                                                                 

            return redirect(url_for('estoque.root'))
    
        if request.method == 'GET':
        
            return render_template('/private/estoque/cadastrar_nota.html')


@estoque_bp.route('/teste', methods=[ 'GET', 'POST'])
@login_required
def teste():
    if request.method == 'POST':
        print("POST_++++++++++++++++++++++++++++++++++++++++")
        nome_produto = request.form.get('nome_produto')
        categoria_produto = request.form.get('categoria_produto')
        quantidade_produto = request.form.get('quantidade_produto')

        novo_produto = Estoque(int(nome_produto),categoria_produto,quantidade_produto)
        db.session.add(novo_produto)
        db.session.commit()
        
    estoque = Estoque.query.all()
    return render_template('/private/estoque/teste.html', estoque=estoque)




    


#Padrão para levar o cargo para a rota correta
@estoque_bp.before_request
@login_required
def check_cargo():
    """if current_user.cargo == 'gestor':
        return redirect(url_for(f'{current_user.setor}.root'))        
        """
 
    if  current_user.cargo != 'gerente' and current_user.cargo == 'gestor' and current_user.setor != 'estoque':
            return redirect(url_for(f'{current_user.cargo}.root'))        
