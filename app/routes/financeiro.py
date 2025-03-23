from flask import Flask, Blueprint, session, render_template, redirect, url_for, request
from flask_login import login_required
import os
import pandas as pd
from app import app
import plotly.express as px
financeiro_bp = Blueprint('financeiro', __name__, template_folder='templates')


@financeiro_bp.route('/', methods=['GET', 'POST'])
@login_required
def root():
    if request.method == 'GET':
        print('METODO GET')
        return render_template('/private/financeiro/home.html', base='False') 

    
    if request.method == 'POST':
        teste = request.form.get('test')
        print(teste)
        base = request.files['base_dados']
        print(base)

        file_path = os.path.join(app.config['UPLOAD_FOLDER_FINANCEIRO'], base.filename)
        base.save(file_path)
        df = pd.read_csv(f'uploads/financeiro/{base.filename}')
        df["salario"] = pd.to_numeric(df["salario"], errors="coerce")
        df["bonus"] = pd.to_numeric(df["bonus"], errors="coerce")

        df_custo = df.groupby("setor")[["salario", "bonus"]].sum().reset_index()
        grafico_custo = px.bar(
            df_custo, 
            x="setor", 
            y=["salario", "bonus"], 
            title="Custo Total por Setor (salario + bonus)", 
            barmode="stack"
        )


        df_maiores_bonus = df.loc[df.groupby("setor")["bonus"].idxmax()]
        grafico_maiores_bonus = px.bar(
            df_maiores_bonus, 
            x="setor", 
            y="bonus", 
            text="nome", 
            title="Maiores bonus por Setor", 
            color="setor"
        )

        # Converter gráficos para HTML
        grafico_custo_html = grafico_custo.to_html(full_html=False)
        grafico_maiores_bonus_html = grafico_maiores_bonus.to_html(full_html=False)



        records = df.to_dict(orient='records')
        



      
        return render_template('/private/financeiro/home.html', base=records, grafico_custo=grafico_custo_html, grafico_maiores_bonus=grafico_maiores_bonus_html) 

     