import requests
import pandas as pd


endpoint = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

query_1 = {
    "linkedin_url": "https://www.linkedin.com/in/albertocouto/",
    "include_skills": "false",
}

query_2 = {
    "linkedin_url": "https://www.linkedin.com/in/caiohenriquessantos//",
    "include_skills": "false",
}

info = {
    "X-RapidAPI-Key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
    "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com",
}


def requestApi(endpoint, info, query):
    try:
        response = requests.get(endpoint, headers=info, params=query)
        response.raise_for_status()

        df = pd.DataFrame(response)
        df.to_json('./resposta1.json', orient='records')
        df.to_html('./resposta1.html')
        df.to_csv('./resposta1.csv', index=False)
        df.to_excel('./resposta1.xlsx', index=False)
    except requests.RequestException as e:
        print("Ocorreu um erro durante a solicitação:", e)


print(requestApi(endpoint, info, query_1))
