from flask import Flask, request, render_template, jsonify
import string
import random

app = Flask (__name__)

def gerar_senha(tamanho, incluir_maiusculas_senha, incluir_numeros_senha, incluir_simbolos_senha):
    caracteres_minusculos_senha = string.ascii_lowercase
    caracteres_maiusculos_senha = string.ascii_uppercase if incluir_maiusculas_senha else ""
    numeros = string.digits if incluir_numeros_senha else ""
    simbolos_esp = string.punctuation if incluir_simbolos_senha else ""
    
    caracteres = caracteres_minusculos_senha + caracteres_maiusculos_senha + numeros + simbolos_esp


    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/criar_conta', methods=['POST'])
def criar_conta():
    dados = request.get_json()
    login = dados.get['login']
    tamanho = int(dados.get('tamanho', 8))
    incluir_maiusculas_senha = dados.get('incluir_maisculas_senha', False)
    incluir_numeros_senha = dados.get('incluir_numeros_senha', False)
    incluir_simbolos_senha = dados.get('incluir_simbolos_senha', False)

    senha = gerar_senha(tamanho, incluir_maiusculas_senha, incluir_numeros_senha, incluir_simbolos_senha)

    return jsonify({"login": login, "senha": senha})

if __name__== '__main__':
    app.run(debug=True)