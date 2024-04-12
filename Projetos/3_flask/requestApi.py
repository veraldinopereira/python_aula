import requests

url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

querystring = {
    "linkedin_url": "https://www.linkedin.com/in/williamhgates/",
    "include_skills": "false",
}

headers = {
    "X-RapidAPI-Key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
    "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
