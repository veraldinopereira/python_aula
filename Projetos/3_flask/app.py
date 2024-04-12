from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resultado", methods=["post"])
def resultado():
    query = request.form["query"]
    response = requests.get(
        "https://servicodados.ibge.gov.br/api/v3/noticias/?tipo=noticia"
    )
    if response.status_code == 200:
        data = response.json()["items"]
        print(query)
        newdata = []
        for element in data:
            if query in element["titulo"]:
                newdata.append(element)

        return render_template("results.html", data=newdata)
    else:
        return "Erro ao obter receitas", 500


if __name__ == "__main__":
    app.run(debug=True)
