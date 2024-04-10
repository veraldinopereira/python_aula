from flask import Flask, render_template
# import requests

app = Flask(__name__)


# ROTA PRINCIPAL
@app.route("/")
def index():
    return render_template("index.html")


# Construção da requisição DA API
@app.route("/busca", methods=['post'])
def busca():
    pass


if __name__ == "__main__":
    app.run(debug=True)