from flask import render_template, request, jsonify, Blueprint, send_from_directory
import json
import os

auth = Blueprint('auth', __name__)

@auth.route('/')
def index_default():
    return render_template('index.html')

@auth.route('/index')
def index():
    return render_template('index.html')

@auth.route('/login')
def login():
    return render_template('login.html')    

@auth.route('/autenticar', methods=['POST'])
def autenticar():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    with open('usuarios.json') as usuariostemp:
        usuarios = json.load(usuariostemp)
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return jsonify({'nome': nome, 'senha': senha})
        return "erro"

@auth.route('/upload')
def upload ():
    return render_template('upload.html' )

@auth.route('/autenticar2', methods=['POST']) 
def autenticar2 ():
    arquivo  = request.files.get('Documento')  
    nome_arquivo = arquivo.filename.replace(" ","-")
    arquivo.save(os.path.join('arquivos', nome_arquivo))
    return f"arquivo {nome_arquivo} salvo com sucesso"

@auth.route('/download')
def download ():
    arquivos = os.listdir('arquivos')
    return render_template('download.html', arquivos=arquivos)
import os

@auth.route('/autenticar3', methods=['POST']) 
def autenticar3():
    nome_do_arquivo = request.form.get('download')
    diretorio = 'arquivos'
    caminho_arquivo = os.path.join(diretorio, nome_do_arquivo)
    
    return send_from_directory(diretorio, nome_do_arquivo, as_attachment=True)

