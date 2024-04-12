import requests

endpoint = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

query = {
    "linkedin_url": "https://www.linkedin.com/in/albertocouto/",
    "include_skills": "false",
}

headers = {
    "X-RapidAPI-Key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
    "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com",
}   

response = requests.get(endpoint, headers=headers, params=query)

print(response.json())
