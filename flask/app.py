from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def cadastro():
    nome = request.form['nome_py']
    print(nome)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)