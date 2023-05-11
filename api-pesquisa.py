import csv

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

app = Flask(__name__)

# Rota de teste
@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensagem': 'API OK'})

# Rota de configuração
@app.route('/pesquisa', methods=['OPTIONS'])
def realizar_pesquisa_optionals():
    response = jsonify({'mensagem': 'ok'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

# Função que usa a rota do POST para pegar os dados JSON do formulario e salvar nas respectivas variáveis
@app.route('/pesquisa', methods=['POST'])
def realizar_pesquisa():
    data = request.get_json()
    idade = data['idade']
    genero = data['genero']
    estado = data['estado']
    frequencia = data['frequencia']
    combustivel = data['combustivel']
    abastecimento = data['abastecimento']
    renda = data['renda']
    transporte = data['transporte']
    delivery = data['delivery']
    posto = data['posto']
    importancia = data['importancia']
    fidelidadePostos = data['fidelidade-postos']
    fidelidadeOutros = data['fidelidade-outros']
    conveniencia = data['conveniencia']
    salvar_pesquisa(idade, genero, estado, frequencia, combustivel, abastecimento, renda, transporte, delivery, posto, importancia, fidelidadePostos, fidelidadeOutros, conveniencia)
    response = jsonify({'mensagem': 'Respostas enviadas com sucesso'})
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    
    return response

# Funçãr que salva os dados do formulario em um arquivo CSV
def salvar_pesquisa(idade, genero, estado, frequencia, combustivel, abastecimento, renda, transporte, delivery, posto, importancia, fidelidadePostos, fidelidadeOutros, conveniencia):
    with open('respostas.csv', 'a', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([idade, genero, estado, frequencia, combustivel, abastecimento, renda, transporte, delivery, posto, importancia, fidelidadePostos, fidelidadeOutros, conveniencia])

if __name__ == '__main__':
    app.run(debug=True)