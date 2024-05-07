from flask import render_template, request, jsonify, Blueprint
import json

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
