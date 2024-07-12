from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/usuarios', methods=['GET'])
def index():
    with open ('data.json', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/api/usuarios/<id>', methods=['GET'])
def buscar_id(id):
    with open ('data.json', encoding='utf-8') as file:
        data = json.load(file)
    for element in data['usuarios']:
        if element['id'] == int(id):
            return jsonify(element)
    return jsonify({'msg':'no existe usuario com esse ID'})

@app.route('/api/cadastrar', methods=['POST'])
def cadastrar():
    new_user = request.get_json()
    with open ('data.json', encoding='utf-8') as file:
        data = json.load(file)

    for element in data['usuarios']:
        if element['email'] == new_user['email']:
            return jsonify({"msg":"email ja cadastrado"})
        if element['nome'] == new_user['nome']:
            return jsonify({"msg": "nome ja cadastrado"})

    new_user['id'] = len(data['usuarios'])+1    
    data['usuarios'].append(new_user)    
    
    with open ('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return jsonify({"msg":"usuario cadastrado com sucesso"})    

if __name__ == '__main__':
    app.run(debug=True)