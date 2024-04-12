import requests

endpoint = "https://api.api-futebol.com.br/v1/campeonatos"

headers = {
    "Authorization": "Bearer test_7ee4ac89d3acbc06c6dc05a2f5474e",
}


def requestApi(endpoint, info):
    try:
        response = requests.get(endpoint, headers=info)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Ocorreu um erro durante a solicitação:", e)


print(requestApi(endpoint, headers))
