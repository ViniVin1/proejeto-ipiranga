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

# Função que pega os dados JSON do formulario e salva nas respectivas variáveis
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
    posto = data['posto']
    importancia = data['importancia']
    fidelidadePostos = data['fidelidade-postos']
    aplicativo = data['aplicativo']
    motivo = data['motivo']
    conveniencia = data['conveniencia']
    classificacao = data['classificacao']
    salvar_pesquisa(idade, genero, estado, frequencia, combustivel, abastecimento, renda, posto, 
                    importancia, fidelidadePostos, aplicativo, motivo, conveniencia, classificacao)
    response = jsonify({'mensagem': 'Respostas enviadas com sucesso!!'})
    
    # Configuração do header da API, para que possa ser acessada de qualquer origem e habilitando todos os métodos
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    
    return response

# Função que salva os dados do formulario em um arquivo CSV
def salvar_pesquisa(idade, genero, estado, frequencia, combustivel, abastecimento, renda, posto, 
                    importancia, fidelidadePostos, aplicativo, motivo, conveniencia, classificacao):
    with open('respostas.csv', 'a', newline='', encoding='utf-8') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([idade, genero, estado, frequencia, combustivel, abastecimento, renda, posto, 
                    importancia, fidelidadePostos, aplicativo, motivo, conveniencia, classificacao])
 

if __name__ == '__main__':
    app.run(debug=True)