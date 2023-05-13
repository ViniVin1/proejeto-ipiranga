import random as rd
import csv


dic = {
    "idade":  ['18-24 anos', '25-35 anos', '36-49 anos', 'Mais de 50 anos'],
    "genero": ["Masculino", "Feminino", "Outros", "Prefiro não dizer"],
    "estado": ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT',
                'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 
                'RR', 'SC', 'SP', 'SE', 'TO'],
    "frequencia": ['Diariamente', '2-4 vezes na semana', 'Semanalmente', 'Quinzenalmente'],
    "combustivel": ['Gasolina comum', 'Gasolina Aditivada', 'GNV', 'Etanol', 'Diesel'],
    "abastecimento": ['Sempre completo', 'Completo as vezes', 'Conforme o uso'],
    "renda": ['Principal', 'Complementar', 'Não utilizo para renda'],
    "transporte": ['Sim', 'Não'],
    "delivery": ['Sim', 'Não'],
    "posto": ['Ipiranga', 'BR', 'Shell', 'Petrobras', 'Texaco'],
    "importancia": ['Preço', 'Localização', 'Qualidade do combustível', 'Conveniência'],
    "fidelidade-postos": ['Sim', 'Não'],
    "fidelidade-outros": ['Sim', 'Não'],
    "conveniencia": ['Sim', 'Não']
}


def gerar_dados():
    dados = {}
    dados['idade'] = dic['idade'][rd.randint(0, len(dic['idade']))-1]
    dados['genero'] = dic['genero'][rd.randint(0, len(dic['genero']))-1]
    dados['estado'] = dic['estado'][rd.randint(0, len(dic['estado']))-1]
    dados['frequencia'] = dic['frequencia'][rd.randint(0, len(dic['frequencia']))-1]
    dados['combustivel'] = dic['combustivel'][rd.randint(0, len(dic['combustivel']))-1]
    dados['abastecimento'] = dic['abastecimento'][rd.randint(0, len(dic['abastecimento']))-1]
    dados['renda'] = dic['renda'][rd.randint(0, len(dic['renda']))-1]
    dados['transporte'] = dic['transporte'][rd.randint(0, len(dic['transporte']))-1]
    dados['delivery'] = dic['delivery'][rd.randint(0, len(dic['delivery']))-1]
    dados['posto'] = dic['posto'][rd.randint(0, len(dic['posto']))-1]
    dados['importancia'] = dic['importancia'][rd.randint(0, len(dic['importancia']))-1]
    dados['fidelidade-postos'] = dic['fidelidade-postos'][rd.randint(0, len(dic['fidelidade-postos']))-1]
    dados['fidelidade-outros'] = dic['fidelidade-outros'][rd.randint(0, len(dic['fidelidade-outros']))-1]
    dados['conveniencia'] = dic['conveniencia'][rd.randint(0, len(dic['conveniencia']))-1]

    return dados


def gerar_csv():
    dados = gerar_dados()
    with open('respostas.csv', 'a', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([dados['idade'], dados['genero'], dados['estado'], dados['frequencia'], dados['combustivel'], dados['abastecimento'], dados['renda'], dados['transporte'], dados['delivery'], dados['posto'], dados['importancia'], dados['fidelidade-postos'], dados['fidelidade-outros'], dados['conveniencia']])


def salvar_dados(qtd):
    for i in range(qtd):
        gerar_csv()


salvar_dados(100)



    