import requests

# URL da API do Banco Central para obter nomes das moedas em português
URL_BCB = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=1000&$format=json'

# URL da API de câmbio (CurrencyLayer, ExchangeRate API, etc.)
API_KEY = 'b411b384fae5df4271f6f0ff98e2bd48'
BASE_URL_CAMBIO = f'http://api.currencylayer.com/live?access_key={API_KEY}'

# Função para obter nomes de moedas em português da API do Banco Central
def obter_nomes_moedas_pt():
    response = requests.get(URL_BCB)
    if response.status_code != 200:
        print("Erro ao acessar a API do Banco Central:", response.json())
        return None
    
    dados = response.json()
    return {moeda['simbolo']: moeda['nomeFormatado'] for moeda in dados['value']}

# Função para obter taxa de câmbio entre duas moedas usando a API de câmbio
def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    url = f'{BASE_URL_CAMBIO}&currencies={moeda_destino}&source={moeda_origem}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao acessar a API de câmbio:", response.json())
        return None
    
    dados = response.json()
    taxa = dados['quotes'].get(f'{moeda_origem}{moeda_destino}')
    return taxa

# Função para converter moedas usando as taxas e exibir o resultado
def converter_moeda(valor, nome_moeda_origem, nome_moeda_destino, moedas_invertido):
    # Remover espaços em branco e converter para minúsculas
    moeda_origem = moedas_invertido.get(nome_moeda_origem.strip().lower())
    moeda_destino = moedas_invertido.get(nome_moeda_destino.strip().lower())
    
    if not moeda_origem or not moeda_destino:
        print("Moeda não reconhecida. Verifique se digitou corretamente.")
        return None

    taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
    if taxa:
        return valor * taxa
    else:
        print("Conversão não disponível.")
        return None

# Carrega os nomes das moedas em português
moedas_pt = obter_nomes_moedas_pt()
if moedas_pt:
    print("Nomes de moedas carregados com sucesso!")
else:
    print("Falha ao carregar nomes de moedas.")

# Dicionário invertido para facilitar busca de moeda pelo nome em português
moedas_invertido = {v.lower(): k for k, v in moedas_pt.items()}

# Teste do Conversor
nome_moeda_origem = input("Digite a moeda de origem que você quer converter (ex: Dólar Americano): ").strip()
nome_moeda_destino = input("Digite a moeda de destino para a qual você quer converter o valor (ex: Real Brasileiro): ").strip()
valor = float(input("Qual o valor que você quer converter: "))

resultado = converter_moeda(valor, nome_moeda_origem, nome_moeda_destino, moedas_invertido)
if resultado:
    print(f"{valor} {nome_moeda_origem} equivale a {resultado:.2f} {nome_moeda_destino}")
