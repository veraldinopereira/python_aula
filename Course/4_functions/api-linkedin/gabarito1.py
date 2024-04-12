import requests
import pandas as pd

endpoint = "https://api.api-futebol.com.br/v1/campeonatos"

headers = {
    "Authorization": "Bearer test_7ee4ac89d3acbc06c6dc05a2f5474e",
}


def request_api(endpoint, info):
    try:
        response = requests.get(endpoint, headers=info)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Ocorreu um erro durante a solicitação:", e)


def api_to_frame():
    data = request_api(endpoint, headers)[0]
    df = pd.DataFrame(data)
    print("aguarde...")
    return df.to_excel("tabela.xlsx", index=False)


api_to_frame()
