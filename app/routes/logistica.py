from flask import Blueprint, render_template, request, session, url_for, redirect, jsonify
from flask_login import login_required, current_user

from app.models.models import User, Perfil, Veiculos, Checklist, ChecklistItem

from app import db, lm

logistica_bp = Blueprint('logistica', __name__, template_folder='templates')

#Raiz
@logistica_bp.route('/', methods=[ 'GET', 'POST'])
@login_required
def root():
    veiculos = Veiculos.query.all()
    return render_template('private/logistica/home.html', veiculos=veiculos)
    
    
@logistica_bp.route('/lista/<id_veiculo>')
@login_required
def lista_checklist(id_veiculo):
    veiculo = Veiculos.query.filter_by(placa=id_veiculo).first()
    
    #lista com todos os checklist
    lista_checklist = Checklist.query.filter_by(veiculo_id=veiculo.codigo_geral_veiculo).all()
    
    #lista de items
    checklists = Checklist.query.filter_by(veiculo_id=veiculo.codigo_geral_veiculo).all()
    for checklist in checklists:
        print(checklist.codigo_geral_user)
        for item in checklist.itens:
            print(item.nome,'=======================================')
        
    return render_template('private/logistica/lista_checklist.html',veiculo=veiculo, checklists=checklists)

            



@logistica_bp.route('/veiculo/<placa_veiculo>', methods=[ 'GET', 'POST'])
@login_required
def veiculo(placa_veiculo):
    #pego os dados do veiculo atraves da placa
    veiculo = Veiculos.query.filter_by(placa=placa_veiculo).first()
    #trago todos os check_list deste veiculo
    #checklists = Checklist.query.filter_by(veiculo_id=veiculo.codigo_geral_veiculo)
    
    #items = ChecklistItem.query.filter_by(checklist_id=checklists[1].id).all()
    
    #CODIGO_VALIOSO
    if current_user.cargo == 'gestor':
        return redirect(url_for('logistica.lista_checklist' , id_veiculo=placa_veiculo))

    
    return render_template('private/logistica/check_list.html', veiculo=veiculo)


@logistica_bp.route('/salvar_checklist/<placa>', methods=[ 'GET', 'POST'])
@login_required
def salvar_checklist(placa):
    problema = request.args.to_dict()
    veiculo = Veiculos.query.filter_by(placa=placa).first()

    check_list = Checklist(veiculo_id=veiculo.codigo_geral_veiculo, codigo_geral_user = current_user.codigo_geral)
    print(f'================={check_list}')
    db.session.add(check_list)
    db.session.commit()
    for chave, valor in request.args.items():
        #print(f'{chave}: {valor}')
        
        print(f'{chave}: {valor}')
        item =(ChecklistItem( checklist_id = check_list.id, nome = chave, valor = valor))
        db.session.add(item)
        db.session.commit()
    
    return f'{problema} '






@logistica_bp.route('/teste', methods=[ 'GET', 'POST'])
@login_required
def teste():
    veiculos_list = [['RGN2E19','Delivery', 500, '20/06/2016'], ['ABC1D23','Bongo', 200, '10/08/2004'], ['XYZ4F56','Strada', 90, '02/02/2025']]
   
    veiculo = Veiculos('RGN2E19','Delivery', 500, '20/06/2016')
    db.session.add(veiculo)
    db.session.commit()
    for veiculo in veiculos_list:
        print(veiculo)
        novo_veiculo = Veiculos(veiculo[0],veiculo[1],veiculo[2],veiculo[3])
        print(novo_veiculo)
        db.session.add(novo_veiculo)
        db.session.commit()
    return 'TESTE'






#Direcionamento padrão de cargo para rota
@logistica_bp.before_request
@login_required
def check_cargo():
    cargos = ['getor', 'motorista', 'ajudante']
    if current_user.cargo not in cargos and current_user.setor != 'logistica':
            return redirect(url_for(f'{current_user.cargo}.root'))        