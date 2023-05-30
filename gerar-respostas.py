import random as rd
import csv

# Dicionário com as informações a serem selecionadas
dic = {
    "idade":  ['18-24 anos', '25-35 anos', '36-49 anos', 'Mais de 50 anos'],
    "genero": ["Masculino", "Feminino",  "Outros", "Prefiro não dizer"],
    "estado": ['Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara', 'Distrito Federal', 'Espirito Santo',
                'Goias', 'Maranhao', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Para', 'Paraiba', 'Parana',
                'Pernambuco', 'Piaui', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondonia', 'Roraima',
                'Santa Catarina', 'Sao Paulo', 'Sergipe', 'Tocantins'],
    "frequencia": ['Diariamente', '2-4 vezes na semana', 'Semanalmente', 'Quinzenalmente'],
    "combustivel": ['Gasolina comum', 'Gasolina Aditivada', 'GNV', 'Etanol', 'Diesel', 'Elétrico'],
    "abastecimento": ['Sempre completo', 'Completo as vezes', 'Conforme o uso'],
    "renda": ['Lazer', 'Locomoção para o trabalho', 'Principal fonte de renda'],
    "posto": ['Ipiranga', 'BR', 'Shell', 'Petrobras', 'Texaco', 'Ale'], 
    "importancia": ['Preço', 'Localização', 'Qualidade do combustível', 'Loja de Conveniência', 'Atendimento', 'Serviços Adicionais'],
    "fidelidade-postos": ['Sim', 'Não'],
    "aplicativo": ['Conheço mas não utilizo', 'Conheço e utilizo', 'Não conheço', 'Utilizo outros'],
    "motivo": ['Não utilizo aplicativos/programas de fidelidade', 'Descontos em abastecimento/serviços', 'Cashback'],
    "conveniencia": ['Sim', 'Não'],
    "classificacao": ['0', '1', '2', '3', '4', '5']
}

# Função que gera os dados de forma aleatória e salva em um novo dicionário
def gerar_dados():
    dados = {}
    dados['idade'] = dic['idade'][rd.randint(0, len(dic['idade']))-1]
    dados['genero'] = dic['genero'][rd.randint(0, len(dic['genero']))-1]
    dados['estado'] = dic['estado'][rd.randint(0, len(dic['estado']))-1]
    dados['frequencia'] = dic['frequencia'][rd.randint(0, len(dic['frequencia']))-1]
    dados['combustivel'] = dic['combustivel'][rd.randint(0, len(dic['combustivel']))-1]
    dados['abastecimento'] = dic['abastecimento'][rd.randint(0, len(dic['abastecimento']))-1]
    dados['renda'] = dic['renda'][rd.randint(0, len(dic['renda']))-1]
    dados['posto'] = dic['posto'][rd.randint(0, len(dic['posto']))-1]
    dados['importancia'] = dic['importancia'][rd.randint(0, len(dic['importancia']))-1]
    dados['fidelidade-postos'] = dic['fidelidade-postos'][rd.randint(0, len(dic['fidelidade-postos']))-1]
    dados['aplicativo'] = dic['aplicativo'][rd.randint(0, len(dic['aplicativo']))-1]
    dados['motivo'] = dic['motivo'][rd.randint(0, len(dic['motivo']))-1]
    dados['conveniencia'] = dic['conveniencia'][rd.randint(0, len(dic['conveniencia']))-1]
    dados['classificacao'] = dic['classificacao'][rd.randint(0, len(dic['classificacao']))-1]

    return dados

# Função que salva os dados gerados em um arquivo CSV
def gerar_linha_csv():
    dados = gerar_dados()
    with open('respostas.csv', 'a', newline='', encoding='utf-8') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow([dados['idade'], dados['genero'], dados['estado'], 
        dados['frequencia'], dados['combustivel'], dados['abastecimento'], dados['renda'], 
        dados['posto'], dados['importancia'], dados['fidelidade-postos'],dados['aplicativo'],
        dados['motivo'], dados['conveniencia'], dados['classificacao']])

# Função que define a quantidade de linhas a serem geradas
def salvar_dados(qtd):
    for i in range(qtd):
        gerar_linha_csv()

# Chamamento da função onde a quantidade de linhas a serem geradas deve ser informada dentro dos parênteses
salvar_dados()





    