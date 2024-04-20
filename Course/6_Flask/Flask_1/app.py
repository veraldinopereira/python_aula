from flask import Flask, render_template, request

app = Flask(__name__)

def get_name():
    if 'py-nome' in request.form and 'py-time' in request.form:
        query_nome = request.form['py-nome']
        query_time = request.form['py-time']
        msg = f'O seu nome é: {query_nome} Campeao liberta: {query_time}'
        return msg
    return None

def get_selecao():
    if 'py-selecao' in request.form:
        query_selecao = request.form['py-selecao']
        return query_selecao
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def buscar():
    resultado_nome = get_name()
    resultado_selecao = get_selecao()
    return render_template('index.html', resultado = resultado_nome, resultado1 = resultado_selecao)

if __name__ == '__main__':
    app.run(debug=True)