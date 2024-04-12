# Importa a biblioteca 'requests', que permite fazer solicitações HTTP
import requests

# Define o endpoint da API que será acessada
endpoint = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

# Define os parâmetros da primeira consulta à API
query_1 = {
    "linkedin_url": "https://www.linkedin.com/in/albertocouto/",
    "include_skills": "false",
}

# Define os parâmetros da segunda consulta à API
query_2 = {
    "linkedin_url": "https://www.linkedin.com/in/caiohenriquessantos//",
    "include_skills": "false",
}

# Define um dicionário chamado 'info' contendo as informações necessárias para acessar a API
# Neste caso, são as chaves de acesso à API RapidAPI
info = {
    "X-RapidAPI-Key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
    "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com",
}


# Define uma função chamada 'requestApi' que faz uma solicitação à API com os parâmetros fornecidos
def requestApi(endpoint, info, query):
    try:
        # Faz uma solicitação GET para o endpoint da API, passando os cabeçalhos e parâmetros necessários
        response = requests.get(endpoint, headers=info, params=query)
        # Verifica se a resposta da solicitação indica um erro
        response.raise_for_status()
        # Se a resposta foi bem-sucedida, retorna os dados da resposta no formato JSON
        return response.json()
    except requests.RequestException as e:
        # Se ocorrer um erro durante a solicitação, imprime uma mensagem de erro
        print("Ocorreu um erro durante a solicitação:", e)


# Chama a função 'requestApi' com os parâmetros definidos anteriormente e imprime o resultado
print(requestApi(endpoint, info, query_2))
