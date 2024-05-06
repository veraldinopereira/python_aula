from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dados_concatenados = None 
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        documento = request.form['documento']
        cidade = request.form['cidade']
        dados_concatenados = f"Nome: {nome}, Idade: {idade}, Sexo: {sexo}, Documento: {documento}, Cidade: {cidade}"
    return render_template('index.html', dados_concatenados=dados_concatenados)

if __name__ == '__main__':
    app.run(debug=True)