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
    return render_template('index.html')

@app.route('/cadastros', methods=['GET'])
def exibir_cadastro():
    return render_template('cadastros.html', resultado = usuarios)

@app.route('/cadastro_nome', methods=['GET'])
def exibir_cadastro_nome():
    resultado = []
    nome_pesquisado = request.args.get('buscar_nome')
    print(nome_pesquisado)
    for element in usuarios:
        element['nome']==nome_pesquisado
        resultado.append(element)
    print(resultado)
    return render_template('index.html')
    
##criar rota para pesquisa

if __name__ == '__main__':
    app.run(debug=True)