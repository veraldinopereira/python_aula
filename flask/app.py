from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def cadastro():
    nome = request.form['nome_py']
    idade = request.form['idade_py']
    usuario = {"nome":nome, "idade": idade}
    usuarios.append(usuario)
    print(usuarios)
    return render_template('index.html', resultado = usuarios)

if __name__ == '__main__':
    app.run(debug=True)