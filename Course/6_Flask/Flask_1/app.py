from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def buscar():
    query_nome = request.form['py-nome']
    msg = f'O seu nome é: {query_nome}'
    return render_template('index.html', resultado=msg)

if __name__ == '__main__':
    app.run(debug=True)